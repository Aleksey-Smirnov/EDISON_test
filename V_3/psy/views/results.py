# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.shortcuts import render

from psy.models.serialization import SerializationData
from psy.models.psychic import Psychic

class Result(TemplateView):

    def get(self, request):

        coding = SerializationData(request)
        n_psy, assistent, psychic = coding.de_serializ(request.session['psychic'])
        # Десериализируем

        helper = Psychic()
        psychic = helper.consider_the_reliability(n_psy, psychic, assistent['hidden_number'])
        # Считаем достоверность

        data_lst = helper.get_data_list(n_psy, psychic)
        # Получаем список данных экстрасенсов

        context = {'hidden_number': assistent['hidden_number'],
                   'all_hidden_number': assistent['all_hidden_number'],
                   'data_lst': data_lst
                   }

        request.session['psychic'] = coding.serializ(psychic, request.session['psychic'])
        # Сериализируем

        return render(request, 'results.html', context)
