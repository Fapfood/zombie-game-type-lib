from .zone_room_category import ZoneRoomCategoryService
from ..base_service import BaseService
from ..model import ZoneRoomBlankModel


class ZoneRoomBlankService(BaseService):
    def __init__(self,
                 zone_room_category_service: ZoneRoomCategoryService):
        self.zone_room_category_service = zone_room_category_service
        super().__init__('zone_room_blank')

    def get_or_create_from_yaml(self, yaml: dict) -> ZoneRoomBlankModel:
        name = yaml.get('name')
        el = self.get_by_name(name)
        if el is None:
            category = self.zone_room_category_service.get_or_create_from_yaml(yaml.get('category'))
            order = int(yaml.get('order'))
            el = ZoneRoomBlankModel(name=name,
                                    category=category,
                                    order=order,
                                    )
            self.update_by_name(name, el)
        return el
