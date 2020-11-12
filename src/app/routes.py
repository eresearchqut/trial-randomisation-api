'''common routes'''
from flask import Blueprint, jsonify, request
from app.n_of_1 import randomise_schedule

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

    # message_id = repository.message.create_message(item)
    response = {
        'schedule': randomise_schedule(req_data['patients'], req_data['cycles'], req_data['treatments'])
    }
    status_code = 200
    return jsonify(response), status_code
