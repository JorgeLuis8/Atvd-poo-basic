'''Crie uma classe para representar uma pessoa, com os atributos privados de nome, data de nascimento e altura. 
Crie os métodos públicos necessários para sets e gets e também um método para imprimir todos os dados de 
uma pessoa. Crie um método para calcular a idade da pessoa'''


import datetime
__slots__ =['nome','nascimeto','altura']
 
class Pessoa:
    def __init__(self, nome, nascimento, altura):
        self._nome = nome
        self._nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')
        self._altura = altura
        self._idade = self.calcula_idade()

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, New_name):
        self._nome = New_name

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, New_nascimento):
        self._nascimento = datetime.datetime.strptime(
            New_nascimento, '%d/%m/%Y')

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, new_altura):
        self._altura = new_altura

    def calcula_idade(self):
        hoje = datetime.datetime.now()
        idade = hoje.year - self._nascimento.year - \
            ((hoje.month, hoje.day) < (self._nascimento.month, self._nascimento.day))
        self._idade = idade
        return idade

    def imprimir(self):
        print(f'Nome {self._nome}')
        print(f'Nascimento {self._nascimento.date()}')
        print(f'Altura {self._altura}')
        print(f'Idade {self._idade}')
