
import logging
from bs4 import BeautifulSoup

from rightmove_client import RightMoveClient
from models.rightmove_request import RightmoveRequest

SOUP_PARSER = "html.parser"
log = logging.getLogger()

class RightMoveService:
    def __init__(self):
        self.client = RightMoveClient()

    def get_number_properties_for_sale(self, context: RightmoveRequest) -> int:
        response = self.client.get_properties_for_sale(context.getParams())
        if response.status_code >= 400:
            raise Exception("Response code is %s, skipping getting number of properties", response.status_code)

        soup = BeautifulSoup(response.content, SOUP_PARSER)
        resultCountList = soup.find_all("span", class_ = "searchHeader-resultCount")
        if not resultCountList:
            raise Exception("Could not find element in result count list")
    
        return resultCountList.pop().get_text().replace(",", "")