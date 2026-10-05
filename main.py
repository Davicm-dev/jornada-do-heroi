def casa_do_heroi():
    print("você acorda com uma notícia entregue por um soldado ferido do castelo")
    print("o castelo foi atacado!")
    print("1 - salvar o dia!")
    print("2 - voltar a dormir")
    print("-" * 50)

    opcao = int(input("o que você faz?: "))

    if opcao == 1:
        print("vamos salvar o dia!")
        print("-" * 50)
        return True
        
    elif opcao == 2:
        print("estou cansado, resolvo amanhã!")
        exit()

    else:
        print("você tem que escolher alguma coisa!")
        return False


def caverna(tem_ovo):
    print("-" * 50)
    print("você encontrou uma caverna!")
    print("na caverna tem um dragão!")
    print("1 - enfrentar o dragão")
    print("2 - pedir um ovo com gentileza")
    print("3 - voltar")
    print("-" * 50)

    opcao = int(input("escolha: "))

    if opcao == 1:
        print("o dragão te devorou!")
        print("você morreu!")
        return None

    elif opcao == 2:
        print("o dragão te deu o ovo!")
        print("-" * 50)
        tem_ovo = True

    elif opcao == 3:
        print("você voltou para a floresta")
        print("-" * 50)

    return tem_ovo


# INVENTÁRIO
tem_ovo = False
# INVENTÁRIO


def ponte_em_um_penhasco(tem_ovo):
    print("-" * 50)
    print("você encontrou uma ponte com um goblin protegendo-a!")
    print("ele pede um ovo de dragão para permitir a passagem!")
    print("1 - entregar o ovo")
    print("2 - voltar")
    print("-" * 50)

    opcao = int(input("escolha: "))

    if opcao == 1:
        if tem_ovo:
            print("você entregou o ovo de dragão para o goblin!")
            return True, tem_ovo
        else:
            print("você não tem um ovo de dragão!")
            return False, tem_ovo

    elif opcao == 2:
        print("você voltou!")
        print("-" * 50)
        return False, tem_ovo

    else:
        print("opção não encontrada!")
        return False, tem_ovo


def depois_da_ponte():
    print("-" * 50)
    print("você passa pela ponte!")
    print("e encontra um acampamento de goblins!")


def acampamento_goblim():
    print("-" * 50)
    print("três goblins do acampamento passam por você segurando sacolas de dinheiro")
    print("1 - passa direto, ignorando-os")
    print("2 - pede dinheiro aos goblins")
    print("3 - espanca um dos goblins e rouba a adaga dele")
    print("-" * 50)

    opcao = int(input("o que você vai fazer?: "))

    if opcao == 1:
        print("você continua seu caminho!")
        print("-" * 50)
        return True

    elif opcao == 2:
        print("os goblins te derrotaram!")
        return False

    elif opcao == 3:
        print("você nocauteia um goblin e pega a adaga dele")
        print("-" * 50)

        print("os dois goblins restantes puxam suas adagas")
        print("1 - você sai correndo com sua arma nova")
        print("2 - você luta contra os goblins")

        opcao = int(input("o que você faz?: "))
        print("-" * 50)

        if opcao == 1:
            print("você corre para o castelo com uma arma nova!")
            print("-" * 50)
            return True

        elif opcao == 2:
            print("você perde a batalha!")
            print("você morreu!")
            return False

        else:
            print("opção não encontrada!")
            return False

    else:
        print("opção não encontrada!")
        return False


def castelo():
    print("ao chegar ao castelo, você vê guardas feridos!")

    print("1 - entrar no castelo")
    print("2 - ajudar os guardas primeiro")

    opcao = int(input("o que você faz?: "))
    print("-" * 50)

    if opcao == 1:
        print("você deixa os guardas de lado para ver o Rei primeiro!")
        print("-" * 50)

    elif opcao == 2:
        print("você ajuda os guardas e entra no castelo")
        print("-" * 50)

    else:
        print("opção não encontrada!")
        return

    print("ao entrar na sala do trono, o Rei te dá uma missão")
    print("a missão é salvar a princesa no reino dos Betas")
    print("-" * 50)


def a_aventura_começa():
    print("com a missão dada")
    print("-" * 50)
    print("1 - salvar a princesa")
    print("2 - ir para casa dormir porque o caminho para o castelo foi cansativo")

    opcao = int(input("o que você faz: "))
    print("-" * 50)

    if opcao == 1:
        print("é hora de salvar a princesa")

    elif opcao == 2:
        print("tô cansado, vou para casa dormir")
        exit()


def a_cruzada_da_indecisão():
    print("com a missão dada, você sai do castelo e vê a cruzada da indecisão")
    print("1 - Um caminho que se diz menor e menos perigoso")
    print("2 - Um caminho que se diz maior e mais perigoso")

    opcao = int(input("qual caminho você escolhe: "))
    print("-" * 50)

    if opcao == 1:
        caminho_que_se_diz_menor()

    elif opcao == 2:
        caminho_que_se_diz_maior()

    else:
        print("opção não encontrada!")


