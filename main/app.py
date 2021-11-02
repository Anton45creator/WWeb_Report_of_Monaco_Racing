import datetime
import json
from flasgger import Swagger
from simplexml import dumps
from flask import Flask, make_response
from flask_restful import Api
import rest

app = Flask(__name__)
api = Api(app, default_mediatype='application/json', prefix='/api/v1')
swagger = Swagger(app)


def converter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


@api.representation('application/json')
def output_json(data, code, headers=None):
    response = make_response(json.dumps({'response': data},
                                        default=converter), code)
    response.headers.extend(headers or {})
    return response


@api.representation('application/xml')
def output_xml(data, code, headers=None):
    response = make_response(dumps({'response': data}), code)
    response.headers.extend(headers or {})
    return response


api.add_resource(rest.Report, '/report')
api.add_resource(rest.Driver, '/driver/<driver_id>')

if __name__ == "__main__":
    app.run()
