import requests
import pytest


@pytest.mark.http
def test_firs_request():
    r = requests.get("https://api.github.com/zen")
    print(f"Response is: {r.text}")

@pytest.mark.http
def test_second_request():
    r = requests.get("https://api.github.com/users/defunkt")

    body = r.json() #значення джейсону буде в змінній з таким іменем
    headers = r.headers
    
    # print(f"Response Body is: {r.json()}") #виводить джейсон формат
    # print(f"Response status code is {r.status_code}") #виводить статус код
    # print(f"Response headers are {r.headers}") #виводить хедери

    assert body['name'] == 'Chris Wanstrath'
    assert r.status_code == 200 #перевірка статус кода
    assert headers['Server'] == 'GitHub.com'


@pytest.mark.http
def test_status_code_request():
    r = requests.get("https://api.github.com/users/valentyn_yushchyshyn")

    assert r.status_code == 404

