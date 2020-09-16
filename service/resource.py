from ..base_service import Service
from ..model import ResourceModel


class ResourceService(Service):
    def get_or_create_bulk(self, lis):
        res = []
        for el in lis:
            entity = self.get_or_create(el)
            res.append(entity)
        return res

    def get_or_create(self, el: ResourceModel):
        entity = self.get_by_name(el.name)
        if entity is None:
            entity = self.update_by_name(el.name, el)
        return entity
