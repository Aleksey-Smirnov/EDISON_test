# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from psy.models.serialization import SerializationData


class ReceivingAssistantData(TemplateView):

    def get(self, request):

        coding = SerializationData(request)
        n_psy, assistent, psychic = coding.de_serializ(request.session['psychic'])
        # Десериализируем

        data_lst = {}
        for i in range(int(n_psy)):
            psychic[i].get_proposed_number()

            # Предполагают экстрасенсы

            data_lst[i] = psychic[i].proposed_number
            # Список - предположенные числа

        request.session['psychic'] = coding.serializ(psychic, request.session['psychic'])
        # Сериализируем

        return render(request, 'receiving_assistant_data.html', {'data_lst': data_lst})

    def post(self, request):

        coding = SerializationData(request)
        n_psy, assistent, psychic = coding.de_serializ(request.session['psychic'])
        # Десериализируем

        if not request.POST.get('num_test'):
            return render(request, 'error.html')
        else:
            for i in range(int(n_psy)):
                psychic[i].to_add()
                print('psychic[i].to_add()', psychic[i].all_proposed_number)
            request.session['psychic'] = coding.serializ(psychic, request.session['psychic'])
            # Сериализируем

            assistent['hidden_number'] = request.POST.get("num_test")
            assistent['all_hidden_number'].append(assistent['hidden_number'])

        return redirect('/result/')
