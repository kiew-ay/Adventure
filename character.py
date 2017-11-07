"""
CHARACTERS

This is where the basic character classes and their helpers are defined.
This includes:
- Character - Most basic and general character class
- Protagonist - The player's character
- Antagonist - Enemy characters
"""

# Most basic and general character class.
class Character():
    def __init__(self, body_attack, body_defense, mind_attack, mind_defense):
