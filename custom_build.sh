#!/bin/bash

cargo build --release -p atuin -p atuin-client -p atuin-common --no-default-features --features atuin/client

cp target/release/atuin ~/.local/share/bin/atuin
