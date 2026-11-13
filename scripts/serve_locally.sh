#!/usr/bin/env bash
# Build the site and serve it at http://localhost:4000.
#
#   scripts/serve_locally.sh                # build once and serve
#   scripts/serve_locally.sh --watch        # rebuild when a file changes
#
# Any option is passed on to `jekyll serve`.
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

if ! command -v ruby >/dev/null 2>&1; then
  echo "Ruby is not installed or not on PATH." >&2
  exit 1
fi

# Run the Bundler that belongs to the Ruby on PATH. The `bundle` launcher on
# PATH can belong to a Ruby that is no longer installed, and then it does not
# start.
if ! bundler_exe="$(ruby -e 'print Gem.bin_path("bundler", "bundle")' 2>/dev/null)"; then
  echo "Bundler is not installed for $(ruby -v). Run: gem install bundler" >&2
  exit 1
fi
bundle() { ruby "$bundler_exe" "$@"; }

# Use that Bundler as it is. Otherwise Bundler downloads the version recorded
# in Gemfile.lock and restarts itself through the launcher on PATH.
export BUNDLE_VERSION=system

# Install the gems on the first run, and again after Ruby or the Gemfile changes.
if ! bundle check >/dev/null 2>&1; then
  echo "Installing gems for Ruby $(ruby -e 'print RUBY_VERSION') ..."
  bundle install
fi

exec ruby "$bundler_exe" exec jekyll serve --no-watch "$@"
