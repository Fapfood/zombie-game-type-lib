from .production import ProductionService
from ..base_service import BaseService
from ..model import BuildingModel


class BuildingService(BaseService):
    def __init__(self,
                 production_service: ProductionService):
        self.production_service = production_service
        super().__init__('building.yml')

    def get_or_create_from_yaml(self, yaml: dict) -> BuildingModel:
        name = yaml.get('name')
        el = self.get_by_name(name)
        if el is None:
            max_workers = int(yaml.get('max_workers'))
            worker_icon_male = yaml.get('worker_icon_male')
            worker_icon_female = yaml.get('worker_icon_female')
            available_productions = self.production_service.get_or_create_bulk_from_yaml(
                yaml.get('available_productions', []))
            el = BuildingModel(name=name,
                               max_workers=max_workers,
                               worker_icon_male=worker_icon_male,
                               worker_icon_female=worker_icon_female,
                               available_productions=available_productions,
                               )
            self.update_by_name(name, el)
            return el
