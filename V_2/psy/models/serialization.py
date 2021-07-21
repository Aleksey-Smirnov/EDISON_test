import pickle


class SerializationData:

    def serializ(self, request, psychic):
        # Сериализируем

        request.session['data'] = pickle.dumps(psychic, 3)

    def de_serializ(self, request):
        # Десериализируем

        assistent = request.session['assistent']
        n_psy = assistent['n_psy']
        psychic = pickle.loads(request.session['data'])

        return assistent, n_psy, psychic
