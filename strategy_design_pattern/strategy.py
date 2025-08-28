from abc import ABC, abstractmethod

# --- Strategy Interface ---
class DrivingStrategy(ABC):
    @abstractmethod
    def drive(self):
        pass

# --- Concrete Strategies ---
class NormalDrive(DrivingStrategy):
    def drive(self):
        print("Driving at a normal speed.")

class SportsDrive(DrivingStrategy):
    def drive(self):
        print("Driving at a high speed like a sports car!")

class OffRoadDrive(DrivingStrategy):
    def drive(self):
        print("Driving off-road through rough terrain.")

# --- Context (Vehicle) ---
class Vehicle:
    def __init__(self, driving_strategy: DrivingStrategy):
        self._driving_strategy = driving_strategy

    def drive(self):
        self._driving_strategy.drive()

    def set_driving_strategy(self, strategy: DrivingStrategy):
        self._driving_strategy = strategy

# --- Usage ---
if __name__ == "__main__":
    car = Vehicle(NormalDrive())
    car.drive()   # Driving at a normal speed.

    # Change behavior at runtime
    car.set_driving_strategy(SportsDrive())
    car.drive()   # Driving at a high speed like a sports car!

    jeep = Vehicle(OffRoadDrive())
    jeep.drive()  # Driving off-road through rough terrain.
