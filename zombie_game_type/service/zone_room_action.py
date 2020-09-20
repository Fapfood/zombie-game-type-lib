from ..base_service import BaseService
from ..model import ZoneRoomActionModel


class ZoneRoomActionService(BaseService):
    def __init__(self):
        super().__init__('zone_room_action')

    def get_or_create_from_yaml(self, yaml: dict) -> ZoneRoomActionModel:
        name = yaml.get('name')
        el = self.get_by_name(name)
        if el is None:
            probability = float(yaml.get('probability'))
            el = ZoneRoomActionModel(name=name,
                                     probability=probability,
                                     )
            self.update_by_name(name, el)
        return el
