# run
from python:3.7-slim-buster
workdir /app
copy . .
run pip install -r requirements.txt
cmd ["python", "manager.py"]

## gunicorn
# from python:3.7-slim-buster
# workdir /app
# copy . .
# run pip install -r requirements.txt
# run pip install gunicorn
# cmd gunicorn -w 1 -b 0.0.0.0:5555 run:app
