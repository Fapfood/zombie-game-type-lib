from .building_category import BuildingCategoryService
from .production import ProductionService
from ..base_service import BaseService
from ..model import BuildingRoomModel


class BuildingRoomService(BaseService):
    def __init__(self,
                 building_category_service: BuildingCategoryService,
                 production_service: ProductionService):
        self.building_category_service = building_category_service
        self.production_service = production_service
        super().__init__('building_room')

    def get_or_create_from_yaml(self, yaml: dict) -> BuildingRoomModel:
        name = yaml.get('name')
        el = self.get_by_name(name)
        if el is None:
            category = self.building_category_service.get_or_create_from_yaml(yaml.get('category'))
            max_workers = int(yaml.get('max_workers', 1))
            worker_icon_male = yaml.get('worker_icon_male')
            worker_icon_female = yaml.get('worker_icon_female')
            available_productions = self.production_service.get_or_create_bulk_from_yaml(
                yaml.get('available_productions', []))
            el = BuildingRoomModel(name=name,
                                   category=category,
                                   max_workers=max_workers,
                                   worker_icon_male=worker_icon_male,
                                   worker_icon_female=worker_icon_female,
                                   available_productions=available_productions,
                                   )
            self.update_by_name(name, el)
            return el
