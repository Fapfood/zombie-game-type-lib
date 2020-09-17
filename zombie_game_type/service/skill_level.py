from .skill import SkillService
from ..base_service import BaseService
from ..model import SkillLevelModel


class SkillLevelService(BaseService):
    def __init__(self,
                 skill_service: SkillService):
        self.skill_service = skill_service
        super().__init__('skill_level.yml')

    def get_or_create_from_yaml(self, yaml: dict) -> SkillLevelModel:
        name = yaml.get('name')
        el = self.get_by_name(name)
        if el is None:
            skill = self.skill_service.get_or_create_from_yaml(yaml.get('skill'))
            level = int(yaml.get('level'))
            el = SkillLevelModel(name=name,
                                 skill=skill,
                                 level=level,
                                 )
            self.update_by_name(name, el)
        return el
