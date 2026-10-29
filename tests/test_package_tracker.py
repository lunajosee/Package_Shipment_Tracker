"""
Program Name: test_package_tracker.py
Author: Jose Luna
Purpose: Unit tests for the PackageTracker class.
Resources: pytest documentation
Date: 10/28/26
"""
from package_tracker import PackageTracker


def test_add_package_stores_it():
    """Adding a package should make it searchable by ID."""
    tracker = PackageTracker()
    assert tracker.add_package("PKG1", "Denver") is True
    assert tracker.search_package("PKG1").destination == "Denver"


def test_add_duplicate_id_is_rejected():
    """Adding an ID that already exists should fail and keep the original."""
    tracker = PackageTracker()
    tracker.add_package("PKG1", "Denver")
    assert tracker.add_package("PKG1", "Miami") is False
    assert tracker.search_package("PKG1").destination == "Denver"


def test_search_missing_package_returns_none():
    """Searching for an ID that was never added should return None."""
    tracker = PackageTracker()
    assert tracker.search_package("NOPE") is None


def test_update_status_changes_status():
    """Updating an existing package should change its status."""
    tracker = PackageTracker()
    tracker.add_package("PKG1", "Denver")
    assert tracker.update_status("PKG1", "in transit") is True
    assert tracker.search_package("PKG1").status == "in transit"


def test_update_status_unknown_id_returns_false():
    """Updating an ID that doesn't exist should return False."""
    tracker = PackageTracker()
    assert tracker.update_status("NOPE", "delivered") is False


def test_list_packages_returns_all_packages():
    """list_packages should return every package that was added."""
    tracker = PackageTracker()
    tracker.add_package("PKG1", "Denver")
    tracker.add_package("PKG2", "Miami")
    assert len(tracker.list_packages()) == 2