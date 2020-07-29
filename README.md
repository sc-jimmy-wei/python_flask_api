# Web Application - GET & POST
Sample web application demonstrating using GET & POST. Added a couple unit tests using Pytest to test the routes.

## Setup
Install Flask
    pip install Flask

Install pytest
    pip install pytest

To run in local server:
1) In terminal, navigate to PythonAPI folder
2) run `python app.py` to start local server
3) navigate to `http://localhost:5000/` in a browser
4) can use curl in terminal to call API
e.g. curl -X POST http://localhost:5000/test --data '{"string_to_cut": "@@@###$$$!!!^^^&&&"}' -H 'Content-Type: application/json'

To run pytest:
1) In terminal, navigate to PythonAPI folder
2) run `pytest` to run unit test suite
3) check result in terminal