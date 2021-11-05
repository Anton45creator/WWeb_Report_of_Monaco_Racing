from flask import request

from app import app

client = app.test_client()


def test_base():
    res = client.get('/')
    assert res.status_code == 200


def test_drivers():
    response = client.get("/report/drivers")
    assert response.status_code == 200


def test_drivers_asc():
    response = client.get("/report/drivers?order=asc")
    assert response.status_code == 200


def test_drivers_desc():
    response = client.get("/report/drivers?order=desc")
    assert response.status_code == 200


def test_driver_id_middle_is_upper():
    response = client.post("/driver?driver_id=Svf")
    assert response.status_code, 200


def test_driver_id_lower():
    response = client.get("/driver?driver_id=svf")
    assert response.status_code == 500


def test_driver_id_upper():
    response = client.get("/driver?driver_id=VBM")
    assert response.status_code, 200


def test_500():
    response = client.get("/driver?driver_id=SDF")
    assert response.status_code, 500


def test_middle_500():
    response = client.get("/driver?driver_id=Sdv")
    assert response.status_code == 500


def test_lower_500():
    response = client.get("/driver?driver_id=sdv")
    assert response.status_code == 500


def test_driver_id_args():
    with app.test_request_context('/driver?driver_id=VBM'):
        assert request.path == '/driver'
        assert request.args['driver_id'] == 'VBM'


def test_report_request_args():
    with app.test_request_context('/report?order=asc'):
        assert request.path == '/report'
        assert request.args['order'] == 'asc'
    with app.test_request_context('/report?order=desc'):
        assert request.path == '/report'
        assert request.args['order'] == 'desc'


def test_drivers_request_args():
    with app.test_request_context('/report/drivers?order=asc'):
        assert request.path == '/report/drivers'
        assert request.args['order'] == 'asc'
    with app.test_request_context('/report/drivers?order=desc'):
        assert request.path == '/report/drivers'
        assert request.args['order'] == 'desc'
