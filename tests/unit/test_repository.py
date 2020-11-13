from moto import mock_dynamodb2
from fixtures.dynamodb_client import mock_client
from uuid import UUID
from app import repository


@mock_dynamodb2
def test_save_schedule(mock_client):
    mock_client()
    id = repository.save_schedule([[['A']]])
    assert isinstance(id, UUID)


@mock_dynamodb2
def test_load_schedule(mock_client):
    mock_client()
    id = repository.save_schedule([[['B']]])
    schedule = repository.load_schedule(id)
    assert schedule == [[['B']]]






