# Singleton Design Pattern - Logger Example

## What is the Singleton Design Pattern?
The **Singleton Design Pattern** ensures that only **one instance of a class** is created during the entire lifecycle of an application.  
Instead of creating multiple objects, the same instance is reused every time it is needed.  

This is useful when:
- You want **a single point of control** (e.g., configuration manager, database connection, logging system).
- You need to avoid duplication of shared resources.
- Consistency is required across the application.

---

## Example: Logger as a Singleton

In this project, we have implemented a **Logger** class as a Singleton.

### How it works:
1. The class has a **class-level variable `_instance`** that stores the single instance of the class.
2. The `__new__` method is overridden:
   - If `_instance` is `None`, a **new object** is created.
   - If `_instance` already exists, the **same object** is returned again.
3. This ensures that no matter how many times you instantiate the class, you always get the same object.
4. The `log()` method is used to store log messages in a list and print them.

---

## Key Observations in the Code

- When you create `logger1 = Logger()`, it prints:  
  **"Creating a new Logger instance..."** → because no instance existed yet.

- When you create `logger2 = Logger()`, it prints:  
  **"Reusing the existing Logger instance..."** → because the instance already exists.

- Both `logger1` and `logger2` point to the **same object in memory**, so their logs are shared.

- Example log flow:
  - `logger1.log("Starting application...")` → Adds log message.
  - `logger2.log("An error occurred.")` → Adds another log message to the same list.
  - Both `logger1` and `logger2` share the same `logs`.

---

## Why Singleton for Logger?
- Ensures **consistent logging across the application**.
- Prevents creation of multiple loggers writing to different places.
- Acts as a **centralized logging system**.

---

## Output Demonstration

