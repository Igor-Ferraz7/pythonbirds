class Pessoa:
    def __init__(self, *filhos, nome=None, idade=16):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá, id de self: {id(self)}'


if __name__ == "__main__":
    Renzo = Pessoa(nome='Renzo')
    Igor = Pessoa(Renzo, nome='Igor')
    print(f"{Igor.cumprimentar()} | id de p:{id(Igor)}")
    print(Igor.nome)
    print(Igor.idade)
    for filho in Igor.filhos:
        print(filho.nome)
