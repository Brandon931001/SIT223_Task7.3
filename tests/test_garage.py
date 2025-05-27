
from garage.core import Vehicle, Garage, add_vehicle


def test_add_vehicle_success():
    garage = Garage("TestGarage", 2)
    vehicle = Vehicle("TestCar")
    assert add_vehicle(garage, vehicle) == True
    assert len(garage.vehicles) == 1

def test_add_vehicle_failure_when_full():
    garage = Garage("SmallGarage", 1)
    vehicle1 = Vehicle("Car1")
    vehicle2 = Vehicle("Car2")
    add_vehicle(garage, vehicle1)
    assert add_vehicle(garage, vehicle2) == False
