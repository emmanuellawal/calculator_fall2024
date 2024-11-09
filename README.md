# Calculator Fall 2024

![Calculator Logo](https://via.placeholder.com/150) <!-- Replace with actual logo if available -->

Welcome to **Calculator Fall 2024**, a robust and extensible Python-based calculator application. Designed with clean architecture and modern design patterns, this project emphasizes maintainability, scalability, and ease of use. Whether you're performing simple arithmetic operations or integrating complex command handling, Calculator Fall 2024 has you covered.

---

## 📚 Table of Contents

1. [Features](#features)
2. [Project Structure](#project-structure)
3. [Installation](#installation)
4. [Setup Instructions](#setup-instructions)
5. [Usage Examples](#usage-examples)
6. [Testing](#testing)
7. [Architectural Decisions](#architectural-decisions)
    - [Design Patterns](#design-patterns)
    - [Logging Strategy](#logging-strategy)
8. [Contributing](#contributing)
9. [License](#license)
10. [Acknowledgements](#acknowledgements)

---

## Features

- **Basic Arithmetic Operations:** Addition, subtraction, multiplication, and division.
- **Command Handling:** Execute and manage commands efficiently using the Command Pattern.
- **History Management:** Track, undo, and manage calculation history.
- **Extensible Architecture:** Easily add new features and functionalities.
- **Comprehensive Testing:** Ensures reliability and correctness with `pytest`.
- **Logging:** Detailed logging for monitoring and debugging.

---

## Project Structure

```bash
calculator_fall2024/
├── app/
│   ├── __init__.py
│   ├── calculator.py
│   ├── commands.py
│   └── operations.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_calculator.py
│   └── test_history.py
├── .env
├── .gitignore
├── requirements.txt
├── pytest.ini
├── README.md
└── setup.py

Video 
https://youtu.be/n4FxGs_V7ZE