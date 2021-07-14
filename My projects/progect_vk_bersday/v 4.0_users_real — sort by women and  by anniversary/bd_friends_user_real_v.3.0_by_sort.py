'''

   Получаем список друзей именинниц и юбиляров в форме id  из вк в файл город_friends_id_дата.txt

                   bd_friend_user_real.py
'''

import vk
import time

########################################################################
def users_search(add_city_id, add_birth_day, add_birth_month, add_birth_year, add_sex): # Функция возвращает всех именинников по заданному городу и дате

    # В запросе формируем ограничение  списка count=1000, 
    #указываем индификатор города add_city(Белокуриха=1396), дату рождения add_birth_day, add_birth_month(день, месяц)
    api = vk.API(session, v = '5.130',count = '1000', sex = add_sex, city = add_city_id, birth_day = add_birth_day, birth_month = add_birth_month, birth_year = add_birth_year)#city=1396 Белокуриха, city=936 Зыряновск.
    result = api.users.search(user_ids = '')

    # оставляем в списке id значение
    bd_users_info = 0 # Счетчик
    users_id=[]
    for values in result['items']:            #Выбираем ключ items
        for key, value  in values.items():    #Выписываем данные с ключем "id"
            if key == 'id':
                bd_users_info += 1
                users_id.append(value)
    
    return users_id, bd_users_info
    
########################################################################
# Функция возвращает именинников- (открытых+актуальных), сохраняет  (всех актуальных)
def users_get(users_id, add_city_name, add_birth_day, add_birth_month, time_unix): 

    api = vk.API(session, v='5.130', fields = 'last_seen')
    get_id = [] # Создаем список для всех id
    for ids in users_id:
        result = api.users.get(user_ids = ids) #Запрос uers.get в вк
        get_id.append(result)                  #Складываем в список
        time.sleep(0.4) # Сон в 0,4 секунды
        
    #Функция сортирует пользователей, оставляя users с актуальным профилем
    #       
    # Сортируем и выбираем открытых актуальных именинников  
    bd_users_all_info = 0 # Счетчик
    get_id_real = [] # Создаем список для  актуальных id
    for values in get_id:
        for value in values:
            for key, val in value.items():
                if (len(value)) >= 6:                 #Убираем забаненных и удаленных
                    if key == 'last_seen' and time_unix - val['time'] < 1000000 :   #Если время последнего посещения меньше 12 дней
                        bd_users_all_info += 1
                        get_id_real.append(value['id']) 
    
        
    #Функция сортирует пользователей, оставляя users с открытым профилем
    #       
    # Сортируем и выбираем открытых актуальных именинников
    bd_users_open_info = 0 # Счетчик
    get_id_real_opens = [] # Создаем список для открытых актуальных id
    for values in get_id:
        for value in values:
            for key, val in value.items():
                if (len(value)) >= 6 and value['is_closed'] == False:               #Убираем забаненных, удаленных и закрытых
                    if key == 'last_seen' and time_unix - val['time'] < 1000000 :   #Если время последнего посещения меньше 12 дней
                        bd_users_open_info += 1
                        get_id_real_opens.append(value['id'])

    get_id_opens = get_id_real_opens
    return get_id_opens, bd_users_all_info, bd_users_open_info

########################################################################    
# Функция возвращает друзей (открытых+актуальных) именинников
def friends_search(add_city_name, add_birth_day, add_birth_month, get_id_opens, add_sex, time_unix): 
    
    # В запросе получаем время последнего посещения users
    api = vk.API(session, v='5.130', fields = 'last_seen')

    #Организуем цикл запросов
    bd_friend_user_info = 0 # Счетчик
    friends_search = [] #новый список с данными - друзей именников

    for ids in get_id_opens:
        results = api.friends.get(user_id=ids)
        if results['count'] > 0:                           #Проверяем пустой список или нет                     
            for values in results['items']:                #Берем из списка элемент items          
                for key, value in values.items():          # В списке items заложены словари. Раскрываем их.
                    if (len(values)) >= 7:                 #Убираем забаненных и удаленных
                        if key == 'id':
                            id_user = value                #Сохраняем id пользователя
                        if key == 'last_seen' and time_unix - value['time'] < 1000000: 
                            #Если время последнего посещения меньше 12 дней
                            #print(str(id_user))
                            bd_friend_user_info += 1
                            friends_search.append(id_user) #Пишем id пользователя в список
        time.sleep(0.4) # Сон в 0,4 секунды
                
    #Записываем данные  
    if  add_sex == '1':
        with open('data/'+ add_city_name + '/' + add_city_name + '_friends_id_sort' + add_birth_day + '_' + add_birth_month  +
        '_real.txt', 'a', encoding='utf-8') as fh: #открываем файл на запись
            for friends_sea in friends_search:
                fh.write(str(friends_sea)+'\n')
        
    if  add_sex != '1':
        with open('data/'+ add_city_name + '/' + add_city_name + '_friends_id_sort' + add_birth_day + '_' + add_birth_month  +
        '_real.txt', 'a', encoding='utf-8') as fh: #открываем файл на запись
            for friends_sea in friends_search:
                fh.write(str(friends_sea)+'\n')
    
    return  [bd_friend_user_info]

