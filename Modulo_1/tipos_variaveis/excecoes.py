print("Exemplo de captura de exceções")
try:
    numero = int(input("Digite um numero inteiro: "))
    resultado = 10/numero
except ValueError as e:
    print("Erro de Value")
except Exception as e:
    print(f"Erro: {e}")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Operação finalizada")
    


