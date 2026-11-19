#!/bin/bash
set -e

PROJECT_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"

echo "Building EdgeLite OS from: $PROJECT_ROOT"

exec "$PROJECT_ROOT/scripts/build.sh" "$@"
