# -*- coding: utf-8 -*-
from flask import Flask, session, redirect, url_for, escape, request
import random
import secrets
import os
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

url = secrets.token_urlsafe(32)
#app.secret_key = secret
result = {}
results = {}


def set_key(value):
    session['id'] = value
    return 'ok'

def get_var_name(key_name):
    
    assist = ''+ str(key_name) +'assit'
    return assist
    
@app.route('/')
def index():
        key = secrets.token_urlsafe(32)
        set_key(key)
        
        return 'Url Name' +  str(key)+ '<br>' + \
               "<center>Программа тестирования экстрасенсов <br><a href = '/test_ext/'></b>" + \
               "<p><input type = submit value = Приступить к тестированию></p></b></a></center>"
               

@app.route('/test_ext/', methods = ['GET', 'POST'])
def test_ext():
    
    key_name = session.get('id')
    assist = get_var_name(key_name)
    
    if request.method == 'POST':
       
       if not result:
           result[assist] = [(request.form.get('num_test'))]   
       else:
           result[assist].append(request.form.get('num_test'))
       '''
       result[''+ str(name_key)1'] = request.form.get('num_test')
       result[''+ str(name_key)2'] = request.form.get('num_test')
       result[''+ str(name_key)3'] = request.form.get('num_test')
       result[''+ str(name_key)4'] = request.form.get('num_test')
       '''
       #name_f = session.get('id')
       #with open(name_f, 'a') as f: #открываем файл на запись
        #    f.write(json.dumps(result))
       
       return redirect('/results/')
        
    return'''
         <center><form action = "/test_ext/" method = "post" >
         <p><input type = "number" min = 10 max = 99 name = num_test></p>
         <p><input type = submit value =Задуманное число></p>
         </form></center>
         '''

@app.route('/results/')
def results():
    
    key_name = session.get('id')
    assist = get_var_name(key_name)
    lst_assist = result[assist]
    
    
    #results[assist] = result[assist]
    #with open(name_f) as f: #Читаем файл
     #   result = json.load(f) # Переводим json формат, в формат python
    return '<center>Задуманное число '+ str(lst_assist[-1]) +  '<br>' + \
           'Все числа' + str(lst_assist) + '<br>'\
           "<b><a href = '/test_ext/'><input type = submit value = Продолжить></a></b></center>"
              
    #return'''
    #     <form action = "/test_ext/<url>" method = "post" >
    #     <p><input type = submit value =Продолжить тест></p>
    #     </form>
    #     '''
if __name__ == "__main__":
    app.run()
