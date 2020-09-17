from .resource_drop_probablility import ResourceDropProbabilityService
from .zone_room import ZoneRoomService
from .zone_room_action import ZoneRoomActionService
from ..base_service import BaseService
from ..model import ZoneRoomFillerModel


class ZoneRoomFillerService(BaseService):
    def __init__(self,
                 zone_room_service: ZoneRoomService,
                 resource_drop_probability_service: ResourceDropProbabilityService,
                 zone_room_action_service: ZoneRoomActionService):
        self.zone_room_service = zone_room_service
        self.resource_drop_probability_service = resource_drop_probability_service
        self.zone_room_action_service = zone_room_action_service
        super().__init__('zone_room_filler.yml')

    def get_or_create_from_yaml(self, yaml: dict) -> ZoneRoomFillerModel:
        name = yaml.get('name')
        el = self.get_by_name(name)
        if el is None:
            type = self.zone_room_service.get_or_create_from_yaml(yaml.get('type'))
            resource_drop_table = self.resource_drop_probability_service.get_or_create_bulk_from_yaml(
                yaml.get('resource_drop_table', []))
            room_actions = self.zone_room_action_service.get_or_create_bulk_from_yaml(yaml.get('room_actions', []))
            el = ZoneRoomFillerModel(name=name,
                                     type=type,
                                     resource_drop_table=resource_drop_table,
                                     room_actions=room_actions,
                                     )
            self.update_by_name(name, el)
        return el
