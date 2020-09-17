import os

from yaml import FullLoader, load

SCRIPT_DIR = os.path.dirname(__file__)


class BaseService:
    def __init__(self, data_file_name):
        self.data = {}
        file_name = '{}/data/{}'.format(SCRIPT_DIR, data_file_name)
        with open(file_name, encoding='utf8') as f:
            lis = load(f.read(), Loader=FullLoader)['list']
        self.get_or_create_bulk_from_yaml(lis)

    def get_by_name(self, name: str):
        return self.data.get(name)

    def get_all(self):
        return frozenset(self.data.values())

    def get_all_names(self):
        return frozenset(self.data.keys())

    def update_by_name(self, name: str, el):
        self.data[name] = el

    def get_or_create_bulk_from_yaml(self, lis: list):
        res = []
        for el in lis:
            res.append(self.get_or_create_from_yaml(el))
        return frozenset(res)

    def get_or_create_from_yaml(self, yaml: dict):
        pass
