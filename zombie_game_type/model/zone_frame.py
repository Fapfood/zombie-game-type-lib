from dataclasses import dataclass

from .zone_category import ZoneCategoryModel
from ..base_model import BaseModel


@dataclass(init=True, repr=True, eq=True, unsafe_hash=True, frozen=True)
class ZoneFrameModel(BaseModel):
    name: str
    category: ZoneCategoryModel
    entry: int
    rooms: frozenset
    # doors: frozenset
    # actions: frozenset
