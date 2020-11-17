import pytest
import boto3


from moto import mock_dynamodb2


@pytest.fixture
def mock_client():
    @mock_dynamodb2
    def dynamodb_client():
        dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-2')
        # Create the table
        dynamodb.create_table(
            TableName='trial-randomisation-schedules',
            KeySchema=[
                {
                    'AttributeName': 'pk',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'sk',
                    'KeyType': 'RANGE'
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'pk',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'sk',
                    'AttributeType': 'S'
                },
            ],
            BillingMode='PAY_PER_REQUEST'
        )
        return dynamodb
    return dynamodb_client
