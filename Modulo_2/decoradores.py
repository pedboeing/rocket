def meu_decorador(func):
    def wrapper():
        print("Antes de ser chamada")
        func()
        print("Depois de ser chamada")
    return wrapper

@meu_decorador
def funcao():
    print("Minha função foi chamada")

funcao()

