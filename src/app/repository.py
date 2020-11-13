'''Message related operations'''
import os

from datetime import datetime
from uuid import uuid4, UUID
import boto3

TABLE_NAME = os.environ.get('TABLE_NAME', 'trial-randomisation-schedules')
AWS_REGION = os.environ.get('AWS_REGION', 'ap-southeast-2')
VERSION_ZERO = 'v0'


def __get_table():
    return boto3.resource('dynamodb', AWS_REGION).Table(TABLE_NAME)


def save_schedule(schedule: dict) -> UUID:
    '''Save the schedule into dynamodb'''
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
    '''Retrieve a schedule from dynamodb'''
    record = __get_table().get_item(
        Key={
            'pk': str(id),
            'sk': VERSION_ZERO
        }
    )
    item = record.get('Item', {})
    return item['schedule']
