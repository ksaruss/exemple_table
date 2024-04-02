from resources import Resources
from entity import Entity


class World:
    def __init__(self):
        self.list_entity = {}
        self.res: Resources = Resources()

    def create_entity(self):
        new_entity = Entity(self)
        self.list_entity[new_entity.id_] = new_entity

    def get_entity(self):
        return print(self.list_entity)

    def get_resources(self):
        self.res.get_resources()