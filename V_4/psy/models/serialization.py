from psy.models.psychic import Psychic


class SerializationData:

    def __init__(self, request):

        self.n_psy = request.session['assistent']['n_psy']
        self.assistent = request.session['assistent']

    def inicial(self, request):
        """Инициализация"""

        request.session['psychic'] = {}
        psychic_list = []

        for i in range(int(self.n_psy)):
            psychic_list.append(Psychic())
            request.session['psychic'][i] = psychic_list[i].to_json()

    def serializ(self, psychic_list, data):
        """Сериализируем"""

        for i in range(int(self.n_psy)):
            data[i] = psychic_list[i].to_json()
        return data

    def de_serializ(self, data):
        """Десериализируем"""

        psychic_list = []
        for i in range(int(self.n_psy)):
            psy = data[i]
            psychic_list.append(Psychic.from_json(psy))

        return self.n_psy, self.assistent, psychic_list
