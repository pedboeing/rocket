# Declaração
minha_lista = [1,2,3,4,5, "Rocketseat", 1.4, True, False]

# Imprimindo a lista
minha_lista[0] = "Python"
print("Minha lista de exemplo", minha_lista)
print("minha_lista[0]:", minha_lista[0])
print("minha_lista[5]:", minha_lista[5])
print("minha_lista[1:7]:", minha_lista[1:7])
print("minha_lista[:6]:", minha_lista[:6])
print("minha_lista[5:]:", minha_lista[5:])


# Métodos

# Método append(): Adiciona um elemento no final da lista
minha_lista.append("Novo elemento")
print("Apos append:", minha_lista)

# Método index(): Retorna índice do elemento alvo
indice = minha_lista.index("Rocketseat")
print(indice)

# Método insert(): Insere um elemento em um índice específico
minha_lista.insert(5, "Alura")
minha_lista.insert(2, 10)
print(minha_lista)

# Método pop(): Remove e retorna o elemento de um índice específico
elemento_removido = minha_lista.pop(3)
print(elemento_removido)
print(minha_lista)

# Método remove(): Remove primeiro elemento com valor especificado
minha_lista.remove(True)
print(minha_lista)

# Método sort(): Organiza a lista em ordem crescente
lista2 = [10, 1, 5, 2, 9, 20, 8, 90]
print(lista2)
lista2.sort()
print(lista2)