class Pessoa:  # A classe funciona como uma forma de gelo
    olhos=2

    def __init__(self,*filhos, nome=None, idade=38):
        self.idade = idade
        self.nome = nome
        self.filhos= list(filhos)

    def cumprimentar(self):  # para criar tipos personalizados
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
         return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
         return f'{cls} - olhos{cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe=super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    rone = Mutante(nome='Rone')
    maria = Homem(rone,nome='Maria')
    print(Pessoa.cumprimentar(maria))
    print(id(maria))
    print(maria.cumprimentar())
    print(maria.nome)
    print(maria.idade)
    for filho in maria.filhos:
        print(filho.nome)
maria.sobrenome='Moreno'
del maria.filhos
maria.olhos=1
del maria.olhos
print(maria.__dict__)
print(rone.__dict__)
#Pessoa.olhos=3
print(Pessoa.olhos)
print(maria.olhos)
print(rone.olhos)
print(id(Pessoa.olhos),id(maria.olhos),id(rone.olhos))
print(Pessoa.metodo_estatico(), maria.metodo_estatico())
print(Pessoa.nome_e_atributos_de_classe(),  maria.nome_e_atributos_de_classe())
pessoa = Pessoa('Anonimo')
print(isinstance(pessoa,Pessoa))
print(isinstance(pessoa,Homem))
print(isinstance(rone,Pessoa))
print(isinstance(rone,Homem))
print(rone.olhos)
print(rone.cumprimentar())
print(maria.cumprimentar())