from dataclasses import dataclass

from .zone_room_category import ZoneRoomCategoryModel
from ..base_model import BaseModel


@dataclass(init=True, repr=True, eq=True, unsafe_hash=True, frozen=True)
class ZoneRoomFillerModel(BaseModel):
    name: str
    category: ZoneRoomCategoryModel
    resource_drop_table: frozenset
    room_actions: frozenset
