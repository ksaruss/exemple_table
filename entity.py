class Entity:
    global_id = 0

    @classmethod
    def increment_id(cls):
        cls.global_id += 1

    def __init__(self, world):
        self.increment_id()
        self.id_ = self.global_id
        self.type_ = None
        world.res.create_new_entity(self.id_)


