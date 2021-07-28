import json
import random


class Psychic:

    def __init__(self):

        self.__proposed_number = None
        self.__all_proposed_number = []
        self.__credibility = 0

    @property
    def proposed_number(self):
        return self.__proposed_number

    @proposed_number.setter
    def proposed_number(self, value):
        self.__proposed_number = value

    @property
    def all_proposed_number(self):
        return self.__all_proposed_number

    @all_proposed_number.setter
    def all_proposed_number(self, value):
        self.__all_proposed_number = value

    @property
    def credibility(self):
        return self.__credibility

    @credibility.setter
    def credibility(self, value):
        self.__credibility = value

    def to_json(self):
        """Сохранение данных экстрасенсов"""
        data = {
            'proposed_number': self.proposed_number,
            'all_proposed_number': self.all_proposed_number,
            'credibility': self.credibility
        }
        return json.dumps(data, ensure_ascii=False, indent=2)

    @staticmethod
    def from_json(data):
        """Получение данных экстрасенсов"""
        json_data = json.loads(data)
        psychic = Psychic()
        psychic.proposed_number = json_data['proposed_number']
        psychic.all_proposed_number = json_data['all_proposed_number']
        psychic.credibility = json_data['credibility']
        return psychic

    @classmethod
    def assumptions_of_psychics(clf, n_psy, data):
        """Работа с предположениями, получение списка предположений"""
        data_lst = {}
        for i in range(int(n_psy)):
            data[i].proposed_number = random.randint(10, 99)
            # Предполагают экстрасенсы

            data_lst[i] = data[i].proposed_number
            # Список - предположенные числа
        return data_lst

    @classmethod
    def save_numbers(clf, n_psy, data):
        """Сохранение списка предположений"""
        for i in range(int(n_psy)):
            data[i].all_proposed_number.append(data[i].proposed_number)

    @classmethod
    def consider_the_reliability(clf, n_psy, data, assistent_num):
        """Вычисление достоверности всех экстрасенсов"""
        for i in range(int(n_psy)):
            if int(data[i].proposed_number) == int(assistent_num):
                data[i].credibility += 1
            else:
                data[i].credibility -= 1

    @classmethod
    def get_data_list(clf, n_psy, data):
        """Получение списка данных экстрасенсов"""
        data_lst = {}
        for i in range(int(n_psy)):
            data_lst[i] = {'proposed': data[i].proposed_number,
                           'cred': data[i].credibility,
                           'all_proposed': data[i].all_proposed_number
                           }
        return data_lst
