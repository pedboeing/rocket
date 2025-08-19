lista = [1,2,3,4,5]

for elemento in lista:
    print(elemento)

print("____________")

tupla = (1,2,3,4,5)

for x in tupla:
    print(x)

print("____________")

pessoa = {
    "nome": "Joao",
    "idade": 30,
    "cidade": "Florianopolis"
}

for x in pessoa.keys():
    print(x)

for chave in pessoa.values():
    print(chave)

for chave, valor in pessoa.items():
    print(chave + ":", valor)

for i in range(5):
    print(i)

print("____________")

for indice in range(1,6):
    print(indice)

# enumerate()

listaEnumerate = ["a", "b", "c"]

for indice, valor in enumerate(listaEnumerate):
    print("Indice:", indice, "Valor:", valor)