# Object-oriented game simulator
# Turid Torheim, NMBU, 2026

class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10) -> None:
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

    def take_damage(self, amount: int) -> None:
        """Reduces character's HP by amount, but not below 0"""
        self._hp = max(self._hp - amount, 0)  # HP cannot go below 0

    def heal(self, amount: int) -> None:
        """Increase character's HP by amount, but not above hp_max"""
        self._hp = min(self._hp + amount, self.hp_max)

    def attack(self, target) -> None:
        """Attack and deal damage to target character"""
        target.take_damage(self.damage)

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
    hero = Character("Hero")
    enemy = Character("Enemy", hp_max=25)

    hero.attack(enemy)
    print(enemy.hp)  # 15
    enemy.heal(100)
    print(enemy.hp)  # 25, stops at hp_maks
    enemy.take_damage(999)
    print(enemy.hp)  # 0, cannot go below 0
    print(enemy.is_alive)  # False
    print(hero.is_alive)  # True
    