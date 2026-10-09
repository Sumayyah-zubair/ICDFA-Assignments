#!/bin/bash
# Educational monitoring example. Does not access production logs or credentials.
LOG_FILE="./monitoring/security_monitor.log"
date '+%Y-%m-%d %H:%M:%S - Monitoring check executed' >> "$LOG_FILE"
echo "Monitoring check recorded in $LOG_FILE"
