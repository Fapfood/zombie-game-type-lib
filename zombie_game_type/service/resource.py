from ..base_service import BaseService
from ..model import ResourceModel


class ResourceService(BaseService):
    def __init__(self):
        super().__init__('resource.yml')

    def get_or_create_from_yaml(self, yaml: dict) -> ResourceModel:
        name = yaml.get('name')
        el = self.get_by_name(name)
        if el is None:
            el = ResourceModel(name=name)
            self.update_by_name(name, el)
        return el
