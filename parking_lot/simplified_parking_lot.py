from datetime import datetime
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
        self.is_free = True
        self.vehicle = None

    def parking_vehicle(self, vehicle):
        self.vehicle = vehicle
        self.is_free = False

    def removing_vehicle(self):
        self.vehicle = None
        self.is_free = True


class Ticket:
    def __init__(self, ticket_id, vehicle, spot_id):
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.spot_id = spot_id
        self.entry_time = datetime.now()


class Receipt:
    def __init__(self, ticket, amount):
        self.ticket = ticket
        self.exit_time = datetime.now()
        self.amount = amount


# ===== Core Service =====
class ParkingLot:
    def __init__(self):
        self.spots = []
        self.active_tickets = {}

    def add_spot(self, spot_id, spot_type):
        spot = ParkingSpot(spot_id, spot_type)
        self.spots.append(spot)

    def find_free_spot(self, vehicle_type):
        for spot in self.spots:
            if spot.is_free and self._is_spot_suitable(spot, vehicle_type):
                return spot
        return None

    def _is_spot_suitable(self, spot, vehicle_type):
        # basic matching logic
        if vehicle_type == VehicleType.BIKE and spot.spot_type == SpotType.SMALL:
            return True
        if vehicle_type == VehicleType.CAR and spot.spot_type == SpotType.MEDIUM:
            return True
        if vehicle_type == VehicleType.TRUCK and spot.spot_type == SpotType.LARGE:
            return True
        return False

    def park_vehicle(self, vehicle):
        spot = self.find_free_spot(vehicle.vehicle_type)
        if not spot:
            print("❌ No available spot for this vehicle.")
            return None

        spot.parking_vehicle(vehicle)
        ticket_id = len(self.active_tickets) + 1
        ticket = Ticket(ticket_id, vehicle, spot.spot_id)
        self.active_tickets[ticket_id] = ticket

        print(f"✅ Vehicle {vehicle.vehicle_number} parked at spot {spot.spot_id}. Ticket ID: {ticket_id}")
        return ticket

    def unpark_vehicle(self, ticket_id):
        if ticket_id not in self.active_tickets:
            print("⚠️ Invalid ticket ID.")
            return None

        ticket = self.active_tickets.pop(ticket_id)
        spot = None
        for s in self.spots:
            if s.spot_id == ticket.spot_id:
                spot = s
                break

        if spot:
            spot.removing_vehicle()
            amount = self.calculate_fare(ticket)
            receipt = Receipt(ticket, amount)
            print(f"🚗 Vehicle {ticket.vehicle.vehicle_number} exited. Amount: ₹{amount}")
            return receipt

    def calculate_fare(self, ticket):
        duration = (datetime.now() - ticket.entry_time).seconds / 60
        return round(max(duration, 0.1) * 50, 2)  # ₹50 per minute minimum 0.1 minute


# ======= Demo =======
parking_lot = ParkingLot()

# Add some parking spots
parking_lot.add_spot(1, SpotType.SMALL)
parking_lot.add_spot(2, SpotType.MEDIUM)
parking_lot.add_spot(3, SpotType.LARGE)

# Create vehicles
car = Vehicle("MH12AB1234", VehicleType.CAR)
bike = Vehicle("MH14XY5678", VehicleType.BIKE)

# Park vehicles
car_ticket = parking_lot.park_vehicle(car)
bike_ticket = parking_lot.park_vehicle(bike)

# Unpark one
if car_ticket:
    parking_lot.unpark_vehicle(car_ticket.ticket_id)
