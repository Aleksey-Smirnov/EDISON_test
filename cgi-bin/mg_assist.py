#!/usr/bin/env python3
import cgi, cgitb
import random

value = random.randint(0,999)
print("Set-cookie: name=value; httponly")   
print('Content-type: text/html')
print()
print("""<center>
              <form action="/cgi-bin/form.py">
              <h1> Enter the two-digit number you think of.<br></h1>
              <input type="number" min = 10 max = 99 name="NUM">
              <input type="submit">
              </form>
              </center>""")
