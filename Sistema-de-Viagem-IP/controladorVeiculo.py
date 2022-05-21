from funcoes import checagem, continuar
from bancoGeral import ler, escrever, get_bv, get_bm

# ========================================= Veículo ===================================================================


def cadastrarVeiculo():
    ler()
    while True:
        print(f'{"Cadastro de Veículos":^40}')
        print('-=' * 20)
        placa = str(input("Insira a placa do seu veículo (ex: 2H6BR22): ")).upper()
        while len(placa) != 7 or not placa.isalnum():
            print("informação incorreta.")
            placa = str(input("Insira a placa do seu veículo com 7 caracteres(ex: 2H6BR22) "
                              "e somente letras e números: ")).strip().upper()
        if not checagem(placa, 1):  # coloquei if not. porque ele só vai continuar se ele não existir (Que é False)
            tipo = str(input("Insira o tipo do seu veículo (moto ou carro): ")).strip().title()
            while tipo != "Moto" and tipo != "Carro":
                tipo = str(input("Infomação incorreta. Digite somente moto ou carro: ")).strip().title()
            veiculo = {"placa": placa, "tipo": tipo, "motorista": None}
            get_bv()[placa] = veiculo
            escrever()
            print("Veículo cadastrado com sucesso!")
        else:
            print("Este veículo já está cadastrado.")
        if not continuar():
            return
        print()


def buscarVeiculo():
    ler()
    if len(get_bv()) == 0:
        print("Ainda não existe nenhum veículo cadastrado.\n")
        return
    while True:
        print('-=-=-=-=Buscar Veículo-=-=-=-=')
        placa = str(input("Insira a placa do seu veículo: ")).strip().upper()
        if placa in get_bv():
            for veiculo in get_bv().values():
                if veiculo.get("placa") == placa:
                    if veiculo.get("Motorista") is not None:
                        print('-=' * 20)
                        print(f'{"Placa":<15}{"Tipo":11}{"Motorista"}')
                        print(f"{veiculo.get('placa'):<15}{veiculo.get('tipo'):11}{veiculo.get('motorista')}")
                        print("-=" * 20)
                        print()
                    else:
                        print('-=' * 20)
                        print(f'{"Placa":<15}{"Tipo":}')
                        print(f"{veiculo.get('placa'):<15}{veiculo.get('tipo'):6}")
                        print("-=" * 20)
                        print()
        else:
            print(f"O veículo com a placa {placa} não está cadastrado.")
        if not continuar():
            return
        print()


def addMotoristaVeic():
    ler()
    if len(get_bv()) == 0:
        print("Ainda não existe nenhum veículo cadastrado.\n")
        return
    else:
        while True:
            print("=-=-=-Adicionar Motorista=-=-=-")
            while True:
                placa = str(input("Digite a placa do veículo desejado: ")).strip().upper()
                existe = False
                for veiculo in get_bv().keys():
                    if placa == veiculo:
                        existe = True
                if not existe:
                    print(f"Esse Veículo não existe. Tente novamente.\n")
                else:
                    break
            nome = str(input("Digite o nome do motorista que você deseja adicionar ao veículo: ")).strip().title()
            nMotorista = False
            for veiculo in get_bv().values():
                if veiculo.get("placa") == placa and nome == veiculo.get("motorista"):
                    print(f"O motorista {nome} já está vinculado a este veículo.\n")
                    nMotorista = True
            if not nMotorista:
                nMotorista = False
                for cpf in get_bm().values():
                    if nome == cpf.get("nome"):
                        for veiculo in get_bv().values():
                            if placa == veiculo.get("placa"):
                                veiculo["motorista"] = nome
                                escrever()
                                nMotorista = True
                if nMotorista:
                    print("Motorista vinculado ao veículo com sucesso!\n")
                else:
                    print("Esse motorista não está cadastrado.")
                if not continuar():
                    return
            else:
                if not continuar():
                    return
            # verificar se a carteira dele é correspondente ao veículo. A - Carro, B - Moto, A/B Carro e Moto


