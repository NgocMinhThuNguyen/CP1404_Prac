from Prac_08.unreliable_car import UnreliableCar


def main():
    """Test Unreliable car program """

    car_test_1 = UnreliableCar("Limo", 100, 50)
    car_test_2 = UnreliableCar("Toyota", 200, 30)

    for i in range(1, 20):
        print(f"Attempt {i}, {car_test_1.name:6} drove {car_test_1.drive(i)} km")
        print(f"Attempt {i}, {car_test_2.name:6} drove {car_test_2.drive(i)} km")


main()