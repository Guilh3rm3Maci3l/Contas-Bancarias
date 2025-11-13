from conta import Conta

def main():
    conta1 = Conta("1234", 1000)
    conta2 = Conta("1235", 500)

    conta1.depositar(200)
    conta1.pagamento(300, conta2, "Transferência para conta 1235")
    conta1.sacar(100)

    conta1.extrato()
    conta2.extrato()

if __name__ == "__main__":
    main()