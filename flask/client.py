import requests
from datetime import datetime

# Send Request to Server with Time
result = requests.get("http://127.0.0.1:5000?time=" + str(datetime.now()))
print(result)