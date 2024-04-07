import world


world = world.World()


world.create_entity()
world.create_entity()

world.res.add_resources(1, 'milk', 13, 0)
world.res.add_resources(1, 'milk', 6, 2)
world.res.add_resources(1, 'milk', 4, 5)

world.get_resources()

world.res.transfer(1, 2, 'milk', 7)

print(world.res.remove_resources(1, 'milk', 10))


world.get_resources()