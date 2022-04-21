from rightmove_service import RightmoveService
from models.rightmove_request import RightmoveRequest
from property_service import PropertyService

class RightmoveScraper:
    def __init__(self):
        self.rightmove_service = RightmoveService()
        self.property_service = PropertyService()


    def get_number_properties_for_sale(self, context: RightmoveRequest) -> int:
        number_of_properties = self.rightmove_service.get_number_properties_for_sale(context)
        self.property_service.insert(number_of_properties, context)
        return number_of_properties
