from abc import ABC, abstractmethod

# --- Observer Interface ---
class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float):
        pass

# --- Subject Interface ---
class Subject(ABC):
    @abstractmethod
    def add_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

# --- Concrete Subject (Weather Station) ---
class WeatherStation(Subject):
    def __init__(self):
        self._observers = []
        self._temperature = None

    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def set_temperature(self, temperature: float):
        print(f"\nWeatherStation: New temperature is {temperature}°C")
        self._temperature = temperature
        self.notify_observers()

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

# --- Concrete Observers ---
class TVDisplay(Observer):
    def update(self, temperature: float):
        print(f"TV Display: Weather updated, temperature = {temperature}°C")

class MobileDisplay(Observer):
    def update(self, temperature: float):
        print(f"Mobile Display: Weather updated, temperature = {temperature}°C")

if __name__ == "__main__":
    # Create subject
    weather_station = WeatherStation()

    # Create observers
    tv = TVDisplay()
    mobile = MobileDisplay()

    # Register observers
    weather_station.add_observer(tv)
    weather_station.add_observer(mobile)

    # Change weather
    weather_station.set_temperature(25)
    weather_station.set_temperature(30)

    # Remove one observer
    weather_station.remove_observer(tv)
    weather_station.set_temperature(28)
