# Search POC

The app (vue on the frontend, flask for the API proxy) leverages the Zinio search API. The API endpoints and credentials are private, so you'll need your own.

![The search POC in action](search_poc_low.gif)

## How to run the app locally

Requires python 3.6+

1. Shell 1:
2. `cd server`
3. `flask run`
4. Shell 2:
5. `cd front`
6. `npm install`
7. `npm run serve`

## How to run the app publicly with ngrok

1. In server, `flask run`
2. `./ngrok start -all`
3. Get url for port 5000
4. Update backend end `.env.production` for prod with it
5. `npm run build`
6. `cd dist`
7. `python3 -m http.server 8081`
8. good to go
