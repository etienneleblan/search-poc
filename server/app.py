from flask import Flask, request, make_response
import requests
import json
import time
import config

app = Flask('__main__')
# Stops flask from sorting JSON keys alphabetically, which alters the search results
app.config['JSON_SORT_KEYS'] = False

ZEN_URL = config.ZEN_URL
CLIENT_ID = config.CLIENT_ID
CLIENT_SECRET = config.CLIENT_SECRET

token_expiry = 0


def get_token():
    # GET ZENITH TOKEN
    url = f"{ZEN_URL}/oauth/v2/tokens"
    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials"
    }
    payload = json.dumps(payload)

    headers = {
        'Content-Type': "application/json"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    data = response.json()
    json_str = json.dumps(data)
    resp = json.loads(json_str)
    global zen_token
    zen_token = resp['access_token']
    global zen_token_expiry
    zen_token_expiry = int(time.time()) + 7100


get_token()

# Proxy to bypass CORS restrictions
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET'])
def proxy(path):
    path = request.full_path

    # Renews token if expiry date is in the past
    if zen_token_expiry < int(time.time()):
        get_token()
        print(f"token granted again, expiry {zen_token_expiry}")

    headers = {
        'Authorization': f'Bearer {zen_token}'
    }
    r = requests.get(url=f'{ZEN_URL}{path}',
                     headers=headers, verify=False)
    print(f'{ZEN_URL}{path}')

    # Get the response and make it usable by the frontend application
    resp = make_response(r.text)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Content-type'] = 'application/json'
    return resp


if __name__ == "__main__":
    app.run(debug=True)
