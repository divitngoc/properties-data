from dataclasses import dataclass, field
from typing import List

@dataclass
class RightmoveRequest():
    min_bedrooms: int = 0;
    max_bedrooms: int = 10;
    min_price: int = 0
    max_price: int = 600000 
    location_identifier: str = "REGION^904" # manchester
    prop_type: List[str] = field(default_factory=lambda: ["bungalow", "detached", "flat", "semi-detached", "terraced"])
    dont_show: List[str] = field(default_factory=lambda: ["sharedOwnership"])
    
    def getParams(self) -> dict:
        return {
            "minBedrooms": self.min_bedrooms,
            "maxBedrooms": self.max_bedrooms,
            "minPrice": self.min_price, 
            "maxPrice": self.max_price, 
            "propertyTypes": ",".join(self.prop_type),
            "locationIdentifier": self.location_identifier,
            "dontShow": ",".join(self.dont_show)}