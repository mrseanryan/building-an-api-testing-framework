
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
    else:
        pass_test()

def assert_that_is_set(actual, fail_message):
    if len(actual) == 0:
        fail(actual, "<something!>", fail_message)
    else:
        pass_test()

def make_request_and_check_response(test_name, url, expected_status = 200):
    test_name += ": "

    response = requests.get(url)
    assert_that(response.status_code, expected_status, test_name + "Response status is not OK!")
    assert_that_is_set(response.text, test_name + "Response text is not set!")
    # TODO could check JSON is valid

make_request_and_check_response('GET knockknock', 'http://localhost:8000/knockknock')
make_request_and_check_response('GET books', 'http://localhost:8000/books')
make_request_and_check_response('GET a non-existing book', 'http://localhost:8000/books/666', 400)
make_request_and_check_response('GET a book', 'http://localhost:8000/books/9b30d321-d242-444f-b2db-884d04a4d806')

print("result:" + run_summary)
