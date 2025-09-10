from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.get("/")
def home():
    # Render a simple template with an H1
    return render_template("index.html")


@app.get("/api/ping")
def api_ping():
    return jsonify({"status": "ok", "message": "works"})

if __name__ == "__main__":
    # For local dev only; in production, use a WSGI server like gunicorn
    app.run(host="127.0.0.1", port=5000, debug=True)
