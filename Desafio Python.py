menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
=> """

saldo = 0
limite_operacao = 500
LIMITE_SAQUE = 3
numero_saques = 0
extrato = ""

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("Informe o valor de depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else: 
            print("A operação falhou: O valor informado é inválido")
    
    elif opcao == 's':
        valor = float(input("Informe um valor para saque: "))

        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite_operacao

        excedeu_saques = numero_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print("A operação falhou: Você não tem saldo suficiente")
        
        elif excedeu_limite:
            print("A operação falhou: O valor do saque excede o limite permitido")
        
        elif excedeu_saques:
            print("A operação falhou: Número de saques excedido")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("A operação falhou: O valor informado é inválido.")
        
    elif opcao == 'e':
        print("\n=================== EXTRATO ===================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")

    elif opcao == 'q':
        break

    else:
        print("Operação inválida. Por favor, selecione novamente a operação desejada.")
