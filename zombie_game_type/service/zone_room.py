from ..base_service import BaseService
from ..model import ZoneRoomModel


class ZoneRoomService(BaseService):
    def __init__(self):
        super().__init__('zone_room')

    def get_or_create_from_yaml(self, yaml: dict) -> ZoneRoomModel:
        name = yaml.get('name')
        el = self.get_by_name(name)
        if el is None:
            el = ZoneRoomModel(name=name)
            self.update_by_name(name, el)
        return el
