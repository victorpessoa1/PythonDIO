total_conta = 0
depositos = []
saques = []
LIMITE_DE_SAQUES = 3
numero_de_saques = 0


def Deposito ():
    global total_conta

    valor_deposito = float(input("informe o valor a ser depositado"))
    total_conta += valor_deposito
    depositos.append(valor_deposito)


def Saque():
    global numero_de_saques, total_conta

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
        numero_de_saques += 1

def Extrato():
    print (f"""Valor total na conta é R${total_conta}
saques: {saques}
depositos: {depositos}
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