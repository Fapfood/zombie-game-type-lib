from dataclasses import dataclass

from ..base_model import BaseModel


@dataclass(init=True, repr=True, eq=True, unsafe_hash=True, frozen=True)
class BuildingModel(BaseModel):
    name: str
    max_workers: int
    worker_icon_male: str
    worker_icon_female: str
    available_productions: frozenset
