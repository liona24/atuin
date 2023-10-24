#!/bin/bash

cargo build --release --no-default-features --features atuin/client

cp target/release/atuin ~/.local/share/bin/atuin
