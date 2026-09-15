"""
Program Name: Package Shipment Tracker
Author: Jose Luna
Purpose: This program tracks the shipment of packages and provides updates on their status.
Resources: None
Date: 2026-09-11
"""

def main():
    """Run the main menu loop for the package tracker program."""
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

        if choice == "5":
            running = False

    choice = input("Enter your choice: ")
    print("You entered:", choice)

    if choice == input("Enter your choice: "):
        print("You entered:", choice)

main()