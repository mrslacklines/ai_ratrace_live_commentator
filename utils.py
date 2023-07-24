import json
import os

from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv("./.env"))

race_data_filepath = os.environ.get("RACE_DATA_JSON")

def load_race_data(race_data_filepath=race_data_filepath):
    with open(race_data_filepath) as json_fh:
        race_data = json.load(json_fh)

    return race_data