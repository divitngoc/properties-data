from datetime import datetime
from property_dao import PropertyDao
from models.db.propery_for_sale_log import PropertyForSaleLog
import logging

log = logging.getLogger()

class PropertyService:
    def __init__(self) -> None:
        self.dao = PropertyDao()

    def insert(self, no_of_properties: int, region: str, created_by: str) -> None:
        log.debug("Inserting into property_for_sale_log...")
        self.dao.insert(
            number_of_properties=no_of_properties, 
            created=datetime.utcnow(),
            region=region,
            created_by=created_by)
    
    def fetchAllPropertyForSaleLog(self) -> list[PropertyForSaleLog]:
        return self.dao.fetchAllPropertyForSaleLog()