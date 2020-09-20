from dataclasses import dataclass

from ..base_model import BaseModel


@dataclass(init=True, repr=True, eq=True, unsafe_hash=True, frozen=True)
class ResourceModel(BaseModel):
    name: str
    icon: str
    weight: int
    size: int
