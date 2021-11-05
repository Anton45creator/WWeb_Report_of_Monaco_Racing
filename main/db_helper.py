from models import *


def find_all_categories():
    return Racer.select()


def report_data():
    report_db = find_all_categories()
    product_data = []
    for report in report_db:
        product_data.append({
            'position': report.position,
            'key': report.key,
            'driver': report.driver,
            'car': report.car,
            'start': report.start,
            'end': report.end,
            'disqualifid': report.disqualifid,
            'result': report.result
        })
    return product_data

