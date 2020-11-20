#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

# Build the sdists and wheels
for package_repo in */; do
    if [[ "$package_repo" == ".packages" ]]; then
        continue
    fi
    python -m build --sdist --wheel $package_repo
done

# Copy to the PyPI test server
cp ./*/dist/* .packages/
