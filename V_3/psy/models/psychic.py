import json
import random


class Psychic:
    
    class Meta:
        abstract = False
    
    def __init__(self):
        
        self.proposed_number = None
        self.all_proposed_number = []
        self.credibility = 0
    
    def to_add(self):
         
        self.all_proposed_number.append(self.proposed_number)
    
    def get_credibility(self, ass_num):
        print('proposed_number', self.proposed_number, 'ass_num', ass_num)
        if int(self.proposed_number) == int(ass_num):
            self.credibility += 1
        else:
            self.credibility -= 1
    
    def get_proposed_number(self):
        self.proposed_number = random.randint(10, 99)

    def to_json(self):
        data = {
            'proposed_number': self.proposed_number,
            'all_proposed_number': self.all_proposed_number,
            'credibility': self.credibility
        }
        return json.dumps(data, ensure_ascii=False, indent=2)

    def from_json(self, data):
        json_data = json.loads(data)
        self.proposed_number = json_data['proposed_number']
        self.all_proposed_number = json_data['all_proposed_number']
        self.credibility = json_data['credibility']