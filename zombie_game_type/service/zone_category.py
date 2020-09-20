from ..base_service import BaseService
from ..model import ZoneCategoryModel


class ZoneCategoryService(BaseService):
    def __init__(self):
        super().__init__('zone_category')

    def get_or_create_from_yaml(self, yaml: dict) -> ZoneCategoryModel:
        name = yaml.get('name')
        el = self.get_by_name(name)
        if el is None:
            el = ZoneCategoryModel(name=name)
            self.update_by_name(name, el)
        return el
