from authlib.integrations.httpx_client import OAuth1Auth
import httpx
import json
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
token = os.getenv("token")
token_secret = os.getenv("token_secret")
url_sensor_history_template = "https://api.telldus.com/json/sensor/history?id={}&includeHumanReadableDate=1"
sensor_id = 0

auth = OAuth1Auth(
    client_id=client_id,
    client_secret=client_secret,
    token=token,
    token_secret=token_secret,
)

url_sensor_history = url_sensor_history_template.format(sensor_id)
respone = httpx.get(url_sensor_history, auth=auth)
print(json.dumps(respone.text, indent=4))
