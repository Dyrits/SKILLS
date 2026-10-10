# Code checks: Rust

Verified: 2026-10-10, against Clippy's documentation; rustfmt's commands are not checked.

| Job | Tool | Present when | Install | Check |
| --- | --- | --- | --- | --- |
| Format | rustfmt | `rustfmt.toml` or `.rustfmt.toml`, or the component installed | `rustup component add rustfmt` | `cargo fmt --check` |
| Lint and typecheck | Clippy | The component installed | `rustup component add clippy` | `cargo clippy --all-targets -- -Dwarnings` |

Clippy compiles the crate, so it is the typecheck too. `-Dwarnings` fails on every warning, including the compiler's own (`dead_code`). With Cargo 1.97 or later, Clippy's documentation prefers `CARGO_BUILD_WARNINGS=deny cargo clippy`, or `warnings = "deny"` under `[build]` in `.cargo/config.toml`, which keeps the build cache valid.

## Choosing

- Both tools come with the standard toolchain: wire them in and install nothing beyond the components.

## Hook lines

```sh
if has_staged '*.rs'; then cargo fmt --check; fi
cargo clippy --all-targets -- -Dwarnings
```

Without `package.json`, add `git config core.hooksPath .githooks` to the project's setup instructions so clones get the hooks.
