from flask import request
from app import app


client = app.test_client()


def test_report():
    response = client.get("/api/v1/report")
    assert response.status_code == 200


def test_driver_id_middle_is_upper():
    response = client.get("/api/v1/driver/Svf")
    assert response.status_code, 200


def test_driver_id_lower():
    response = client.get("/api/v1/driver?SVF")
    assert response.status_code, 200


def test_drivers_id_upper():
    response = client.get("/api/v1/driver/svf")
    assert response.status_code, 200


def test_driver_error():
    response = client.get("/api/v1/driver/mji")
    assert response.status_code == 404


def test_report_asc():
    response = client.get("/api/v1/report?order=asc")
    assert response.status_code == 200


def test_report_desc():
    response = client.get("/api/v1/report?order=desc")
    assert response.status_code == 200


def test_driver_id_args():
    with app.test_request_context('/api/v1/driver?driver_id=VBM'):
        assert request.path == '/api/v1/driver'
        assert request.args['driver_id'] == 'VBM'


def test_report_request_args():
    with app.test_request_context('/api/v1/report?order=asc'):
        assert request.path == '/api/v1/report'
        assert request.args['order'] == 'asc'
    with app.test_request_context('/api/v1/report?order=desc'):
        assert request.path == '/api/v1/report'
        assert request.args['order'] == 'desc'
