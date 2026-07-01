import requests

def test_get_taches():
    response = requests.get("http://localhost:8000/taches")

    assert response.status_code == 200
