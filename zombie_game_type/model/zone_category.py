from dataclasses import dataclass

from ..base_model import BaseModel


@dataclass(init=True, repr=True, eq=True, unsafe_hash=True, frozen=True)
class ZoneCategoryModel(BaseModel):
    name: str
