# Product Notify System (Observer Pattern)

## Overview
This project demonstrates the **Observer Design Pattern** in Python by implementing a simple notification system.  
Whenever a product goes **out of stock**, the system automatically notifies all subscribed observers (e.g., Email or SMS services).

## How It Works

### 1. **Subject (Observable)**
- `Subject` interface defines methods to attach, detach, and notify observers.
- `ProductSubject` implements this interface:
  - Holds a `Product`.
  - Keeps track of observers.
  - Notifies all observers when the product goes **out of stock**.

### 2. **Observer**
- `Observer` interface defines the `update` method.
- Concrete observers (`EmailObserver`, `SMSObserver`) implement how they react when notified.

### 3. **Flow**
1. A `ProductSubject` is created for a product.
2. Observers (Email and SMS) are attached to this subject.
3. When the product’s stock is reduced to `0`, `ProductSubject` calls `notify()`.
4. All attached observers receive the notification.