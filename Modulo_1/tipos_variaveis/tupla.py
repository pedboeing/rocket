# Criando uma tupla de exemplo
minha_tupla = (1, 2, 2, 3, 4)

print(minha_tupla)

print("Primeiro elemento da tupla:", minha_tupla[0])
print("Ultimo elemento da tupla:", minha_tupla[-1])

# Método count(): Conta o número de vezes que um elemento aparece
print("Numero de vezes que o numero 1 aparece:", minha_tupla.count(1))
print("Numero de vezes que o numero 2 aparece:", minha_tupla.count(2))
print("Numero de vezes que o numero 5 aparece:", minha_tupla.count(5))

print("Indice da primeira ocorrencia do numero 2:", minha_tupla.index(2))