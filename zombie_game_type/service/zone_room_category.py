from ..base_service import BaseService
from ..model import ZoneRoomCategoryModel


class ZoneRoomCategoryService(BaseService):
    def __init__(self):
        super().__init__('zone_room_category')

    def get_or_create_from_yaml(self, yaml: dict) -> ZoneRoomCategoryModel:
        name = yaml.get('name')
        el = self.get_by_name(name)
        if el is None:
            el = ZoneRoomCategoryModel(name=name)
            self.update_by_name(name, el)
        return el
