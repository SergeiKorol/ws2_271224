import requests

def test_add():
    body = {"title":"generated","completed":False}
    respons1e = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response_body123 = response1.json()

    assert response1.status_code == 201
    assert response_body123['completed'] == False

