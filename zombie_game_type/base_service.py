import os
from random import sample

from yaml import FullLoader, load

SCRIPT_DIR = os.path.dirname(__file__)


class BaseService:
    def __init__(self, name):
        self.data = {}

        file_name = '{}/data/{}.yml'.format(SCRIPT_DIR, name)
        if os.path.isfile(file_name):
            with open(file_name, encoding='utf8') as f:
                lis = load(f.read(), Loader=FullLoader)['list']
            self.get_or_create_bulk_from_yaml(lis)

        dir_name = '{}/data/{}'.format(SCRIPT_DIR, name)
        if os.path.isdir(dir_name):
            for _, _, file_names in os.walk(dir_name):
                for file_name in file_names:
                    file_name = '{}/data/{}/{}'.format(SCRIPT_DIR, name, file_name)
                    with open(file_name, encoding='utf8') as f:
                        el = load(f.read(), Loader=FullLoader)
                    self.get_or_create_from_yaml(el)

    def get_by_name(self, name: str):
        return self.data.get(name)

    def get_random(self):
        return sample(self.get_all(), 1)[0]

    def get_random_name(self):
        return sample(self.get_all_names(), 1)[0]

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