########################################################################
 # Функция  выводит информацию и пишет в файл
def info_file(add_city_name, add_birth_day, add_birth_month, bd_users_info, bd_users_all_info, bd_users_open_info, bd_friend_user_info):
    
    if add_sex == '1':
        info = add_city_name + '\nИменинниц всего ' + str(bd_users_info) + '\nИменинниц всего с актуальными акаунтами (посещали не позже 12 дней) ' + str(bd_users_all_info) + '\nИменинниц актуальных, с открытыми аккаунтами ' + str(bd_users_open_info) + '\nАктуальных друзей именинниц с актуальными аккаунтами ' + str(bd_friend_user_info)
        print(info)
    if  add_sex != '1': 
        info = add_city_name + '\nЮбиляров всего ' + str(bd_users_info) + '\nЮбиляров всего с актуальными акаунтами (посещали не позже 12 дней) ' + str(bd_users_all_info) + '\nЮбиляров актуальных, с открытыми аккаунтами ' + str(bd_users_open_info) + '\nАктуальных друзей Юбиляров с актуальными аккаунтами ' + str(bd_friend_user_info)
        print(info)
    
    
########################################################################        
# Основная функция
def bd_friend_user(add_city_id, add_city_name, add_birth_day, add_birth_month, add_birth_year, add_sex, time_unix):
    return_uers_id, bd_users_info = users_search(add_city_id, add_birth_day, add_birth_month, add_birth_year, add_sex)
    
    return_get_id_opens, bd_users_all_info, bd_users_open_info = users_get(return_uers_id, add_city_name, add_birth_day, add_birth_month, time_unix)
    
    bd_friend_user_info = friends_search(add_city_name, add_birth_day, add_birth_month, return_get_id_opens, add_sex, time_unix)
    
    info_file(add_city_name, add_birth_day, add_birth_month, bd_users_info, bd_users_all_info, bd_users_open_info, bd_friend_user_info)

########################################################################
# Переводим словарь с данными из текстового файла в код, словарь dic_bd_data
# Читам словарь из текстового файла

with open('bd_data.txt') as file: #Читаем файл
  lines = file.read().splitlines() # read().splitlines() - чтобы небыло пустых строк
  
buf = {}#Буферный словарь
dic_bd_data = {} # Создаем пустой словарь

for line in lines: # Проходимся по каждой строчке
    key, *value = line.split(':') # Разделяем каждую строку по двоеточии(в key будет - city, в value - данные)
    dic_bd_data[key] = value     # Добавляем в словарь
        
for key, value in dic_bd_data.items(): # Расскладываем словарь на ключ и значение.
    for val in value: 
        val = val.split(' ')              # В значении раскладываем данные по пробелу
        dic_bd_data.update({key:val})  # Обновляем данные в словаре

i = 0
for keys, values in dic_bd_data.items(): # Добавляем данные в  словарь. Ключу city присваиваем значения словаря с данными, ключ id города, значение name_city 
    for value in values: 
        
        if keys == 'city':
            i += 1
            if i == 1: 
                key = value
                
            if i == 2:
                val = value
                buf[key] = val
                i = 0
                
dic_bd_data['city'] = buf       

########################################################################
#сессия в вк
#
time_unix = time.time()# получение настоящей даты и времени в UNIX

for val_access_token in dic_bd_data['access_token']:
    add_access_token = val_access_token
    
session = vk.Session(access_token = add_access_token)#Выставляем актуальный токен
print(str(add_access_token))
########################################################################
# Главный цикл
buf  = dic_bd_data['city']
add_sex_dict = ['1', '0']
new_time = time.strftime("%Y-%m-%d", time.localtime())
new_time = new_time.replace('-', '')
new_year = new_time [0:4]

for keys, values in buf.items():
        add_city_id = keys
        add_city_name = values
        
        for val_birth_month in dic_bd_data['birth_month']:
            add_birth_month = val_birth_month
            
            for val_birth_day in dic_bd_data['birth_day']:
                add_birth_day = val_birth_day
                
                for add_sex  in add_sex_dict:
                    if add_sex == '1':
                        add_birth_year = None
                        bd_friend_user(add_city_id, add_city_name,
                                        add_birth_day, add_birth_month,
                                         add_birth_year, add_sex, time_unix)
                    if add_sex != '1':
                        for val_birth_year in range((int(new_year)-70), (int(new_year)-10), 10):
                            print('Год ' + str(val_birth_year))
                            add_birth_year = val_birth_year
                            bd_friend_user(add_city_id, add_city_name,
                                            add_birth_day, add_birth_month,
                                             add_birth_year, add_sex, time_unix)

                
x = input('End')
                
