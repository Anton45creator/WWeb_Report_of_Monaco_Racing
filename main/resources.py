from flask import request
from flask_restful import Resource
from models import *


class Report(Resource):
    def get(self):
        """
        file: yaml/report.yaml
        """
        order = request.args.get('order')
        report = []
        if order == 'asc' or not order:
            for drivers in Racer.select().dicts():
                report.append(drivers)
            return report
        else:
            for drivers in Racer.select().dicts().order_by(Racer.id.desc()):
                report.append(drivers)
            return report


class Driver(Resource):
    def get(self, driver_id):
        """
        file: yaml/driver.yaml
        """
        for driver in Racer.select().where(Racer.key == driver_id.upper())\
                .dicts():
            return driver
        return {"status": "Requested data does not exist!"}, 404
