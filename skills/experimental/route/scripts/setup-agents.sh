#!/usr/bin/env bash
# Create the tiered subagents route dispatches to, one model pinned per tier.
# Idempotent: existing files are left alone unless --force is passed.
#
#   setup-agents.sh [--check] [--force] [--shadow-readonly]
#                   [--read M] [--fast M] [--mid M] [--heavy M]           # Claude Code
#                   [--oc-read M] [--oc-fast M] [--oc-mid M] [--oc-heavy M]  # OpenCode
#
# --check            report what is missing, write nothing, exit 1 if any
# --shadow-readonly  also pin Claude Code's Explore and Plan (see caveat below)
#
# OpenCode models are resolved from a per-tier preference list: the first entry
# whose provider is authenticated wins, so a machine on OpenCode Go gets those
# models and one on Z.ai gets those, with no flags. Any flag overrides outright.

set -euo pipefail

# Claude Code takes the aliases, which survive model releases.
READ=sonnet
FAST=haiku
MID=sonnet
HEAVY=opus

# OpenCode has no alias form, so these are preference lists, best first. The
# capability ordering inside a provider is inferred from the model names, so
# adjust with flags rather than trusting it.
OC_READ_PREF="zai-coding-plan/glm-5.2 opencode-go/glm-5.3"
OC_FAST_PREF="zai-coding-plan/glm-5.3-flash opencode-go/glm-5.3-flash"
OC_MID_PREF="zai-coding-plan/glm-5.2 opencode-go/glm-5.3"
OC_HEAVY_PREF="zai-coding-plan/glm-5.3opencode-go/qwen3.8-max"
OC_READ="" OC_FAST="" OC_MID="" OC_HEAVY=""

CHECK=0
FORCE=0
SHADOW_READONLY=0

while [ $# -gt 0 ]; do
  case "$1" in
    --check) CHECK=1 ;;
    --force) FORCE=1 ;;
    --shadow-readonly) SHADOW_READONLY=1 ;;
    --read) READ="$2"; shift ;;
    --fast) FAST="$2"; shift ;;
    --mid) MID="$2"; shift ;;
    --heavy) HEAVY="$2"; shift ;;
    --oc-read) OC_READ="$2"; shift ;;
    --oc-fast) OC_FAST="$2"; shift ;;
    --oc-mid) OC_MID="$2"; shift ;;
    --oc-heavy) OC_HEAVY="$2"; shift ;;
    -h|--help) sed -n '2,16p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
  shift
done

command -v python3 >/dev/null || { echo "python3 is required" >&2; exit 1; }

CLAUDE_AGENTS="$HOME/.claude/agents"
CLAUDE_SETTINGS="$HOME/.claude/settings.json"
OC_DIR="$HOME/.config/opencode"
OC_AGENTS="$OC_DIR/agents"
OC_CONFIG="$OC_DIR/opencode.json"
OC_AUTH="$HOME/.local/share/opencode/auth.json"

MISSING=0
note() { echo "$1"; }
miss() { MISSING=1; echo "missing: $1"; }

# Provider names only. Credentials in this file are never read or printed.
authenticated_providers() {
  [ -f "$OC_AUTH" ] || return 0
  python3 -c 'import json,sys;print(" ".join(json.load(open(sys.argv[1])).keys()))' "$OC_AUTH" 2>/dev/null || true
}

# First entry in the preference list whose provider is authenticated; the last
# entry is the backstop when none are.
resolve_model() { # preference-list authenticated-providers
  local entry provider last=""
  for entry in $1; do
    last="$entry"
    provider="${entry%%/*}"
    case " $2 " in *" $provider "*) echo "$entry"; return ;; esac
  done
  echo "$last"
}

BODY_READ='You are a read-only agent. You search, read and reason, then report what you
found and what you conclude. You never create, edit or delete a file, and you
never run a command that changes state. Report findings and the evidence for
them, not a narrative of your search.'

