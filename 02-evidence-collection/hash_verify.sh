#!/usr/bin/env bash
# hash_verify.sh — compute and optionally verify a SHA-256 hash for a forensic
# disk image, and log the result with a timestamp for chain-of-custody records.
#
# Usage:
#   ./hash_verify.sh <image-file>                     # compute & log hash
#   ./hash_verify.sh <image-file> <expected-sha256>    # compute & compare

set -euo pipefail

IMAGE="${1:?Usage: $0 <image-file> [expected-sha256]}"
EXPECTED="${2:-}"
LOG_FILE="hash_log.csv"

if [[ ! -f "$IMAGE" ]]; then
  echo "ERROR: file not found: $IMAGE" >&2
  exit 1
fi

TIMESTAMP="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
HASH="$(sha256sum "$IMAGE" | awk '{print $1}')"

echo "File:      $IMAGE"
echo "SHA-256:   $HASH"
echo "Timestamp: $TIMESTAMP (UTC)"

if [[ -n "$EXPECTED" ]]; then
  if [[ "$HASH" == "$EXPECTED" ]]; then
    echo "RESULT:    MATCH — image integrity verified"
    STATUS="MATCH"
  else
    echo "RESULT:    MISMATCH — image may have been altered!" >&2
    STATUS="MISMATCH"
  fi
else
  STATUS="RECORDED"
fi

# Append to a simple CSV log for the chain-of-custody paper trail
if [[ ! -f "$LOG_FILE" ]]; then
  echo "timestamp_utc,file,sha256,status" > "$LOG_FILE"
fi
echo "${TIMESTAMP},${IMAGE},${HASH},${STATUS}" >> "$LOG_FILE"