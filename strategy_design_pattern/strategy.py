from abc import ABC, abstractmethod

# --- Strategy Interface ---
class DrivingStrategy(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def toll_rate(self):
        """Return toll rate for this driving type."""
        pass


# --- Concrete Strategies ---
class NormalDrive(DrivingStrategy):
    def drive(self):
        print("🚗 Driving at a normal speed.")
    
    def toll_rate(self):
        return 50  # Rs. 50 per toll


class SportsDrive(DrivingStrategy):
    def drive(self):
        print("🏎️ Driving at a high speed like a sports car!")
    
    def toll_rate(self):
        return 100  # Rs. 100 per toll


class OffRoadDrive(DrivingStrategy):
    def drive(self):
        print("🚙 Driving off-road through rough terrain.")
    
    def toll_rate(self):
        return 30  # Rs. 30 per toll


# --- Context (Vehicle) ---
class Vehicle:
    def __init__(self, driving_strategy):
        self.driving_strategy = driving_strategy

    def drive(self):
        self.driving_strategy.drive()
        print(f"Toll Rate: ₹{self.driving_strategy.toll_rate()}")

    def set_driving_strategy(self, strategy):
        self.driving_strategy = strategy


# --- Usage ---
car = Vehicle(NormalDrive())
car.drive()   # Normal driving + toll info

# Change behavior at runtime
car.set_driving_strategy(SportsDrive())
car.drive()   # Sports driving + new toll rate

jeep = Vehicle(OffRoadDrive())
jeep.drive()  # Off-road driving + toll info
