# @classmethod 
# @staticmethod 

class MinhaClasse:
    valor = 10

    def __init__(self, nome):
        self.nome = nome

    def metodo_instancia(self):
        return f"Método de instância chamado para {self.nome}"
    
    @classmethod
    def metodo_classe(cls):
        return f"Método de classe chamado para o valor {cls.valor}"
    
    @staticmethod
    def meotodo_estattico():
        return "Método estático chamado"
    
obj = MinhaClasse("Objeto")
print(obj.metodo_instancia())
print(MinhaClasse.valor)
print(MinhaClasse.metodo_classe())
print(MinhaClasse.meotodo_estattico())


class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(ano))


config1 = "Toyota,Corolla,2022"
carro1 = Carro.criar_carro(config1)
print(carro1.marca, carro1.modelo)


