#
#Эмулятор браузера. Входит в ОК, авторизуется, осуществляет поиск и сохраняет в html файл
#


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os

def get_driver():
#Входим в ОК получаем управление броузером

    driver = webdriver.Chrome(r'C:\Python\chrom_dryve\chromedriver.exe')
    driver.maximize_window()
    driver.get("http://ok.ru")

    element_email = driver.find_element_by_id("field_email")
    element_passw = driver.find_element_by_id("field_password")


    element_email.send_keys("")
    element_passw.send_keys("", Keys.ENTER)
    
    return driver
    
def get_sel(months, days, citys_urls_finde):
#Переходим по поисковым ссылкам сохраняем данные 
    
    driver = get_driver()
    
    for city, url in citys_urls_finde.items():
        for month in months:
            for day in days:
                         
                print('\nCity ',city)
                print(month, '_', day)
                
                url_finde = url[0] + str(month) + url[1] + str(day) + url[2]
                content_html = get_finde(url_finde, driver)
                        
               #Сохранеяем файл
                catalog_city = 'html/' + str(city) + '/'
                catalog_month = 'html/' + str(city) + '/' + str(month) + '/'
                         
               #Проверяем создан или нет каталог, если нет создаем 
                if not os.path.exists(catalog_city):
                     os.mkdir(catalog_city)
                     os.mkdir(catalog_month)
                if not os.path.exists(catalog_month):
                      os.mkdir(catalog_month)
                       
                #Записываем
                with open(catalog_month + str(city) + '_' + str(month) + \
                          '_' + str(day) + '.html', 'w', encoding="utf-8") as f:
                     f.write(content_html)
    driver.close()
    
def get_finde(url_finde, driver):
#Поисковый модуль. Получает ссылку выдает содержимое

    #Открываем url поиска
    driver.get(url_finde)

    #Поиск класса, в котором указан размер списка
    content = driver.find_element_by_xpath("//div[contains(@class, 'heading__unijc __h2__unijc')]")
    print(content.text)

    # Выделяем количество именинников
    if  'Найдено ' in content.text:
        num_user = content.text.replace('Найдено ', '')

        x = ''
        for num in num_user:
            if num == ' ':
                break
            else:
                x = x + num 
        x = int(x)
    if  'Найден ' in content.text:
        num_user = content.text.replace('Найден ', '')

        x = ''
        for num in num_user:
            if num == ' ':
                break
            else:
                x = x + num 
        x = int(x)

    #Поиск классов с прокруткой, в котором указаны пользователи
    content = driver.find_elements_by_xpath("//div[contains(@class, 'row__px8cs skip-first-gap__m3nyy')]")
    while x - len(content):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        content = driver.find_elements_by_xpath("//div[contains(@class, 'row__px8cs skip-first-gap__m3nyy')]")
        
    for con in content:
        print(con.text)
        
    print('Найдено ', x)
    print('В списке ', len(content),' человек')
    
    return driver.page_source
    
                
def main(months, days, citys_urls_finde):
    get_sel(months, days, citys_urls_finde)
    
if __name__=='__main__':
    
    months = [3]
    days = [20, 21, 22, 23]
    citys_urls_finde = {'Ziryanovsk':['https://ok.ru/dk?st.cmd=searchResult&st.mode=Users\
        &st.bthMonth=','&st.grmode=Groups\
        &st.bthDay=','&st.country=10415971874\
        &st.location=%D0%97%D1%8B%D1%80%D1%8F%D0%BD%D0%BE%D0%B2%D1%81%D0%BA\
        &st.cityId=10395281447']}
    
    main(months, days, citys_urls_finde)
    


