# reunite-server
Included services:
- Web API (to serve web app &amp; mobile apps)
- SMS/phone services


## Development

Activate the virtual env & install dependencies (make sure you have pip & virtualenv installed first)

```
$ source env/bin/activate
$ pip install -r requirements.txt
```

Add the firebase api key to your environment (ask somebody for this, it's a secret)
```
$ export FIREBASE_API_KEY=<key>
```

Run the server
```
$ python api/server.py
```