BODY_FAST='You are a fast implementer. You handle small, well-scoped changes: renames, small
functions, tweaks, formatting, small bug fixes, test additions. Do exactly what is
asked, no refactoring beyond the request, no commentary beyond the result.'

BODY_MID='You are the default implementer. You handle moderate changes: multi-step edits
within a component, new functions and their call sites, ordinary feature work and
bug fixes. You also take general multi-step tasks and searches that need more than
a quick grep.

Read the surrounding code before changing it, keep the change coherent, and verify
with the project'"'"'s lint, typecheck and test commands when present. Do what is
asked, no refactoring beyond the request, no commentary beyond the result. When the
brief is read-only (explore, review, plan), report findings and change no files.'

BODY_HEAVY='You are a heavyweight implementer for drastic changes: cross-cutting refactors,
architecture changes, large feature work, migrations, security-sensitive edits.
Read the surrounding code before changing it, keep changes coherent across files,
and verify with the project'"'"'s lint, typecheck and test commands when present.'

DESC_EXPLORE='Read-only codebase explorer. Searches and reads, reports findings, changes no files.'
DESC_PLAN='Read-only planner. Designs an approach and reports it, changes no files.'
DESC_FAST='Fast, cheap implementer for simple small changes. Renames, small functions, config tweaks, formatting, small bug fixes, test additions.'
DESC_MID='Default implementer and general worker. Moderate changes, multi-step tasks, code search, and read-only investigation that needs more than a quick grep.'
DESC_HEAVY='Heavyweight implementer for large or drastic changes. Cross-cutting refactors, architecture changes, large feature work, migrations, security-sensitive edits.'

write_claude_agent() { # name description model body
  local path="$CLAUDE_AGENTS/$1.md"
  if [ -e "$path" ] && [ "$FORCE" -eq 0 ]; then note "kept: $path"; return; fi
  mkdir -p "$CLAUDE_AGENTS"
  printf -- '---\nname: %s\ndescription: %s\nmodel: %s\n---\n\n%s\n' "$1" "$2" "$3" "$4" > "$path"
  note "wrote: $path ($3)"
}

write_opencode_agent() { # id description model body
  local path="$OC_AGENTS/$1.md"
  if [ -e "$path" ] && [ "$FORCE" -eq 0 ]; then note "kept: $path"; return; fi
  mkdir -p "$OC_AGENTS"
  printf -- '---\ndescription: %s\nmode: subagent\nmodel: %s\n---\n\n%s\n' "$2" "$3" "$4" > "$path"
  note "wrote: $path ($3)"
}

PROVIDERS="$(authenticated_providers)"
[ -n "$OC_READ" ]  || OC_READ="$(resolve_model "$OC_READ_PREF" "$PROVIDERS")"
[ -n "$OC_FAST" ]  || OC_FAST="$(resolve_model "$OC_FAST_PREF" "$PROVIDERS")"
[ -n "$OC_MID" ]   || OC_MID="$(resolve_model "$OC_MID_PREF" "$PROVIDERS")"
[ -n "$OC_HEAVY" ] || OC_HEAVY="$(resolve_model "$OC_HEAVY_PREF" "$PROVIDERS")"

if [ "$CHECK" -eq 1 ]; then
  for n in General Fast Heavy; do
    [ -e "$CLAUDE_AGENTS/$n.md" ] || miss "$CLAUDE_AGENTS/$n.md"
  done
  if [ "$SHADOW_READONLY" -eq 1 ]; then
    for n in Explore Plan; do
      [ -e "$CLAUDE_AGENTS/$n.md" ] || miss "$CLAUDE_AGENTS/$n.md"
    done
  fi
  python3 - "$CLAUDE_SETTINGS" <<'PY' || MISSING=1
import json, sys, pathlib
p = pathlib.Path(sys.argv[1])
cfg = json.loads(p.read_text() or "{}") if p.exists() else {}
if "Agent(general-purpose)" not in cfg.get("permissions", {}).get("deny", []):
    print(f"missing: deny rule Agent(general-purpose) in {p}")
    sys.exit(1)
