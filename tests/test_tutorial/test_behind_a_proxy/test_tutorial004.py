from fastapi.testclient import TestClient

from docs_src.behind_a_proxy.tutorial004 import app

client = TestClient(app)


def test_main():
    response = client.get("/app")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World", "root_path": "/api/v1"}


def test_openapi():
    response = client.get("/openapi.json")
    assert response.status_code == 200
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "FastAPI", "version": "0.1.0"},
        "servers": [
            {"url": "https://stag.example.com", "description": "Staging environment"},
            {
                "url": "https://prod.example.com",
                "description": "Production environment",
            },
        ],
        "paths": {
            "/app": {
                "get": {
                    "summary": "Read Main",
                    "operationId": "read_main_app_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        }
                    },
                }
            }
        },
    }
