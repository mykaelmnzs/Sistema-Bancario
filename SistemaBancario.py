MENU = '''
Selecione a opção desejada:

[1]Depositar
[2]Sacar
[3]Extrato
[0]Sair

=> ''' 

saldo=0 #Saldo inicial da conta
limite=500 # Valor máximo do saque
extrato="" # Armazena as transações
Numeros_Saques=0 # Contabiliza a quantidade dos saques
LIMITE_SAQUE=3 # Limite de saques diário

while True:
    opcao = input(MENU) # Recebe a opção escolhida no menu
    
    if opcao == "1":
        deposito = float(input("Informe o valor do depósito: ")) # Solicita ao usuario o valor desejado
        if deposito > 0:
            saldo += deposito # Adiciona o valor ao saldo
            extrato += f"Depósito:R$ {deposito:.2f}\n" # Registra a transação no extrato
            
        else:
            print("insira um valor valido")
                            
    elif opcao == "2":
        saque = float(input("Informe o valor do saque: "))
        
        saldo_insuficiente = saque > saldo  # Verifica se o saldo é suficiente
        saque_acima_limite = saque > limite  # Verifica se o saque excede o limite
        saques_exedidos = LIMITE_SAQUE <= Numeros_Saques # Verifica se excedeu o limite de saques
            
        if saldo_insuficiente:
            print("Falha na operação! A conta não possui saldo suficiente. ")     
        elif saque_acima_limite:
            print("Falha na operação! O valor do saque execede o limite")             
        elif saques_exedidos:
            print("Falha na operação! O limite de saque diário foi atingido")    
        elif saque > 0:
             saldo -= saque # Subtrai o valor ao saldo
             extrato += f"Saque:R$ {saque:.2f}\n" # Registra a transação no extrato
             Numeros_Saques += 1  # Incrementa o contador de saques
        else:
            print("Por favor digite um valor válido")
                              
    elif opcao == "3":
        # Exbibe o extrato ou a mensagem padrão quando não houver movimentações
        print("\n=====EXTRATO DE MOVIMENTAÇÕES=====")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("====================================")
     
    elif opcao == "0":
         break # Sai do loop while e encerra o programa!

    else:
        print("Por favor selecione uma opção valida") # Opção inválida

