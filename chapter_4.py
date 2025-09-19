# chapter_4.py

import random

# The cursor summoned allies from the Repository of Legends.

def summon_allies():
allies = ["Lady Patch", "Lord Branch", "Duke Fork", "Count Clone"]
chosen = random.choice(allies)
print(f"The blinking cursor said, 'I summon {chosen} to aid us!'")

summon_allies()