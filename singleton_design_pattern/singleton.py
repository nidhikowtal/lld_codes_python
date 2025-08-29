class Logger:
    _instance = None    # Class-level variable to store the single instance

    def __new__(cls):
        if cls._instance is None:
            print("Creating a new Logger instance...")
            cls._instance = super().__new__(cls)    # __new__ ensures only one object is ever created.
            cls._instance.logs = []
        else:
            print("Reusing the existing Logger instance...")
        return cls._instance

    def log(self, message):
        print(f"Logging message: {message}")
        self.logs.append(message)
        print(self.logs)


logger1 = Logger()
logger2 = Logger()

logger1.log("Starting application...")
logger2.log("An error occurred.")

print(logger1 is logger2)   # True → both are the same instance

