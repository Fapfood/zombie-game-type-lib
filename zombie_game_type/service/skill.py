from ..base_service import BaseService
from ..model import SkillModel


class SkillService(BaseService):
    def __init__(self):
        super().__init__('skill')

    def get_or_create_from_yaml(self, yaml: dict) -> SkillModel:
        name = yaml.get('name')
        el = self.get_by_name(name)
        if el is None:
            el = SkillModel(name=name)
            self.update_by_name(name, el)
        return el