def caminho_que_se_diz_menor():
    print("-" * 50)
    print("você escolheu o caminho menor e menos perigoso!")
    print("de repente, você encontra uma ponte quebrada.")
    print("você precisa encontrar uma maneira de atravessar.")
    print("1 - procurar outro caminho")
    print("2 - tentar consertar a ponte")

    opcao = int(input("o que você faz?: "))

    if opcao == 1:
        print("você encontra uma passagem pela floresta.")

    elif opcao == 2:
        print("você consegue atravessar a ponte!")

    else:
        print("opção não encontrada!")


def caminho_que_se_diz_maior():
    print("-" * 50)
    print("você escolheu o caminho maior e mais perigoso!")
    print("depois de horas caminhando, você encontra uma pequena vila.")
    print("os moradores parecem assustados.")
    print("-" * 50)

    print("um morador se aproxima e pergunta:")
    print('"você está indo para o Reino dos Betas?"')
    print("1 - perguntar o que está acontecendo")
    print("2 - ignorar e continuar")

    opcao = int(input("o que você faz?: "))
    print("-" * 50)

    if opcao == 1:
        print("o morador conta que várias pessoas desapareceram na estrada.")
        print("ele diz que ninguém sabe o que está causando os desaparecimentos.")
        print("antes de sair, ele entrega um mapa antigo.")
        print("-" * 50)

        print("você segue pelo caminho indicado no mapa.")
        print("depois de algum tempo, encontra uma floresta escura.")
        print("1 - entrar na floresta")
        print("2 - procurar outro caminho")

        opcao = int(input("qual caminho você escolhe?: "))
        print("-" * 50)

        if opcao == 1:
            print("você entra na floresta.")
            print("depois de alguns minutos, encontra uma cabana abandonada.")
            print("-" * 50)

            print("dentro da cabana, você encontra uma carta misteriosa.")
            print("a carta fala sobre um antigo inimigo do Reino dos Betas.")
            print("você guarda a carta e continua sua jornada.")
            print("-" * 50)

            print("ao sair da floresta, você encontra uma estrada de pedra.")
            print("essa estrada parece levar até o Reino dos Betas.")
            print("-" * 50)

        elif opcao == 2:
            print("você decide não entrar na floresta.")
            print("depois de caminhar bastante, encontra uma estrada antiga.")
            print("você segue por ela durante o resto do dia.")
            print("-" * 50)

        else:
            print("opção não encontrada!")
            return

    elif opcao == 2:
        print("você decide continuar sozinho.")
        print("a estrada fica cada vez mais deserta.")
        print("de repente, você encontra uma carroça abandonada.")
        print("-" * 50)

        print("dentro dela existem algumas provisões e uma espada velha.")
        print("você pega as provisões e continua sua jornada.")
        print("-" * 50)

        print("depois de algumas horas, encontra uma estrada de pedra.")
        print("ao longe, consegue ver as muralhas do Reino dos Betas.")
        print("-" * 50)

    else:
        print("opção não encontrada!")
        return

    print("depois de uma longa jornada...")
    print("você finalmente chega diante dos portões do Reino dos Betas!")
    print("-" * 50)

# TELA INICIAL
while True:

    letreiro = """

     _____    _____    _____
    |  _  \\  |  _  \\  |     \\
    | |_)  | | |_)  | |  ___/
    |  _  /  |  ___/  | |  __
    | | \\ \\  | |      | | |  |
    | |  \\ | | |      | |_|  |
    |_|   \\| |_|      |______|

    """

    print(letreiro)

    print("-" * 50)
    print("[1] para entrar/esquerda ou [2] sair/direita")
    print("bem-vindo ao RPG")
    print("1 - entrar")
    print("2 - sair")
    print("-" * 50)

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("carregando...")
        print("-" * 50)
        break

    elif opcao == 2:
        print("Obrigado por jogar!")
        break

    else:
        print("opção não encontrada!")
        continue


# COMEÇA A AVENTURA
if casa_do_heroi():

    while True:

        print("você está na floresta")
        print("existem 2 caminhos:")
        print("1 - para a esquerda")
        print("2 - para a direita")

        caminho = int(input("escolha: "))

        if caminho == 1:

            passou, tem_ovo = ponte_em_um_penhasco(tem_ovo)

            if passou:
                depois_da_ponte()

                sobreviveu = acampamento_goblim()

                if not sobreviveu:
                    print("-" * 50)
                    print("VOCÊ MORREU!")
                    print("voltando para a tela inicial...")
                    print("-" * 50)
                    break

                castelo()

                a_aventura_começa()

                a_cruzada_da_indecisão()

        elif caminho == 2:

            tem_ovo = caverna(tem_ovo)

            if tem_ovo is None:
                print("-" * 50)
                print("VOCÊ MORREU!")
                print("voltando para a tela inicial...")
                print("-" * 50)
                break

        else:
            print("não tem esse caminho!")