# API app

## Notes
`gunicorn --reload api_app.app` (linux, mac) or `waitress-serve --port=8000 api_app:app` (win)
`http localhost:8000/images`
`http --json POST localhost:8000/images foo=bar`