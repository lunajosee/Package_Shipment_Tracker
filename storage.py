"""
Program Name: storage.py
Author: Jose Luna
Purpose: Saves and loads PackageTracker data to and from a JSON file
         so packages persist between runs.
Resources: Python json module documentation
Date: 10/29/26
"""
import json

from package_tracker import PackageTracker

DEFAULT_FILEPATH = "packages.json"


def save_packages(tracker, filepath=DEFAULT_FILEPATH):
    """Write every package in the tracker to a JSON file."""
    data = [package.to_dict() for package in tracker.list_packages()]
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def load_packages(filepath=DEFAULT_FILEPATH):
    """Return a PackageTracker filled from a JSON file.

    If the file is missing or unreadable, return an empty tracker
    instead of crashing.
    """
    tracker = PackageTracker()
    try:
        with open(filepath, encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        return tracker
    except json.JSONDecodeError:
        print("Saved data could not be read. Starting with no packages.")
        return tracker

    for entry in data:
        tracker.add_package(entry["package_id"], entry["destination"])
        tracker.update_status(entry["package_id"], entry["status"])
    return tracker