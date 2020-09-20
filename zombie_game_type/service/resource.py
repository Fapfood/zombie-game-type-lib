from ..base_service import BaseService
from ..model import ResourceModel


class ResourceService(BaseService):
    def __init__(self):
        super().__init__('resource')

    def get_or_create_from_yaml(self, yaml: dict) -> ResourceModel:
        name = yaml.get('name')
        el = self.get_by_name(name)
        if el is None:
            icon = yaml.get('icon')
            weight = int(yaml.get('weight', 1))
            size = int(yaml.get('size', 1))
            el = ResourceModel(name=name,
                               icon=icon,
                               weight=weight,
                               size=size,
                               )
            self.update_by_name(name, el)
        return el
