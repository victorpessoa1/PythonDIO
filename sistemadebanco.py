import datetime


def Cadastrar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = [cliente for cliente in clientes if cliente["cpf"] == cpf]

    if cliente:
        print("Já existe um cliente cadastrado com o cpf informado")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")
    
    
def Cadastrar_conta_bancaria(agencia, numero_conta, clientes):
    cpf = input("Informe o CPF do usuário: ")
    cliente = [cliente for cliente in clientes if cliente["cpf"] == cpf]

    if cliente:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def Deposito (total_conta, depositos):

    valor_deposito = float(input("informe o valor a ser depositado: "))
    total_conta += valor_deposito
    depositos.append({valor_deposito, datetime.datetime.now()})
    print("Deposito realizado com sucesso")
    return total_conta, depositos


def Saque(LIMITE_DE_SAQUES_DIARIO, saques, numero_de_saques, total_conta ):
    
    if total_conta == 0:
        print ("impossivel sacar, sem saldo na conta")
        return

    if LIMITE_DE_SAQUES_DIARIO == numero_de_saques:
        print ("Impossivel sacar, limite diario de saques atingido")
        return

    valor_saque = float(input("Informe o valor a ser sacado, lembrando que deve ser até R$ 500.00 e dentro do seu limite na conta: "))

    if valor_saque > 500 or valor_saque > total_conta:
        print ("impossivel sacar")
        return

    else:
        total_conta -= valor_saque
        saques.append({valor_saque, datetime.datetime.now()})
        print ("saque realizado com sucesso")
        numero_de_saques += 1

def Extrato(saques, depositos, total_conta):
    print (f"Valor total na conta é R$ {total_conta:.2f}")
    for key, val in saques:
        print (f"foi sacado R${key:.2f} ás {val}")
    for key, val in depositos:
        print (f"foi depositado R${key:.2f} ás {val}")


        
        
def main():
    LIMITE_DE_SAQUES_DIARIO = 10
    AGENCIA = "0001"
    total_conta = 0
    depositos = []
    saques = []
    clientes = []
    contas = []
    numero_de_saques = 0
    
    
    operacao = ""
    while operacao != "sair":

        operacao = input ("""
    digite 'saque' para saques
    digite 'deposito' para depositos
    digite 'extrato' para extrato
    digite 'sair' para sair
    digite 'cadastrar cliente' para cadastrar um novo cliente
    digite 'nova conta' para Criar uma nova conta bancária
    """)

        if operacao == "saque":
            saques, numero_de_saques, total_conta = Saque(LIMITE_DE_SAQUES_DIARIO, saques, numero_de_saques, total_conta )
            
        elif operacao == "deposito":
            total_conta, depositos = Deposito(total_conta, depositos)
            
        elif operacao == "extrato":
            Extrato(saques, depositos)
            
        elif operacao == "cadastrar cliente":
            clientes = Cadastrar_cliente()
            
        elif operacao == "nova conta":
            numero_conta = len(contas) + 1
            contas = Cadastrar_conta_bancaria(AGENCIA, numero_conta, clientes)
            
        else:
            operacao = input ("""
    Comando inválido
    digite 'saque' para saques
    digite 'deposito' para depositos
    digite 'extrato' para extrato
    digite 'sair' para sair
    digite 'cadastrar cliente' para cadastrar um novo cliente
    digite 'nova conta' para Criar uma nova conta bancária
    """)
    
main()