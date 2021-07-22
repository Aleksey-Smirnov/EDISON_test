# -*- coding: utf-8 -*-

from django.shortcuts import redirect
from django.views.generic import TemplateView

from psy.models.serialization import SerializationData


class GetPsy(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        if 'assistent' in request.session:
            return redirect('/receiving_assistant_data/')
        return super().get(request, *args, **kwargs)

    def post(self, request):

        request.session['assistent'] = {'hidden_number': None, 'all_hidden_number': [], 'n_psy': None}
        request.session['assistent']['n_psy'] = request.POST.get("num_psy")
        # Данные ассистента

        coding = SerializationData(request)
        coding.inicial(request)
        # Инициализация

        return redirect('/receiving_assistant_data/')
