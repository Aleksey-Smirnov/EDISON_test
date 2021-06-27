# -*- coding: utf-8 -*-
import cgi, cgitb
import random
cgitb.enable()

class Mg_assist():
    def __init__(self):
        pass
        
    def form_num(self):
    
        print()
        print('''
              <center>
              <form action="/cgi-bin/form.py">
              <h1> Enter the two-digit number you think of.<br></h1>
              <input type="number" min = 10 max = 99 name="NUM">
              <input type="submit">
              </form>
              </center>''')
              
class Psychic():
    
    def __init__(self, name):
        self.name = name
        self.num_gu = 0
    def guess (self,):
        self.num_gu = random.randint(10,99)
        
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
        

over = Overseer()
mg = Mg_assist()
ps1 = Psychic('White')
ps2 = Psychic('Black')

ps1.guess()
ps2.guess()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Psychic test result</title>
        </head>
        <body>
        <center>""")

print("<h1>Psychics test, for guessing the two-digit number you have guessed.</h1>")
print("<h2>Psychic {} suggested that this number{}</h2>".format(ps1.name, ps1.num_gu))
print("<h2>Psychic {} suggested that this number{}</h2>".format(ps2.name, ps2.num_gu))

print("""</body>
        </html>""")

mg.form_num()
form = cgi.FieldStorage()
num1 = form.getfirst("NUM", "не задано")


over.in_arhiv(num1, ps1.num_gu, ps2.num_gu)
#print (over.arhiv_mg_num, over.arhiv_psy_num_1, over.arhiv_psy_num_2)


print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Psychic test result</title>
        </head>
        <body>
        <center>""")

print("<h1>Previous test results.</h1>")
print("<h2>Previous hidden numbers{}</h2>".format(over.arhiv_mg_num))
print("<h2>Variants {} {}</h2>".format(ps1.name, over.arhiv_psy_num_1))
print("<h2>Variants {} {}</h2>".format(ps2.name, over.arhiv_psy_num_2))

print("""</body>
        </html>""")

