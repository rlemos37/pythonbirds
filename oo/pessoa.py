class Pessoa:#A classe funciona como uma forma de gelo
     def cumprimentar(self):           # para criar tipos personalizados
         return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())