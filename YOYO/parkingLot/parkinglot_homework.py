class ParkingLot:

    def __init__(self,capacity):
        self.capacity = capacity
        self.empty = capacity
        self.seat = []

    def parking(self,car):
        if car:
            self.seat.append(car)
            self.empty -= 1

    def check(self,car):
        if car in self.seat:
            raise ValueError('This car has already in the park.')

    def take_out(self,car):
        self.seat.remove(car)
        self.empty += 1

class Car:
    pass

class ParkingBoy:

    def __init__(self,parkinglotlist):
        self.parkinglotlist = parkinglotlist
        if type(parkinglotlist) != list:
            raise TypeError('This is not a list!')

    def parking(self, car):
        self.parkinglotlist.parking(car)

    def take_out(self, car):
        self.parkinglotlist.take_out(car)


BMW = Car()
Auto = Car()

yoyo_park = ParkingLot(20)
momo_park = ParkingLot(10)
lolo_park = ParkingLot(50)
yoyo = ParkingBoy([yoyo_park, momo_park, lolo_park])

yoyo_park.parking(BMW)
momo_park.parking(Auto)


print(yoyo.parkinglotlist)




