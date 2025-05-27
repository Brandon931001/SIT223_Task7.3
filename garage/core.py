class VehicleType:
    CAR = "Car"
    TRUCK = "Truck"
    MOTORCYCLE = "Motorcycle"
    BICYCLE = "Bicycle"
    BUS = "Bus"

class Vehicle:
    def __init__(self, name="UNKNOWN", vehicle_type=VehicleType.CAR, speed=0, capacity=0, fuel_level=100, mileage=0, maintenance_due=10000):
        self.name = name
        self.type = vehicle_type
        self.speed = speed
        self.capacity = capacity
        self.fuel_level = fuel_level
        self.mileage = mileage
        self.maintenance_due = maintenance_due

class Garage:
    def __init__(self, name="UNKNOWN", max_capacity=10):
        self.name = name
        self.vehicles = []
        self.max_capacity = max_capacity

def read_string(prompt):
    return input(prompt)

def read_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")

def read_integer_range(prompt, min_val, max_val):
    while True:
        try:
            result = int(input(prompt))
            if min_val <= result <= max_val:
                return result
            else:
                print(f"Please enter a number between {min_val} and {max_val}")
        except ValueError:
            print("Please enter a whole number.")

def read_double(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a double.")

def read_double_range(prompt, min_val, max_val):
    while True:
        try:
            result = float(input(prompt))
            if min_val <= result <= max_val:
                return result
            else:
                print(f"Please enter a number between {min_val} and {max_val}")
        except ValueError:
            print("Please enter a double.")

def read_boolean(prompt):
    while True:
        result = input(prompt).strip().lower()
        if result in ["y", "yes"]:
            return True
        elif result in ["n", "no"]:
            return False
        else:
            print("Please enter y/n.")

def create_vehicle(name, vehicle_type, speed, capacity, fuel_level, mileage, maintenance_due):
    return Vehicle(name, vehicle_type, speed, capacity, fuel_level, mileage, maintenance_due)

def show_vehicle_info(v):
    print(f"Name: {v.name}")
    print(f"Type: {v.type}")
    print(f"Speed: {v.speed} km/h")
    print(f"Capacity: {v.capacity} passengers")
    print(f"Fuel Level: {v.fuel_level} %")
    print(f"Mileage: {v.mileage} km")
    print(f"Maintenance Due: {v.maintenance_due} km")

def refuel_vehicle(v, amount):
    v.fuel_level = min(100, v.fuel_level + amount)

def drive_vehicle(v, trip_distance):
    fuel_consumed = int(trip_distance / 10)
    if v.fuel_level >= fuel_consumed:
        v.fuel_level -= fuel_consumed
        v.mileage += int(trip_distance)
        v.maintenance_due -= int(trip_distance)
        print(f"{v.name} drove {trip_distance} km.")
    else:
        print(f"{v.name} doesn't have enough fuel to drive {trip_distance} km.")

def perform_maintenance(v):
    if v.maintenance_due <= 0:
        v.maintenance_due = 10000
        print(f"{v.name} has been serviced.")
    else:
        print(f"{v.name} doesn't need maintenance yet.")

def add_vehicle(g, v):
    if len(g.vehicles) < g.max_capacity:
        g.vehicles.append(v)
        return True
    else:
        print(f"Garage is full, cannot add {v.name}")
        return False

def remove_vehicle(g, vehicle_name):
    for i, v in enumerate(g.vehicles):
        if v.name == vehicle_name:
            del g.vehicles[i]
            return True
    return False

def find_vehicle(g, vehicle_name):
    for v in g.vehicles:
        if v.name == vehicle_name:
            return v
    return None

def show_garage_info(g):
    print(f"Garage Name: {g.name}")
    print(f"Maximum Capacity: {g.max_capacity}")
    print("Vehicles:")
    for v in g.vehicles:
        show_vehicle_info(v)

def service_vehicles(g):
    for v in g.vehicles:
        perform_maintenance(v)

def drive_vehicle_in_garage(g, vehicle_name, trip_distance):
    v = find_vehicle(g, vehicle_name)
    if v is not None:
        drive_vehicle(v, trip_distance)
    else:
        print("Vehicle not found.")

def refuel_vehicle_in_garage(g, vehicle_name, fuel_amount):
    v = find_vehicle(g, vehicle_name)
    if v is not None:
        refuel_vehicle(v, fuel_amount)
    else:
        print("Vehicle not found.")

def list_vehicles_needing_maintenance(g):
    print("Vehicles needing maintenance:")
    for v in g.vehicles:
        if v.maintenance_due <= 0:
            show_vehicle_info(v)

def manage_garage(g):
    while True:
        print("1. Show garage info")
        print("2. Add vehicle")
        print("3. Remove vehicle")
        print("4. Service vehicles")
        print("5. Drive a vehicle")
        print("6. Refuel a vehicle")
        print("7. List vehicles needing maintenance")
        print("8. Find vehicle by name")
        print("9. Exit")
        option = read_integer("Choose an option: ")

        if option == 1:
            show_garage_info(g)
        elif option == 2:
            name = read_string("Enter vehicle name: ")
            type_choice = read_integer_range("Enter vehicle type (0=CAR, 1=TRUCK, 2=MOTORCYCLE, 3=BICYCLE, 4=BUS): ", 0, 4)
            vehicle_type = [VehicleType.CAR, VehicleType.TRUCK, VehicleType.MOTORCYCLE, VehicleType.BICYCLE, VehicleType.BUS][type_choice]
            speed = read_double("Enter vehicle speed: ")
            capacity = read_integer("Enter vehicle capacity: ")
            fuel_level = read_integer("Enter vehicle fuel level: ")
            mileage = read_integer("Enter vehicle mileage: ")
            maintenance_due = read_integer("Enter maintenance due kilometers: ")
            v = create_vehicle(name, vehicle_type, speed, capacity, fuel_level, mileage, maintenance_due)
            if add_vehicle(g, v):
                print("Vehicle added successfully.")
            else:
                print("Failed to add vehicle. Garage might be full.")
        elif option == 3:
            vehicle_name = read_string("Enter the name of the vehicle to remove: ")
            if remove_vehicle(g, vehicle_name):
                print("Vehicle removed successfully.")
            else:
                print("Vehicle not found.")
        elif option == 4:
            service_vehicles(g)
        elif option == 5:
            vehicle_name = read_string("Enter the name of the vehicle to drive: ")
            trip_distance = read_double("Enter trip distance to drive: ")
            drive_vehicle_in_garage(g, vehicle_name, trip_distance)
        elif option == 6:
            vehicle_name = read_string("Enter the name of the vehicle to refuel: ")
            fuel_amount = read_integer("Enter the amount of fuel to add: ")
            refuel_vehicle_in_garage(g, vehicle_name, fuel_amount)
        elif option == 7:
            list_vehicles_needing_maintenance(g)
        elif option == 8:
            name = read_string("Enter vehicle name: ")
            v = find_vehicle(g, name)
            if v is not None:
                show_vehicle_info(v)
            else:
                print("Vehicle not found.")
        elif option == 9:
            break
        else:
            print("Invalid option, please try again.")

def manage_multiple_garages(garages):
    while True:
        print("1. Create new garage")
        print("2. Select garage")
        print("3. Delete garage")
        print("4. List all garages")
        print("5. Exit")
        option = read_integer("Choose an option: ")

        if option == 1:
            name = read_string("Enter garage name: ")
            max_capacity = read_integer("Enter garage maximum capacity: ")
            garages.append(Garage(name, max_capacity))
            print("Garage created successfully.")
        elif option == 2:
            if not garages:
                print("No garages available.")
                continue
            print("Available garages:")
            for i, g in enumerate(garages):
                print(f"{i + 1}. {g.name}")
            garage_index = read_integer("Select garage number: ") - 1
            if 0 <= garage_index < len(garages):
                manage_garage(garages[garage_index])
            else:
                print("Invalid garage number.")
        elif option == 3:
            if not garages:
                print("No garages available.")
                continue
            print("Available garages:")
            for i, g in enumerate(garages):
                print(f"{i + 1}. {g.name}")
            garage_index = read_integer("Select garage number to delete: ") - 1
            if 0 <= garage_index < len(garages):
                del garages[garage_index]
                print("Garage deleted successfully.")
            else:
                print("Invalid garage number.")
        elif option == 4:
            if not garages:
                print("No garages available.")
            else:
                print("Available garages:")
                for g in garages:
                    print(f"- {g.name}")
        elif option == 5:
            break
        else:
            print("Invalid option, please try again.")

def main():
    garages = []
    manage_multiple_garages(garages)

if __name__ == "__main__":
    main()
