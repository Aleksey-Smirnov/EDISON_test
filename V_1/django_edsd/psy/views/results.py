# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect 
from django.http import HttpResponseRedirect, HttpResponse
from psy.models.psychic import Psychic
import pickle

def results(request):
        
        psychic = {}
        assistent = request.session['assistent']
        N_psy = assistent['N_psy']
        
        psychic['list_psy'] = pickle.loads(request.session['data'])
        #Десериализируем Psychyc
        
        for i in range(int(N_psy)):        
            psychic['list_psy'][i].\
            get_credibility(assistent['hidden_number'])
            #Считаем достоверность
                    
        data_lst ={}
        for i in range(int(N_psy)):
            data_lst[i] = {'proposed':psychic['list_psy'][i].proposed_number,\
                            'cred':psychic['list_psy'][i].credibility,\
                            'all_proposed':psychic['list_psy'][i].\
                                                all_proposed_number
                            }
                    
        request.session['data'] = pickle.dumps(psychic['list_psy'],3)
        #Сериализируем
        
        context = {'hidden_number':assistent['hidden_number'],\
                    'all_hidden_number':assistent['all_hidden_number'],\
                    'data_lst':data_lst}
        
        return render(request, 'results.html', context)
