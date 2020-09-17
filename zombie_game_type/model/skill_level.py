from dataclasses import dataclass

from .skill import SkillModel
from ..base_model import BaseModel


@dataclass(init=True, repr=True, eq=True, unsafe_hash=True, frozen=True)
class SkillLevelModel(BaseModel):
    name: str
    skill: SkillModel
    level: int

    def __post_init__(self):
        name_format = '{} {}'.format(self.skill.name, self.level)
        if self.name != name_format:
            raise Exception('Wrong name of {}'.format(self.name))
