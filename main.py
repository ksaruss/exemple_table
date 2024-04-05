import world


world = world.World()


world.create_entity()
world.create_entity()

world.res.add_resources(1, 'milk', 10, 0)
world.res.add_resources(1, 'milk', 6, 2)
world.res.add_resources(1, 'milk', 2, 5)


print(world.res.remove_resources(1, 'milk', 17))


world.get_resources()