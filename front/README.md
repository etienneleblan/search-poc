# search poc

## How to run the app locally

1. Shell 1:
2. `cd server`
3. `flask run`
4. Shell 2:
5. `cd front`
6. `npm run serve`

## How to run the app publicly with ngrok

1. In server, `flask run`
2. `./ngrok start -all`
3. Get url for port 5000
4. Update backend end `.env.production` for prod with it
5. `npm run build`
6. `cd dist`
7. `python3 -m http.server 8081`
8. good to go

## Project setup

```
npm install
```

### Compiles and hot-reloads for development

```
npm run serve
```

### Compiles and minifies for production

```
npm run build
```

### Lints and fixes files

```
npm run lint
```

### Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/).
