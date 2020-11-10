import json
import numpy as np
import requests
import string


rng = np.random.default_rng()

class HttpVerb:
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'
    HEAD = 'HEAD'
    DELETE = 'DELETE'
    OPTIONS = 'OPTIONS'
    ALL = '*'


def lambda_handler(event, context):
    """n_of_1 api request handler

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    print("Received event: " + json.dumps(event, indent=2))

    try:
        ip = requests.get("http://checkip.amazonaws.com/")
        return {
            "statusCode": 200,
            "body": json.dumps({
                "type": "n_of_1",
                "ip": ip.text.rstrip(),
                "schedule": randomise_schedule(5, 3, 4)
            }, cls=NumpyEncoder),
        }
    except requests.RequestException as e:
        print(e)
        raise e


def randomise_schedule(number_of_patients: int, number_of_cycles: int, number_of_treatments: int):
    return [repeat_treatment(number_of_cycles, number_of_treatments) for _ in range(number_of_patients)]


def repeat_treatment(number_of_cycles: int, number_of_treatments: int):
    return [shuffle_treatment(number_of_treatments) for _ in range(number_of_cycles)]


def shuffle_treatment(number_of_treatments: int):
    treatments = list(string.ascii_uppercase)[:number_of_treatments]
    rng.shuffle(treatments)
    return treatments


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)
