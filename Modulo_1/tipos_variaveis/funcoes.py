# Exemplo

def saudacao(nome):
    print("Olá,", nome)

nome = input("Qual seu nome? ")

saudacao(nome)

def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("Quadrado de 5:", quadrado(5))

# Funcao com múltiplos parametros 

def soma(n1, n2):
    resultado = n1 + n2
    return resultado

print("Soma de 10 e 20:", soma(10, 20))