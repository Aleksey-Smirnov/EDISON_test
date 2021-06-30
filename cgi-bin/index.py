#! /usr/local/bin/python3.8
# -*- coding: utf-8 -*-
import cgi, cgitb
import os
import http.cookies
import random
cgitb.enable()

def hi_text():  
    print(""" <form action="/cgi-bin/form.py">
       <center>
       <h1>Are you ready to test psychics!
       Think of a two-digit number and click - done..</h1>
       <button type="submit">Ready </button>
       </center>
       </form>""")

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
name = cookie.get("name")
value = random.randint(10,999)
if name is None:
    print("Set-cookie: name="+str(value)+"")
    print("Content-type: text/html\n")
    hi_text()
    
else:
    print("Content-type: text/html\n")
    hi_text()

