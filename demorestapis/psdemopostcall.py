import requests


def do_login(uri='https://reqres.in/api/login'):
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = requests.post(uri, json=payload)
    return response.status_code, response.json()['token']


if __name__ == '__main__':
    print(do_login())
