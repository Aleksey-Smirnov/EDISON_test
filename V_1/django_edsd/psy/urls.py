from django.urls import path
from psy.views.get_n_psy import get_n_psy
from psy.views.receiving_assistant_data import  receiving_assistant_data
from psy.views.results import results

urlpatterns = [
    path('', get_n_psy, name='index'),
    path('receiving_assistant_data/', receiving_assistant_data,\
                                     name='receiving_assistant_data'),
    path('results/', results, name= 'results'),
    
]
