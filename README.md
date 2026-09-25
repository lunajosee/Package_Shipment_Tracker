[Video link coming soon]

# Package Shipment Tracker

A command-line Python program that simulates tracking a set of packages through their shipment lifecycle — adding new packages, updating their status, searching by ID, and viewing everything currently tracked.

## Features

- **Add a package** — store a new package with a destination and starting status ("warehouse")
- **Update package status** — move a package through its lifecycle (e.g. warehouse → in transit → delivered)
- **Search for a package** — look up a specific package by ID and view its details
- **View all packages** — list every tracked package and its current status

## How to run

```
python tracker.py
```

Follow the on-screen menu to add, update, search, or view packages, or quit the program.

## Design notes

This project uses a **dictionary** (`packages`) as its main data structure, keyed by package ID. A dictionary was chosen over a list because the program's core operations — searching for a specific package and updating its status — require fast lookup by ID rather than scanning through items in order. Each package's details (destination, status) are stored as a nested dictionary under its ID.

A tuple wasn't used because none of the program's data is fixed — packages are added, and their status changes over time, so a mutable structure (dictionary) fits better than an immutable one.

## Concepts demonstrated

- Variables & simple data types (strings, booleans)
- Collections (dictionary, including nested dictionaries)
- Control flow (if/elif/else)
- Iteration (while loop for the menu, for loop to display packages)
- User interaction (input/print)
- Functions (each feature is its own function: `add_package`, `view_packages`, `update_package_status`, `search_package`)