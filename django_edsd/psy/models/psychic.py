import random

class Psychic():
    
    class Meta:
        abstract = False
    
    def __init__(self):
        
        self.proposed_number = None
        self.all_proposed_number = []
        self.credibility = 0
    
    def to_add(self):
         
        self.all_proposed_number.append(self.proposed_number)
    
    def get_credibility(self, ass_num):
        
        if int(self.proposed_number) == int(ass_num):
            self.credibility += 1
        else:
            self.credibility -= 1
    
    def get_proposed_number(self):
        self.proposed_number = random.randint(10,99)
