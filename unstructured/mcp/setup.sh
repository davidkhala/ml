#!/usr/bin/env bash
set -euo pipefail

CONFIG_DIR="$HOME/.bob/settings"
CONFIG_FILE="$CONFIG_DIR/mcp.json"
SERVER_NAME="unstructured-transform"
SERVER_URL="https://mcp.transform.unstructured.io"

install() {
  mkdir -p "$CONFIG_DIR"

  CONFIG_FILE="$CONFIG_FILE" SERVER_NAME="$SERVER_NAME" SERVER_URL="$SERVER_URL" node <<'EOF'
const fs = require('fs');
const path = process.env.CONFIG_FILE;
const serverName = process.env.SERVER_NAME;
const serverUrl = process.env.SERVER_URL;

const serverConfig = {
  command: 'npx',
  args: ['-y', 'mcp-remote', serverUrl],
  alwaysAllow: [
    'request_file_upload_url',
    'start_transform_job',
    'check_job_status',
    'get_job_results',
    'start_extraction_job',
    'suggest_extraction_schema_for_file',
    'get_instructions'
  ],
  disabled: false
};

let config = {};

if (fs.existsSync(path)) {
  config = JSON.parse(fs.readFileSync(path, 'utf8'));
}

if (!config.mcpServers || typeof config.mcpServers !== 'object' || Array.isArray(config.mcpServers)) {
  config.mcpServers = {};
}

config.mcpServers[serverName] = serverConfig;

fs.writeFileSync(path, `${JSON.stringify(config, null, 2)}\n`);
EOF

  echo "Updated MCP config at $CONFIG_FILE"
 
  npx -y mcp-remote "$SERVER_URL"
}

uninstall() {
  if [ ! -f "$CONFIG_FILE" ]; then
    echo "Config file not found: $CONFIG_FILE"
    return 0
  fi

  CONFIG_FILE="$CONFIG_FILE" SERVER_NAME="$SERVER_NAME" node <<'EOF'
const fs = require('fs');
const path = process.env.CONFIG_FILE;
const serverName = process.env.SERVER_NAME;

const config = JSON.parse(fs.readFileSync(path, 'utf8'));

if (!config.mcpServers || typeof config.mcpServers !== 'object' || Array.isArray(config.mcpServers)) {
  process.exit(0);
}

delete config.mcpServers[serverName];

fs.writeFileSync(path, `${JSON.stringify(config, null, 2)}\n`);
EOF

  echo "Removed $SERVER_NAME from $CONFIG_FILE"
}

"$@"
