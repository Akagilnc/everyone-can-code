class ParkingLot:

    def __init__(self,capacity):
        self.capacity = capacity
        self.empty = capacity
        self.park = []

    def parking(self,car):
        self.park.append(car)
        self.empty -= 1

    def check(self,car):
        if car in self.park:
            raise ValueError('This car has already in the park.')

    def take_out(self,car):
        self.park.remove(car)
        self.empty += 1

class Car:
    pass

class ParkingBoy:
    def __init__(self,park):
        self.park = park

    def parking(self, car):
        self.park.append(car)

    def take_out(self, car):
        self.park.remove(car)


SUV = Car()
yoyo_park = ParkingLot(20)
yoyo = ParkingBoy






