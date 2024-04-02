import world


world = world.World()


world.create_entity()
world.create_entity()
world.res.add_resources(1, 'milk', 10, 0)
world.res.add_resources(1, 'milk', 5, 2)
world.res.add_resources(1, 'milk', 2, 5)
world.get_resources()

