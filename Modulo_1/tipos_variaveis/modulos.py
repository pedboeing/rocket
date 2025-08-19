print("Exemplo de importação de módulo padrão")
from math import sqrt

raiz_quadrada = sqrt(25)

print(f"Raiz quadrada de 25 é {raiz_quadrada}")

print("Criação de módulo personalizado")

import meu_modulo

mensagem = meu_modulo.saudacao("Igor")
dobro = meu_modulo.dobro(5)

print(mensagem, dobro)