import json
import random


class Psychic:

    def __init__(self):

        self.proposed_number = None
        self.all_proposed_number = []
        self.credibility = 0

    def to_add(self):
        """Сохранение предположенных чисел"""
        self.all_proposed_number.append(self.proposed_number)

    def get_credibility(self, ass_num):
        """Получение достоверности"""
        if int(self.proposed_number) == int(ass_num):
            self.credibility += 1
        else:
            self.credibility -= 1

    def get_proposed_number(self):
        """Получение предположенных чисел"""
        self.proposed_number = random.randint(10, 99)

    def to_json(self):
        """Сохранение данных экстрасенсов"""
        data = {
            'proposed_number': self.proposed_number,
            'all_proposed_number': self.all_proposed_number,
            'credibility': self.credibility
        }
        return json.dumps(data, ensure_ascii=False, indent=2)

    def from_json(self, data):
        """Получение данных экстрасенсов"""
        json_data = json.loads(data)
        self.proposed_number = json_data['proposed_number']
        self.all_proposed_number = json_data['all_proposed_number']
        self.credibility = json_data['credibility']

    def assumptions_of_psychics(self, n_psy, data):
        """Работа с предположениями, получение списка предположений"""
        data_lst = {}
        for i in range(int(n_psy)):
            data[i].get_proposed_number()
            # Предполагают экстрасенсы

            data_lst[i] = data[i].proposed_number
            # Список - предположенные числа
        return data_lst

    def save_numbers(self, n_psy, data):
        """Сохранение списка предположений"""
        for i in range(int(n_psy)):
            data[i].to_add()
        return data

    def consider_the_reliability(self, n_psy, data, assistent_num):
        """Вычисление достоверности всех экстрасенсов"""
        for i in range(int(n_psy)):
            data[i].get_credibility(assistent_num)
        return data

    def get_data_list(self, n_psy, data):
        """Получение списка данных экстрасенсов"""
        data_lst = {}
        for i in range(int(n_psy)):
            data_lst[i] = {'proposed': data[i].proposed_number,
                           'cred': data[i].credibility,
                           'all_proposed': data[i].all_proposed_number
                           }
        return data_lst
