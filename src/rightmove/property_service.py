from datetime import datetime
from property_dao import PropertyDao
from models.rightmove_request import RightmoveRequest
import logging

log = logging.getLogger()

class PropertyService:
    def __init__(self) -> None:
        self.dao = PropertyDao()

    def insert(self, no_of_properties: int, rightmove_request: RightmoveRequest) -> None:
        log.debug("Inserting into property_for_sale_log...")
        self.dao.insert(
            number_of_properties=no_of_properties, 
            created=datetime.utcnow(),
            region=rightmove_request.location_identifier)