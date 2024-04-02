class Resources:
    def __init__(self):
        self.res = {}

    def create_new_entity(self, id_):
        self.res[id_] = {}

    def __len__(self):
        return len(self.res)

    def __next__(self):
        pass

    def add_resources(self, id_, resource, amount, cost):
        if self.res[id_].get(resource) is None:
            self.res[id_][resource] = {'amount': amount, 'cost': cost}
        else:
            self.res[id_][resource]['amount'] += amount
            self.res[id_][resource]['cost'] += cost * amount

    def get_resources(self):
        print(self.res)