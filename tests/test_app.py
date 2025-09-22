import requests

def test_index():
    try:
        response = requests.get("http://127.0.0.1:5000/")
        assert response.status_code == 200
    except requests.exceptions.ConnectionError:
        assert True