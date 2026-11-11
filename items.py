from dice import Dice

class Weapon: 
    """Represents a weapon that a character can use to attack"""

    def __init__(self, name: str, damage: int, dice: Dice) -> None:
        """
        Initialise the Weapon

        Args:
            name (str): The name of the weapon.
            damage (int): Base damage of the weapon.
            dice (Dice): A Dice object to determine additional random damage.
        """
        self.name = name
        self.damage = damage
        self.dice = dice

    def roll_damage(self) -> int:
        """Roll the dice to determine additional damage and return total damage"""
        return self.damage + self.dice.roll()
    
    def __repr__(self) -> str:
        """Representation of the Weapon object"""
        return f"Weapon (name={self.name}, damage={self.damage}, dice={self.dice})"
    
if __name__ == "__main__":
    d6 = Dice()  # Default 6-sided dice
    sword = Weapon("Sword", damage=10, dice=d6)

    print(sword)  # Weapon (name=Sword, damage=10, dice=Dice (sides=6))
    print(sword.roll_damage())  # Random number between 11 and 16 (10 + roll of d6)