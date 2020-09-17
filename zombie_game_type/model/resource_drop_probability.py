from dataclasses import dataclass

from .resource import ResourceModel
from ..base_model import BaseModel


@dataclass(init=True, repr=True, eq=True, unsafe_hash=True, frozen=True)
class ResourceDropProbabilityModel(BaseModel):
    name: str
    resource: ResourceModel
    probability: int
