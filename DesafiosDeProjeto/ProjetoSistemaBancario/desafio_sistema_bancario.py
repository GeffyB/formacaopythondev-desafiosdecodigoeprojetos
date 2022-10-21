

menu = """\n
================ MENU ================
[d]Depositar
[s]Sacar
[e]Extrato
[q]Sair

=> """
    


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).lower()                         # Garantindo que ainda que o user entre com uma letra maiuscula, a opção seja entendida

    if opcao =="d":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:                                   # Garantindo que o valor informado no depósito seja um número maior que 0
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"\n== O Depósito no valor de R${valor:.2f} foi efetuado com sucesso! ==")
        
        else:
            print("Operação falhou! O valor informado não é válido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não possue saldo suficiente!")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque solicitado é maior que o limite possível!")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques permitidos excedido!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque : R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"\n== Saque no valor de R${valor:.2f} efetuado com sucesso, confira suas cédulas! ==")

        else:
            print("Operação falhou! O valor informado é invalido!")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações na conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")

    elif opcao == "q":
        print("\n== Obrigado por usar nossos serviços! Até mais! ==")
        break

    else:
        print("Operação inválida, verifique as operações disponíveis e tente novamente")