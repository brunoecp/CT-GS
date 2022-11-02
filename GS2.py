def verificarLogin(usuario):
    if usuario not in listaEmpresa["empresa"] and usuario not in listaUsuarios["usuario"]:
        return False
    return True
def opcaoLogado():
    print(f"{pula:_^30}\nOlá {usuario}\nSelecione uma das opções\n")
def cadastrar(tipousuario, nome, senha):
    if tipousuario == "empresa":
        listaEmpresa["empresa"].append(nome)
        listaEmpresa["empresaSenha"].append(senha)
    elif tipousuario == "usuario":
        listaUsuarios["usuario"].append(nome)
        listaUsuarios["usuarioSenha"].append(senha)
def erroOpcao():
    print("Você inseriu algo estranho na opção, favor selecionar uma das opções oferecidas")
def excluirCarro(id):
    indice = 0
    for i in range(len(listaCarro["id"])):
        if id == listaCarro['id'][i]:
            indice = i
    for i in listaCarro:
        listaCarro[i].pop(indice)
def logar(tipo, nome, senha):
    if tipo == 'empresa':
        if(verificarLogin):
            for i in range(len(listaEmpresa["empresa"])):
                if nome == listaEmpresa["empresa"][i]:
                    indice = i
            if senha == listaEmpresa["empresaSenha"][indice]:
                print("Login efetuado com sucesso")
                return True 
            else:
                print("Senha incorreta")
        else:
            print("Usuario não encontrado")   
    elif tipo == 'usuario':
        if(verificarLogin):
            for i in range(len(listaUsuarios["usuario"])):
                if nome == listaUsuarios["usuario"][i]:
                    indice = i
            if senha == listaUsuarios["usuarioSenha"][indice]:
                print("Login efetuado com sucesso")
                return True 
            else:
                print("Senha incorreta")
        else:
            print("Usuario não encontrado")      

def excessederOpcao():
    print("Favor selecionar uma das opções oferecidas")
def contratarCarro(id):
    indice = 0
    for i in range(len(listaCarro["id"])):
        if id == listaCarro['id'][i]:
            indice = i
    listaCarro["alugado"][indice] = True
def adicionarCarro(marca,ano,modelo,qntdPassageiros,placa,tipo,id,usuario):
    listaCarro["marca"].append(marca)
    listaCarro["ano"].append(ano)
    listaCarro["modelo"].append(modelo)
    listaCarro["qntdPassageiros"].append(qntdPassageiros)
    listaCarro["placa"].append(placa)
    listaCarro["tipo"].append(tipo)
    listaCarro["id"].append(id)
    listaCarro["dono"].append(usuario)
    listaCarro["alugado"].append(False)    
listaUsuarios = {"usuario": ["empresa"], "usuarioSenha" : ["empresao"]}
listaEmpresa = {"empresa" : ["usuario"], "empresaSenha" : ["usuarao"]}
listaCarro = {"id" : [],"marca" : [], "placa": [], "modelo": [], "ano": [], "tipo": [], "qntdPassageiros": [] , "dono": [], "alugado": []}
usuario = ""
pula = ""
id = 0

