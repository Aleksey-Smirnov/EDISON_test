import random

class Psychic():
    
    def __init__(self, name):
        self.name = name
        self.num_gu = None
        self.cred = 0
        
    def guess (self):
        self.num_gu = random.randint(10,99)
