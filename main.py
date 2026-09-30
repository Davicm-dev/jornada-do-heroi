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
    print("3 - espancar um dos goblins e rouba a adaga dele")
    print("-" * 50)
    
    opcao = int(input("o que você vai fazer?: "))

    if opcao == 1:
        print("você continua seu caminho!")
        print("-" * 50)
        return True
    
    elif opcao == 2:
        print("os goblins te derrotaram!")
        print("você morreu!")
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
    print("ao chegar ao castelo, você vê uma explosão na porta")
    
    print("1 - para entrar")

    opcao = int(input("o que você faz?: "))
    print("-" * 50)

    if opcao == 1:
        print("você descobre que o rei só tinha colocado um garfo no micro-ondas, mas estão todos bem")
        return None

    else:
        print("opção não encontrada!")

#TELA INICIAL
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
