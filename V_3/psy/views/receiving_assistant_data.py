# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from psy.models.serialization import SerializationData
from psy.models.psychic import Psychic


class ReceivingAssistantData(TemplateView):

    def get(self, request):

        coding = SerializationData(request)
        n_psy, assistent, psychic = coding.de_serializ(request.session['psychic'])
        # Десериализируем

        helper = Psychic()
        data_lst = helper.assumptions_of_psychics(n_psy, psychic)
        # Получаем предположения экстрасенсов

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
            helper = Psychic()
            psychic = helper.save_numbers(n_psy, psychic)
            # Сохраняем предположенные числа в список

            request.session['psychic'] = coding.serializ(psychic, request.session['psychic'])
            # Сериализируем

            assistent['hidden_number'] = request.POST.get("num_test")
            assistent['all_hidden_number'].append(assistent['hidden_number'])

        return redirect('/result/')
