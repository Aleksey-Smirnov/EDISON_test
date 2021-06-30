# -*- coding: utf-8 -*-
from assay import Assays
from psychic import Psychic


psy1 = Psychic('Светлый')
psy2 = Psychic('Тёмный')
ass = Assays(psy1, psy2)             #Экземпляр проверки
ass.get_assay(ass.app)               #Запуск проверки

app = ass.app


if __name__ == "__main__":
    app.run()
