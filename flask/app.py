from flask import Flask, request
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    args = request.args
    time = args.get("time")
    a = datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f")
    b = datetime.now()

    # Calculate Time
    print("Time Taken from client to server")
    print(b-a)
    return {"Response": "Success"}