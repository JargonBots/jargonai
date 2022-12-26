#!/usr/bin/env bash

# echo "PWD: $PWD"
# echo `Content: ls -la`

set -e

# activate our virtual environment here
. /opt/pysetup/.venv/bin/activate
pushd /opt/pysetup && poetry shell && popd

exec "$@"