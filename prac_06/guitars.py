from prac_06.guitar import Guitar
from operator import attrgetter


def main():
    """Guitars program"""
    guitars = []

    print("My guitars!")
    name = input("Name: ")

    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        add_guitar = Guitar(name, year, cost)
        guitars.append(add_guitar)
        print(add_guitar, "added.")
        print()
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitars.sort(key=attrgetter("year"))

    print()
    print("...snip...")
    print()
    print("These are my guitars: ")

    i = 0
    for guitar in guitars:
        string = ""
        i += 1
        if guitar.is_vintage():
            string = "(vintage)"
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth $ {guitar.cost:10,.2f} {string}")


main()