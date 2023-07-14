# telldus
An example how to get information from Telldus API

## How to run it

1. Install *requirements.txt*
```
pip install -r requirements.txt
```
1. Copy *.env-template* to *.env*
2. Fill the variables in *.env* with the correct values. You find them here: [Telldus API Keys](https://api.telldus.com/keys/index)
```
client_id = ""
client_secret = ""
token = ""
token_secret = ""
```
3. Get a sensor id for you of your Telldus sensors.
4. Copy that sensor id to the sensor_id declaration in *main.py*.
5. Run main.py
```
alt 1:
py main.py

alt 2:
python main.py

alt 3:
python3 main.py
```