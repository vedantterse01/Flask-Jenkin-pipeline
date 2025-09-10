# Flask Hello World

A minimal Flask app with:
- An HTML homepage rendered from a template showing an H1 “Hello, World!”
- A tiny JSON endpoint at `/api/ping` that returns `{ "status": "ok", "message": "pong" }`

## Prerequisites
- Python 3.9+ installed and on PATH

## Setup (Windows PowerShell)

```powershell
# 1) Create and activate a virtual environment
python -m venv .venv
. .\.venv\Scripts\Activate.ps1

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run the app
python app.py
# App listens on http://127.0.0.1:5000/

# View it
# - Open http://127.0.0.1:5000 to see the H1 page
# - Try http://127.0.0.1:5000/api/ping for a JSON response
```

## Alternative: Use Flask's built-in runner
```powershell
$env:FLASK_APP = "app:app"; $env:FLASK_ENV = "development"; flask run
```

## Test quickly without starting server
```powershell
python smoke_test.py
```
