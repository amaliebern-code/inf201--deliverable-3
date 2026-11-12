from typing import Optional
from character import Character


class Battle: 
    """Manages a turn-based battle between two characters"""

    def __init__(self, hero: Character, enemy: Character) -> None: 
        """Initialise the Battle

        Args: 
            hero (Character): The hero character
            enemy (Character): The enemy character
        """
        self.hero = hero
        self.enemy = enemy
        self.round_number = 0

    def play_round(self) -> None:
        """Play one round: hero attacks, and enemy attacks back if still alive"""
        self.round_number += 1
        self.hero.attack(self.enemy)
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

        print(
            f"Round {self.round_number}: "
            f"{self.hero.name} {self.hero.hp} HP, "
            f"{self.enemy.name} {self.enemy.hp} HP"
        )

    def simulate_battle(self, max_rounds: int = 100) -> Optional[Character]:
        """
        
        Play rounds until one character is no longer alive
        
        Args: 
            max_round (int) : Stop after this many rounds to avoid and endless

        Returns:
            The winning character, or None if nobody won within max_rounds. 
        """

        while self.hero.is_alive and self.enemy.is_alive:
            if self.round_number >= max_rounds: 
                print(f"No winner after {max_rounds} rounds")
                return None
            self.play_round()

        winner = self.hero if self.hero.is_alive else self.enemy
        print(f"{winner.name} wins after {self.round_number} rounds!")
        return winner

if __name__ == "__main__":
    from character import Mage, Warrior
    from dice import Dice
    from items import Weapon

    sword = Weapon("Sword", Dice(sides=12))
    hero = Warrior("Aragorn", weapon=sword)
    enemy = Mage("Saruman")

    battle = Battle(hero, enemy)
    battle.simulate_battle()

