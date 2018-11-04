class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.empty = capacity
        self.seat = []

    def parking(self, car):
        self.check(car)
        if type(car) is Car:
            if self.empty <= 0:
                raise ValueError('No room.')
            self.seat.append(car)
            self.empty -= 1

    def check(self, car):
        if car in self.seat:
            raise ValueError('This car has already in the park.')

    def take_out(self, car):
        self.seat.remove(car)
        self.empty += 1


class Car:
    def print(self):
        print("test")


class ParkingBoy:
    def __init__(self, parking_lot):
        self.parkingLot = parking_lot

    def parking(self, car):
        self.parkingLot.parking(car)
        return car

    def take_out(self, car):
        self.parkingLot.take_out(car)

    def test(self, car):
        self.parking(car).print()


BMW = Car()
Auto = Car()

yoyo_park = ParkingLot(20)
momo_park = ParkingLot(10)
lolo_park = ParkingLot(50)
# test_park = ParkingLot(1)
# test_park.parking(BMW)
# test_park.parking(Auto)
yoyo_park.parking(BMW)
print(yoyo_park.empty)
yoyo_park.take_out(BMW)
print(yoyo_park.empty)

yoyo = ParkingBoy(yoyo_park)

yoyo.parking(Auto)
print(yoyo.parkinglot.empty)
yoyo.take_out(Auto)
print(yoyo.parkinglot.empty)
