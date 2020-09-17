from .resource import ResourceService
from ..base_service import BaseService
from ..model import ResourcePackModel


class ResourcePackService(BaseService):
    def __init__(self,
                 resource_service: ResourceService):
        self.resource_service = resource_service
        super().__init__('resource_pack.yml')

    def get_or_create_from_yaml(self, yaml: dict) -> ResourcePackModel:
        name = yaml.get('name')
        el = self.get_by_name(name)
        if el is None:
            resource = self.resource_service.get_or_create_from_yaml(yaml.get('resource'))
            quantity = int(yaml.get('quantity'))
            el = ResourcePackModel(name=name,
                                   resource=resource,
                                   quantity=quantity,
                                   )
            self.update_by_name(name, el)
        return el
