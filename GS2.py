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
def adicionarCarro(marca,ano,modelo,qntdPassageiros,placa,tipo,usuario):
    listaCarro["marca"].append(marca)
    listaCarro["ano"].append(ano)
    listaCarro["modelo"].append(modelo)
    listaCarro["qntdPassageiros"].append(qntdPassageiros)
    listaCarro["placa"].append(placa)
    listaCarro["tipo"].append(tipo)
    listaCarro["id"].append(id)
    listaCarro["dono"].append(usuario)    
listaUsuarios = {"usuario": ["empresa"], "usuarioSenha" : ["empresao"]}
listaEmpresa = {"empresa" : ["usuario"], "empresaSenha" : ["usuarao"]}
listaCarro = {"marca" : [], "placa": [], "modelo": [], "ano": [], "tipo": [], "qntdPassageiros": [], "id" : [], "dono": []}
usuario = ""
pula = ""
id = 0

while(True):
    if(verificarLogin(usuario)):
        try:
            if usuario in listaEmpresa["empresa"]:
                opcaoLogado()
                opcao = int(input(f"1-adicionar Carro\n2-Mostrar seus carros\n3-LogOut\n: "))
                if opcao == 1:
                    try:
                        marca = input("qual a marca?")
                        ano = int(input("qual o ano?"))
                        modelo = input("qual o modelo?")
                        qntdPassageiros = int(input("quantas pessoas cabem?"))
                        placa = input("qual a placa?")
                        tipo = input("qual o tipo do carro(ex: SUV)?")
                        confirmarInfos= input(f"{pula:_^30}\nessas são as informações do carros?\nmarca: {marca}, ano: {ano}, modelo : {modelo}, quantidade de passageiros: {qntdPassageiros}, placa: {placa}, tipo: {tipo}\nse sim digite 's', se não, insira qualquer outra tecla").lower()
                        if(confirmarInfos == 's'):
                            adicionarCarro(marca,ano,modelo,qntdPassageiros,placa,tipo,id,usuario)
                            id =+1
                            print(f"adicionado com sucesso")
                    except:
                        print("As informações não foram colocadas de maneira correta.")
                elif opcao == 2:
                    for i in range(listaCarro["dono"]):
                        if listaCarro["dono"][i] == usuario:
                            print(f'{listaCarro["id"]} | {listaCarro["modelo"][i]} | {listaCarro["modelo"][i]}')
                elif opcao == 3:
                    usuario = ""
                    continue
            elif usuario in listaUsuarios["usuario"]:
                opcaoLogado()
                opcao = int(input(f"1-ver carros disponiveis\n3-LogOut\n:"))
                if opcao ==1:
                    print(listaCarro)
                elif opcao == 3: 
                    usuario = ""
                    continue
        except:
            print(f"{pula:_^30}\nVocê inseriu algo estranho na opção, favor selecionar uma das opções oferecidas")
    else:
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
    