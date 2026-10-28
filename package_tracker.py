"""
Program Name: package_tracker.py
Author: Jose Luna
Purpose: Defines the PackageTracker class, which manages a collection of Package objects keyed by package ID.
Resource: Refactored from the Project 1 tracker.py functions
Date: 10/27/26
"""
from package import Package

class PackageTracker:
    """Manages a collection of packages."""

    def __init__(self):
        """Create a tracker that starts with no packages"""
        self.packages = {}

    def add_package(self, package_id, destination):
        """Add a new package. Return True if added, False if the ID is taken."""
        if package_id in self.packages:
            return False
        self.packages[package_id] = Package(package_id, destination)
        return True

    def search_package(self, package_id):
        """Return the Package with the given ID, or None if it isn't found"""
        return self.packages.get(package_id)

    def update_status(self, package_id, new_status):
        """Update a packages status. Return True if updated, False if not found"""
        package = self.search_package(package_id)
        if package is None:
            return False
        package.status = new_status
        return True

    def list_packages(self):
        """Return a list of all Packages objects being tracked."""
        return list(self.packages.values())

