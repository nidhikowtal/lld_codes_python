from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime

# ===== Enums =====
class LogLevel(Enum):
    INFO = 1
    WARNING = 2
    ERROR = 3

# ===== Logger Interface =====
class LoggerInterface(ABC):
    @abstractmethod
    def log(self, message, level):
        pass

# ===== Concrete Loggers =====
class ConsoleLogger(LoggerInterface):
    def log(self, message, level):
        print(f"[{datetime.now()}] [{level.name}] {message}")

class FileLogger(LoggerInterface):
    def __init__(self, file_name):
        self.file_name = file_name

    def log(self, message, level):
        with open(self.file_name, "a") as f:
            f.write(f"[{datetime.now()}] [{level.name}] {message}\n")

# ===== Logger Manager =====
class LoggerManager:
    def __init__(self):
        self.loggers = []

    def add_logger(self, logger):
        self.loggers.append(logger)

    def log(self, message, level):
        for logger in self.loggers:
            logger.log(message, level)

# ======= Demo =======

logger = LoggerManager()
logger.add_logger(ConsoleLogger())
logger.add_logger(FileLogger("app.log"))

logger.log("System started", LogLevel.INFO)
logger.log("This is a warning", LogLevel.WARNING)
logger.log("Something went wrong!", LogLevel.ERROR)
