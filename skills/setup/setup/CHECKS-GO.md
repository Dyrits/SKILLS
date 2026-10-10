# Code checks: Go

Verified: 2026-10-10, against each tool's documentation.

| Job | Tool | Present when | Install | Check |
| --- | --- | --- | --- | --- |
| Format | gofmt | Comes with Go | Comes with Go | `gofmt -l <files>` prints unformatted files and exits 0, so the hook fails on output |
| Lint and format | golangci-lint | A `.golangci.*` configuration, or `golangci-lint` on the path | `curl -sSfL https://golangci-lint.run/install.sh \| sh -s -- -b $(go env GOPATH)/bin <version>`, or `brew install golangci-lint` | `golangci-lint run` and `golangci-lint fmt --diff <files>` |
| Vet | go vet | Comes with Go | Comes with Go | `go vet ./...` |

Go compiles as it lints, so there is no separate typecheck. golangci-lint lints packages, not files: run it on the whole module, or limit reports with `--new-from-rev HEAD`. Its maintainers recommend the install script over Homebrew and `go install`; pin the version the script installs.

## Choosing

- **Nothing present**: gofmt and go vet, which need no install; offer golangci-lint for more linters.
- **A golangci-lint v1 configuration**: `golangci-lint migrate` converts it to v2.

## Hook lines

```sh
if has_staged '*.go'; then
  unformatted=$(staged '*.go' | xargs -0 gofmt -l)
  [ -z "$unformatted" ] || { echo "gofmt: $unformatted"; exit 1; }
fi
go vet ./...
golangci-lint run
```

Without `package.json`, add `git config core.hooksPath .githooks` to the project's setup instructions so clones get the hooks.
