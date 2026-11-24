#!/bin/bash
set -e
SRC=$1
rsync -a --exclude venv --exclude todo.db --exclude .git "$SRC"/ /opt/todo/
python3 -m venv /opt/todo/venv
/opt/todo/venv/bin/pip install -r /opt/todo/requirements.txt
sudo systemctl restart todo
sleep 3
curl -f http://127.0.0.1:5000/health