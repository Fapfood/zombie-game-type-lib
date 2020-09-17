from dataclasses import dataclass

from .resource import ResourceModel
from ..base_model import BaseModel


@dataclass(init=True, repr=True, eq=True, unsafe_hash=True, frozen=True)
class ResourcePackModel(BaseModel):
    name: str
    resource: ResourceModel
    quantity: int

    def __post_init__(self):
        name_format = '{} {}'.format(self.resource.name, self.quantity)
        if self.name != name_format:
            raise Exception('Wrong name of {}'.format(self.name))
