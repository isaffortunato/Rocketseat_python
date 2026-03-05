def adicionar_contato(nome_contato, telefone, email, favorito):
    agenda = {"contato": nome_contato, "telefone": telefone, "email": email, "favorito": favorito}
    contatos.append(agenda)
    print(f"O contato {nome_contato} foi adicionado com sucesso!")
    return

def ver_agenda(contatos):
    print("\nLista de Contatos:")
    for indice, agenda in enumerate(contatos, start=1):
        status = "★" if agenda["favorito"] == True else " "
        nome_contato = agenda["contato"]
        telefone = agenda["telefone"]
        email = agenda["email"]
        print(f"{indice}. {status} {nome_contato}, {telefone}, {email}")
    return


def atualizar_contato(contatos, campo, campo_contato):
    for agenda in contatos:
        if agenda["contato"] == campo_contato:
            if campo == "contato":
                novo_nome = input(f"Digite o novo nome para o contato {campo_contato}: ")
                agenda["contato"] = novo_nome
            elif campo == "telefone":
                novo_telefone = input(f"Digite o novo telefone para o contato {campo_contato}: ")
                agenda["telefone"] = novo_telefone
                print(agenda["telefone"])
            elif campo == "email":
                novo_email = input(f"Digite o novo email para o contato {campo_contato}: ")
                agenda["email"] = novo_email
            else:
                print("Campo inválido")
    return

def contato_favorito(contatos, campo_contato):
    for agenda in contatos:
        if agenda["contato"] == campo_contato:
            agenda["favorito"] = True
        print(f"{nome_contato} marcado como favorito.")
        return
    print("Contato não encontrado.")


def desmarcar_favorito(contatos, campo_contato):
    for agenda in contatos:
        if agenda["contato"] == campo_contato:
            agenda["favorito"] = False
            print(f"{nome_contato} desmarcado como favorito.")
            return
    print("Contato não encontrado.")


def ver_favoritos(contatos):
    print("\nLista de Contatos Favoritos:")
    for indice, agenda in enumerate(contatos, start=1):
        if agenda["favorito"] == True:
            status = "★"
            nome_contato = agenda["contato"]
            telefone = agenda["telefone"]
            email = agenda["email"]
            print(f"{indice}. {status} {nome_contato}, {telefone}, {email}")
    return

def deletar_contato(contatos, campo_contato):
    for agenda in contatos:
        if agenda["contato"] == campo_contato:
            contatos.remove(agenda)
    print(f"O contato {nome_contato} foi deletado.")
    return

    
contatos = []
while True:
    print("\nLista de Contatos:")
    print("1. Adicionar contato")
    print("2. Ver minha agenda")
    print("3. Editar contato")
    print("4. Marcar contato como favorito")
    print("5. Desmarcar contato como favorito")
    print("6. Ver contatos favoritos")
    print("7. Deletar contato")
    print("8. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_contato = input("Digite o nome do contato que deseja adicionar: ")
        telefone = input("Digite o número do contato que deseja adicionar: ") #adicionar validação p número
        email = input("Digite o email do contato que deseja adicionar: ")
        favorito = input("Deseja adicionar à lista de favoritos? (s/n) ").lower() == "s"
        '''for agenda in contatos:
            if favorito == "s":
                agenda["favorito"] = True
            else:
                agenda["favorito"] = False'''
        adicionar_contato(nome_contato, telefone, email, favorito)

    elif escolha == "2":
        ver_agenda(contatos)

    elif escolha == "3":
        ver_agenda(contatos)
        campo_contato = input("Digite o nome do contato que deseja atualizar: ")
        campo = input("Qual campo deseja atualizar? (contato, telefone, email): ")
        atualizar_contato(contatos, campo, campo_contato)
        print("\nContato atualizado com sucesso!")

    elif escolha == "4":
        ver_agenda(contatos)
        campo_contato = input("Digite o nome do contato que deseja favoritar: ")
        contato_favorito(contatos, campo_contato)

    elif escolha == "5":
        ver_agenda(contatos)
        campo_contato = input("Digite o nome do contato que deseja desfavoritar: ")
        desmarcar_favorito(contatos, campo_contato)

    elif escolha == "6":
        ver_favoritos(contatos)

    
    elif escolha == "7":
        ver_agenda(contatos)
        campo_contato = input("Digite o nome do contato que deseja deletar: ")
        deletar_contato(contatos, campo_contato)
        
                
    elif escolha == "8":
        break
