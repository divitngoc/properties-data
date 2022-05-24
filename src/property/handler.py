import logging
import os
from rightmove_scraper import RightmoveScraper
from models.rightmove_request import RightmoveRequest

logging_level = os.environ.get("logging-level", "DEBUG")
logging.basicConfig(level = logging._nameToLevel.get(logging_level))
log = logging.getLogger()

app = RightmoveScraper()

def lambda_handler(event=None, context=None):
    number_of_properties_for_sale = app.get_number_properties_for_sale(RightmoveRequest())
    return number_of_properties_for_sale

if __name__ == '__main__':
    log.info(lambda_handler(None, None))