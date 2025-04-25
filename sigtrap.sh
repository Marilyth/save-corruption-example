#!/bin/bash

LOGFILE="signals.log"

handle_signal() {
  echo "Received signal: $1 at $(date)" >> "$LOGFILE"
  exit 0
}

for sig in HUP INT QUIT TERM USR1 USR2; do
  trap "handle_signal $sig" $sig
done

echo "Waiting for signal... (PID $$)"
while true; do sleep 1; done

