
from random import randrange


class Spell:

    """
    Base class used for spell creation.
    Takes arguments self, name, cost, dmg, and type
    """

    def __init__(self, name, cost, dmg, type):
        # defines spell name
        self.name = name
        # defines spell cost
        self.cost = cost
        # defines damage value (int)
        self.dmg = dmg
        # defines spell type (Black(str), White(str))
        self.type = type

    def generate_damage(self):

        """
        Method used to calculate and return spell damage
        """
        # Set variable for low range point
        low = self.dmg - 15
        # Set variable for high range point
        high = self.dmg + 15
        # Calculate and return final damage (int)
        return randrange(low, high)
