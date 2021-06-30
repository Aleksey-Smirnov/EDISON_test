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
               self.global_dict[self.id] = {                #Определяем словарь под текущую сессию
                                           'assist':[],     #Данные ассистента
                                           'psy1':[],       #Первого экстрасенса
                                           'psy2':[],       #Второго экстрасенса
                                           'psy1_cr':0,     #Достовернось первого
                                           'psy2_cr':0      #Достоверность второго 
                                           }                 
               
               return "<br><br><br><center><h2>Загадайте двухзначное\
                      число<br><a href = '/test_ext/'>" + \
                      "<p><input type = submit value = Загадал>\
                      </p></a></h2></center>"
                      
        
        @app.route('/test_ext/', methods = ['GET', 'POST'])
        def test_ext():
            
            name =  str(self.session['id'])
                            
            if request.method == 'POST':
                if not request.form.get('num_test'):
                   
                   return"<br><br><br><center><h2>Экстрасенсы сбиваются.\
                          Пожалуйста не вводите их в заблуждение!<dr>\
                           <br><a href = '/test_ext/'>" + \
                          "<p><input type = submit value = Хорошо>\
                          </p></a></h2></center>"
                else:
                   guss_num = int(request.form.get('num_test'))                         #Загаданный номер
                   self.global_dict[name]['assist'].append(guss_num)                    #Записываем 
                   self.global_dict[name]['psy1'].append(self.psy1.num_gu)               #данные
                   self.global_dict[name]['psy2'].append(self.psy2.num_gu)               #
                   self.global_dict[name]['psy1_cr'] = self.psy1.creds(
                                                        self.global_dict[name]['psy1_cr'],
                                                        guss_num,
                                                        self.psy1.num_gu
                                                                       )
                   self.global_dict[name]['psy2_cr'] = self.psy2.creds(
                                                        self.global_dict[name]['psy2_cr'],
                                                        guss_num,
                                                        self.psy2.num_gu
                                                                       )
               
                   return redirect('/results/')
               
            self.psy1.guess() #Загадывает первый экстрасенс
            self.psy2.guess() #Загадывает второй экстрасенс      
            
            return'<h2><center>Экстрасенс ' + self.psy1.name +\
                 ' предсказывает, что загаданное число ' + str(self.psy1.num_gu) + '<br>' + \
                 '<center>Экстрасенс ' + self.psy2.name +\
                 ' предсказывает, что загаданное число ' + str(self.psy2.num_gu) + '<br>' + \
                 'Введите загаданное Вами число!'\
                 '<form action = "/test_ext/" method = "post" >'\
                 '<p><input type = "number" min = 10 max = 99 name = num_test></p>'\
                 '<p><input type = submit value = Отправить></p>'\
                 '</form></center></h2>'
                 

        @app.route('/results/')
        def results():

            name =  str(self.session['id'])
             
            lst_assist = self.global_dict[name]['assist']
            lst_psy1 = self.global_dict[name]['psy1']
            lst_psy2 = self.global_dict[name]['psy2']
            psy1_cr = self.global_dict[name]['psy1_cr']
            psy2_cr = self.global_dict[name]['psy2_cr']
                 
            return '<center><h2>Загаданное число '+ str(lst_assist[-1]) +  '<br>' + \
                   '' + self.psy1.name + ' предположил что это число ' + str(lst_psy1[-1])\
                   + ', его достоверность составляет   ' + str(psy1_cr) +'.' '<br>' + \
                   '' + self.psy2.name + ' предположил что это число ' + str(lst_psy2[-1])\
                    + ', его достоверность составляет   ' + str(psy2_cr) +'.' '' + \
                    '<br><br><center>Загадайте двухзначное число</h2>'\
                   "<a href = '/test_ext/'><input type = submit value = Загадал>\
                   </a></b></center>"'<br>'+ '<br>'+'<br><h3>'+'Числа загаданные помошником'\
                    + str(lst_assist) + '<br>'\
                    + 'Числа предложенные экстрасенсом ' + self.psy1.name +' '\
                     + str(lst_psy1) + '<br>'\
                     + 'Числа предложенные экстрасенсом ' + self.psy2.name +' '\
                     + str(lst_psy2) + '</h3><br>'\
                   
        

