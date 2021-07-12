# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect 
from django.http import HttpResponseRedirect, HttpResponse
from psy.models.psychic import Psychic
import pickle

def receiving_assistant_data(request):
        
        psychic = {}
        assistent = request.session['assistent']
        N_psy = assistent['N_psy']
        
        psychic['list_psy'] = pickle.loads(request.session['data'])
        #Десериализируем Psychyc
               
        if request.method == 'POST':
            
            if not request.POST.get('num_test'):
                    return render(request, 'error.html')
            
            else:
                
                for i in range(int(N_psy)):   
                    psychic['list_psy'][i].to_add()
                    
                request.session['data'] = pickle.dumps(psychic['list_psy'],3)
                #Сериализируем
                
                assistent['hidden_number'] = request.POST.get("num_test")
                assistent['all_hidden_number'].\
                            append(assistent['hidden_number'])
            return redirect ('/results/')
            
        
        data_lst ={}
        for i in range(int(N_psy)):   
            psychic['list_psy'][i].get_proposed_number()                  
            #Предполагают экстрасенсы
            
            data_lst[i] = psychic['list_psy'][i].proposed_number     
            #Список - предположенные числа
            
        request.session['data'] = pickle.dumps(psychic['list_psy'],3)
        #Сериализируем
                
        return render(request, 'receiving_assistant_data.html',\
                                            {'data_lst':data_lst})
 
