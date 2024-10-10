#!/bin/bash

process_info=$(ps aux | grep '[i]nfinite.sh' | awk '{print $2, $11}')
pid=$(echo $process_info | awk '{print $1}')
processName=$(echo $process_info | awk '{print $2}')

if [ -n "$pid" ]; then
    kill $pid
    echo "Process $pid named $processName has been killed."
else
    echo "There is no running process for Infinite.sh"
fi
