# 🧩 Chain of Responsibility Pattern — Logger Example

## 📘 Overview
The **Chain of Responsibility (CoR)** pattern is a **behavioral design pattern** that lets you **pass requests along a chain of handlers**, where each handler decides either to **process the request** or **pass it to the next handler** in the chain.

This helps you **decouple the sender and receiver** of a request, making the system **flexible**, **extensible**, and **easy to maintain**.

---

## 🧠 Concept

In a typical logging system, you may want to log messages to:
- The **console**
- A **file**
- Send an **email alert**

If you hard-code all these actions together, your code becomes tightly coupled and harder to extend.  
The Chain of Responsibility pattern solves this by organizing the loggers into a **linked chain of handlers**.

Each handler decides:
1. Whether to handle the log message, and then  
2. Whether to forward it to the **next handler**.

---

## 🏗️ Code Structure

### 🔹 Enum: `LogLevel`
Defines levels of logging (e.g., INFO, DEBUG, ERROR).

```python
class LogLevel(Enum):
    INFO = 1
    DEBUG = 2
    ERROR = 3
```

---

### 🔹 Abstract Handler: `LogHandler`
The base class (interface) for all loggers.

- Contains a reference to the **next handler**.
- Defines an **abstract `handle()`** method to be implemented by subclasses.

```python
class LogHandler(ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def set_next(self, next_handler):
        self.next_handler = next_handler
        return next_handler  # allows chaining

    @abstractmethod
    def handle(self, level, message):
        pass
```

---

### 🔹 Concrete Handlers

#### 🖥️ ConsoleLogger
Prints the log message to the console.

```python
class ConsoleLogger(LogHandler):
    def handle(self, level, message):
        print(f"[{datetime.now()}] [{level.name}] {message}")
        if self.next_handler:
            self.next_handler.handle(level, message)
```

#### 📁 FileLogger
Writes the log message to a file (`app.log`).

```python
class FileLogger(LogHandler):
    def __init__(self, file_name, next_handler=None):
        super().__init__(next_handler)
        self.file_name = file_name

    def handle(self, level, message):
        with open(self.file_name, "a") as f:
            f.write(f"[{datetime.now()}] [{level.name}] {message}\n")
        if self.next_handler:
            self.next_handler.handle(level, message)
```

#### 📧 EmailLogger
Simulates sending an email alert for the log.

```python
class EmailLogger(LogHandler):
    def handle(self, level, message):
        print(f"📧 Email alert sent: {message}")
        if self.next_handler:
            self.next_handler.handle(level, message)
```

---

### 🔹 Logger (Entry Point)
Acts as the single interface for the client.  
It holds the **first handler** in the chain and starts the logging process.

```python
class Logger:
    def __init__(self, handler):
        self.handler = handler

    def log(self, level, message):
        self.handler.handle(level, message)
```

---

## 🔗 Chain Setup

You can easily **customize the flow** by changing how handlers are chained.

```python
console = ConsoleLogger()
file_logger = FileLogger("app.log")
email = EmailLogger()

# Chain of Responsibility: console → file → email
console.set_next(file_logger).set_next(email)

logger = Logger(console)
```

---

## 🚀 Example Run

```python
logger.log(LogLevel.INFO, "System started")
logger.log(LogLevel.DEBUG, "Debugging cache initialization")
logger.log(LogLevel.ERROR, "Database connection failed!")
```

### 🧾 Output

```
[2025-10-16 17:30:00] [INFO] System started
📧 Email alert sent: System started

[2025-10-16 17:30:00] [DEBUG] Debugging cache initialization
📧 Email alert sent: Debugging cache initialization

[2025-10-16 17:30:00] [ERROR] Database connection failed!
📧 Email alert sent: Database connection failed!
```

A log file `app.log` will also contain:
```
[2025-10-16 17:30:00] [INFO] System started
[2025-10-16 17:30:00] [DEBUG] Debugging cache initialization
[2025-10-16 17:30:00] [ERROR] Database connection failed!
```

---

## 💡 Key Takeaways

- **Extensible**: Add new loggers (e.g., `SlackLogger`, `DatabaseLogger`) without changing existing code.
- **Decoupled**: Each handler works independently and only knows about the *next* handler.
- **Flexible**: You can change the logging flow easily (e.g., skip file logging).

---

## 🧩 Pattern Summary

| Component | Responsibility |
|------------|----------------|
| `LogHandler` | Abstract base defining the interface |
| `ConsoleLogger`, `FileLogger`, `EmailLogger` | Concrete handlers |
| `Logger` | Entry point that starts the chain |
| `set_next()` | Connects handlers dynamically |
| `handle()` | Processes request and forwards it |

---

## 🏁 Interview Tip
When explaining in interviews:
- Emphasize **decoupling** and **open/closed principle** (easy extension without modifying existing code).
- Mention **real-world analogy**: like a *customer complaint chain*—if one employee can’t handle it, they pass it to the next.
