from controllers.conta_controller import ContaController
from datetime import datetime

def menu():
    controller = ContaController()

    while True:
        print("\n=== Banco Python ===")
        print("1. Abrir conta")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Saldo")
        print("5. Extrato")
        print("6. Fechar conta")
        print("7. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            numero = controller.registranumero()
            if numero != -1:
                resultado = controller.criar_conta(numero)
                print(resultado)


        elif opcao == "2":
            numero = controller.registranumero()
            if numero != -1:
                try:
                    valor = float(input("Valor do depósito: "))
                    descricao = input("Descrição: ")
                    data = datetime.now()
                    resultado = controller.realizar_deposito(numero, valor, data, descricao)
                    print(resultado)
                except ValueError:
                    print("ERRO: Digite um valor numérico válido.")

        elif opcao == "3":
            numero = controller.registranumero()
            if numero != -1:
                try:
                    valor = float(input("Valor do saque: "))
                    descricao = input("Descrição: ")
                    data = datetime.now()
                    resultado = controller.realizar_saque(numero, valor, data, descricao)
                    print(resultado)
                except ValueError:
                    print("ERRO: Digite um valor numérico válido.")

        elif opcao == "4":
            numero = controller.registranumero()
            if numero != -1:
                resultado = controller.consultar_saldo(numero)
                print(resultado)

        elif opcao == "5":
            numero = controller.registranumero()
            if numero != -1:
                data_inicial = input("Data de inicio (dd/mm/aaaa) ou Enter para tudo: ")
                resultado = controller.mostrar_extrato(numero, data_inicial)
                print(resultado)

        elif opcao == "6":
            numero = controller.registranumero()
            if numero != -1:
                resultado = controller.fechar_conta(numero)
                print(resultado)

        elif opcao == "7":
            numero = controller.registranumero()
            if numero != -1:
                print("Saindo...")
                break
        else:
            print("Opção inválida!")