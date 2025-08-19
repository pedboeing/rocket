# Exemplo de herança

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def andar(self):
        print(f"O {self.nome} andou")
        return

    def emitir_som():
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au"
    
class Gato(Animal):
    def emitir_som(self):
        return "Miau"
    

dog = Cachorro("Rex")
cat = Gato("Felix")

animais = [dog,cat]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")

print("\nExemplo de encapsulamento:")

class ContaBancaria():
    def __init__(self, saldo):
        self.__saldo = saldo # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo
    
conta = ContaBancaria(1000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.sacar(200)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

conta_do_zezinho = ContaBancaria(50)

print("\nExemplo de abstração:")
from abc import ABC, abstractmethod

class Veiculo(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self):
        pass

    def ligar(self):
        return "Carro ligado usando a chave"
    
    def desligar(self):
        return "Carro desligado usando a chave"
    
    

carro_amarelo = Carro()
print(carro_amarelo.ligar())