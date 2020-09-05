class Pessoa:  # A classe funciona como uma forma de gelo
    def __init__(self, nome=None, idade=38):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):  # para criar tipos personalizados
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Maria')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome='Rone'
    print(p.nome)
    print(p.idade)
