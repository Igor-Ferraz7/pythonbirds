class Pessoa:
    def cumprimentar(self):
        return f'Olá, id de self: {id(self)}'


if __name__ == "__main__":
    p = Pessoa()
    print(f"{p.cumprimentar()} | id de p:{id(p)}")
