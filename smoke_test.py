from app import app


def test_root_html():
    with app.test_client() as c:
        r = c.get("/")
        assert r.status_code == 200
        assert b"<h1>Hello, World!</h1>" in r.data


def test_api_ping():
    with app.test_client() as c:
        r = c.get("/api/ping")
        assert r.status_code == 200
        assert r.is_json
        assert r.get_json() == {"status": "ok", "message": "pong"}


if __name__ == "__main__":
    test_root_html()
    test_api_ping()
    print("Smoke test passed: '/' shows H1 and '/api/ping' returns JSON")