def removerMotoristaVeic():
    ler()
    if len(get_bv()) == 0:
        print("Ainda não existe nenhum veículo cadastrado.\n")
        return
    else:
        motoristaCadastrado = 0
        for veiculo in get_bv().values():
            if veiculo.get("motorista") is not None:
                motoristaCadastrado += 1
        if motoristaCadastrado != 0:
            print("=-=-=-Remover Motorista do Veículo=-=-=-")
            print('=-'*15)
            while True:
                nMotoristas = 0
                nome = str(input("Digite o nome do motorista que você deseja desvincular do veículo: ")).strip().title()
                for motorista in get_bv().values():
                    if motorista.get("motorista") == nome:
                        nMotoristas += 1
                if nMotoristas == 0:
                    print(f"O motorista {nome} não está vinculado a nenhum veículo ou não existe.\n")
                else:
                    print(f"=-=-=-Veículo(s) de {nome}-=-=-=")
                    print(f'{" " * 7}{"Placa":<12}{"Tipo":8}')
                    for veiculo in get_bv().values():
                        if nome == veiculo.get("motorista"):
                            print(f'{" " * 7}{veiculo.get("placa"):<12}{veiculo.get("tipo"):8}')
                    while True:
                        placa = str(input(f"Digite a placa do veículo que deseja desvincular "
                                          f"do motorista {nome}: ")).strip().upper()
                        existe = False
                        for veiculo in get_bv().values():
                            if veiculo.get("placa") == placa and veiculo.get("motorista") == nome:
                                existe = True
                                opcao = str(input("Você tem certeza [S/N]? ")).strip().upper()
                                while opcao not in "SN":
                                    opcao = str(input("Opção incorreta. Digite somente s - Sim ou n - Não: ")).strip().upper()
                                print()
                                if opcao == "N":
                                    break
                                else:
                                    if veiculo.get('placa') == placa:
                                        veiculo["motorista"] = None
                                        escrever()
                                        print("Motorista desvinculado com sucesso!\n")
                                        break
                        if not existe:
                            print("Este veículo não existe. Tente novamente")
                        break
                    break
        else:
            print("Ainda não existe nenhum motorista vinculado a um veículo.\n")
            return
        if not continuar():
            return
        removerMotoristaVeic()


def listarVeicCMotorista():
    ler()
    if len(get_bv()) == 0:
        print("Ainda não existe nenhum veículo cadastrado.\n")
        return
    else:
        nMotoristas = 0
        for veiculo in get_bv().values():
            if veiculo.get("motorista") is not None:
                nMotoristas += 1
        if nMotoristas == 0:
            print("Não existe motorista vinculado ao veículo.\n")
            return
        else:
            print("=-=-=-Veículos Com Motorista-=-=-=")
            print(f'{"Placa":<12}{"Tipo":8}{"Motorista"}')
            for veiculo in get_bv().values():
                if veiculo.get("motorista") is not None:
                    print(f'{veiculo.get("placa"):<12}{veiculo.get("tipo"):8}{veiculo.get("motorista")}')
            print('=-' * 17)
            print()


def listarVeicSMotorista():
    ler()
    if len(get_bv()) == 0:
        print("Ainda não existe nenhum veículo cadastrado.\n")
        return
    nMotoristas = 0
    for veiculo in get_bv().values():
        if veiculo.get("motorista") is None:
            nMotoristas += 1
    if nMotoristas == 0:
        print("Não existe motorista vinculado ao veículo.\n")
        return
    else:
        print("=-=-=-Veículos Sem Motorista-=-=-=")
        print(f'{" " * 9}{"Placa":<12}{"Tipo":8}')
        for veiculo in get_bv().values():
            if veiculo.get("motorista") is None:
                print(f'{" " * 9}{veiculo.get("placa"):<12}{veiculo.get("tipo"):8}')
        print('=-' * 17)
        print()


def removerVeiculo():
    ler()
    print("=-=-=-Remover Veículo-=-=-=")
    if len(get_bv()) == 0:
        print("Ainda não existe nenhum veículo cadastrado.\n")
        return
    else:
        placa = str(input("Digite a placa do veículo que deseja remover do cadastro: ")).strip().upper()
        cadastrado = False
        for veiculo in get_bv():
            if placa == veiculo:
                cadastrado = True
        if cadastrado:
            for veiculo in get_bv().values():
                if placa == veiculo["placa"]:
                    if veiculo.get('motorista') is not None:
                        print('=-' * 15)
                        print(f'{"Placa":<12}{"Tipo":8}{"Motorista"}')
                        print(f'{veiculo.get("placa"):<12}{veiculo.get("tipo"):8}{veiculo.get("motorista")}')
                        print('=-' * 15)
                    else:
                        print('=-' * 15)
                        print(f'{"Placa":<12}{"Tipo"}')
                        print(f'{veiculo.get("placa"):<12}{veiculo.get("tipo")}')
                        print('=-' * 15)
                    opcao = str(input("Você tem certeza [S/N]? ")).strip().upper()
                    while opcao not in "SN":
                        opcao = str(input("Opção incorreta. Digite somente s - Sim ou n - Não: ")).strip().upper()
                    print()
                    if opcao == "N":
                        return
                    else:
                        del get_bv()[placa]
                        escrever()
                        print("Veículo removido com sucesso!")
                        return
        else:
            print("Este veículo ainda não está cadastrado.")
            if not continuar():
                return
            else:
                removerVeiculo()

