from test.conftest import *
from flask import request


def test_base(prepare_db):
    res = client.get('/')
    assert res.status_code, 200


def test_drivers(prepare_db):
    response = client.get("/report/drivers")
    assert response.status_code, 200


def test_drivers_asc(prepare_db):
    response = client.get("/report/drivers?order=asc")
    assert response.status_code, 200


def test_drivers_desc(prepare_db):
    response = client.get("/report/drivers?order=desc")
    assert response.status_code, 200


def test_driver_id_middle_is_upper(prepare_db):
    response = client.post("/driver?driver_id=Svf")
    assert response.status_code, 200


def test_driver_id_lower(prepare_db):
    response = client.get("/driver?driver_id=svf")
    assert response.status_code == 500


def test_driver_id_upper(prepare_db):
    response = client.get("/driver?driver_id=VBM")
    assert response.status_code, 200


def test_500(prepare_db):
    response = client.get("/driver?driver_id=SDF")
    assert response.status_code, 500


def test_middle_500(prepare_db):
    response = client.get("/driver?driver_id=Sdv")
    assert response.status_code == 500


def test_lower_500(prepare_db):
    response = client.get("/driver?driver_id=sdv")
    assert response.status_code == 500


def test_report_request_args(prepare_db):
    with app.test_request_context('/report?order=asc'):
        assert request.path == '/report'
        assert request.args['order'] == 'asc'
    with app.test_request_context('/report?order=desc'):
        assert request.path == '/report'
        assert request.args['order'] == 'desc'


def test_drivers_request_args(prepare_db):
    with app.test_request_context('/report/drivers?order=asc'):
        assert request.path == '/report/drivers'
        assert request.args['order'] == 'asc'
    with app.test_request_context('/report/drivers?order=desc'):
        assert request.path == '/report/drivers'
        assert request.args['order'] == 'desc'
