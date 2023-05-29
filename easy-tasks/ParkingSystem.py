"""
Design a parking system for a parking lot. The parking lot has three kinds of parking spaces:
big, medium, and small, with a fixed number of slots for each size.
Implement the ParkingSystem class:
ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class.
The number of slots for each parking space are given as part of the constructor.
bool addCar(int carType) Checks whether there is a parking space of carType for the
car that wants to get into the parking lot. carType can be of three kinds: big, medium, or small,
which are represented by 1, 2, and 3 respectively. A car can only park in a parking space of
its carType. If there is no space available, return false, else park the car in that size space
and return true.
"""


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def add_car(self, car_type: int) -> bool:
        if car_type == 1:
            self.big -= 1
            if self.big < 0:
                self.big += 1
                return False
            return True
        elif car_type == 2:
            self.medium -= 1
            if self.medium < 0:
                self.medium += 1
                return False
            return True
        else:
            self.small -= 1
            if self.small < 0:
                self.small += 1
                return False
            return True


def test_parking_system():
    parking = ParkingSystem(2, 1, 3)
    assert parking.big == 2
    assert parking.medium == 1
    assert parking.small == 3

    assert parking.add_car(1) is True
    assert parking.big == 1

    assert parking.add_car(2) is True
    assert parking.medium == 0

    assert parking.add_car(3) is True
    assert parking.small == 2

    assert parking.add_car(1) is True
    assert parking.add_car(2) is False
    assert parking.add_car(3) is True

    assert parking.big == 0
    assert parking.medium == 0
    assert parking.small == 1

    print("Tests passed!")


if __name__ == '__main__':
    test_parking_system()
