'''Поиск друзей именинниц и юбиляров с программным отбором отбором. 
Список именинников собирается модулем selenium, затем сортируется 
и осуществляется поиск друзей именинниц и юбиляров'''

from ok_api import OkApi
from def_get_id_user import get_id
from def_modul_get_param import createParser
from def_get_selenium import get_sel

import json
import time
import sys
import os

# Получаем информацию на всех users в списке    
def users_get_info(id_users):
            
    get_info = [] # Создаем пустой список
    json_load_get_info = []
    for ids in id_users: # Проходимся по каждой строчке
        
        get_info = ok.users.getInfo(uids = ids,  fields = 'birthday, gender, LAST_ONLINE, show_lock')
        json_load_get = json.loads(get_info.text) # Переводим json формат, в формат python
        json_load_get_info.append(json_load_get)
    print(json_load_get_info)
    return json_load_get_info
        
# Проводим сортировку. Осталяем открытые профили и профили с 2х месячной свежестью.
def for_search_aktual(users_info):
    
    id_list = []
    for line in users_info:
        line = line[0]
        print (line)
        
        #Юзер открыт и последнее посещение известно
        if line['show_lock'] == False and line['last_online'] != '': 

# Расчет времени. Из настоящего вычитаем последнее посещение. Диапазон 0-2 месяцев      
            print(line)
            old_time = line['last_online']
            old_time = old_time.replace('-', '')
            old_time = old_time.replace(':', '')
            old_year = old_time[0:4]
            old_m = old_time[4:6]
            old_day = old_time[6:8]
            print(old_year, old_m, old_day)
            
            print(line)
            old_year_bd = line['birthday']
            old_year_bd = old_year_bd.replace('-', '')
            old_year_bd = old_year_bd.replace(':', '')
            old_year_bd_year = old_year_bd[0:4]
            
            print(old_year_bd_year)


            new_time = time.strftime("%Y-%m-%d", time.localtime())
            new_time = new_time.replace('-', '')
            new_year = new_time [0:4]
            new_m = new_time [4:6]
            new_day = new_time [6:8]
            print(new_year, new_m, new_day)

            result_year = int(new_year) - int(old_year)
            result_m = int(new_m) - int(old_m)
            result_day = int(new_day) - int(old_day)

            print(result_year, result_m, result_day)
            
            #Проверяем юбиляр или женщина или нет
            if (int(new_year) - int(old_year_bd_year)) % 10 == 0 or line['gender'] == 'female':
                # Проверяем как давно user был в сети   
                if (result_year == 1 and result_m == -11) or (result_year == 0 and result_m <= 2):
                    id_list.append(line['uid'])
    return(id_list)

#По списку именинников id_list находим и составляем список друзей
def find_friends(id_list, city, month, day):
    
    i = 0
    for id_lt in id_list:
        
        info_friend = ok.friends.get(fid = id_lt)
        info_friends = info_friend.text
        
        lsty = []
        lsty = info_friends.replace('","', '\n')
        lsty = lsty.replace('["', '')
        lsty = lsty.replace('"]', '\n')
        i += 1
        

                    #Записываем данные
                   #Сохранеяем файл
        catalog_city = 'data/' + str(city) + '/'
        catalog_month = 'data/' + str(city) + '/' + str(month) + '/'
            #Проверяем создан или нет каталог, если нет создаем 
        if not os.path.exists(catalog_city):
               os.mkdir(catalog_city)
               os.mkdir(catalog_month)
        if not os.path.exists(catalog_month):
                os.mkdir(catalog_month)
        #Записываем данные  
        with open(catalog_month + str(city) + '_' + str(month) + \
                          '_' + str(day) + '.txt', 'a', encoding='utf-8') as fh: #открываем файл на дозапись
            fh.write(str(lsty))
            
    print('Всего актуальных юбиляров и именинниц в городе ' \
          + str(city) + ' ' + str(month)+ '_' + str(day) + '\t' + str(i))
    

def main(ok, citys_urls_finde, months, days):
    
    #Формируем поисковый запрос и сохраняем в файл
    get_sel(months, days, citys_urls_finde)
    
        #Получаем список id из файла     
    for city, url in citys_urls_finde.items():
            for month in months:
                for day in days:
                    
                    catalog_month = 'html/' + str(city) + '/' + str(month) + '/'
                    
                    res, num = get_id(catalog_month + str(city) + '_' + str(month) + \
                                  '_' + str(day) + '.html')
                    
                    # Получаем информацию по каждому имениннику
                    users_info = users_get_info(res) # users_info Список. С вложенным словарем
                    print(users_info)
                    print('Всего ' + str(city) + '_' + str(month) + \
                                  '_' + str(day) + '\t' + str(num))
                    
                    # Сортируем и получаем актуальные id для поиска друзей
                    id_list = for_search_aktual(users_info)
                    print(id_list)      
                           
                    # Поиск друзей и запись в файл по листу id_list
                    find_friends(id_list, city, month, day)
                    
if __name__ == '__main__':
    
    ok = OkApi(access_token='', 
               application_key='', 
               application_secret_key='')
            
    citys_urls_finde = {}
    
     #Получаем аргументы командной строки
            
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    
    citys_urls =  namespace.c
    #Выделяю из списка словарь с городами и ссылками
    citys_urls = citys_urls[0]
    if ';' in citys_urls:
        citys_urls = citys_urls.split(';')
    
    x = 0
    for n in citys_urls:
        
        key, value = citys_urls[x].split('::')
        value = value.split(',')
        citys_urls_finde[key] = value
        x += 1
    
    print('citys_urls_finde',citys_urls_finde)
   # print('value',*value)
    print('1',citys_urls[0])
    print('2',citys_urls[1])
    print(type(citys_urls))
    
    months = namespace.m
    months = months[0]
    if ',' in months:
        months = months.split(',')
    print(type(months))
    print(months)
    
    days = namespace.d
    days = days[0]
    if ',' in days:
        days = days.split(',')
    print(type(days))
    print(days)
    
    main(ok, citys_urls_finde, months, days)
    
    input('End')
