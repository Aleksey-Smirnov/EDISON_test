# -*- coding: utf-8 -*-

from django.shortcuts import redirect
from django.views.generic import TemplateView

from psy.models.psychic import Psychic
from psy.models.serialization import SerializationData


class GetPsy(TemplateView):
    #template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        if 'assistent' in request.session:
            return redirect('/receiving_assistant_data/')
        #return super().get(request, *args, **kwargs)
        return render(request, 'index.html')

    def post(self, request):

        if request.method == 'POST':

            request.session['assistent'] = {'hidden_number': None, 'all_hidden_number': [], 'n_psy': None}
            assistent = request.session['assistent']  # Данные ассистента

            request.session['psychic'] = {'list_psy': []}
            psychic = request.session['psychic']  # Данные экстрасенсов

            assistent['n_psy'] = request.POST.get("num_psy")
            n_psy = assistent['n_psy']
            # Получаем и записываем количество экстрасенсов

            for i in range(int(n_psy)):  # Создаем экземпляры
                psychic['list_psy'].append(Psychic())

            coding = SerializationData()
            coding.serializ(request, psychic['list_psy'])
            # Сериализируем

            return redirect('/receiving_assistant_data/')
