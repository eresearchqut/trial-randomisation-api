'''common routes'''
from flask import Blueprint, jsonify, request
from app.n_of_1 import randomise_n_of_1_schedule
from app.repository import save_schedule, load_schedule
from uuid import UUID

routes = Blueprint('routes', __name__)


@routes.route('/health', methods=['GET'])
def health():
    '''health endpoint'''
    response = {'status': 'UP'}
    status_code = 200
    return jsonify(response), status_code


@routes.route('/n_of_1/v1', methods=['POST'])
def n_of_1_v1():
    '''n-of-1 endpoint'''
    req_data = request.get_json(force=True)
    schedule = randomise_n_of_1_schedule(req_data['patients'], req_data['cycles'], req_data['treatments'])
    id = save_schedule(schedule)
    # message_id = repository.message.create_message(item)
    response = {
        'id': id,
        'schedule': schedule
    }
    status_code = 200
    return jsonify(response), status_code


@routes.route('/n_of_1/v1/<id>', methods=['GET'])
def n_of_1_v1_load(id: UUID):
    '''n-of-1 endpoint'''
    schedule = load_schedule(id)
    status_code = 200
    return jsonify(schedule), status_code
