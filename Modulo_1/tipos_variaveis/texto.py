# Declaração
nome_completo = "Pedro Boeing"

nome_completo_aspas = """Pedro
Boeing"""

nome_completo_quebra = "Pedro " \
"Boeing"

nome = "Pedro"
sobrenome = "Boeing"

# Formatação
print("Nome completo (1a forma):", nome_completo)   
print("Nome completo (2a forma):" + nome_completo)   
print("Nome completo (3a forma):" + "Pedro" + "Boeing")   
print("Nome completo (4a forma):" + " Pedro", "Boeing")
print("Nome completo (5a forma):", nome_completo_aspas)
print("Nome completo (6a forma):", nome_completo_quebra)
print("Nome completo (7a forma): %s, e %s" % (nome_completo, nome_completo_aspas))
print(f"Nome completo (8a forma): {nome} {sobrenome}")
print("Nome completo (9a forma): {} {}".format(nome, sobrenome))