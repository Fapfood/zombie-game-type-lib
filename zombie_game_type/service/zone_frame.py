from .zone_category import ZoneCategoryService
from .zone_room_blank import ZoneRoomBlankService
from ..base_service import BaseService
from ..model import ZoneFrameModel


class ZoneFrameService(BaseService):
    def __init__(self,
                 zone_category_service: ZoneCategoryService,
                 zone_room_blank_service: ZoneRoomBlankService):
        self.zone_category_service = zone_category_service
        self.zone_room_blank_service = zone_room_blank_service
        super().__init__('zone_frame')

    def get_or_create_from_yaml(self, yaml: dict) -> ZoneFrameModel:
        name = yaml.get('name')
        el = self.get_by_name(name)
        if el is None:
            category = self.zone_category_service.get_or_create_from_yaml(yaml.get('category'))
            entry = int(yaml.get('entry'))
            rooms = self.zone_room_blank_service.get_or_create_bulk_from_yaml(yaml.get('rooms', []))
            el = ZoneFrameModel(name=name,
                                category=category,
                                entry=entry,
                                rooms=rooms,
                                )
        self.update_by_name(name, el)
        return el
