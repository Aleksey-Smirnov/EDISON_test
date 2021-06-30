import random

class Psychic():
    ''' Класс экстрасенс'''
    
    def __init__(self, name):
        self.name = name
        self.num_gu = None
        self.cred = 0
        
    def guess (self):                            
        #Догадка
        self.num_gu = random.randint(10,99)
    
    def creds (self, res_num, num_assist, num_psych):
        #Подсчет достоверности
        if num_assist == num_psych:
            return res_num + 1
        else:
            return res_num - 1
        
