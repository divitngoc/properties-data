import logging
import os
from rightmove_scraper import RightmoveScraper
from models.rightmove_request import RightmoveRequest

logging_level = os.environ.get("logging-level", "DEBUG")

logging.basicConfig(level = logging._nameToLevel.get(logging_level))
log = logging.getLogger()

app = RightmoveScraper()

if __name__ == '__main__':
    #TODO able to pass in different params for rightmove request
    number_of_properties_for_sale = app.get_number_properties_for_sale(RightmoveRequest())
