from flask import Flask
from routes import routes
import json

app = Flask(__name__)
routes(app)
client = app.test_client()
mock_request_header = {"Content-Type": "application/json"}
mock_request_data = {"string_to_cut": "iamyourlyftdriver"}

def test_base_route():
    url = "/"

    response = client.get(url)
    assert response.status_code == 200
    assert response.get_data() == "Home Page"

def test_post_test_route_success():
    url = "/test"

    response = client.post(url, data=json.dumps(mock_request_data), headers=mock_request_header)
    assert response.status_code == 201
    assert response.get_data().rstrip("\n") == '{"return_string":"muydv"}'

def test_post_test_route_success_length_than_three():
    url = "/test"
    mock_request_data = {"string_to_cut": "ia"}

    response = client.post(url, data=json.dumps(mock_request_data), headers=mock_request_header)
    assert response.status_code == 201
    assert response.get_data().rstrip("\n") == '{"return_string":""}'

def test_post_test_route_success_special_character():
    url = "/test"
    mock_request_data = {"string_to_cut": "@@@###$$$!!!^^^&&&"}

    response = client.post(url, data=json.dumps(mock_request_data), headers=mock_request_header)
    assert response.status_code == 201
    assert response.get_data().rstrip("\n") == '{"return_string":"@#$!^&"}'

def test_post_test_route_success_space_character():
    url = "/test"
    mock_request_data = {"string_to_cut": "      "}

    response = client.post(url, data=json.dumps(mock_request_data), headers=mock_request_header)
    assert response.status_code == 201
    assert response.get_data().rstrip("\n") == '{"return_string":"  "}'

def test_post_test_route_failure_invalid_data_type_integer():
    url = "/test"
    mock_request_data = {"string_to_cut": 12354}

    response = client.post(url, data=json.dumps(mock_request_data), headers=mock_request_header)
    assert response.status_code == 422
    assert response.get_data().rstrip("\n") == '{"error":"Data Type Error! Please enter string"}'

def test_post_test_route_failure_invalid_data_type_boolean():
    url = "/test"
    mock_request_data = {"string_to_cut": True}

    response = client.post(url, data=json.dumps(mock_request_data), headers=mock_request_header)
    assert response.status_code == 422
    assert response.get_data().rstrip("\n") == '{"error":"Data Type Error! Please enter string"}'

def test_post_test_route_failure_invalid_json():
    url = "/test"
    mock_request_data = None

    response = client.post(url, data=json.dumps(mock_request_data), headers=mock_request_header)
    assert response.status_code == 422
    assert response.get_data().rstrip("\n") == '{"error":"Unable to process posted data!"}'

def test_post_test_route_failure_empty_json():
    url = "/test"
    mock_request_data = {}

    response = client.post(url, data=json.dumps(mock_request_data), headers=mock_request_header)
    assert response.status_code == 422
    assert response.get_data().rstrip("\n") == '{"error":"Unable to process posted data!"}'

def test_post_test_route_failure_without_body():
    url = "/test"

    response = client.post(url, headers=mock_request_header)
    assert response.status_code == 400