import string
import random
from difflib import SequenceMatcher

target = "methinks it is like a weasel"

def generate (size):
    generated = {}
    for x in range(size):
        individual = ''
        for c in range(len(target)):
            individual += random.choice(string.printable)
        generated[individual] = fitness(individual)
    return generated

def fitness (individual):
    return SequenceMatcher(None, target, individual).ratio()
        
print(generate(5))
