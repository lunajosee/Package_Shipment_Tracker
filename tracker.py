"""
Program Name: Package Shipment Tracker
Author: Jose Luna
Purpose: This program tracks the shipment of packages and provides updates on their status.
Resources: None
Date: 2026-09-11
"""
def add_package(packages):
    """Prompt the user for package details and add it to the packages dictionary."""
    package_id = input("Enter package ID: ")
    destination = input("Enter destination: ")
    packages[package_id] = {"destination": destination, "status": "warehouse"}
    print("Package added successfully.")

def view_packages(packages):
        """Print all packages and their details."""
        if packages:
            for package_id, details in packages.items():
                print(package_id, "-", details["destination"], "-", details["status"])
        else:
            print("No packages found.")

def update_package_status(packages):
    """Prompt the user for a package ID and update its status."""
    package_id = input("Enter package ID to update: ")

    if package_id in packages:
        print("Current status:", packages[package_id]["status"])
        new_status = input("Enter new status: ")
        packages[package_id]["status"] = new_status
        print("Package status updated successfully.")
    else:
        print("Package ID not found.")

def search_package(packages):
    """Prompt the user for a package ID and display its details."""
    package_id = input("Enter package ID to search: ")

    if package_id in packages:
        details = packages[package_id]
        print("Package ID:", package_id)
        print("Destination:", details["destination"])
        print("Status:", details["status"])
    else:
        print("Package ID not found.")

def main():
    """Run the main menu loop for the package tracker program."""
    packages = {}
    running = True

    while running:
        print("Package Shipment Tracker")
        print("1. Add package")
        print("2. Update package status")
        print("3. Search for package")
        print("4. View all packages")
        print("5. Quit")

        choice = input("Enter your choice: ")
        print("You entered:", choice)

        if choice == "1":
            add_package(packages)
        elif choice == "2":
            update_package_status(packages)
        elif choice == "3":
            search_package(packages)
        elif choice == "4":
            view_packages(packages)
        elif choice == "5":
            running = False
        else:
            print("Invalid choice. Please try again.")
    
main()