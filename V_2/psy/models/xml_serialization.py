from django.core import serializers
from psy.models.psychic import QuantityPsychic


class SerializationData:

    def serializ(self, request, psychic):
        # Сериализируем

        QuantityPsychic
        request.session['data'] = serializers.serialize("xml", psychic.objects.all())


    def de_serializ(self, request):
        # Десериализируем

        psychic = []
        assistent = request.session['assistent']
        n_psy = assistent['n_psy']
        for obj in serializers.deserialize("xml", request.session['data']):
            psychic.append(obj)


        return assistent, n_psy, psychic