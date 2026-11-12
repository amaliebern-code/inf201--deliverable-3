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

class Warrior(Character):
    """A defensive character with armor that reduves incoming damage"""

    def __init__(
            self,
            name: str,
            hp_max: int= 100,
            damage: int = 10, 
            weapon: Optional [Weapon] = None,
            armor: int = 5, 
    ) -> None:
        """
        Initialise the Warrior

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
            armor (int): Reduces incoming damage by this amount (default = 5)
        """
        super().__init__(name, hp_max, damage, weapon)
        self.armor = armor

    def take_damage(self, amount: int) -> None:
        """Reduce the incoming damage by armor before applying it"""
        reduced = max(amount- self.armor, 0)  # Armor cant turn damage into healing
        super().take_damage(reduced)

class Mage(Character):
    """A character that can cast spells to deal damage"""

    def __init__(
            self,
            name: str,
            hp_max: int= 100,
            damage: int = 10, 
            weapon: Optional [Weapon] = None,
            mana: int = 30,
            mana_max: int=30, 
    ) ->None:
        """
        Initialise the Mage

        Args:
            mana (int): Mana the mage starts with (default = 30)
            mana_max (int): Max mana (default = 30)
            The other arguments are the same as for Character.
        """
        super().__init__(name, hp_max, damage, weapon)
        self.mana = mana
        self.mana_max = mana_max

    def attack(self, target) -> None:
        """Cast a spell if there is enough mana, otherwise use the base attack"""
        if self.mana >= 10:
            self.mana -= 10
            target.take_damage(self.damage * 2)  # Spell: double damage, no weapon
        else:
            super().attack(target)  # Base attack, uses weapon if equipped
            self.mana = min(self.mana + 5, self.mana_max)

if __name__ == "__main__":
    warrior = Warrior("Warrior")
    mage = Mage("Mage")

    mage.attack(warrior)     # spell: 20 damage, armor blocks 5
    print(warrior.hp)        # 85
    print(mage.mana)         # 20
    mage.attack(warrior)
    mage.attack(warrior)
    print(mage.mana)         # 0
    mage.attack(warrior)     # no mana: base attack of 10, armor blocks 5
    print(warrior.hp)        # 50
    print(mage.mana)         # 5