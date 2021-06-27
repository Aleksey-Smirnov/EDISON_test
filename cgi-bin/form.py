# -*- coding: utf-8 -*-
import cgi
from psychic import Psychic

form = cgi.FieldStorage()
num1 = form.getfirst("NUM", "не задано")

ps1 = Psychic('White')
ps1.guess()
ps2 = Psychic('Black')
ps2.guess()

print('Content-type: text/html\n')
print('''<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Getting results from psychics.</title>
        </head>
        <body>''')

print('<h1>The first one was guessing {}</h1>'.format(ps1.name))
print('<p>His number is: {}</p>'.format(ps1.num_gu))

print('<h1>The second was guessing {}</h1>'.format(ps2.name))
print('<p>His number is: {}</p>'.format(ps2.num_gu))




print("""</body>
        </html>""")

