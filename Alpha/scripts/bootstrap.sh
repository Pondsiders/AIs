#!/usr/bin/env bash
# bootstrap.sh — write a template env file for alpha-mechanism.
#
# Run once on a fresh VM after `claude plugin install Alpha@AIs`. Writes a
# template to $XDG_CONFIG_HOME/alpha/env (default ~/.config/alpha/env) with
# placeholder values. Edit the file to fill in real connection strings.
#
# Safe to re-run: refuses to overwrite an existing env file.

set -euo pipefail

CONFIG_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/alpha"
ENV_FILE="$CONFIG_DIR/env"

if [[ -f "$ENV_FILE" ]]; then
    echo "$ENV_FILE already exists. Not overwriting."
    exit 0
fi

mkdir -p "$CONFIG_DIR"
chmod 700 "$CONFIG_DIR"

cat > "$ENV_FILE" <<'EOF'
# alpha-mechanism configuration.
# Edit these values before running `claude`.

DATABASE_URL=postgresql://USER:PASSWORD@HOST:PORT/DATABASE

# PROD_DATABASE_URL is only needed for `copy-from-prod`. Leave commented
# out in production runtime.
# PROD_DATABASE_URL=postgresql://alpha_reader:PASSWORD@HOST:PORT/DATABASE
EOF

chmod 600 "$ENV_FILE"

echo "Wrote template to $ENV_FILE"
echo "Edit it to fill in connection strings, then run claude."
