from .skill_level import SkillLevelService
from ..base_service import BaseService
from ..model import SkillPackModel


class SkillPackService(BaseService):
    def __init__(self,
                 skill_level_service: SkillLevelService):
        self.skill_level_service = skill_level_service
        super().__init__('skill_pack')

    def get_or_create_from_yaml(self, yaml: dict) -> SkillPackModel:
        name = yaml.get('name')
        el = self.get_by_name(name)
        if el is None:
            skills = self.skill_level_service.get_or_create_bulk_from_yaml(yaml.get('skills', []))
            el = SkillPackModel(name=name,
                                skills=skills,
                                )
            self.update_by_name(name, el)
        return el
