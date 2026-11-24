#!/bin/bash
if curl -sf http://127.0.0.1:5000/health > /dev/null; then
  echo "$(date) OK"
else
  echo "$(date) FAIL: app not responding"
fi
USAGE=$(df / --output=pcent | tail -1 | tr -dc '0-9')
if [ "$USAGE" -gt 80 ]; then
  echo "$(date) WARNING: disk usage at ${USAGE}%"
fi
exit 0