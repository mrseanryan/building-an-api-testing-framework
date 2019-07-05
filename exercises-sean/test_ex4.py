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
def create_book(get_books_api):
    book = get_books_api.create()
    return book

@pytest.fixture()
def get_token():
    api = api_client.TokenApi()
    return api.get()

@pytest.fixture()
def get_books_api(get_token):
    api = api_client.BooksApi(get_token)
    return api        

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

def test_get_books(get_books_api):
    books = get_books_api.get_books()
    assert len(books) > 0

def test_get_a_book(get_books_api):
    book_id = '9b30d321-d242-444f-b2db-884d04a4d806'
    book = get_books_api.get_book(book_id)
    assert len(book) > 0
