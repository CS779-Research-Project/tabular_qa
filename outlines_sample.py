from enum import Enum
from pydantic import BaseModel, constr
import torch
import outlines

MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"

class Weapon(str, Enum):
    sword = "sword"
    axe = "axe"
    mace = "mace"
    spear = "spear"
    bow = "bow"
    crossbow = "crossbow"


class Armor(str, Enum):
    leather = "leather"
    chainmail = "chainmail"
    plate = "plate"


class Character(BaseModel):
    name: constr(max_length=10)
    age: int
    armor: Armor
    weapon: Weapon
    strength: int

model = outlines.models.transformers(MODEL_NAME, device=torch.device("cuda"))

# Construct structured sequence generator
generator = outlines.generate.json(model, Character)

# Draw a sample
seed = 789001

character = generator("Give me a character description")

print(repr(character))
print(character.name)
# Character(name='Anderson', age=28, armor=<Armor.chainmail: 'chainmail'>, weapon=<Weapon.sword: 'sword'>, strength=8)

character = generator("Give me an interesting character description")

print(repr(character))
# Character(name='Vivian Thr', age=44, armor=<Armor.plate: 'plate'>, weapon=<Weapon.crossbow: 'crossbow'>, strength=125)