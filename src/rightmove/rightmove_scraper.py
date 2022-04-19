from rightmove_service import RightMoveService
from models.rightmove_request import RightmoveRequest

class RightMoveScraper:
    def __init__(self):
        self.rightmove_service = RightMoveService()

    def get_number_properties_for_sale(self, context: RightmoveRequest) -> int:
        return self.rightmove_service.get_number_properties_for_sale(context);
