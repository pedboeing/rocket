# Criando um dicionário exemplar
pessoa = {"nome": "Joao", "idade": 30, "cidade": "Sao Paulo"}

# Exibindo o dicionário
print("Meu dicionario de pessoa:", pessoa)

# Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

pessoa["sobrenome"] = "Silva"

print("Sobrenome:", pessoa)

# Removendo um par chave-valor
del pessoa["sobrenome"]
print("Sobrenome:", pessoa)

# Métodos: keys(), values(), items()
chaves = list(pessoa.keys())
print("Chaves do dicionario:", chaves)
print("Primeira chave:", chaves[0])

valores = list(pessoa.values())
print("Valores do dicionario:", valores)
print("Primeiro valor:", valores[0])

items = list(pessoa.items())
print("Itens do dicionario:", items)
print("Primeiro item:", items[0])
print("Primeira chave-valor: %s - %s" % (items[0][0], items[0][1]))