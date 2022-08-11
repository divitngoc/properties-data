from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class PropertyForSaleLog:
    id: int
    no_properties: int
    created: datetime
    region: str
    created_by: str 