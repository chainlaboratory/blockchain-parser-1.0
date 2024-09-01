#!/bin/bash

cron

while true; do
    current_second=$(date +%-S)
    if [ "$current_second" -eq 60 ]; then
          echo "Container aktiv"
    fi      
   
    sleep 3  # Warte 3 Sekunden, bevor die nächste Überprüfung erfolgt
done

exit 0
