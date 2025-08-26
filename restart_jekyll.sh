#!/usr/bin/bash

# Variables

PORT=4001
TARGET_DIR="/home/kalibasenji42/jekyll/Xeroideas-Root"

# Find the PID(s) of Jekyll (Based on Port)
PIDS=$(lsof -t -i:$PORT )

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
if [ "$PWD" != "$TARGET_DIR" ]; then
  echo "Changing to directory: $TARGET_DIR"
  cd "$TARGET_DIR" || { echo "Failed to change directory to $TARGET_DIR"; exit 1; }
fi

# Start Jekyll
echo "Starting Jekyll..."
bundle exec jekyll serve -P $PORT -t &

# Confirm the process was started
if [ $? -eq 0 ]; then
  echo "Jekyll started successfully."
else
  echo "Failed to start Jekyll."
  exit 1
fi
