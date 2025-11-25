#calculo de frete
from abc import ABC, abstractmethod
import os

class TransporteStrategy(ABC):
    @abstractmethod
    def calcular_frete(self, distancia_km):
        pass

class Moto(TransporteStrategy):
    def calcular_frete(self, distancia_km):
        return 5.00 + (distancia_km * 1.50)

class Carro(TransporteStrategy):
    def calcular_frete(self, distancia_km):
        return 10.00 + (distancia_km * 3.00)

class Caminhao(TransporteStrategy):
    def calcular_frete(self, distancia_km):
        return 50.00 + (distancia_km * 6.00)

class LogisticaFactory:
    @staticmethod
    def criar_transporte(tipo):
        tipo = tipo.upper()
        
        if tipo == "EXPRESSO":
            return Moto()
        elif tipo == "PADRAO":
            return Carro()
        elif tipo == "CARGA PESADA":
            return Caminhao()
        else:
            return Carro()
def limpar():
    os.system('cls')
    
if __name__ == "__main__":

    historico_de_envios = []

    while True:
        limpar()
        print("\n SISTEMA DE LOGÍSTICA ")
        print("\n=== NOVO PEDIDO DE FRETE ===")
        nome = input("Nome do Cliente: ")
        
        print("\nSelecione o tipo de serviço:")
        print("1 - Expresso (Moto)")
        print("2 - Padrão (Carro)")
        print("3 - Carga Pesada (Caminhão)")
         
        opcao = input("Digite o número da opção: ")
        
        tipo_servico = ""
        if opcao == "1":
            tipo_servico = "EXPRESSO"
        elif opcao == "3":
            tipo_servico = "CARGA_PESADA"
        else:
            tipo_servico = "PADRAO"

        try:
            distancia = float(input("\nDigite a distância (km): "))
        except ValueError:
            print("Erro: Digite apenas números para a distância.")
            continue

        veiculo = LogisticaFactory.criar_transporte(tipo_servico)
        
        dados_do_pedido = {
            "cliente": nome,
            "veiculo_objeto": veiculo, 
            "km": distancia
        }

        historico_de_envios.append(dados_do_pedido)

        custo_atual = veiculo.calcular_frete(distancia)
        print(f"Pedido adicionado! Custo: R${custo_atual:.2f}")

        continuar = input("\nDeseja calcular outro frete? (s/n): ")
        if continuar.lower() != 's':
            break
        
    print("\n\n=== RELATÓRIO DO DIA  ===")
    
    for pedido in historico_de_envios:
        obj_veiculo = pedido["veiculo_objeto"]
        dist = pedido["km"]
        cli = pedido["cliente"]

        valor_final = obj_veiculo.calcular_frete(dist)
        
        print(f"Cliente: {cli} | Veículo: {type(obj_veiculo).__name__} | Distância: {dist}km | Total: R${valor_final:.2f}")