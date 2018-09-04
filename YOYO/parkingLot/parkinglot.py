class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.empty = capacity
        self.seat = []

    def parking(self, car):
        self.check_car(car)
        self.empty -= 1
        self.seat.append(car)

    def check_car(self, car):
        if car in self.seat:
            raise ValueError('The car has already in ')

    def pick_up(self, car):
        self.seat.remove(car)
        self.empty += 1


class Car:
    pass


class ParkingBoy:
    def __init__(self, parking_lot_list):
        # temp = {}
        if type(parking_lot_list) != list:
            raise TypeError('You should input a list')
        # for parkinglot in parking_lot_list:
        #     temp[parkinglot] = parkinglot.empty

        # sorted_parkinglot_list = sorted(temp, key=temp.__getitem__, reverse=True)
        self.parkingLotList = parking_lot_list

    def parking(self, car):
        parkling_list = self.parkingLotList
        self.parkingLotList = sorted(parkling_list, key=lambda parkinglot: parkinglot.empty, reverse=True)
        if self.parkingLotList[0].empty == 0:
            raise ValueError('No empty! ')
        self.parkingLotList[0].parking(car)

    def pick_up(self, car):
        self.parkingLotList.pick_up(car)

    def lambda1(self, parkinglot):
        return parkinglot.empty


xinyue_parking_lot = ParkingLot(2)
ak_parking_lot = ParkingLot(3)
temp_parking_lot = ParkingLot(1)
CRV = Car()
# RAV4 = Car()
# bmw3 = Car()
# bmw5 = Car()
xinyue_parking_lot.parking(CRV)
xinyue_parking_lot.pick_up(CRV)

xinyue = ParkingBoy([xinyue_parking_lot, ak_parking_lot, temp_parking_lot])

# xinyue.parking(RAV4)
xinyue.parking(CRV)
# xinyue.parking(bmw3)
# xinyue.parking(bmw5)
print(xinyue_parking_lot.empty, ak_parking_lot.empty, temp_parking_lot.empty)