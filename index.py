from flask import Flask, session, redirect, url_for, escape, request, render_template
import random
import secrets
import os
from psychic import Psychic
from assistent import Assistent as As

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
session = session
          
                
def get_assay(app):
        
        buf = {}
        
        def save_buf(my_buf, ids, N_psychic):
            '''Сохранеяем экземпляры'''
             
            buf[ids + 'as'] = my_buf[ids + 'as']
            for i in range(N_psychic):
                buf[ids + str(i)] = my_buf[ids + str(i)]  
         
        @app.route('/', methods = ['GET', 'POST'])
        def index():
             
            if request.method == 'POST':
                if 'id' not in session:
                    '''Новая сессия'''
                    session['N_psychic'] = request.form.get('num_psy') # Получаем количество экстрасенсов
                    session['id'] = secrets.token_urlsafe(32)
                    ids = str(session['id'])
                    N_psychic = int(session['N_psychic'])
                    
                    buf[ids+ 'as'] = As()
                    for i in range(N_psychic):
                        buf[ids+ str(i)] = Psychic(str(i))    #Создаем экземпляры 
                    
                return redirect('/test_ext/')
            
            if 'id' in session:
                return redirect('/test_ext/')     
            return render_template('index.html')
                      
        
        @app.route('/test_ext/', methods = ['GET', 'POST'])
        def test_ext():
            
            '''Переменные'''
            ids = str(session['id'])
            N_psychic = int(session['N_psychic'])
            my_buf = {}
            
            '''Извлекаем экземпляры'''
            my_buf[ids + 'as'] = buf[ids + 'as']
            del buf[ids + 'as']                             #Чистим буфер
            for i in range(N_psychic):
                my_buf[ids + str(i)] = buf[ids + str(i)]
                del buf[ids + str(i)]                       #Чистим буфер
            
            if request.method == 'POST':
                
                if not request.form.get('num_test'):
                    save_buf(my_buf, ids, N_psychic)                #Сохранеяем экземпляры 
                    return render_template('error.html')
                
                else:
                    guss_num = int(request.form.get('num_test'))    #Загаданный номер
                    my_buf[ids + 'as'].append_list_nums(guss_num)   #Записываем 
                    guss_nums = my_buf[ids + 'as'].list_num
                    
                    for i in range(N_psychic):        
                        my_buf[ids+ str(i)].append_list_nums(\
                                    my_buf[ids+ str(i)].num_gu)     #Сохраняем предположенное
                        my_buf[ids+ str(i)].creds(guss_num)         #Считаем достоверность
                    
                    data_lst ={}
                    for i in range(N_psychic):
                        data_lst[i] = {'num_gu':my_buf[ids+ str(i)].num_gu,\
                                        'cred':my_buf[ids+ str(i)].cred,\
                                        'list_nums_gu':my_buf[ids+ str(i)].list_nums_gu\
                                        }
                    
                    save_buf(my_buf, ids, N_psychic)        #Сохранеяем экземпляры             
                    
                    return render_template('results.html',guss_num = guss_num,\
                                            guss_nums = guss_nums,\
                                            data_list = data_lst) 
            
            data_lst ={}
            for i in range(N_psychic):   
                my_buf[ids+ str(i)].guess()                  #Предполагают экстрасенсы
                
                data_lst[i] = my_buf[ids+ str(i)].num_gu     #Список - предположенные числа
                
            save_buf(my_buf, ids, N_psychic)                 #Сохранеяем экземпляры    
            
            return render_template('test_ext.html',ids = ids,\
                                   idss = session, data_list = data_lst)
                  
get_assay(app)                                               #Запуск проверки

if __name__ == "__main__":
    app.debug = True
    app.run()
