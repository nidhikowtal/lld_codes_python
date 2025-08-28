# Strategy Pattern in Python — Vehicles & Driving Behaviors

## Overview
This mini project demonstrates the **Strategy Design Pattern** by modeling different driving behaviors for vehicles. A vehicle can switch its driving behavior at runtime without changing its own code, making the system flexible and easy to extend.

---

## What is the Strategy Pattern?
The **Strategy Pattern** is a behavioral design pattern that:
- Defines a **family of algorithms/behaviors**.
- **Encapsulates** each behavior behind a common interface.
- Makes the behaviors **interchangeable at runtime**.
- Lets the algorithm **vary independently** from the object that uses it.

Use it when you have multiple ways to perform a task and you want to:
- Avoid `if/elif` chains scattered through your code.
- Swap behaviors dynamically.
- Add new behaviors without modifying existing logic.

---

## How it’s applied here
- **Context**: `Vehicle`  
  Holds a reference to a driving behavior and delegates the driving action to it. It exposes a method to change the current behavior at runtime.

- **Strategy Interface**: `DrivingStrategy`  
  Defines the contract that all driving behaviors must follow (e.g., a `drive` action).

- **Concrete Strategies**: `NormalDrive`, `SportsDrive`, `OffRoadDrive`  
  Each class encapsulates a distinct driving behavior. They are interchangeable because they share the same interface.

- **Runtime switching**:  
  A vehicle can start with one behavior (e.g., normal driving) and later switch to another (e.g., sports or off-road) without changing the `Vehicle` class.

---

## Running the example
1. Save the script to a file (for example, `strategy_vehicle.py`).
2. Run it as a normal Python program (for example, using `python strategy_vehicle.py` from your terminal).
3. Observe how the vehicle behavior changes at runtime.

> If you keep this inside a package or larger project, run it the same way you would run any Python script in your environment.

---

## Expected behavior (example)
- A vehicle created with the normal driving behavior prints a message indicating normal speed.
- After switching to a sports driving behavior, it prints a message indicating high speed.
- A separate vehicle using off-road behavior prints a message indicating off-road driving.

---

## Why this pattern helps
- **Flexibility**: Swap behaviors on the fly without touching the vehicle class.
- **Extensibility**: Add a new driving style (e.g., eco, autonomous) without modifying existing code.
- **Maintainability**: Clear separation of concerns; each behavior lives in its own class.
- **Testability**: Each behavior can be tested in isolation.

---

## SOLID principles in this example
- **Single Responsibility (SRP)**:  
  Each behavior class focuses on one driving style; the vehicle only coordinates which behavior to use.
- **Open/Closed (OCP)**:  
  New strategies can be added without modifying the `Vehicle` or existing strategies.
- **Liskov Substitution (LSP)**:  
  Any concrete driving behavior can replace another wherever a strategy is expected.
- **Interface Segregation (ISP)**:  
  The strategy interface is minimal and specific to the driving action.
- **Dependency Inversion (DIP)**:  
  The vehicle depends on an abstraction (strategy interface), not concrete behavior classes.

---

## Extending the example
- Add a new behavior (e.g., “Eco Drive” for energy-efficient driving).
- Introduce configuration to select the initial behavior based on environment or user preferences.
- Combine with other patterns (e.g., Factory to construct strategies based on input).

---

## Common pitfalls to avoid
- **Leaking behavior-specific logic into `Vehicle`**: keep all driving variations inside strategy classes.
- **Overusing strategies**: only extract behaviors that genuinely vary or are likely to change.
- **Tight coupling**: the context should work with the interface, not with specific strategy implementations.

---