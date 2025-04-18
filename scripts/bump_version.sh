#!/usr/bin/env bash

set -e

# Usage: ./bump_version.sh PATCH|MINOR|MAJOR
LEVEL=${1:-PATCH}
poetry version $LEVEL
NEW_TAG=$(poetry version --short)
 git add pyproject.toml
 git commit -m "chore: bump version to $NEW_TAG"
 git tag "v$NEW_TAG"
 echo "Bumped version and created tag v$NEW_TAG"
