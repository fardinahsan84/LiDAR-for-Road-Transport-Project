# Define a dictionary to manage the status of zones
zones = {
    "1A": "OFF",
    "1B": "OFF",
    "2A": "OFF",
    "2B": "OFF"
}
yeldingSpeed = 0.1

def elapsedTime():
    print("\nSafe to go")

def checkSpeed(speed):
    if speed <= yeldingSpeed:
        elapsedTime()
    else:
        print("\nRepeat the process!!")



def set_occupancy(zone, status, speed):

    """Set the occupancy status for a specific zone."""
    if zone in zones and status in ["ON", "OFF"]:
        zones[zone] = status
        print(f"Zone {zone} is now set to {status}.")
    else:
        print("Invalid zone or status. Please try again.")

    """"Check zones, current speed and safety"""

    print("\nCurrent Zone Status:")
    for zone, status in zones.items():
        print(f"Zone {zone}: {status}")

    print(f"\nCurrent speed: {speed} KPH")

    if any(status == "ON" for status in zones.values()):
        print("At least one zone is ON.")

        if zones["1A"] == "ON" or zones["1B"] == "ON":
            if zones["2A"] == "OFF" and zones["2B"] == "OFF":
                elapsedTime()
            else:
                checkSpeed(speed)
        else:
            if zones["2A"] == "ON" or zones["2B"] == "ON":
                checkSpeed(speed)
            else:
                elapsedTime()
    else:
        elapsedTime()


def check_zones():
    """Check and display the status of all zones."""
    print("\nCurrent Zone Status:")
    for zone, status in zones.items():
        print(f"Zone {zone}: {status}")




# Main function for interaction
def main():
    while True:
        print("\nMenu:")
        print("1. Set Occupancy")
        print("2. Check Zones")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            zone = input("Enter the zone (1A, 1B, 2A, 2B): ").upper()
            status = input("Enter status (ON/OFF): ").upper()
            speed = float(input("Current speed (in KPH): "))
            set_occupancy(zone, status, speed)
        
        elif choice == "2":
            check_zones()
        
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
