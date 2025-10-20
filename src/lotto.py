import random

def lotto():
    return sorted(random.sample(range(1, 50), 6))