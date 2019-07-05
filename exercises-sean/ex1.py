
# Print the status code and response for the following API calls:
# - GET knockknock
# - GET books
# - GET one book
# - POST a book
# - POST token

import requests

run_summary = ""

def fail(actual, expected, fail_message):
    global run_summary
    print("FAIL: " + fail_message)
    print("actual: " + str(actual))
    print("expected: " + str(expected))
    run_summary += "F"

def pass_test():
    global run_summary
    run_summary += "."

def assert_that(actual, expected, fail_message):
    if actual != expected:
        fail(actual, expected, fail_message)
        return False
    else:
        pass_test()
        return True

def assert_that_is_set(actual, fail_message):
    if len(actual) == 0:
        fail(actual, "<something!>", fail_message)
        return False
    else:
        pass_test()
        return True

def make_request_and_check_response(test_name, url, expected_status = 200):
    test_name += ": "

    response = requests.get(url)
    assert_that(response.status_code, expected_status, test_name + "Response status is not OK!")
    assert_that_is_set(response.text, test_name + "Response text is not set!")
    # TODO could check JSON is valid

def make_post_request_and_check_response(test_name, url, data_object, expected_status = 200, headers = None):
    test_name += ": "

    ## post - does NOT need a token - put DOES
    response = requests.post(url, json = data_object, headers = headers)
    assert_that(response.status_code, expected_status, test_name + "Response status is not OK!")

    if response.status_code == 200:
        assert_that_is_set(str(response.json()), test_name + "Response text is not set!")
    # TODO could check JSON is valid

def make_put_request_and_check_response(test_name, url, data_object, expected_status = 200, headers = None):
    test_name += ": "

    ## post - does NOT need a token - put DOES
    response = requests.put(url, json = data_object, headers = headers)
    if not assert_that(response.status_code, expected_status, test_name + "Response status is not OK!"):
        print("response:" + str(response.text))

    if response.status_code == 200:
        assert_that_is_set(str(response.json()), test_name + "Response text is not set!")
    # TODO could check JSON is valid

# TODO avoid dupe url
make_request_and_check_response('GET knockknock', 'http://localhost:8000/knockknock')
make_request_and_check_response('GET books', 'http://localhost:8000/books')
make_request_and_check_response('GET a non-existing book', 'http://localhost:8000/books/666', 400)
book_id = '9b30d321-d242-444f-b2db-884d04a4d806'
make_request_and_check_response('GET a book', 'http://localhost:8000/books/' + book_id)

# **PUT /books/{book-id}**
# requires token    
#request body: book details (no id) (json)  
#return code: 200  
#return body: updated book (json)# - POST a book

book_json = {"title": "The Life and Times of Bob", "sub_title": None, "author": "Bob the Builder", "publisher": "Dorset House Publishing", "year": 2019, "pages": 666}

## post - does NOT need a token - put DOES
make_post_request_and_check_response("post a book - no token", 'http://localhost:8000/books', book_json, 201)

# - POST token
response = requests.post('http://localhost:8000/token/sean')
token = response.json()['token']

# in HEADER:
headers = { 'user': 'sean', 'token': token }
## post - does NOT need a token - put DOES
make_post_request_and_check_response("post a book - WITH token", 'http://localhost:8000/books', book_json, 201, headers)

# PUT /token/{user}**  
# request body: none  
make_put_request_and_check_response("put a book - WITH token - non-existing book", 'http://localhost:8000/books/123', book_json, 400, headers)

make_put_request_and_check_response("put a book - WITH token - existing book", 'http://localhost:8000/books/9b30d321-d242-444f-b2db-884d04a4d806', book_json, 200, headers)

# return code: 201  
# return body: token (json)

print("result:" + run_summary)
