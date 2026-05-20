from conta import conta
conta = conta()

while True:
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Calcular rendimento")
    print("4 - Sair")
    opcao = int(input("Digite a opção desejada: "))

    match opcao:
        case 1:
            valor = float(input("Digite o valor a ser depositado: "))
            conta.deposita(valor)
            print(f"Saldo atual: {conta.saldo}")    
        case 2:
            valor = float(input("Digite o valor a ser sacado: "))
            conta.Saca(valor)
            print(f"Saldo atual: {conta.saldo}")
        case 3:            
            rendimento = conta.calculaRendimento()
            print(f"Rendimento: {rendimento}")
        case 4:
            break