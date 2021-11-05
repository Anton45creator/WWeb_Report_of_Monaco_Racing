from flask import request
from flask_restful import Resource
from db_helper import *


report = report_data()
report_reverse = sorted(report, key=lambda k: k['position'], reverse=True)


class Report(Resource):
    def get(self):
        """
        file: yaml/report.yaml
        """
        order = request.args.get('order')
        if order == 'asc' or not order:
            return report
        else:
            return report_reverse


class Driver(Resource):
    def get(self, driver_id):
        """
        file: yaml/driver.yaml
        """
        for driver in report:
            if driver['key'] == driver_id.upper():
                return driver
        return {"status": "Requested data does not exist!"}, 404
