"""
Controller module
"""
from flask_restful import abort, Resource
from datetime import datetime
from .scrape import get_data
from .config import *


class DataListController(Resource):
    def get(self):
        json_data = get_data(Config.CORONA_KEY)
        if json_data:
            json_data = json_data[0]
            json_data.pop('key',None)
        return json_data, 200, {'Content-Type: application/json'}

class DataController(Resource):
    def get(self,country_id):
        print(country_id)
        json_data = get_data(Config.CORONA_KEY)
        if json_data:
            json_data = json_data[0]
            json_data.pop('key',None)
            if not country_id in json_data:
                abort(404, message="Country {} details doesn't exist in our db".format(country_id))
            return json_data[country_id], 200, {'Content-Type: application/json'}