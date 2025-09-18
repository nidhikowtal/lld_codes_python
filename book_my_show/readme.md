# 🎬 BookMyShow Low-Level Design (Python)

This project is a **Low-Level Design (LLD)** implementation of a simplified version of *BookMyShow* in Python, inspired by the Java implementation.  
It models core entities like `Movie`, `Theatre`, `Show`, `Seat`, and `Booking` while following **object-oriented design** and **SOLID principles**.

---

## 🚀 Features

- Manage movies across multiple cities  
- Manage theatres, screens, shows, and seats  
- Search movies by city  
- Search shows for a given movie in a city  
- Book seats for a show (with duplicate seat check)  
- Simple logging for key events (movie/show lookup, booking success/failure)

---


---

## 🧩 Design Overview

The system is designed around **entities** and **controllers**:

- **Entities:**  
  - `Movie`, `Theatre`, `Screen`, `Seat`, `Show`, `Booking`, `Payment`  
  - These represent real-world objects in BookMyShow.  
  - Each entity encapsulates its own data and behavior.

- **Controllers:**  
  - `MovieController` → handles CRUD for movies  
  - `TheatreController` → manages theatres, screens, shows  
  - These act as **service layers** between the client (`BookMyShow`) and entities.

- **Main Orchestrator (`BookMyShow`)**  
  - Initializes data (movies, theatres, shows)  
  - Handles user booking flow:  
    1. Search movie by city  
    2. Pick a show  
    3. Choose a seat  
    4. Confirm booking  

---

## 🧱 SOLID Principles in Use

1. **Single Responsibility Principle (SRP):**  
   - Each class has a *single responsibility*.  
   - Example: `MovieController` only manages movies, `TheatreController` only manages theatres & shows.  
   - `BookMyShow` orchestrates flow without mixing responsibilities.

2. **Open/Closed Principle (OCP):**  
   - The system is *open for extension but closed for modification*.  
   - Example: Adding new `SeatCategory` or `Payment` methods won’t break existing code, only requires extension.

3. **Liskov Substitution Principle (LSP):**  
   - Entities like `Seat` or `Screen` can be replaced by their subtypes without affecting correctness (if extended in future).  
   - Example: If we subclass `PremiumSeat` or `IMAXScreen`, the controllers still work.

4. **Interface Segregation Principle (ISP):**  
   - Python doesn’t enforce interfaces, but our controllers are designed with *focused responsibilities*.  
   - Example: `MovieController` exposes only `addMovie`, `getMovieByName`, `getMoviesByCity`—not unrelated methods.

5. **Dependency Inversion Principle (DIP):**  
   - High-level modules (`BookMyShow`) don’t depend on low-level details.  
   - Instead, they depend on abstractions (`MovieController`, `TheatreController`).  
   - Makes the system easier to test and extend.

---
