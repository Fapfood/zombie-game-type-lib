from ..base_service import BaseService
from ..model import BuildingCategoryModel


class BuildingCategoryService(BaseService):
    def __init__(self):
        super().__init__('building_category')

    def get_or_create_from_yaml(self, yaml: dict) -> BuildingCategoryModel:
        name = yaml.get('name')
        el = self.get_by_name(name)
        if el is None:
            el = BuildingCategoryModel(name=name)
            self.update_by_name(name, el)
        return el
