# HypatiaAuth

### By Skye Lane Goetz

HypatiaAuth is a minimal CLI for generating and securely storing API keys, utilizing Redis for fast storage and xxhash for secure key hashing.

## Quick Start

```bash
# Install dependencies using uv
uv sync

# Verify install
uv run main.py --help
```

## Generate Command

```bash
# Generate a new API key for a user
uv run main.py <username>
```

### Arguments

| Argument | Required | Default | Description |
| --- | --- | --- | --- |
| `username` | Yes | N/A | The username to generate an API key for |

### Output Artifacts

- Generates a secure, URL-safe API key prefixed with the username.
- Hashes the key using `xxhash` and stores it in a local Redis instance (`localhost:6379`) (when enabled).
- Prints the generated credentials to the console for secure storage.

### Examples

```bash
# Generate an API key for user 'alice'
uv run main.py alice
```

### Runtime Behavior

- Connects to a local Redis instance on port 6379 (db=0).
- Keys are hashed before storage to ensure security.
- The raw API key is only displayed once and is not stored.

## Maintainer

Skye Lane Goetz
