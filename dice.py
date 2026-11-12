import random

class Dice: 
    """Represents a dice with a given number of sides"""

    def __init__(self,sides : int = 6) -> None: 
        """Initialise the Dice
    
        Args: 
            sides (int): Number of sides, must be at least 2 (default = 6)
        """
        if sides < 2: 
            raise ValueError("Dice must have at least 2 sides")
        self.sides = sides
    
    def roll(self) -> int: 
        """Roll the dice and return a random number between 1 and sides"""
        return random.randint(1, self.sides)
    
    def __call__(self) -> int:
        """Allow the dice to be called like a function to roll it"""
        return self.roll()

    def __repr__(self) -> str: 
        """Representation of the Dice object"""
        return f"Dice(sides={self.sides})"
    
if __name__ == "__main__":
    d6 = Dice()  # Default 6-sided dice
    d20 = Dice(sides=20)  # 20-sided dice

    print(d6)           #Dice sides=6
    print(d20)          #Dice sides=20
    print(d6.roll())  # Random number between 1 and 6
    print(d20.roll())  # Random number between 1 and 20