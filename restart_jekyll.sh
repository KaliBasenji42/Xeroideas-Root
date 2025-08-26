#!/usr/bin/bash

# Find the PID(s) of Jekyll
PIDS=$(pgrep bundle)

# Check if Jekyll is running
if [ -z "$PIDS" ]; then
  echo "No Jekyll process found."
else
  # Kill the Jekyll process(es)
  echo "Killing Jekyll process(es) with PID(s): $PIDS"
  kill -9 $PIDS

  # Verify if the processes were killed
  if [ $? -eq 0 ]; then
    echo "Jekyll process(es) terminated successfully."
  else
    echo "Failed to terminate Jekyll process(es)."
    exit 1
  fi
fi

# Change to the correct directory
TARGET_DIR="/home/jekyll/Xeroideas-Root"
if [ "$PWD" != "$TARGET_DIR" ]; then
  echo "Changing to directory: $TARGET_DIR"
  cd "$TARGET_DIR" || { echo "Failed to change directory to $TARGET_DIR"; exit 1; }
fi

# Start Jekyll
echo "Starting Jekyll..."
bundle exec jekyll serve -P 4001 -t &

# Confirm the process was started
if [ $? -eq 0 ]; then
  echo "Jekyll started successfully."
else
  echo "Failed to start Jekyll."
  exit 1
fi
