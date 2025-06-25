# Snake and Ladder - Low Level Design (LLD) in Python

This project is a clean, modular implementation of the classic **Snake and Ladder** game using Python, crafted to demonstrate good Low-Level Design (LLD) principles.

---

## Core Functionality

- The board is a 2D grid (default 10x10) where each cell can optionally contain a snake or a ladder.
- Snakes and ladders are represented using `Jump` objects with a `start` and `end` position.
- Players take alternate turns, roll a die, and move forward by the rolled number.
- If a player lands at the `start` of a snake or ladder, they are automatically moved to the `end` of that jump.
- The first player to reach or pass the final cell (bottom-right) wins.
- Turn management is handled using a `deque` for smooth player rotation.
- The game logic is modular, testable, and cleanly separated from data representations.

---

## Class Responsibilities

| Module         | Class      | Responsibility |
|----------------|------------|----------------|
| `entities/`    | `Board`    | Creates a board, places snakes and ladders randomly |
|                | `Cell`     | Represents a single square on the board |
|                | `Jump`     | Represents a snake or ladder (start and end positions) |
|                | `Player`   | Holds player ID and current board position |
| `services/`    | `Dice`     | Rolls the die and returns the total |
|                | `Game`     | Manages game turns, player movement, win condition, and jumps |
| Root           | `main.py`  | Entry point that starts the game |

---

## Design Principles Used

### 1. **Single Responsibility Principle (SRP)**
- Each class does **one thing**: e.g., `Dice` handles randomness, `Board` manages layout, `Player` stores identity and position.

### 2. **Open-Closed Principle (OCP)**
- The system can be extended (e.g., multiple dice, new player types) without modifying existing logic.

### 3. **Encapsulation**
- Classes encapsulate their own behavior and expose only what is necessary.

### 4. **Separation of Concerns**
- Business logic (`Game`) is separated from the board structure and utility components (`Dice`, `Jump`, etc).

### 5. **DRY (Don't Repeat Yourself)**
- Reusable logic for jumps, turns, and cell computation is abstracted into methods.

### 6. **Modularity**
- Clearly separated modules (`entities/`, `services/`) for clean organization and testability.

### 7. **Loose Coupling**
- `Game` interacts with high-level interfaces like `Board` and `Dice`, not their internals directly.

---

