# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.shortcuts import render

from psy.models.serialization import SerializationData


class Result(TemplateView):

    def get(self, request):

        coding = SerializationData()
        assistent, n_psy, psychic = coding.de_serializ(request)
        # Десериализируем

        for i in range(int(n_psy)):
            psychic[i].get_credibility(assistent['hidden_number'])
            # Считаем достоверность

        data_lst = {}
        for i in range(int(n_psy)):
            data_lst[i] = {'proposed': psychic[i].proposed_number,
                           'cred': psychic[i].credibility,
                           'all_proposed': psychic[i].all_proposed_number
                           }

        context = {'hidden_number': assistent['hidden_number'],
                   'all_hidden_number': assistent['all_hidden_number'],
                   'data_lst': data_lst
                   }

        coding.serializ(request, psychic)
        # Сериализируем

        return render(request, 'results.html', context)
