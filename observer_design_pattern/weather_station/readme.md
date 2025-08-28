# Observer Pattern in Python

## What is the Observer Pattern?

The **Observer Pattern** is a behavioral design pattern that defines a one-to-many dependency between objects.  
When the state of one object (called the **Subject**) changes, all its dependent objects (called **Observers**) are notified and updated automatically.

It is often used when multiple objects need to be updated whenever one object changes, without tightly coupling the objects together.

**Key points:**
- The **Subject** maintains a list of observers.
- Observers can subscribe (attach) or unsubscribe (detach).
- When the subject’s state changes, it **notifies all observers** by calling their update method.

This decouples the subject from the observers, making the system more flexible and extensible.

---

## How Observer Pattern is Used Here

In this code:
- **Subject (`Product`)**: Represents a product whose availability can change. It maintains a list of observers (customers) who are interested in updates.
- **Observers (`Customer`)**: Each customer registers interest in the product. When the product’s availability changes, they get notified automatically.

### Flow:
1. A product is created (subject).
2. Customers subscribe (attach) themselves as observers to the product.
3. When the product becomes available, the product notifies all subscribed customers.
4. Each customer receives a notification (through the `update` method).

