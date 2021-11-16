from test.conftest import *
from flask import request


def test_report(prepare_db):
    response = client.get("/api/v1/report")
    assert response.status_code, 200


def test_driver_id_middle_is_upper(prepare_db):
    response = client.get("/api/v1/driver/Svf")
    assert response.status_code, 200


def test_driver_id_lower(prepare_db):
    response = client.get("/api/v1/driver?SVF")
    assert response.status_code, 200


def test_drivers_id_upper(prepare_db):
    response = client.get("/api/v1/driver/svf")
    assert response.status_code, 200


def test_driver_error(prepare_db):
    response = client.get("/api/v1/driver/mji")
    assert response.status_code, 404


def test_report_asc(prepare_db):
    response = client.get("/api/v1/report?order=asc")
    assert response.status_code, 200


def test_report_desc(prepare_db):
    response = client.get("/api/v1/report?order=desc")
    assert response.status_code, 200


def test_report_request_args(prepare_db):
    with app.test_request_context('/api/v1/report?order=asc'):
        assert request.path == '/api/v1/report'
        assert request.args['order'] == 'asc'
    with app.test_request_context('/api/v1/report?order=desc'):
        assert request.path == '/api/v1/report'
        assert request.args['order'] == 'desc'
