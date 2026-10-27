"""
Program Name: package.py
Author: Jose Luna
Purpose: Defines the Package class, which stores the ID, destination, and the status of a single shipment.
Resources: Refactored from the Project 1 tracker.py
Date: 10/26/26
"""


class Package:
    """Represents a single package being tracked through shipment."""

    def __init__(self, package_id, destination, status="warehouse"):
        """Create a package with an ID, a destination, and a starting status."""
        self.package_id = package_id
        self.destination = destination
        self.status = status

    def to_dict(self):
        """Return the package's data as a dictionary for saving to JSON."""
        return {
            "package_id": self.package_id,
            "destination": self.destination,
            "status": self.status
        }