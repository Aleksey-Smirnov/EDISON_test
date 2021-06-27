#!/usr/bin/env python3
import cgi, cgitb
cgitb.enable()

class Mg_assist():
    def __init__(self):
        pass
        
    def form_num(self):
    
        print('Content-type: text/html')
        print()
        print('''
              <center>
              <form action="/cgi-bin/form.py">
              <h1> Please enter the hidden two-digit number.<br></h1>
              <input type="number" min = 10 max = 99 name="NUM">
              <input type="submit">
              </form>
              </center>''')
       

