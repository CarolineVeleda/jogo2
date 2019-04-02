from datetime import datetime

class Jogo:
    def __init__(self,nome,genero,lancamento):
        self._nome = nome
        #self._lancamento = format(datetime.strptime(str(lancamento),"%d-%m-%Y"),"%d-%m-%Y")
        #if(isinstance(lancamento, datetime.date)):
            #self._lancamento = lancamento
        
        if(isinstance(lancamento, str)):
            try:
                self._lancamento = format(datetime.strptime(str(lancamento),"%d-%m-%Y"),"%d-%m-%Y")
            except ValueError:
                raise ValueError("O formato da data é inválido.")

        self._genero = genero
        self._cod = ""

    def _get_nome(self):
        return self._nome
    def _get_lancamento(self):
        return self._lancamento
    def _get_genero(self):
        return self._genero
    def _get_cod(self):
        return self._cod
    def _set_nome(self, nome):
        self._nome = nome
    def _set_lancamento(self, lancamento):
        self._lancamento = lancamento
    def _set_genero(self, genero):
        self._genero = genero
    def _set_cod(self, cod):
        self._cod = cod
    
    nome = property(_get_nome,_set_nome)
    genero = property(_get_genero,_set_genero)
    lancamento = property(_get_lancamento,_set_lancamento)
    cod = property(_get_cod,_set_cod)
    
    def __str__(self):
        return "{},{},{},{}".format(self._cod,self._nome,self._genero,self._lancamento)




