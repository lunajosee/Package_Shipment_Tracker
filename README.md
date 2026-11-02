[(https://youtu.be/ZDlVCM4PGkA)]

# Package Shipment Tracker

A command-line Python program for tracking packages through a shipment lifecycle. Project 2 refactors my Project 1 tracker into separate modules and classes, adds JSON data persistence, and adds automated tests with pytest.

## Features

- Add a package with a destination (duplicate IDs are rejected)
- Update a package's status (warehouse, in transit, delivered)
- Search for a package by ID
- View all packages
- Packages are saved to `packages.json` and reloaded the next time the program runs

## Project structure

| File | Purpose |
|---|---|
| `package.py` | `Package` class: one shipment's ID, destination, and status |
| `package_tracker.py` | `PackageTracker` class: manages the collection of packages |
| `storage.py` | Saves and loads packages as JSON, with error handling |
| `tracker.py` | Menu loop that handles user input and output |
| `tests/` | pytest unit tests for `Package`, `PackageTracker`, and `storage` |

## How to run

```
python tracker.py
```

## How to run the tests

```
python -m pip install -r requirements.txt
python -m pytest
```

## Design notes

- **Composition over inheritance.** `PackageTracker` holds `Package` objects but is not a kind of package, so inheritance would not model the problem. A flat class structure keeps the code simple.
- **Dictionary for the collection.** Packages are stored in a dictionary keyed by ID because the main operations (search and update) look packages up by ID.
- **Separation of concerns.** The classes only manage data. `tracker.py` is the only file that calls `input()` and `print()`, which keeps the logic testable.
- **JSON persistence with error handling.** `storage.py` uses `try/except` so a missing or corrupted data file starts the program with no packages instead of crashing.

## Chapter 8-11 concepts demonstrated

- **Functions and modules:** separate modules, default arguments, return values
- **Classes:** `Package` and `PackageTracker`, with attributes and methods
- **File I/O and exceptions:** reading and writing a file with `try/except`
- **Data persistence:** the `json` module
- **Testing:** 12 pytest unit tests

## Project 1 video

The original Project 1 version of this tracker: https://youtu.be/t4IR0Josfvs