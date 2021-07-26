import random

class Psychic():
    ''' Класс экстрасенс'''
    
    def __init__(self, name):
        self.name = name     
        self.num_gu = None
        self.list_nums_gu = []
        self.cred = 0
        
    def guess (self):                            
        #Догадка
        self.num_gu = random.randint(10,99)
    
    def creds (self, num_assist):
        #Подсчет достоверности
        if num_assist == self.num_gu:
            self.cred += 1
        else:
            self.cred -= 1
    
    def append_list_nums (self, num):   
        #Сохраняем предложенные числа
        self.list_nums_gu.append(num)
        
