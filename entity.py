class Entity:

    def __init__(self, world):
        self.id_ = world.count_id()
        world.res.create_new_entity(self.id_)
        self.type_ = None


class Country(Entity):
    pass