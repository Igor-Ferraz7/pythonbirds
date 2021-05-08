class Pessoa:
    def __init__(self, nome=None, idade=16):
        self.nome = nome
        self.idade = idade
    def cumprimentar(self):
        return f'Olá, id de self: {id(self)}'


if __name__ == "__main__":
    p = Pessoa('Rogi', 61)
    print(f"{p.cumprimentar()} | id de p:{id(p)}")
    print(p.nome)
    print(p.idade)
    p.nome = "Igor"
    p.idade = 16
    print(p.nome)
    print(p.idade)
