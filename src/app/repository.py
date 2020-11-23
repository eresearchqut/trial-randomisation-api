"""Message related operations"""
import os
import boto3
import json

from datetime import datetime
from uuid import uuid4, UUID


TABLE_NAME = os.environ.get('TABLE_NAME', 'trial-randomisation-schedules')
AWS_REGION = os.environ.get('AWS_REGION', 'ap-southeast-2')
AWS_SAM_LOCAL = json.loads(os.environ.get('AWS_SAM_LOCAL', 'false'))
LOCAL_ENDPOINT = os.environ.get('ENDPOINT_URL', 'http://dynamodb:8000')

VERSION_ZERO = 'v0'

print(TABLE_NAME)

def __get_table():
    return boto3.resource('dynamodb', endpoint_url=LOCAL_ENDPOINT).Table(TABLE_NAME) \
        if AWS_SAM_LOCAL else boto3.resource('dynamodb', region_name=AWS_REGION).Table(TABLE_NAME)


def save_schedule(schedule: dict) -> UUID:
    """Save the schedule into dynamodb"""
    item = dict()
    id = uuid4()
    item['pk'] = str(id)
    item['sk'] = VERSION_ZERO
    item['schedule'] = schedule
    item['timestamp'] = datetime.utcnow().isoformat()
    __get_table().put_item(
        Item=item
    )
    return id


def load_schedule(id: UUID) -> dict:
    """Retrieve a schedule from dynamodb"""
    record = __get_table().get_item(
        Key={
            'pk': str(id),
            'sk': VERSION_ZERO
        }
    )
    item = record.get('Item', {})
    return item['schedule']
