# Object-oriented game simulator
# Turid Torheim, NMBU, 2026

from typing import Optional

from items import Weapon


class Character:
    """Represents a character in the RPG"""

    def __init__(
        self,
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        weapon: Optional[Weapon] = None,
    ) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

    def take_damage(self, amount: int) -> None:
        """Reduces character's HP by amount, but not below 0"""
        self._hp = max(self._hp - amount, 0)  # HP cannot go below 0

    def heal(self, amount: int) -> None:
        """Increase character's HP by amount, but not above hp_max"""
        self._hp = min(self._hp + amount, self.hp_max)

    def attack(self, target) -> None:
        """Attack and deal damage to target character"""
        if self.weapon is not None:
            damage = self.weapon.roll_damage()
        else:
            damage = self.damage
        target.take_damage(damage)

    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp
    
    @property
    def is_alive(self) -> bool:
        """Read-only property: True if character is alive (HP > 0), False otherwise."""
        return self._hp > 0

if __name__ == "__main__":
    from dice import Dice

    sword = Weapon("Sword", Dice(sides=8))
    hero = Character("Hero", weapon=sword)
    enemy = Character("Enemy")

    hero.attack(enemy)   # uses the sword: random damage from 1 to 8
    print(enemy.hp)      # between 92 and 99
    enemy.attack(hero)   # no weapon: fixed damage of 10
    print(hero.hp)       # 90