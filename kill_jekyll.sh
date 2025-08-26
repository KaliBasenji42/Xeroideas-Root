#!/usr/bin/bash

# Find the PID(s) of Jekyll
PIDS=$(pgrep bundle)

# Check if Jekyll is running
if [ -z "$PIDS" ]; then
  echo "No Jekyll process found."
  exit 1
fi

# Kill the Jekyll process(es)
echo "Killing Jekyll process(es) with PID(s): $PIDS"
kill -9 $PIDS

# Verify if the processes were killed
if [ $? -eq 0 ]; then
  echo "Jekyll process(es) terminated successfully."
else
  echo "Failed to terminate Jekyll process(es)."
fi
