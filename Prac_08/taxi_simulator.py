from Prac_08.taxi import Taxi
from Prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator program"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "c":
            print("Taxi available: ")
            print_taxis(taxis)
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            total_bill += drive(current_taxi)
        print(f"Bill to date :${total_bill}")
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    print_taxis(taxis)


def print_taxis(taxis):
    """Print taxi list"""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Choose a valid taxi from taxis"""
    try:
        taxi_choice = int(input("Choose Taxi: "))
        if taxi_choice < 0 or taxi_choice > len(taxis) - 1:
            print('Invalid Taxi Choice')
            return None
        return taxis[taxi_choice]
    except ValueError:
        print("Invalid Taxi Choice")
        return None


def drive(current_taxi):
    """Drive the taxi"""
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
        return 0
    else:
        miles_drive = int(input('Drive how far? '))
        current_taxi.drive(miles_drive)
        fare = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip will cost you ${fare}")
        current_taxi.start_fare()
        return fare


main()