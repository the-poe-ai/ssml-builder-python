from fastapi.testclient import TestClient
from ssml.api.server import app

client = TestClient(app)


def test_generate_ssml_api():
    resp = client.post(
        "/api/ssml",
        json={
            "elements": [
                {"type": "text", "text": "Hello"},
                {"type": "break", "time": "300ms"},
                {"type": "say_as", "text": "2025", "interpret_as": "digits"},
            ]
        },
    )
    assert resp.status_code == 200
    data = resp.json()
    assert "ssml" in data
    assert data["ssml"].startswith("<speak>")
