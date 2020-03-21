#!/bin/bash
# Run my program.
python3 src/main.py & python3 src/db.py & python3 src/nameMap.py & python3 src/userAgent.py

exit 0