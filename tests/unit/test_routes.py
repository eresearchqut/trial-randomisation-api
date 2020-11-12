import json
import app

app = app.create_app()


def test_health():
    response = app.test_client().get(
        '/health',
        content_type='application/json',
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['status'] == 'UP'


def test_n_of_1_v1():
    response = app.test_client().post(
        '/n_of_1/v1',
        data=json.dumps({'patients': 1, 'cycles': 1, 'treatments': 1}),
        content_type='application/json',
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['schedule'] == [[['A']]]