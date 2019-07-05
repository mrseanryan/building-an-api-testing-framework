import pytest
import requests
from pprint import pformat

import api_client

def build_url(suffix):
    return 'http://localhost:8000/' + suffix

def build_headers(token):
    headers = { 'user': 'sean', 'token': token }
    return headers

@pytest.fixture()
def create_book(get_token):
    api = api_client.BooksApi(get_token)
    book = api.create()
    return book

@pytest.fixture()
def get_token():
    api = api_client.TokenApi()
    return api.get()

def test_delete_book(get_token, create_book):
    token = get_token
    book = create_book
    books_api = api_client.BooksApi(token)
    books_api.delete(book['id'])
    
def test_knockknock():
    api = api_client.KnockKnockApi()
    response = api.get()
    assert response.status_code == 200
    assert len(response.text) > 0
