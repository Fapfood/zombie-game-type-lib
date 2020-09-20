from .resource import ResourceService
from ..base_service import BaseService
from ..model import ResourceDropProbabilityModel


class ResourceDropProbabilityService(BaseService):
    def __init__(self,
                 resource_service: ResourceService):
        self.resource_service = resource_service
        super().__init__('resource_drop_probability')

    def get_or_create_from_yaml(self, yaml: dict) -> ResourceDropProbabilityModel:
        name = yaml.get('name')
        el = self.get_by_name(name)
        if el is None:
            resource = self.resource_service.get_or_create_from_yaml(yaml.get('resource'))
            probability = float(yaml.get('probability'))
            el = ResourceDropProbabilityModel(name=name,
                                              resource=resource,
                                              probability=probability,
                                              )
            self.update_by_name(name, el)
        return el
