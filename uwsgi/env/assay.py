# -*- coding: utf-8 -*-
from flask import Flask, session, redirect, url_for, escape, request
import random
import secrets
import os


class Assays():
    
    def __init__(self, psy1, psy2):
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = os.urandom(24)
        self.session = session
        
        self.psy1 = psy1
        self.psy2 = psy2
        
        self.id = None
        self.global_dict = {}          #Словарь данных всех сессий
        self.global_dict[self.id] = {} #Словарь данных текущей сессии
        
    def get_assay(self, app):
        
        @app.route('/')
        def index():
               self.session['id'] = secrets.token_urlsafe(32)
               self.id = str(self.session['id'])
               self.global_dict[self.id] = {
                                           'assist':[],
                                           'psy1':[],
                                           'psy2':[],
                                           'psy1_ch':[],
                                           'psy2_ch':[]
                                           }                 #Определяем словарь под текущую сессию 
               
               return "<center>Программа тестирования экстрасенсов <br><a href = '/test_ext/'></b>" + \
                      "<p><input type = submit value = Приступить к тестированию></p></b></a></center>"\
                      ''+ '' +''   
        
        @app.route('/test_ext/', methods = ['GET', 'POST'])
        def test_ext():
            
            name =  str(self.session['id'])
            
            self.psy1.guess() #Загадывает первый экстрасенс
            self.psy2.guess() #Загадывает второй экстрасенс
                
            if request.method == 'POST':
               self.global_dict[name]['assist'].append(request.form.get('num_test'))
               '''   
               if not ass:
                   ass[name] = [(request.form.get('num_test'))]
                   
                  # ids[self.psy1.name] = [self.psy1.num_gu]
                  # ids[self.psy2.name] = [self.psy2.num_gu]
               else:
                   ass[name].append(request.form.get('num_test'))
                  # ids[self.psy1.name].append(self.psy1.num_gu)
                  # ids[self.psy2.name].append(self.psy2.num_gu)
                  '''
               return redirect('/results/')
                  
            return'<center>Экстрасенс ' + self.psy1.name +\
                 ' предсказывает что загаданное число ' + str(self.psy1.num_gu) + '<br>' + \
                 '<center>Экстрасенс ' + self.psy2.name +\
                 ' предсказывает что загаданное число ' + str(self.psy2.num_gu) + '<br>' + \
                 'Введите правильное число!'\
                 '<form action = "/test_ext/" method = "post" >'\
                 '<p><input type = "number" min = 10 max = 99 name = num_test></p>'\
                 '<p><input type = submit value = Отправить></p>'\
                 '</form></center>'
                 

        @app.route('/results/')
        def results():

            name =  str(self.session['id'])
             
            lst_assist = self.global_dict[name]['assist']
           # lst_psy1 =  ids[self.psy1.name] 
           # lst_psy2 =  ids[self.psy2.name]
                 
            return '<center>Загаданное число '+ str(lst_assist[-1]) +  '<br>' + \
                   'Первый ' + 'str(lst_psy1[-1])'+ ' Второй ' + 'str(lst_psy2[-1])'+ '<br>'+ \
                   'Все числа' + str(lst_assist) + '<br>'\
                   "<b><a href = '/test_ext/'><input type = submit value = Продолжить></a></b></center>"
        

