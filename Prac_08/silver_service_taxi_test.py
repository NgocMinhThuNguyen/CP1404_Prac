from Prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Test Silver service taxi"""
    taxi = SilverServiceTaxi("Limo", 100, 6)
    taxi.drive(18)
    print(taxi)
    print(f"The fare is ${taxi.get_fare()}")


main()
