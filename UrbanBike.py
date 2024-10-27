#Guilherme Berghann Bach
#Matrícula 201420093

# PARTE 1

class ContaUrbanBike:    
    def __init__(self, numero_conta):
        self.numero_conta = numero_conta
        self.carteira = 0

    def pedalar(self, valor):
        pass  # Método abstrato

    def creditar(self, valor):
        pass  # Método abstrato

    def transferir(self, valor, outro_pedal):
        self.pedalar(valor)
        outro_pedal.creditar(valor)

# PARTE 2

class PedalPop(ContaUrbanBike):
    taxa_de_operacao = 0.1 # ATRIBUTO EXIGIDO

    def pedalar(self, valor):
        valor_com_taxa = valor * (1 + self.taxa_de_operacao)
        if self.carteira >= valor_com_taxa:
            self.carteira -= valor_com_taxa

    def creditar(self, valor):
        valor_com_taxa = valor * (1 + self.taxa_de_operacao)
        self.carteira += valor - valor_com_taxa

class PedalPremium(ContaUrbanBike):
    limite = 100  #ATRIBUTO EXIGIDO

    def __init__(self, numero_conta):
        super().__init__(numero_conta)
        if self.carteira < 100:
            raise ValueError("Saldo inicial para PedalPremium deve ser pelo menos R$100,00")

    def pedalar(self, valor):
        self.carteira -= valor
        if self.carteira < -self.limite:
            self.carteira = -self.limite


#PARTE 3 - INTERFACE IMPRIMÍVEL 

class Imprimivel:
    def mostrar_dados(self):
        pass

class Ciclistas:
    def __init__(self):
        self.pedais = []

    def inserir(self, pedal):
        self.pedais.append(pedal)

    def remover(self, numero_pedal):
        for i, pedal in enumerate(self.pedais):
            if pedal.numero_conta == numero_pedal:
                del self.pedais[i]
                return True
        return False

    def procurar_pedal(self, numero_pedal):
        for pedal in self.pedais:
            if pedal.numero_conta == numero_pedal:
                return pedal
        return None

    def gerar_relatorio(self):
        for pedal in self.pedais:
            pedal.mostrar_dados()

# PARTE 4

class PedalPop(ContaUrbanBike, Imprimivel):
   

    def mostrar_dados(self):
        print(f"Pedal Pop - Número: {self.numero_conta}")
        print(f"Saldo: R$ {self.carteira:.2f}")
        print(f"Taxa de operação: {self.taxa_de_operacao:.2f}")

class PedalPremium(ContaUrbanBike, Imprimivel):
    

    def mostrar_dados(self):
        print(f"Pedal Premium - Número: {self.numero_conta}")
        print(f"Saldo: R$ {self.carteira:.2f}")
        print(f"Limite: R$ {self.limite}")


class ContaUrbanBike: #PARTE 05
    
    def main():
        ciclistas = Ciclistas()

        while True:
            print("\nMenu:")
            print("I. Criar pedal")
            print("II. Remover Pedal")
            print("III. Gerar relatório")
            print("IV. Selecionar Pedal e realizar operação")
            print("V. Finalizar")

            opcao = input("Digite a opção desejada: ").upper()

            if opcao == 'I':
                tipo = input("Digite o tipo de pedal (Pop ou Premium): ").lower()
                numero_conta = int(input("Digite o número da conta: "))
                saldo_inicial = float(input("Digite o saldo inicial: "))
                try:
                    if tipo == 'pop':
                        pedal = PedalPop(numero_conta)
                    else:
                        pedal = PedalPremium(numero_conta)
                    pedal.creditar(saldo_inicial)
                    ciclistas.inserir(pedal)
                    print("Pedal criado com sucesso!")
                except ValueError as e:
                    print(f"Erro ao criar pedal: {e}")

            elif opcao == 'II':
                numero_pedal = int(input("Digite o número do pedal a ser removido: "))
                if ciclistas.remover(numero_pedal):
                    print("Pedal removido com sucesso!")
                else:
                    print("Pedal não encontrado.")

            elif opcao == 'III':
                ciclistas.gerar_relatorio()

            elif opcao == 'IV':
                numero_pedal = int(input("Digite o número do pedal: "))
                pedal = ciclistas.procurar_pedal(numero_pedal)
                if pedal:
                    while True:
                        print("\nOperações disponíveis:")
                        print("1. Creditar")
                        print("2. Pedalar")
                        print("3. Transferir")
                        print("4. Voltar")
                        operacao = input("Digite a operação desejada: ")
                        if operacao == '1':
                            valor = float(input("Digite o valor a ser creditado: "))
                            pedal.creditar(valor)
                            print("Crédito realizado com sucesso!")
                        elif operacao == '2':
                            valor = float(input("Digite o valor a ser pedalado: "))
                            pedal.pedalar(valor)
                            print("Saque realizado com sucesso!")
                        elif operacao == '3':
                            numero_destino = int(input("Digite o número da conta destino: "))
                            pedal_destino = ciclistas.procurar_pedal(numero_destino)
                            if pedal_destino:
                                valor = float(input("Digite o valor a ser transferido: "))
                                pedal.transferir(valor, pedal_destino)
                                print("Transferência realizada com sucesso!")
                            else:
                                print("Pedal destino não encontrado.")
                        elif operacao == '4':
                            break
                        else:
                            print("Opção inválida.")
                else:
                    print("Pedal não encontrado.")

            elif opcao == 'V':
                break
            else:
                print("Opção inválida.")

    if __name__ == "__main__":
        main()