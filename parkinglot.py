from datetime import datetime
from math import ceil


class Parkinglot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.empty = capacity
        self.slots = []

    def parking(self, car):
        if self.empty == 0:
            raise ValueError("It's full")

        self.check_car(car)
        if car in self.slots:
            raise ValueError("It's here")
        car.start_time = datetime.now()
        self.slots.append(car)
        self.empty -= 1

    def taking(self, car):
        self.check_car(car)
        print(self.slots)
        if car not in self.slots:
            raise ValueError('''It's not here''')
        car.end_time = datetime.now()
        self.payment(car)
        self.slots.remove(car)
        self.empty += 1

    def check_car(self, car):
        if type(car) != Car:
            raise TypeError('It is not a car')

    def payment(self, car):
        parking_time = car.end_time - car.start_time
        if parking_time.total_seconds() < 2 * 3600:
            car.fee = 5
        else:
            ex_seconds = parking_time.total_seconds() - 2 * 3600
            ex_hours = ceil(ex_seconds / 3600)
            car.fee = 5 + ex_hours * 5


class ParkingBoy:
    def __init__(self, parkinglots, name):
        if type(parkinglots) != list:
            raise TypeError("It's not a parkinglots list")
        for item in parkinglots:
            if type(item) != Parkinglot:
                raise TypeError("Item in parkinglots must be Parkinglot")

        self.parkinglots = parkinglots
        self.name = name

    def input_parkinglot(self):

        result_parkinglot, highest_empty_rate = '', 0

        for parkinglot in self.parkinglots:
            empty_rate = parkinglot.empty / parkinglot.capacity
            if empty_rate > highest_empty_rate:
                highest_empty_rate = empty_rate
                result_parkinglot = parkinglot

        self.last_parkinglot = result_parkinglot
        print(result_parkinglot.capacity)
        return result_parkinglot

    def output_parkingLot(self, car):
        if type(car) != Car:
            raise TypeError("It is not a car!")

        for parkinglot in self.parkinglots:
            if car in parkinglot.slots:
                return parkinglot

    def parking(self, car):
        parkinglot = self.input_parkinglot()
        parkinglot.parking(car)

    def taking(self, car):
        self.output_parkingLot(car).taking(car)

    def get_last_empty(self):
        return self.last_parkinglot.empty


class Car:
    def __init__(self, ID):
        self.ID = ID
        self.start_time = 0
        self.end_time = 0
        self.fee = 0


optimus_prime = Car("川A666666")
CFLS = Parkinglot(2)
WFJ = Parkinglot(10)
SB = ParkingBoy([CFLS, WFJ], "ShaBe")

CFLS.parking(optimus_prime)
# if SB.getLastEmpty() != SB.last_parkinglot.capacity - 1:
# raise ValueError("empty should be 1 small")

# CFLS.taking(optimus_prime)

SB.taking(optimus_prime)
print(optimus_prime.fee)
