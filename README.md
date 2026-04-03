# Civil Registry System (CLI - Python)

## Overview

This project is a **command-line Civil Registry System** built in Python for learning backend development concepts.

It simulates real-world civil registry operations such as:

* Birth records
* Marriage records
* Death records

The system uses **JSON as a temporary storage** and is designed to be **upgradeable to SQL databases in the future**.

---

## Features

* Add and store different types of records
* Relationship-based system (Marriage and Death linked to Birth records via IDs)
* Data validation rules:

  * Prevent duplicate records
  * Prevent invalid marriages (non-existent, deceased, etc.)
* JSON-based persistence
* Simple CLI interface

---

## Project Structure

```
record.py        # Data models (Birth, Marriage, Death)
services.py      # Business logic and validation rules
json_db.py       # Storage layer (JSON database)
main.py          # CLI interface
validators.py    # (Planned) input validation
data/            # JSON storage
```

---

## Current Status

⚠️ **Work in Progress**

This project is still being improved and is not yet production-ready.

Planned improvements:

* Better validation system
* Improved CLI user experience
* Transition to SQLite / SQL database
* Refactoring and code cleanup
* More advanced relationship handling

---

## Learning Goals

This project focuses on:

* Object-Oriented Programming (OOP)
* Separation of concerns (models, services, storage)
* Data serialization/deserialization
* Basic backend architecture
* Preparing for SQL and frameworks like Django

---

## How to Run

```bash
python main.py
```

---

## Notes

This project is part of my learning journey toward becoming a backend developer.
Code may change frequently as improvements are made.
