# create a class where you can add passangers limit and remove them


# Flight(3)
class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passangers = []

    def add_passangers(self, name):
        if not self.open_seats():
            return False
        self.passangers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passangers)
