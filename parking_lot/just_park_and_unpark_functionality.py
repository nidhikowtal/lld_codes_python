from enum import Enum

# ===== Enums =====
class VehicleType(Enum):
    CAR = 1
    BIKE = 2
    TRUCK = 3

class SpotType(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

# ===== Entities =====
class Vehicle:
    def __init__(self, vehicle_number, vehicle_type):
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type

class ParkingSpot:
    def __init__(self, spot_id, spot_type):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.vehicle = None
        self.is_free = True

    def park_vehicle(self, vehicle):
        self.vehicle = vehicle
        self.is_free = False

    def remove_vehicle(self):
        self.vehicle = None
        self.is_free = True

# ===== Core Service =====
class ParkingLot:
    def __init__(self):
        self.spots = []                 # list of spots
        self.vehicle_to_spot = {}       # vehicle object -> spot

    def add_spot(self, spot_id, spot_type):
        self.spots.append(ParkingSpot(spot_id, spot_type))

    def _is_suitable(self, spot, vehicle_type):
        if vehicle_type == VehicleType.BIKE and spot.spot_type == SpotType.SMALL:
            return True
        if vehicle_type == VehicleType.CAR and spot.spot_type == SpotType.MEDIUM:
            return True
        if vehicle_type == VehicleType.TRUCK and spot.spot_type == SpotType.LARGE:
            return True
        return False

    def find_free_spot(self, vehicle_type):
        for spot in self.spots:
            if spot.is_free and self._is_suitable(spot, vehicle_type):
                return spot
        return None

    def park_vehicle(self, vehicle):
        spot = self.find_free_spot(vehicle.vehicle_type)
        if not spot:
            print(f"❌ No available spot for {vehicle.vehicle_number}.")
            return

        spot.park_vehicle(vehicle)
        self.vehicle_to_spot[vehicle] = spot
        print(f"✅ Vehicle {vehicle.vehicle_number} parked at spot {spot.spot_id}.")

    def unpark_vehicle(self, vehicle):
        spot = self.vehicle_to_spot[vehicle]
        if spot:
            del self.vehicle_to_spot[vehicle]
            spot.remove_vehicle()
            print(f" Vehicle {vehicle.vehicle_number} unparked from spot {spot.spot_id}.")
        else:
            print(f"⚠️ Vehicle {vehicle.vehicle_number} not found in parking lot.")

# ======= Demo =======
parking_lot = ParkingLot()

# Add parking spots
parking_lot.add_spot(1, SpotType.SMALL)
parking_lot.add_spot(2, SpotType.MEDIUM)
parking_lot.add_spot(3, SpotType.LARGE)

# Create vehicles
car = Vehicle("MH12AB1234", VehicleType.CAR)
bike = Vehicle("MH14XY5678", VehicleType.BIKE)
truck = Vehicle("MH20TR0001", VehicleType.TRUCK)

# Park vehicles
parking_lot.park_vehicle(car)
parking_lot.park_vehicle(bike)
parking_lot.park_vehicle(truck)

# Unpark vehicles
parking_lot.unpark_vehicle(car)
parking_lot.unpark_vehicle(bike)
parking_lot.unpark_vehicle(truck)
