from django.urls import path
from psy.views.get_n_psy import GetPsy
from psy.views.receiving_assistant_data import  ReceivingAssistantData
from psy.views.results import Result

urlpatterns = [
    path('', GetPsy.as_view()),
    path('receiving_assistant_data/', ReceivingAssistantData.as_view(), name='receiving_assistant_data'),
    path('result/', Result.as_view(), name='result'),

]
