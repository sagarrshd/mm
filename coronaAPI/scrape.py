"""
Scrapes the data and dumps it to tinydb
"""

import requests
from bs4 import BeautifulSoup
import json
from tinydb import TinyDB,Query
from .config import *

DB = TinyDB(Config.JSON_PATH)


DB_DATA = Query()

def clean_number(in_text):
	"""
	Input - string
	Output - Cleans special characters like , and + and returns int if text after 
	cleaning is digits else 0
	"""
	in_text = in_text.replace(",","").replace("+","").strip()
	return int(in_text or 0)

def scrape_data():
	"""
	Returns scraped data in json format
	"""
	json_table_output = {}
	r = requests.get(Config.DATA_POINT_URL)
	soup = BeautifulSoup(r.text, 'html.parser')
	table_data = soup.find('table',id='main_table_countries_today')
	for each_row in table_data.select("tbody > tr"):
		country = each_row.select_one("td:nth-of-type(2)").text
		if country.strip() in ["World","Total:","North America", "Oceania", "Africa", "Asia", "Europe","South America",""]:
			continue
		total_cases =  clean_number(each_row.select_one("td:nth-of-type(3)").text)
		active_cases =  clean_number(each_row.select_one("td:nth-of-type(9)").text)
		total_deaths =  clean_number(each_row.select_one("td:nth-of-type(5)").text)
		total_recovered = clean_number(each_row.select_one("td:nth-of-type(7)").text)
		population = clean_number(each_row.select_one("td:nth-of-type(15)").text)
		recovery_rate = None
		percentage_infected = None
		if total_cases:
			recovery_rate =  total_recovered/ total_cases
		if population:
			percentage_infected = total_cases / population
		json_table_output[country] = {"key":Config.CORONA_KEY,"total_cases":total_cases,"active_cases":active_cases,"total_deaths":total_deaths,"recovery_rate":recovery_rate,"percentage_infected":percentage_infected}
	return json_table_output

def add_data_to_db(json_data,key):
	"""
	Add data to tinydb
	"""
	DB.upsert(json_data, DB_DATA.key == key)

def get_data(key):
	"""
	Get data from tinydb
	"""
	json_data = DB.search(DB_DATA.key == key)
	return json_data

if __name__ == '__main__':
	json_data = scrape_data()
