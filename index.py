#!/usr/bin/env python3
import cgi, cgitb
import random

value = random.randint(0,999)
#print("Set-cookie: name=value; httponly")   
print('Content-type: text/html')
print()
print(""" <form action="/cgi-bin/form.py">
       <center>
       <h1>Are you ready to test psychics!
       Think of a two-digit number and click - done..</h1>
       <button type="submit">Ready </button>
       </center>
       </form>""")
