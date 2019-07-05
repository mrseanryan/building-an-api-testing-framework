import pytest
import requests
from pprint import pformat

def build_url(suffix):
    return 'http://localhost:8000/' + suffix

def build_headers(token):
    headers = { 'user': 'sean', 'token': token }
    return headers

@pytest.fixture()
def create_book(get_token):
    book_json = {"title": "The Life and Times of Bob", "sub_title": None, "author": "Bob the Builder", "publisher": "Dorset House Publishing", "year": 2019, "pages": 666}

    response = requests.post(build_url('/books'), json = book_json, headers = build_headers(get_token))
    assert response.status_code == 201
    return response.json()

@pytest.fixture()
def get_token():
    response = requests.post(build_url('token/sean'))
    assert response.status_code == 201
    token = response.json()['token']
    return token

def test_delete_book(get_token, create_book):
    token = get_token
    book = create_book
    print("create_book: {}".format(pformat(book)))

    url = build_url('books/'+book['id'])
    print("url={}".format(url))
    response = requests.delete(url, headers = build_headers(token))

    assert response.status_code == 200
    