PY
  if [ -d "$OC_DIR" ]; then
    for n in fast heavy; do
      [ -e "$OC_AGENTS/$n.md" ] || miss "$OC_AGENTS/$n.md"
    done
    python3 - "$OC_CONFIG" <<'PY' || MISSING=1
import json, sys, pathlib
p = pathlib.Path(sys.argv[1])
cfg = json.loads(p.read_text() or "{}") if p.exists() else {}
agents = cfg.get("agent", {})
absent = [a for a in ("general", "explore", "plan") if not agents.get(a, {}).get("model")]
if absent:
    print(f"missing: model pin for {', '.join(absent)} in {p}")
    sys.exit(1)
PY
  fi
  [ "$MISSING" -eq 0 ] && echo "routing agents: complete"
  exit "$MISSING"
fi

write_claude_agent General "$DESC_MID" "$MID" "$BODY_MID"
write_claude_agent Fast "$DESC_FAST" "$FAST" "$BODY_FAST"
write_claude_agent Heavy "$DESC_HEAVY" "$HEAVY" "$BODY_HEAVY"

# Claude Code cannot pin a built-in's model while keeping its prompt: a file named
# Explore.md or Plan.md replaces the built-in wholesale. Opt in deliberately.
if [ "$SHADOW_READONLY" -eq 1 ]; then
  write_claude_agent Explore "$DESC_EXPLORE" "$READ" "$BODY_READ"
  write_claude_agent Plan "$DESC_PLAN" "$READ" "$BODY_READ"
else
  note "skipped: Explore and Plan left built in (pass --shadow-readonly to pin them)"
fi

# General sits beside the built-in general-purpose rather than replacing it, so deny
# the built-in to leave one agent per role. The harness default agent is left alone.
python3 - "$CLAUDE_SETTINGS" <<'PY'
import json, sys, pathlib
p = pathlib.Path(sys.argv[1])
p.parent.mkdir(parents=True, exist_ok=True)
cfg = json.loads(p.read_text() or "{}") if p.exists() else {}
deny = cfg.setdefault("permissions", {}).setdefault("deny", [])
if "Agent(general-purpose)" in deny:
    print(f"kept: deny rule already in {p}")
else:
    deny.append("Agent(general-purpose)")
    p.write_text(json.dumps(cfg, indent=2) + "\n")
    print(f"wrote: deny rule Agent(general-purpose) in {p}")
PY

if [ -d "$OC_DIR" ] || command -v opencode >/dev/null 2>&1; then
  write_opencode_agent fast "$DESC_FAST" "$OC_FAST" "$BODY_FAST"
  write_opencode_agent heavy "$DESC_HEAVY" "$OC_HEAVY" "$BODY_HEAVY"
  # general, explore and plan already exist, and a config pin sets their model while
  # leaving the built-in prompt intact, which a markdown file would replace. build is
  # OpenCode's primary session agent, so it is left alone.
  python3 - "$OC_CONFIG" "$OC_MID" "$OC_READ" <<'PY'
import json, sys, pathlib
p, mid, read = pathlib.Path(sys.argv[1]), sys.argv[2], sys.argv[3]
p.parent.mkdir(parents=True, exist_ok=True)
cfg = json.loads(p.read_text() or "{}") if p.exists() else {}
cfg.setdefault("$schema", "https://opencode.ai/config.json")
agent = cfg.setdefault("agent", {})
changed = []
for name, model in (("general", mid), ("explore", read), ("plan", read)):
    entry = agent.setdefault(name, {})
    if entry.get("model") != model:
        entry["model"] = model
        changed.append(f"{name}={model}")
if changed:
    p.write_text(json.dumps(cfg, indent=2) + "\n")
    print(f"wrote: {', '.join(changed)} in {p}")
else:
    print(f"kept: general, explore and plan already pinned in {p}")
PY
else
  note "skipped: no OpenCode install found"
fi

echo
echo "Claude Code picks new agent definitions up without a restart, though not instantly."
