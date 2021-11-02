from flask import request
from flask_restful import Resource
import monaco
import cli


data = {'abb': cli.get_file_content('data', 'abbreviations.txt'),
        'start': cli.get_file_content('data', 'start.log', True, '_', 3),
        'end': cli.get_file_content('data', 'end.log', True, '_', 3)}


class Report(Resource):
    def get(self):
        """
        file: report.yaml
        """
        report = monaco.build_report(data)
        report_reverse = monaco.build_report(data, False)
        order = request.args.get('order')
        if order == 'asc' or not order:
            return report
        else:
            return report_reverse


class Driver(Resource):
    def get(self, driver_id):
        """
        file: driver.yaml
        """
        for driver in monaco.build_report(data):
            if driver['key'] == driver_id.upper():
                return driver
        return {"status": "Requested data does not exist!"}, 404
