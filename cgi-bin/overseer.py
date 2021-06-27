import cgi

class Overseer():
    
    def __init__(self):
        '''
        self.mg_num = mg_num
        self.psy_num_1 = psy_num_1
        self.psy_num_2 = psy_num_2
        '''
        self.arhiv_mg_num = []
        self.arhiv_psy_num_1 = []
        self.arhiv_psy_num_2 = []
         
    def in_arhiv(self, mg_num, psy_num_1, psy_num_2):
        self.arhiv_mg_num.append(mg_num)
        self.arhiv_psy_num_1.append(psy_num_1)
        self.arhiv_psy_num_2.append(psy_num_2)
