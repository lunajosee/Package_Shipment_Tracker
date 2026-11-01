"""
Program Name: tracker.py
Author: Jose Luna
Purpose: Command-line menu for the Package Shipment Tracker. Handles
         user input and output and delegates the data work to
         PackageTracker and the storage module.
Resources: Refactored from the Project 1 tracker.py
Date: 10/30/26
"""
from package_tracker import PackageTracker
from storage import load_packages, save_packages


def handle_add(tracker):
    """Ask for package details and add the package to the tracker."""
    package_id = input("Enter package ID: ").strip()
    destination = input("Enter destination: ").strip()
    if tracker.add_package(package_id, destination):
        print("Package added successfully.")
    else:
        print("That package ID already exists.")


def handle_update(tracker):
    """Ask which package to update and change its status."""
    package_id = input("Enter package ID to update: ").strip()
    package = tracker.search_package(package_id)
    if package is None:
        print("Package ID not found.")
        return
    print("Current status:", package.status)
    new_status = input("Enter new status (warehouse/in transit/delivered): ").strip()
    tracker.update_status(package_id, new_status)
    print("Status updated successfully.")


def handle_search(tracker):
    """Ask for a package ID and display that package's details."""
    package_id = input("Enter package ID to search: ").strip()
    package = tracker.search_package(package_id)
    if package is None:
        print("Package ID not found.")
    else:
        print("Package ID:", package.package_id)
        print("Destination:", package.destination)
        print("Status:", package.status)


def handle_view(tracker):
    """Display every package currently being tracked."""
    packages = tracker.list_packages()
    if not packages:
        print("No packages found.")
        return
    for package in packages:
        print(package.package_id, "-", package.destination, "-", package.status)


def main():
    """Load saved packages and run the menu loop until the user quits."""
    tracker = load_packages()
    running = True

    while running:
        print("\nPackage Shipment Tracker")
        print("1. Add package")
        print("2. Update package status")
        print("3. Search for package")
        print("4. View all packages")
        print("5. Quit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            handle_add(tracker)
            save_packages(tracker)
        elif choice == "2":
            handle_update(tracker)
            save_packages(tracker)
        elif choice == "3":
            handle_search(tracker)
        elif choice == "4":
            handle_view(tracker)
        elif choice == "5":
            running = False
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()