while(True):
    if(verificarLogin(usuario)):
        try:
            if usuario in listaEmpresa["empresa"]:
                opcaoLogado()
                opcao = int(input(f"1-adicionar Carro\n2-Mostrar seus carros\n3-Apagar Carro\n4-LogOut\n: "))
                if opcao == 1:
                    try:
                        marca = input("qual a marca?: ")
                        ano = int(input("qual o ano?: "))
                        modelo = input("qual o modelo?: ")
                        qntdPassageiros = int(input("quantas pessoas cabem?: "))
                        placa = input("qual a placa?: ")
                        tipo = input("qual o tipo do carro(ex: SUV)?: ")
                        confirmarInfos= input(f"{pula:_^30}\nessas são as informações do carros?\nmarca: {marca}, ano: {ano}, modelo : {modelo}, quantidade de passageiros: {qntdPassageiros}, placa: {placa}, tipo: {tipo}\nse sim digite 's', se não, insira qualquer outra tecla").lower()
                        if(confirmarInfos == 's'):
                            adicionarCarro(marca,ano,modelo,qntdPassageiros,placa,tipo,id,usuario)
                            id =+1
                            print(f"adicionado com sucesso")
                    except:
                        print("As informações não foram colocadas de maneira correta.")
                elif opcao == 2:
                    for i in range(len(listaCarro["dono"])):
                        if listaCarro["dono"][i] == usuario:
                            print(f'{listaCarro["id"][i]} | {listaCarro["marca"][i]} | {listaCarro["modelo"][i]}')
                elif opcao == 3:
                    excluir = int(input("Qual o ID do carro que você quer excluir?(caso não saiba, saia digitando '-1', e veja na opcao 2)\n: "))
                    if excluir == -1:
                        continue
                    elif excluir in listaCarro["id"]:
                        excluirCarro(excluir)
                    else: 
                        print(f"{pula:_^30}\nid não encontrado") 
                elif opcao == 4:
                    usuario = ""
                    continue
                else:
                    excessederOpcao()
            elif usuario in listaUsuarios["usuario"]:
                opcaoLogado()
                opcao = int(input(f"1-ver carros disponiveis\n2-Contratar Carro\n3-LogOut\n:"))
                if opcao ==1:
                    for i in range(len(listaCarro)):
                        if listaCarro["alugado"][i] is False:
                            print(f"carro {listaCarro['id'][i] + 1}")
                            for j in listaCarro:
                                print(f'{pula:_^30}\n{j} : {listaCarro[j][i]}')
                elif opcao == 2:
                    contratar = int(input("Qual o id do carro que deseja contratar?(caso não saiba digite -1 e veja na primeira opção)"))
                    if contratar == -1:
                        continue
                    elif contratar in listaCarro["id"]:
                        contratarCarro(contratar)
                    else: 
                        print(f"{pula:_^30}\nid não encontrado") 
                elif opcao == 3: 
                    usuario = ""
                    continue
                else:
                    excessederOpcao()
        except:
            print(f"{pula:_^30}\nVocê inseriu algo estranho na opção, favor selecionar uma das opções oferecidas")
    else:
        try:
            print(usuario)
            print(f"{pula:_^30}\nVocê não está logado, deseja: ")
            opcao = int(input("1-Cadastrar-se\n2-logar-me\n3-sair\n : "))
            if opcao == 1:
                try:
                    opcao2 = int(input(f"{pula:_^30}\n1-sou da empresa\n2-sou um usuario\n3-voltar\n: "))
                    if opcao2 == 1:
                        nome = input(f"{pula:_^30}\nInsira seu nome: ")
                        senha = input("Digite uma senha:")
                        if(verificarLogin(nome)):
                            print(f"{pula:_^30}\nusuario já existente")
                        else:    
                            cadastrar("empresa",nome,senha)
                            usuario = nome
                    elif opcao2 == 2:
                        nome = input(f"{pula:_^30}\nInsira seu nome: ")
                        senha = input("Digite uma senha: ")
                        if(verificarLogin(nome)):
                            print(f"{pula:_^30}\nusuario já existente")
                        else:    
                            cadastrar("usuario",nome,senha)
                            usuario = nome
                    elif opcao2 == 3:
                        continue
                    else:
                        excessederOpcao()
                except:
                    erroOpcao()
            elif opcao == 2:
                    opcao2 = int(input(f"{pula:_^30}\n1-sou da empresa\n2-sou um usuario\n3-voltar\n: "))
                    if opcao2 == 1:
                        nome= input(f"{pula:_^30}\nInsira seu nome: ")
                        senha = input("Digite sua senha: ")
                        if(logar("empresa",nome,senha)):
                            usuario = nome
                    elif opcao2 == 2:
                        nome= input(f"{pula:_^30}\nInsira seu nome: ")
                        senha = input("Digite sua senha: ")
                        if(logar("usuario",nome,senha)):
                            usuario = nome
                    elif opcao2 == 3:
                        continue
                    else:
                        excessederOpcao()
            elif opcao == 3:
                print(f"{pula:_^30}\nAdeus ><")
                break
            else:
                excessederOpcao()
        except:
            erroOpcao()
    