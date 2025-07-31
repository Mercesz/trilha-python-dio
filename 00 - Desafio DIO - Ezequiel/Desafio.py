menu = """

-----------------------------------
[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair
-----------------------------------

Escolha uma opção: """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("\nInforme o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("O valor do depósito deve ser positivo.")

    elif opcao == "2":
        saque = float(input("\nInforme o valor do saque: "))
        if saque > saldo:
            print("Saldo insuficiente!")
        elif saque > limite:
            print("Saque excede o limite de R$500.00")
        elif numero_saques >= LIMITE_SAQUES:
            print("Limite de saques atingido")
        elif saque <= 0:
            print("Valor inválido.")
        else:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso")

    elif opcao == "3":
        print("\n-------Extrato-----")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("-----------------------")

    elif opcao == "4":
        print("\nEncerrando o sistema... Volte sempre!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")
