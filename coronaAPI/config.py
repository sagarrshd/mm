"""
Config file
"""
from pathlib import Path

class Config:
    __ROOT_PATH = Path(__file__).resolve().parent
    DEBUG = False
    TESTING = False
    ROOT_PATH = __ROOT_PATH
    DATA_POINT_URL = "https://www.worldometers.info/coronavirus/"
    JSON_PATH =  f'{ROOT_PATH}/db.json'
    CORONA_KEY = "corona_stats"

class ProductionConfig(Config):
    DATABASE_URI = '' 

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
