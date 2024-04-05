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
        return resource, amount, (cost*amount)

    def remove_resources(self, id_, resource, amount):
        if self.res[id_][resource]['amount'] == amount:
            self.res[id_][resource]['amount'] = 0
            cost = self.res[id_][resource]['cost']
            self.res[id_][resource]['cost'] = 0
            return resource, amount, cost
        elif self.res[id_][resource]['amount'] < amount:
            raise Exception
        else:
            average_cost = self.res[id_][resource]['cost'] / self.res[id_][resource]['amount']
            cost = round(average_cost * amount)
            self.res[id_][resource]['cost'] -= cost
            self.res[id_][resource]['amount'] -= amount
            return resource, cost, amount

    def transfer(self, id_out, id_in, resource, amount):
        pass

    def get_resources(self):
        print(self.res)
