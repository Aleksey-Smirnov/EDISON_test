'''
Выделение ID именинников, из поискового списка "Одноклассники"
'''
from bs4 import BeautifulSoup

def get_id(name_html):
	
	# Принимаем имя файла
	
	with open(name_html, encoding='utf-8') as fp:
		soup = BeautifulSoup(fp, "html.parser")

	results = soup.find_all("a", class_="link__91azp title-link__79ad9")

	res_dict = {} #Словарь с id
	entityId = [] #Список id
	i = 0
	for result in results:
		i += 1
			
		#Очищаем строку от лишних знаков
		res = result.get('data-l')
		res = res.replace('searchCtx,{', '')
		res = res.replace('}', '')
		res = res.replace('\\', '')
		res = res.replace('\"', '')
		res = res.replace(',', '\n')
		
		#Создаем из строки словарь
		for line in res.split('\n'): # Проходимся по каждой строчке
			
			if not line.strip():
				continue
			key, value = [word.strip() for word in line.split(":")]
			res_dict[key] = value
		
		# Извлекаем из словаря id
		entityId.append(res_dict['entityId'])
		
		
	
	return entityId, i
