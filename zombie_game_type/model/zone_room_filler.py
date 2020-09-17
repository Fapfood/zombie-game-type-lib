from dataclasses import dataclass

from .zone_room import ZoneRoomModel
from ..base_model import BaseModel


@dataclass(init=True, repr=True, eq=True, unsafe_hash=True, frozen=True)
class ZoneRoomFillerModel(BaseModel):
    name: str
    type: ZoneRoomModel
    resource_drop_table: frozenset
    room_actions: frozenset
