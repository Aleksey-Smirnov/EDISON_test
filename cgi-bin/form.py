#! /usr/local/bin/python
# -*- coding: utf-8 -*-
import cgi, cgitb
import http.cookies
import random
import os
cgitb.enable()

class Mg_assist():
    '''Helper class'''
    
    def __init__(self):
        self.my_num = 'None'
        
    def form_num(self):
        '''Transmits the hidden number'''
        
        print("Content-type: text/html\n")
        print()
        print('''
              <center>
              <form>
              <h1> Enter the two-digit number you think of.<br></h1>
              <input type="number" min = 10 max = 99 name="NUM">
              <input type="submit">
              </form>
              </center>''')
        form = cgi.FieldStorage()
        self.my_num = form.getfirst("NUM", "None")
        
class Psychic():
    '''Psychic class'''
    
    def __init__(self, name):
        self.name = name
        self.cred = 0
        self.num_gu = None
    def guess (self,):
        self.num_gu = random.randint(10,99)
        
    def change_cred(self, flag):
        '''Changing the reliability'''
        
        if flag:
            self.cred += 1
        else:
            self.cred -= 1  
              
class Overseer():
    '''Overseer class'''
    
    def __init__(self):
        
        self.arhiv_mg_num = ['None']
        self.arhiv_psy_num_1 = ['None']
        self.arhiv_psy_num_2 = ['None']
         
    def in_arhiv(self, mg_num, psy_num_1, psy_num_2):
        '''Save date'''
        
        self.arhiv_mg_num.append(mg_num)
        self.arhiv_psy_num_1.append(psy_num_1)
        self.arhiv_psy_num_2.append(psy_num_2)
        
def next_test():
    
    print()
    print('''
              <form target = "_top" >
              <center>
              <h1>Are you ready to test psychics!
              Think of a two-digit number and click - done..</h1>
              <button type="submit">Ready </button>
              </center>
              </form>''')

def main (arhiv_mg_num, arhiv_psy_num_1, arhiv_psy_num_2):
    
    #print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
            <html>
            <head>
                <meta charset="utf-8">
                <title>Psychic test result</title>
            </head>
            <body>
                <center>""")
        
    print("")
    print("<h2>Psychic {} suggested that this number{}</h2>"\
              .format(ps1.name, arhiv_psy_num_1[-1]))
    print("<h2>Psychic {} suggested that this number{}</h2>"\
              .format(ps2.name, arhiv_psy_num_2[-1]))

    print("""</body>
                </html>""")
       
        #ps1.change_cred()
        #ps2.change_cred()
        

    print("""<!DOCTYPE HTML>
             <html>
             <head>
                 <meta charset="utf-8">
                 <title>Psychic test result</title>
             </head>
             <body>
                <center>""")

    print("<h1>Previous test results.</h1>")
    print("<h2>Previous hidden numbers{}</h2>".format(arhiv_mg_num[2:]))
    print("<h2>Variants {} {}</h2>".format(ps1.name, arhiv_psy_num_1[2:]))
    print("<h2>Variants {} {}</h2>".format(ps2.name, arhiv_psy_num_2[2:]))
    cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
    name = cookie.get("name")
    print('cook', name.value)
    print("""</body>
                </html>""")




over = Overseer()
mg = Mg_assist()
ps1 = Psychic('White')
ps2 = Psychic('Black')

mg.form_num()


ps1.guess()
ps2.guess()
over.in_arhiv(mg.my_num, ps1.num_gu, ps2.num_gu)
main (over.arhiv_mg_num, over.arhiv_psy_num_1, over.arhiv_psy_num_2)
