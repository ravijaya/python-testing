import requests
from demorestapis.psdemopostcall import do_login


def test_user_login(base_url):
    uri = base_url + '/login'
    status_code, token = do_login(uri)
    assert status_code == 200 and token == 'QpwL5tke4Pnpja7X4'


def test_list_users(base_url):
    uri = base_url + '/users?page=2'
    response = requests.get(uri)
    assert response.status_code == 200
    payload = response.json()
    assert payload['total'] == payload['page'] * payload['per_page']
