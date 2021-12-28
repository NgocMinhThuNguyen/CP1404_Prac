VINTAGE_AGE = 50


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string that represents Guitar"""
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Return age of a Guitar"""
        return 2021 - self.year

    def is_vintage(self):
        """Determine whether guitar is vintage"""
        return self.get_age() >= VINTAGE_AGE
