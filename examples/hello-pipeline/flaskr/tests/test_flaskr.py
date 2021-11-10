import pytest
import flaskr

from unittest.mock import MagicMock

@pytest.fixture(scope='function')
def client():
    file = open('./tests/assets/model.pkl', 'rb')
    flaskr.open = MagicMock(return_value=file)
    flaskr.app.config['TESTING'] = True
    client = flaskr.app.test_client()

    yield client

def test_health_check(client):
    r = client.get('/')

    assert r.status == '200 OK'


@pytest.mark.parametrize('input, expected_output', [
    ({
        "SepalLengthCm": [5.4, 5.8, 7.1], 
        "SepalWidthCm": [3.4, 2.7, 3.0], 
        "PetalLengthCm": [1.7, 3.9, 5.9], 
        "PetalWidthCm": [0.2, 1.2, 2.1]
    }, '[Iris-virginica Iris-virginica Iris-virginica]'),
    ({
        "SepalLengthCm": [5.4], 
        "SepalWidthCm": [3.4], 
        "PetalLengthCm": [1.7], 
        "PetalWidthCm": [0.2]
    }, '[Iris-virginica]'),
    ({
        "SepalLengthCm": [5.4, 5.8], 
        "SepalWidthCm": [3.4, 2.7], 
        "PetalLengthCm": [1.7, 3.9], 
        "PetalWidthCm": [0.2, 1.2]
    }, '[Iris-virginica Iris-virginica]')
])
def test_get_predict(client, input, expected_output):
    r = client.get('/predict', json=input)

    assert r.data.decode("utf-8") == expected_output