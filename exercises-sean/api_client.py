import requests


def build_url(suffix):
    return 'http://localhost:8000/' + suffix


class KnockKnockApi():  # class MyClass(): in Python 3
    def __init__(self):
        # this code is run when instantiating the class my_class = MyClass()
        # one thing you can do here, is store the endpoint of the url:
        self.url = build_url("knockknock")

    def get(self):
        # this code is run for an instance with my_class.my_method()
        # so if we want to the GET of our smoketest:
        return requests.get(self.url)


class TokenApi():
    def __init__(self):
        self.url = build_url("token")

    def get(self):
        response = requests.post(self.url + '/sean')
        assert response.status_code == 201
        token=response.json()['token']
        return token

class TokenUtils():
    @staticmethod
    def build_headers(token):
        headers={'user': 'sean', 'token': token}
        return headers

class BooksApi():
    def __init__(self, token):
        self.url=build_url("books")
        self.token = token

    def create(self):
        book_json={"title": "The Life and Times of Bob", "sub_title": None, "author": "Bob the Builder",
            "publisher": "Dorset House Publishing", "year": 2019, "pages": 666}

        response = requests.post(self.url, json=book_json,
                               headers = TokenUtils.build_headers(self.token))
        assert response.status_code == 201
        return response.json()

    def delete(self, id):
        url = self.url + '/'+ id
        response = requests.delete(url, headers = TokenUtils.build_headers(self.token))

        assert response.status_code == 200
