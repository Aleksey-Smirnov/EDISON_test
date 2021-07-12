# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect 
from django.http import HttpResponseRedirect, HttpResponse
from psy.models.psychic import Psychic
import pickle


def get_n_psy(request):
    
    if request.method == 'POST':
        
        request.session['assistent'] = {'hidden_number':None,\
                                        'all_hidden_number':[],\
                                        'N_psy':None}
        assistent = request.session['assistent'] #Данные ассистента
        
        request.session['psychic'] = {'list_psy':[]}
        psychic = request.session['psychic'] #Данные экстрасенсов
        
        assistent['N_psy'] = request.POST.get("num_psy")
        N_psy = assistent['N_psy']
        #Получаем и записываем количество экстрасенсов
                      
        for i in range(int(N_psy)): #Создаем экземпляры 
            psychic['list_psy'].append(Psychic())
       
        request.session['data'] = pickle.dumps(psychic['list_psy'])
        #Сериализируем
        
        return redirect ('/receiving_assistant_data/')

    if 'assistent' in request.session:
                return redirect('/receiving_assistant_data/')
    return render(request, 'index.html')
