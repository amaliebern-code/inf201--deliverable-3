from dice import Dice


class Weapon:
    """Represents a weapon that a character can use to attack"""

    def __init__(self, name: str, damage_dice: Dice) -> None:
        """
        Initialise the Weapon

        Args:
            name (str): The name of the weapon.
            damage_dice (Dice): The dice rolled to decide the damage.
        """
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        """Roll the weapon's dice and return the damage"""
        return self.damage_dice.roll()

    def __repr__(self) -> str:
        """Representation of weapon object"""
        return f"Weapon(name={self.name}, damage_dice={self.damage_dice})"


if __name__ == "__main__":
    sword = Weapon("Sword", Dice(sides=8))
    print(sword)                # Weapon(name=Sword, damage_dice=Dice(sides=8))
    print(sword.roll_damage())  # random number from 1 to 8