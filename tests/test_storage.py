"""
Program Name: test_storage.py
Author: Jose Luna
Purpose: Unit tests for the storage module's save and load functions.
Resources: pytest documentation
Date: 10/29/26
"""
from package_tracker import PackageTracker
from storage import load_packages, save_packages


def test_save_then_load_restores_packages(tmp_path):
    """Packages saved to a file should come back unchanged when loaded."""
    filepath = tmp_path / "packages.json"
    tracker = PackageTracker()
    tracker.add_package("PKG1", "Denver")
    tracker.update_status("PKG1", "in transit")

    save_packages(tracker, filepath)
    loaded = load_packages(filepath)

    package = loaded.search_package("PKG1")
    assert package.destination == "Denver"
    assert package.status == "in transit"


def test_load_missing_file_returns_empty_tracker(tmp_path):
    """Loading a file that doesn't exist should give an empty tracker."""
    loaded = load_packages(tmp_path / "does_not_exist.json")
    assert loaded.list_packages() == []


def test_load_corrupted_file_returns_empty_tracker(tmp_path):
    """Loading a file with invalid JSON should give an empty tracker."""
    filepath = tmp_path / "packages.json"
    filepath.write_text("this is not valid json", encoding="utf-8")
    loaded = load_packages(filepath)
    assert loaded.list_packages() == []