"""
Program Name: test_package.py
Author: Jose Luna
Purpose: Unit tests for the Package class.
Resources: pytest documentation
Date: 10/27/26
"""
from package import Package


def test_status_defaults_to_warehouse():
    """A package created without a status should start in the warehouse."""
    package = Package("PKG1", "Denver")
    assert package.status == "warehouse"

def test_package_stores_id_and_destination():
    """A package should keep the ID and destination it was created with."""
    package = Package("PKG1", "Denver")
    assert package.package_id == "PKG1"
    assert package.destination == "Denver"

def test_to_dict_returns_all_fields():
    """to_dict should return the package's data as a dictionary."""
    package = Package("PKG1", "Denver", "in transit")
    assert package.to_dict() == {
        "package_id": "PKG1",
        "destination": "Denver",
        "status": "in transit"
        }