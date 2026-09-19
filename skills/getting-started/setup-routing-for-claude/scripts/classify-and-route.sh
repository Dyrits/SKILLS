#!/usr/bin/env bash
# UserPromptSubmit hook: classify every prompt with classifier.dev and speak only
# when the verdict changes from the previous prompt in this session, so the line
# means a boundary: work starting, ending, or shifting shape. Fails open: any
# missing prompt, network error, timeout or non-2xx response emits
# {"continue":true} with no systemMessage, so a classifier outage never blocks
# the turn. The model keeps the judgement: the line recommends, it never
# dispatches.

set -uo pipefail

TASK_LABELS='["Implementation or refactoring","Debugging or diagnosis","Planning or design","Specification refinement","Codebase exploration","Code review","Undefined"]'
COMPLEXITY_LABELS='["Fast and simple","Moderate","Large or risky change"]'
INSTRUCTIONS='Judge the scope and risk of the work described, not how it is worded. A rename, a small function, a configuration tweak, a small fix is fast and simple. Multi-file refactors, architecture changes, migrations, anything security-sensitive are large or risky. Exploration describes what is; planning decides what will be. Debugging and diagnosis investigate a defect or unexpected behaviour before any fix; implementation and refactoring change code.'

emit_silent() { echo '{"continue":true}'; exit 0; }

command -v jq >/dev/null 2>&1 || emit_silent
command -v curl >/dev/null 2>&1 || emit_silent

input="$(cat)"
prompt="$(printf '%s' "$input" | jq -r '.user_prompt // empty' 2>/dev/null)"
[ -n "$prompt" ] || emit_silent

session_id="$(printf '%s' "$input" | jq -j '.session_id // empty' 2>/dev/null | tr -c 'A-Za-z0-9_.-' '_')"
[ -n "$session_id" ] || session_id="default"
state_file="${TMPDIR:-/tmp}/classify-and-route-${session_id}.json"

body="$(jq -n \
  --arg p "$prompt" \
  --argjson task "$TASK_LABELS" \
  --argjson complexity "$COMPLEXITY_LABELS" \
  --arg instructions "$INSTRUCTIONS" \
  '{items: [$p], dimensions: {task: $task, complexity: $complexity}, instructions: $instructions}' 2>/dev/null)"
[ -n "$body" ] || emit_silent

response="$(curl -sS --max-time 4 -H 'content-type: application/json' -d "$body" https://classifier.dev 2>/dev/null)"
[ -n "$response" ] || emit_silent

printf '%s' "$response" | jq -e '.error' >/dev/null 2>&1 && emit_silent

task_label="$(printf '%s' "$response" | jq -r '.results[0].dimensions.task.label // empty' 2>/dev/null)"
task_conf="$(printf '%s' "$response" | jq -r '.results[0].dimensions.task.confidence // 0' 2>/dev/null)"
complexity_label="$(printf '%s' "$response" | jq -r '.results[0].dimensions.complexity.label // empty' 2>/dev/null)"
complexity_conf="$(printf '%s' "$response" | jq -r '.results[0].dimensions.complexity.confidence // 0' 2>/dev/null)"
[ -n "$task_label" ] || emit_silent
[ -n "$complexity_label" ] || emit_silent

below() { awk -v a="$1" -v b="$2" 'BEGIN{exit !(a<b)}'; }

# A low-confidence verdict reads as Undefined.
if [ "$task_label" = "Undefined" ] || below "$task_conf" 0.7; then
  route_task="Undefined"
else
  route_task="$task_label"
fi

prev_task=""
prev_complexity=""
if [ -r "$state_file" ]; then
  prev_task="$(jq -r '.task // empty' "$state_file" 2>/dev/null)"
  prev_complexity="$(jq -r '.complexity // empty' "$state_file" 2>/dev/null)"
fi

# Record the verdict even when staying silent, so a return from Undefined fires.
jq -n --arg t "$route_task" --arg c "$complexity_label" '{task: $t, complexity: $c}' > "$state_file" 2>/dev/null

# Transitions to Undefined say nothing; from Undefined (or from nothing, the
# first prompt of a session) the line fires.
[ "$route_task" != "Undefined" ] || emit_silent
[ "$route_task" != "$prev_task" ] || [ "$complexity_label" != "$prev_complexity" ] || emit_silent

if [ -z "$prev_task" ]; then
  message="Route: ${route_task} (${task_conf}) | ${complexity_label} (${complexity_conf}). Use the relevant skills. Consider /dispatch."
else
  message="Route: ${route_task} (${task_conf}) | ${complexity_label} (${complexity_conf}) (Previous route: ${prev_task} | ${prev_complexity}). Use the relevant skills. Consider /dispatch as a priority."
fi

jq -n --arg msg "$message" '{continue: true, systemMessage: $msg}'
