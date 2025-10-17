from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime

# ---------- ENUM ----------
class LogLevel(Enum):
    INFO = 1
    DEBUG = 2
    ERROR = 3


# ---------- HANDLER INTERFACE ----------
class LogHandler(ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def set_next(self, next_handler):
        self.next_handler = next_handler
        return next_handler  # allows chaining

    @abstractmethod
    def handle(self, level, message):
        pass


# ---------- CONSOLE LOGGER ----------
class ConsoleLogger(LogHandler):
    def handle(self, level, message):
        print(f"[{datetime.now()}] [{level.name}] {message}")
        if self.next_handler:
            self.next_handler.handle(level, message)


# ---------- FILE LOGGER ----------
class FileLogger(LogHandler):
    def __init__(self, file_name, next_handler=None):
        super().__init__(next_handler)
        self.file_name = file_name

    def handle(self, level, message):
        with open(self.file_name, "a") as f:
            f.write(f"[{datetime.now()}] [{level.name}] {message}\n")
        if self.next_handler:
            self.next_handler.handle(level, message)


# ---------- EMAIL LOGGER ----------
class EmailLogger(LogHandler):
    def handle(self, level, message):
        print(f"📧 Email alert sent: {message}")
        if self.next_handler:
            self.next_handler.handle(level, message)


# ---------- LOGGER (ENTRY POINT) ----------
class Logger:
    def __init__(self, handler):
        self.handler = handler

    def log(self, level, message):
        self.handler.handle(level, message)


# ---------- CLIENT CODE ----------

console = ConsoleLogger()
file_logger = FileLogger("app.log")
email = EmailLogger()

# Chain: console → file → email
console.set_next(file_logger).set_next(email)

logger = Logger(console)

logger.log(LogLevel.INFO, "System started")
logger.log(LogLevel.DEBUG, "Debugging cache initialization")
logger.log(LogLevel.ERROR, "Database connection failed!")
