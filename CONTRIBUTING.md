# Contributing

Thank you so much for considering contributing to Atuin! We really appreciate it <3

Atuin doesn't require anything super special to develop - standard Rust tooling will do you just fine. We commit to supporting the latest stable version of Rust - nothing more, nothing less, no nightly.

Before working on anything, we suggest taking a copy of your Atuin data directory (`~/.local/share/atuin` on most \*nix platforms). If anything goes wrong, you can always restore it!

While data directory backups are always a good idea, you can instruct Atuin to use custom path using the following environment variables:

```shell
export ATUIN_DB_PATH=/tmp/atuin_dev.db
export ATUIN_RECORD_STORE_PATH=/tmp/atuin_records.db
```

It is also recommended to update your `$PATH` so that the pre-exec scripts would use the locally built version:

```shell
export PATH="./target/release:$PATH"
```

These 3 variables can be added in a local `.envrc` file, read by [direnv](https://direnv.net/).

## What to work on?

Any issues labeled "bug" or "help wanted" would be fantastic, just drop a comment and feel free to ask for help!

If there's anything you want to work on that isn't already an issue, either open a feature request or get in touch on the [forum](https://forum.atuin.sh)/Discord. 

## Setup

```
git clone https://github.com/atuinsh/atuin
cd atuin
cargo build
```

## Running

When iterating on a feature, it's useful to use `cargo run`

For example, if working on a search feature

```
cargo run -- search --a-new-flag
```

While iterating on the server, I find it helpful to run a new user on my system, with `sync_server` set to be `localhost`.

## Tests

Our test coverage is currently not the best, but we are working on it! Generally tests live in the file next to the functionality they are testing, and are executed just with `cargo test`.


## Migrations

Be careful creating database migrations - once your database has migrated ahead of current stable, there is no going back

### Stickers

We try to ship anyone contributing to Atuin a sticker! Only contributors get a shiny one. Fill out [this form](https://notionforms.io/forms/contributors-stickers) if you'd like one.
