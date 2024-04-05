from resources import Resources
from entity import Entity


class World:
    def __init__(self):
        self.global_id = 0
        self.list_entity = {}
        self.res: Resources = Resources()

    def count_id(self):
        self.global_id += 1
        return self.global_id

    def create_entity(self):
        new_entity = Entity(self)
        self.list_entity[new_entity.id_] = new_entity

    def create_country(self):
        pass

    def get_entity(self):
        return print(self.list_entity)

    def get_resources(self):
        self.res.get_resources()