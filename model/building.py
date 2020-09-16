from .t_production import ProductionModel
from ..base_model import Model


class BuildingModel(Model):
    def __init__(self,
                 name,
                 max_workers,
                 worker_icon_male,
                 worker_icon_female,
                 available_productions,
                 ):
        self.name = name
        self.max_workers = max_workers
        self.worker_icon_male = worker_icon_male
        self.worker_icon_female = worker_icon_female
        self.available_productions = frozenset(available_productions)

    def __eq__(self, other):
        return (self.name == other.name
                and self.max_workers == other.max_workers
                and self.worker_icon_male == other.worker_icon_male
                and self.worker_icon_female == other.worker_icon_female
                and self.available_productions == other.available_productions
                )

    def __hash__(self):
        return (hash(self.name)
                + hash(self.max_workers)
                + hash(self.worker_icon_male)
                + hash(self.worker_icon_female)
                + hash(self.available_productions)
                )

    @staticmethod
    def from_yaml(yaml):
        el = BuildingModel(name=yaml['name'],
                           max_workers=yaml['max_workers'],
                           worker_icon_male=yaml['worker_icon_male'],
                           worker_icon_female=yaml['worker_icon_female'],
                           available_productions=[ProductionModel.from_yaml(e) for e in yaml['available_productions']],
                           )
        return el
