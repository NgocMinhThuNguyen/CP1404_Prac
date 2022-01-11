from Prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialize silver service taxi"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * fanciness

    def get_fare(self):
        """Get fare"""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Print a statement that represents the silver service taxi"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"