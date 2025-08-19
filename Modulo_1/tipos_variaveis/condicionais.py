# if, elif e else

# Exemplo de IF
idade = int(input("Qual sua idade? "))

if idade >= 18:
    print("Voce eh maior de idade")
elif idade >= 12:
    print("Voce eh um adolescente")
else:
    print("Voce nao eh maior de idade")

mensagem = "Pode tirar a CNH" if idade >= 18 else "Nao pode tirar CNH"
print(mensagem)