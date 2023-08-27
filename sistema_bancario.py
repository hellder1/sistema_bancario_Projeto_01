menu = '''

[a] Depositar
[b] Sacar
[c] Extrato
[d] Sair

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "a":
        valor = float(input("Informe o valor do depósito: "))
        # Verificação para não haver depositos de valores negativos
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'

        else:
            print("Operação falhou! O valor informado é inválido, tente novamente com outro valor.")
    # Verificação de saldos, limite e limite de saques.
    elif opcao == "b":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES
        # Mensagens informativas sobre cada falha nas operações.
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! Número máximo  de saques excedido.")
        
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        #Verificação no valor d saque para evitar valores negativos.
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido")
    # Verificação do extrato com if ternário para verificar se há movimentoções ou não.
    elif opcao == "c":
        print("\n============= EXTRATO =============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print("=====================================")
    # Break para encerrer o programa.
    elif opcao == "d":
        break
    #Mensagem de alerta de operação não reconhecida pelo sistema    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")
        
      


