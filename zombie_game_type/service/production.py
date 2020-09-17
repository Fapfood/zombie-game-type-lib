from .resource_pack import ResourcePackService
from .skill_pack import SkillPackService
from ..base_service import BaseService
from ..model import ProductionModel


class ProductionService(BaseService):
    def __init__(self,
                 skill_pack_service: SkillPackService,
                 resource_pack_service: ResourcePackService):
        self.skill_pack_service = skill_pack_service
        self.resource_pack_service = resource_pack_service
        super().__init__('production.yml')

    def get_or_create_from_yaml(self, yaml: dict) -> ProductionModel:
        name = yaml.get('name')
        el = self.get_by_name(name)
        if el is None:
            minutes = int(yaml.get('minutes'))
            required_skills = self.skill_pack_service.get_or_create_bulk_from_yaml(yaml.get('required_skills', []))
            required_tools = self.resource_pack_service.get_or_create_bulk_from_yaml(yaml.get('required_tools', []))
            from_resources = self.resource_pack_service.get_or_create_bulk_from_yaml(yaml.get('from_resources', []))
            to_resources_successful = self.resource_pack_service.get_or_create_bulk_from_yaml(
                yaml.get('to_resources_successful', []))
            to_resources_interrupted = self.resource_pack_service.get_or_create_bulk_from_yaml(
                yaml.get('to_resources_interrupted', []))
            el = ProductionModel(name=name,
                                 minutes=minutes,
                                 required_skills=required_skills,
                                 required_tools=required_tools,
                                 from_resources=from_resources,
                                 to_resources_successful=to_resources_successful,
                                 to_resources_interrupted=to_resources_interrupted,
                                 )
            self.update_by_name(name, el)
        return el
