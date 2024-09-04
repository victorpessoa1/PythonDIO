total_conta = 0
depositos = []
saques = []
LIMITE_DE_SAQUES = 3
numero_de_saques = 0


def Deposito ():
    global total_conta

    valor_deposito = float(input("informe o valor a ser depositado: "))
    total_conta += valor_deposito
    depositos.append(valor_deposito)
    print("Deposito realizado com sucesso")


def Saque():
    global numero_de_saques, total_conta

    if total_conta == 0:
        print ("impossivel sacar, sem saldo na conta")
        return

    if LIMITE_DE_SAQUES == numero_de_saques:
        print ("Impossivel sacar, limite diario de saques atingido")
        return

    valor_saque = float(input("Informe o valor a ser sacado, lembrando que deve ser até R$ 500.00 e dentro do seu limite na conta: "))

    if valor_saque > 500 or valor_saque > total_conta:
        print ("impossivel sacar")
        return

    else:
        total_conta -= valor_saque
        saques.append(valor_saque)
        print ("saque realizado com sucesso")
        numero_de_saques += 1

def Extrato():
    print (f"""Valor total na conta é R$ {total_conta:.2f}
saques: {saques:.2f}
depositos: {depositos:.2f}
""")


operacao = ""
while operacao != "sair":

    operacao = input ("""
digite 'saque' para saques
digite 'deposito' para depositos
digite 'extrato' para extrato
digite 'sair' para sair
""")

    if operacao == "saque":
        Saque()
    elif operacao == "deposito":
        Deposito()
    elif operacao == "extrato":
        Extrato()
    else:
        operacao = input ("""
Comando inválido
digite 'saque' para saques
digite 'deposito' para depositos
digite 'extrato' para extrato
digite 'sair' para sair
""")