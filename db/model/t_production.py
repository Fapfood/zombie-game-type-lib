from .t_resource_pack import ResourcePackModel
from .t_skill_pack import SkillPack
from ..base_model import Model


class ProductionModel(Model):
    def __init__(self,
                 name,
                 minutes,
                 required_skills,
                 required_tools,
                 from_resources,
                 to_resources_successful,
                 to_resources_interrupted,
                 ):
        self.name = name
        self.minutes = minutes
        self.required_skills = frozenset(required_skills)
        self.required_tools = frozenset(required_tools)
        self.from_resources = frozenset(from_resources)
        self.to_resources_successful = frozenset(to_resources_successful)
        self.to_resources_interrupted = frozenset(to_resources_interrupted)

    def __eq__(self, other):
        return (self.name == other.name
                and self.minutes == other.minutes
                and self.required_skills == other.required_skills
                and self.required_tools == other.required_tools
                and self.from_resources == other.from_resources
                and self.to_resources_successful == other.to_resources_successful
                and self.to_resources_interrupted == other.to_resources_interrupted
                )

    def __hash__(self):
        return (hash(self.name)
                + hash(self.minutes)
                + hash(self.required_skills)
                + hash(self.required_tools)
                + hash(self.from_resources)
                + hash(self.to_resources_successful)
                + hash(self.to_resources_interrupted)
                )

    @staticmethod
    def from_yaml(yaml):
        el = ProductionModel(name=yaml.get('name'),
                             minutes=yaml.get('minutes'),
                             required_skills=[SkillPack.from_yaml(el) for el in yaml.get('required_skills', [])],
                             required_tools=[ResourcePackModel.from_yaml(el) for el in yaml.get('required_tools', [])],
                             from_resources=[ResourcePackModel.from_yaml(el) for el in yaml.get('from_resources', [])],
                             to_resources_successful=[ResourcePackModel.from_yaml(el)
                                                      for el in yaml.get('to_resources_successful', [])],
                             to_resources_interrupted=[ResourcePackModel.from_yaml(el)
                                                       for el in yaml.get('to_resources_interrupted', [])],
                             )
        return el
