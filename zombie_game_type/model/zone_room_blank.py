from dataclasses import dataclass

from .zone_room_category import ZoneRoomCategoryModel
from ..base_model import BaseModel


@dataclass(init=True, repr=True, eq=True, unsafe_hash=True, frozen=True)
class ZoneRoomBlankModel(BaseModel):
    name: str
    category: ZoneRoomCategoryModel
    order: int
