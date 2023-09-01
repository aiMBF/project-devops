#!/bin/bash
# wait-for-it.sh
# Wait for a service to become available

# Parse command-line arguments
while [[ $# -gt 0 ]]; do
  case "$1" in
    --host=*)
      host="${1#*=}"
      shift
      ;;
    --port=*)
      port="${1#*=}"
      shift
      ;;
    --timeout=*)
      timeout="${1#*=}"
      shift
      ;;
    *)
      echo "Invalid argument: $1"
      exit 1
      ;;
  esac
done

# Default values if not provided
host=${host:-db}
port=${port:-5432}
timeout=${timeout:-60}

echo "Waiting for service to become available at $host:$port..."

while ! nc -z "$host" "$port"; do
  sleep 1
  ((timeout--))
  if [ "$timeout" -le 0 ]; then
    echo "Service not available, timed out."
    exit 1
  fi
done

echo "Service is available!"
