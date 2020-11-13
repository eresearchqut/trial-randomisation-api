import json
import app

from moto import mock_dynamodb2
from fixtures.dynamodb_client import mock_client
from uuid import UUID

app = app.create_app()


def test_health():
    response = app.test_client().get(
        '/health',
        content_type='application/json',
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['status'] == 'UP'

@mock_dynamodb2
def test_n_of_1_v1(mock_client):
    mock_client()
    response = app.test_client().post(
        '/n_of_1/v1',
        data=json.dumps({'patients': 1, 'cycles': 1, 'treatments': 1}),
        content_type='application/json',
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['schedule'] == [[['A']]]
    assert isinstance(UUID(data['id']), UUID)

@mock_dynamodb2
def test_n_of_1_v1_load(mock_client):
    mock_client()
    response = app.test_client().post(
        '/n_of_1/v1',
        data=json.dumps({'patients': 1, 'cycles': 2, 'treatments': 1}),
        content_type='application/json',
    )
    data = json.loads(response.get_data(as_text=True))
    response = app.test_client().get(
        '/n_of_1/v1/' + data['id'],
        content_type='application/json',
    )
    data = json.loads(response.get_data(as_text=True))
    assert data == [[['A'], ['A']]]