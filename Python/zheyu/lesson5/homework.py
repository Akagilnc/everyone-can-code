class Parkinglot:
    cars = []

    def __init__(self, capacity, name):
        self.empty = self.capacity = capacity
        self.name = name

    def parking(self, car):
        self.empty -= 1
        self.cars.append(car)


class ParkingBoy:
    def __init__(self, parkinglot):
        self.parkinglot = parkinglot


parkinglot1 = Parkinglot(10, 'name1')
Allen = ParkingBoy(parkinglot1)
