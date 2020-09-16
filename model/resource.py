from db.base_model import Model


class ResourceModel(Model):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    @staticmethod
    def from_yaml(yaml):
        el = ResourceModel(name=yaml.get('name'))
        return el
