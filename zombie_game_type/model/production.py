from dataclasses import dataclass

from ..base_model import BaseModel


@dataclass(init=True, repr=True, eq=True, unsafe_hash=True, frozen=True)
class ProductionModel(BaseModel):
    name: str
    minutes: int
    required_skills: frozenset
    required_tools: frozenset
    from_resources: frozenset
    to_resources_successful: frozenset
    to_resources_interrupted: frozenset
