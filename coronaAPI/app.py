"""
Develped in python3.9 envo.
"""
from waitress import serve
from flask import Flask
from flask_restful import Api
from flask_apscheduler import APScheduler
from datetime import datetime
from .controller import *
from .scrape import scrape_data,add_data_to_db
from .config import *

# App init
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

# initialize scheduler
scheduler = APScheduler()


@scheduler.task("interval", id="scrape_data", minutes=5, misfire_grace_time=900,next_run_time=datetime.now())
def job_scrape_data():
    """
    Schedule the scraping job
    Runs in every 5 minutes, also at the beginning of server start
    """
    json_data = scrape_data()
    add_data_to_db(json_data,Config.CORONA_KEY)

scheduler.api_enabled = True
scheduler.init_app(app)
scheduler.start()
api = Api(app)
api.add_resource(DataListController, '/api/cases')
api.add_resource(DataController, '/api/case/<string:country_id>')

# if __name__ == '__main__':
#     app.run(debug=True)