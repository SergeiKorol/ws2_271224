import requests


def test_id():
    body = {"title": "generated", "completed": False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    first_id = response.json()["id"]

    body = {"title": "generated-1"}
    response = requests.patch(f'https://todo-app-sky.herokuapp.com/{first_id}', json=body)
    updated_id = response.json()["id"]

    assert first_id == updated_id
    assert response.status_code == 200
