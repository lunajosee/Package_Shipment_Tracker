"""
Program Name: Package Shipment Tracker
Author: Jose Luna
Purpose: This program tracks the shipment of packages and provides updates on their status.
Resources: None
Date: 2026-09-11
"""

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
            package_id = input("Enter package ID: ")
            destination = input("Enter destination: ")
            packages[package_id] = {"destination": destination, "status": "warehouse"}
            print("Package added successfully.")
        elif choice == "2":
            print("Update status selected")
        elif choice == "3":
            print("Search package selected.")           
        elif choice == "4":
            if packages:
                for package_id, details in packages.items():
                    print(package_id, "-", details["destination"], "-", details["status"])
            else:
                print("No packages found.")
        elif choice == "5":
            running = False
        else:
            print("Invalid choice, please try again.")
    

main()