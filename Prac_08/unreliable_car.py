from Prac_08.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        """Initialize Unreliable Car instance"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Generate random number from 0 to 100 and drive 0 if reliability is less or equal"""
        if self.reliability <= random.randint(1, 100):
            distance = 0
        else:
            distance = super().drive(distance)
        return distance