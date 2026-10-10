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
    while True:
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
            print("você conversa com o dragão e pede um ovo.")
            print("o dragão aceita o pedido e te entrega um ovo.")
            print("você guarda o ovo e volta para a floresta.")
            print("-" * 50)
            tem_ovo = True
            return tem_ovo
        elif opcao == 3:
            print("você decide não mexer com o dragão.")
            print("você volta para a floresta e procura outro caminho.")
            print("-" * 50)
            return tem_ovo
        else:
            print("opção não encontrada!")
            print("escolha novamente!")

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
            print("você entrega o ovo de dragão para o goblin!")
            print("o goblin abre a passagem e deixa você atravessar.")
            print("você percebe que a ponte leva para a estrada do castelo.")
            return True, False
        else:
            print("você não tem um ovo de dragão!")
            print("o goblin bloqueia a passagem.")
            print("você terá que encontrar outra maneira de conseguir um ovo.")
            return False, tem_ovo
    elif opcao == 2:
        print("você decide voltar e procurar outra maneira de atravessar.")
        print("-" * 50)
        return False, tem_ovo
    else:
        print("opção não encontrada!")
        return False, tem_ovo

def depois_da_ponte():
    print("-" * 50)
    print("você passa pela ponte!")
    print("e encontra um acampamento de goblins!")
    print("o acampamento parece estar no caminho para o castelo.")

def acampamento_goblim():
    print("-" * 50)
    print("três goblins do acampamento passam por você segurando sacolas de dinheiro")
    print("1 - passa direto, ignorando-os")
    print("2 - pede dinheiro aos goblins")
    print("3 - espanca um dos goblins e rouba a adaga dele")
    print("-" * 50)
    opcao = int(input("o que você vai fazer?: "))
    if opcao == 1:
        print("você decide não arrumar confusão.")
        print("os goblins deixam você passar e você segue em direção ao castelo.")
        print("-" * 50)
        return True
    elif opcao == 2:
        print("os goblins não gostam do seu pedido.")
        print("eles cercam você e você não consegue escapar.")
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
            print("os goblins desistem de perseguir você.")
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
        print("um guarda aponta para a sala do trono e diz que o Rei precisa de ajuda.")
        print("você entra no castelo e vai falar com o Rei.")
        print("-" * 50)
    elif opcao == 2:
        print("você ajuda os guardas e descobre que eles foram atacados por soldados desconhecidos.")
        print("um dos guardas agradece e indica o caminho para a sala do trono.")
        print("você entra no castelo.")
        print("-" * 50)
    else:
        print("opção não encontrada!")
        return False
    print("ao entrar na sala do trono, o Rei te dá uma missão")
    print("a missão é salvar a princesa no reino dos Betas")
    print("o Rei explica que a princesa desapareceu durante o ataque.")
    print("-" * 50)
    return True

def a_aventura_começa():
    print("com a missão dada")
    print("-" * 50)
    print("1 - salvar a princesa")
    print("2 - ir para casa dormir porque o caminho para o castelo foi cansativo")
    opcao = int(input("o que você faz: "))
    print("-" * 50)
    if opcao == 1:
        print("é hora de salvar a princesa")
        print("você pega seu equipamento e se prepara para sair do castelo.")
        print("o Rei entrega uma pequena insígnia para provar que você está em uma missão oficial.")
        print("-" * 50)
        return True
    elif opcao == 2:
        print("tô cansado, vou para casa dormir")
        exit()
    else:
        print("opção não encontrada!")
        return False

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

def chegar_ao_reino_dos_betas():
    print("-" * 50)
    print("você finalmente chega ao Reino dos Betas.")
    print("as muralhas são enormes e os portões estão parcialmente destruídos.")
    print("alguns soldados estão tentando proteger a entrada.")
    print("-" * 50)
    print("um soldado se aproxima e pergunta:")
    print('"você veio ajudar o reino?"')
    print("1 - sim, vim salvar a princesa")
    print("2 - não, só estou de passagem")
    opcao = int(input("o que você responde?: "))
    print("-" * 50)
    if opcao == 1:
        print("o soldado fica aliviado.")
        print('"então você chegou na hora certa!"')
        print("ele conta que a princesa foi levada para uma torre abandonada.")
        print("o soldado entrega uma chave para você.")
        print("-" * 50)
        print("você entra no reino segurando a chave.")
        print("agora precisa encontrar a torre da princesa.")
        return True
    elif opcao == 2:
        print("o soldado desconfia de você.")
        print('"então explique o que está fazendo aqui!"')
        print("você conta sobre sua missão.")
        print("o soldado percebe que você está dizendo a verdade.")
        print("ele deixa você entrar, mas avisa para tomar cuidado com os traidores.")
        print("-" * 50)
        return True
    else:
        print("opção não encontrada!")
        return False

def entrar_no_reino():
    print("-" * 50)
    print("você vê dois caminhos dentro do reino:")
    print("1 - seguir pela praça")
    print("2 - passar pelo mercado")
    print("-" * 50)
    opcao = int(input("qual caminho você escolhe?: "))
    print("-" * 50)
    if opcao == 1:
        print("você atravessa a praça.")
        print("alguns moradores apontam para uma torre no fundo do castelo.")
        print("um menino avisa que a entrada principal está sendo vigiada.")
        print("você decide entrar por uma passagem lateral.")
        print("-" * 50)
        entrada_do_castelo()
    elif opcao == 2:
        print("você passa pelo mercado abandonado.")
        print("atrás de uma barraca, encontra uma passagem escondida.")
        print("a passagem leva diretamente para dentro do castelo.")
        print("antes de entrar, você encontra uma marca estranha na parede.")
        print("parece ser o símbolo de alguém que está ajudando os inimigos.")
        print("você guarda essa informação e continua.")
        print("-" * 50)
        entrada_do_castelo()
    else:
        print("opção não encontrada!")

def entrada_do_castelo():
    print("você chega a uma parte mais profunda do castelo.")
    print("existem duas maneiras de continuar:")
    print("1 - seguir pelas escadas principais")
    print("2 - usar uma passagem lateral")
    print("-" * 50)
    opcao = int(input("qual caminho você escolhe?: "))
    print("-" * 50)
    if opcao == 1:
        print("você sobe pelas escadas principais.")
        print("dois guardas aparecem e perguntam quem você é.")
        print("você mostra a insígnia entregue pelo Rei.")
        print("os guardas deixam você passar.")
        print("você chega à sala das três portas.")
        as_tres_portas()
    elif opcao == 2:
        print("você entra pela passagem lateral.")
        print("o caminho é apertado e escuro.")
        print("depois de alguns minutos, você encontra uma porta escondida.")
        print("atrás dela existe uma sala que leva à torre.")
        print("você abre a porta e chega à sala das três portas.")
        as_tres_portas()
    else:
        print("opção não encontrada!")

def caminho_que_se_diz_menor():
    print("-" * 50)
    print("você escolheu o caminho menor e menos perigoso!")
    print("depois de algum tempo caminhando, você encontra uma ponte quebrada.")
    print("parece que será impossível atravessar.")
    print("-" * 50)
    print("1 - procurar outro caminho")
    print("2 - tentar consertar a ponte")
    opcao = int(input("o que você faz?: "))
    print("-" * 50)
    if opcao == 1:
        print("você decide procurar outro caminho.")
        print("depois de alguns minutos, encontra uma trilha escondida.")
        print("-" * 50)
        print("a trilha leva até uma pequena casa.")
        print("na frente da casa há um velho sentado.")
        print("1 - falar com o velho")
        print("2 - continuar pela trilha")
        opcao = int(input("o que você faz?: "))
        print("-" * 50)
        if opcao == 1:
            print("o velho pergunta para onde você está indo.")
            print("você explica que precisa chegar ao Reino dos Betas.")
            print('o velho diz: "eu conheço uma estrada segura até lá."')
            print("ele entrega uma pequena bússola para você.")
            print("-" * 50)
            print("você agradece ao velho e segue a direção indicada pela bússola.")
        elif opcao == 2:
            print("você ignora a casa e continua pela trilha.")
            print("a trilha fica mais difícil, mas você encontra marcas de rodas no chão.")
            print("seguindo essas marcas, você chega a uma estrada.")
            print("uma placa indica que o Reino dos Betas está naquela direção.")
            print("-" * 50)
        else:
            print("opção não encontrada!")
            return
    elif opcao == 2:
        print("você decide tentar consertar a ponte.")
        print("depois de algum esforço, consegue criar uma passagem.")
        print("você atravessa a ponte com cuidado.")
        print("-" * 50)
        print("do outro lado, encontra uma placa:")
        print('"Reino dos Betas →"')
        print("você segue pela estrada indicada.")
        print("-" * 50)
    else:
        print("opção não encontrada!")
        return
    if chegar_ao_reino_dos_betas():
        entrar_no_reino()

def as_tres_portas():
    print("-" * 50)
    print("você entra em uma parte mais profunda do castelo.")
    print("na sua frente existem três portas.")
    print("você precisa descobrir qual delas leva até a princesa.")
    print("-" * 50)
    print("1 - porta de madeira")
    print("2 - porta de ferro")
    print("3 - porta dourada")
    print("-" * 50)
    opcao = int(input("qual porta você escolhe?: "))
    print("-" * 50)
    if opcao == 1:
        print("você abre a porta de madeira.")
        print("a sala está vazia.")
        print("você encontra uma passagem secreta.")
        print("na parede existe uma mensagem: 'a torre fica acima de você'.")
        print("você sobe pela passagem e chega até a sala da princesa.")
        print("-" * 50)
        a_princesa_revela_a_verdade()
    elif opcao == 2:
        print("você abre a porta de ferro.")
        print("dois guardas aparecem e bloqueiam sua passagem.")
        print("1 - explicar que veio salvar a princesa")
        print("2 - tentar passar escondido")
        print("-" * 50)
        opcao = int(input("o que você faz?: "))
        print("-" * 50)
        if opcao == 1:
            print("você explica sua missão aos guardas.")
            print("os guardas acreditam em você.")
            print("um deles revela que recebeu ordens para esconder a princesa.")
            print("ele aponta para uma escada que leva à torre.")
            print("você sobe as escadas e encontra a princesa.")
            print("-" * 50)
            a_princesa_revela_a_verdade()
        elif opcao == 2:
            print("você tenta passar escondido.")
            print("um dos guardas percebe você.")
            print("você corre por um corredor enquanto os guardas o perseguem.")
            print("no final do corredor, encontra uma passagem secreta.")
            print("você entra nela e os guardas perdem seu rastro.")
            print("a passagem leva até a torre da princesa.")
            print("-" * 50)
            a_princesa_revela_a_verdade()
        else:
            print("opção não encontrada!")
    elif opcao == 3:
        print("você abre a porta dourada.")
        print("dentro da sala, você encontra a princesa!")
        print('"finalmente alguém veio me salvar!"')
        print("-" * 50)
        a_princesa_revela_a_verdade()
    else:
        print("opção não encontrada!")

def a_princesa_revela_a_verdade():
    print("-" * 50)
    print("a princesa parece preocupada.")
    print('"precisamos sair daqui agora!"')
    print("-" * 50)
    print("1 - perguntar o que está acontecendo")
    print("2 - sair imediatamente com a princesa")
    opcao = int(input("o que você faz?: "))
    print("-" * 50)
    if opcao == 1:
        print("a princesa respira fundo e começa a explicar.")
        print('"eu não fui sequestrada por um inimigo qualquer..."')
        print('"alguém do próprio reino está ajudando eles."')
        print("ela conta que o traidor abriu os portões durante o ataque.")
        print("-" * 50)
        print("de repente, vocês escutam passos vindo pelo corredor.")
        print("alguém está se aproximando!")
        print("1 - se esconder")
        print("2 - enfrentar quem está vindo")
        opcao = int(input("o que você faz?: "))
        print("-" * 50)
        if opcao == 1:
            print("você e a princesa se escondem atrás de algumas caixas.")
            print("um homem passa pelo corredor usando a armadura dos guardas do reino.")
            print("ele segura uma carta com o mesmo símbolo que você viu no mercado.")
            print("agora você tem uma pista sobre o traidor.")
            print("quando ele vai embora, vocês saem do esconderijo.")
            print("a princesa diz que o símbolo pertence ao conselheiro do Rei.")
        elif opcao == 2:
            print("você prepara sua arma e espera o inimigo aparecer.")
            print("um guarda do reino entra na sala.")
            print("ele percebe que a princesa está com você e tenta impedir a fuga.")
            print("você consegue ganhar tempo e a princesa encontra uma passagem escondida.")
            print("antes de fugir, o guarda deixa cair uma carta com o símbolo do traidor.")
            print("a princesa reconhece o símbolo: ele pertence ao conselheiro do Rei.")
        else:
            print("opção não encontrada!")
            return
    elif opcao == 2:
        print("você decide fugir primeiro e descobrir a verdade depois.")
        print("vocês correm pelos corredores do castelo.")
        print("um guarda percebe a fuga, mas a princesa encontra uma passagem secreta.")
        print("vocês escapam e encontram uma carta caída no chão.")
        print("a carta tem o símbolo do conselheiro do Rei.")
        print("a princesa percebe que o conselheiro pode ser o traidor.")
        print("-" * 50)
    else:
        print("opção não encontrada!")
        return
    print("-" * 50)
    print("vocês chegam até uma saída secreta do castelo.")
    print("a princesa aponta para uma passagem escondida.")
    print('"por aqui! essa passagem leva para fora do reino."')
    print("-" * 50)
    print("vocês conseguem escapar do castelo.")
    print("a princesa olha para o horizonte e revela a última informação:")
    print('"o verdadeiro inimigo está vindo para cá."')
    print("agora vocês precisam voltar ao Rei e revelar quem é o traidor.")
    print("-" * 50)
    print("A PRIMEIRA PARTE DA MISSÃO FOI CONCLUÍDA!")
    print("A PRÓXIMA MISSÃO SERÁ DESCOBRIR A VERDADE SOBRE O CONSELHEIRO.")
    retorno_ao_rei()

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
            print("essa estrada leva até o Reino dos Betas.")
        elif opcao == 2:
            print("você decide não entrar na floresta.")
            print("depois de caminhar bastante, encontra uma estrada antiga.")
            print("você segue por ela durante o resto do dia.")
            print("um viajante encontra você e confirma que a estrada leva ao Reino dos Betas.")
            print("ele também avisa que os portões estão sem muitos guardas.")
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
        print("entre as provisões, encontra um pequeno mapa do Reino dos Betas.")
        print("agora você sabe exatamente qual estrada seguir.")
        print("-" * 50)
        print("depois de algumas horas, encontra uma estrada de pedra.")
        print("ao longe, consegue ver as muralhas do Reino dos Betas.")
    else:
        print("opção não encontrada!")
        return
    print("-" * 50)
    print("você finalmente chega diante dos portões do Reino dos Betas!")
    print("-" * 50)
    print("mas existe algo estranho...")
    print("não há nenhum soldado protegendo a entrada.")
    print("você entra no reino e encontra uma praça completamente vazia.")
    print("-" * 50)
    print("no chão existe uma espada quebrada e um pedaço de papel.")
    print("no papel está escrito:")
    print('"NÃO CONFIE EM NINGUÉM."')
    print("-" * 50)
    print("de repente, você escuta um barulho atrás de você.")
    print("1 - virar para descobrir o que é")
    print("2 - continuar correndo em direção ao castelo")
    opcao = int(input("o que você faz?: "))
    print("-" * 50)
    if opcao == 1:
        print("você se vira e encontra um soldado ferido.")
        print("ele diz que sabe onde a princesa está.")
        print("mas antes de contar, pede sua ajuda.")
        print("-" * 50)
        print("1 - ajudar o soldado")
        print("2 - pedir que ele indique o caminho")
        opcao = int(input("o que você faz?: "))
        print("-" * 50)
        if opcao == 1:
            print("você ajuda o soldado a se levantar.")
            print("ele agradece e mostra uma entrada escondida no castelo.")
            print("você segue pela entrada escondida.")
            as_tres_portas()
        elif opcao == 2:
            print("o soldado aponta para a entrada principal do castelo.")
            print("ele avisa que os corredores estão cheios de guardas.")
            print("você agradece e segue rapidamente até lá.")
            entrada_do_castelo()
        else:
            print("opção não encontrada!")
    elif opcao == 2:
        print("você corre em direção ao castelo.")
        print("as portas estão abertas.")
        print("você entra lentamente.")
        print("um corredor escuro aparece à sua frente.")
        print("você segue pelo corredor até encontrar a sala das três portas.")
        print("-" * 50)
        as_tres_portas()
    else:
        print("opção não encontrada!")

def retorno_ao_rei():
    print("você e a princesa voltam ao castelo do Rei.")
    print("o Rei escuta tudo o que aconteceu no Reino dos Betas.")
    print("a princesa explica que encontrou pistas sobre o conselheiro.")
    print("o Rei fica preocupado, mas decide não acusar ninguém sem investigar.")
    print("-" * 50)
    print("1 - investigar os registros da biblioteca")
    print("2 - conversar com os guardas")
    print("3 - seguir o conselheiro em segredo")
    print("-" * 50)
    opcao = int(input("o que você faz?: "))
    print("-" * 50)
    if opcao == 1:
        investigar_conselheiro()
    elif opcao == 2:
        print("você conversa com os guardas que estavam de serviço durante o ataque.")
        print("um deles conta que viu o conselheiro sair do castelo tarde da noite.")
        print("ele não sabe para onde o conselheiro foi, mas menciona uma passagem antiga.")
        passagem_subterranea()
    elif opcao == 3:
        print("você espera anoitecer e segue o conselheiro sem ser visto.")
        print("ele atravessa o pátio e entra por uma porta escondida perto da biblioteca.")
        passagem_subterranea()
    else:
        print("opção não encontrada!")
        retorno_ao_rei()


def investigar_conselheiro():
    print("você entra na biblioteca real e procura registros antigos.")
    print("entre documentos e mapas, encontra anotações sobre uma passagem subterrânea.")
    print("um dos documentos mostra que essa passagem leva para fora das muralhas.")
    print("isso ainda não prova que o conselheiro seja um traidor, mas é uma pista importante.")
    print("-" * 50)
    print("1 - examinar melhor os documentos")
    print("2 - procurar a passagem subterrânea")
    print("-" * 50)
    opcao = int(input("o que você faz?: "))
    print("-" * 50)
    if opcao == 1:
        print("você encontra uma anotação sobre entregas feitas perto de uma vila abandonada.")
        print("o nome do conselheiro aparece como responsável por autorizar algumas viagens.")
        print("isso levanta suspeitas, mas ainda pode haver outra explicação.")
        passagem_subterranea()
    elif opcao == 2:
        passagem_subterranea()
    else:
        print("opção não encontrada!")
        investigar_conselheiro()


def passagem_subterranea():
    print("você encontra uma escadaria escondida sob uma estante da biblioteca.")
    print("a passagem é antiga e leva para fora do castelo.")
    print("no chão, há marcas recentes de botas e restos de cera de uma carta selada.")
    print("no fim do túnel, você encontra um mapa que indica uma fortaleza abandonada.")
    print("-" * 50)
    print("1 - ir até a fortaleza agora")
    print("2 - voltar ao Rei e contar o que encontrou")
    print("-" * 50)
    opcao = int(input("o que você faz?: "))
    print("-" * 50)
    if opcao == 1:
        fortaleza_das_sombras()
    elif opcao == 2:
        print("você mostra o mapa ao Rei.")
        print("ele autoriza a missão e entrega uma pequena equipe para acompanhar você.")
        fortaleza_das_sombras()
    else:
        print("opção não encontrada!")
        passagem_subterranea()


def fortaleza_das_sombras():
    print("você chega à Fortaleza das Sombras, escondida entre árvores e pedras.")
    print("há luzes nas janelas, embora a fortaleza pareça abandonada.")
    print("você precisa entrar sem alertar quem está lá dentro.")
    print("-" * 50)
    print("1 - entrar pelo portão principal")
    print("2 - procurar uma entrada escondida")
    print("-" * 50)
    opcao = int(input("como você entra?: "))
    print("-" * 50)
    if opcao == 1:
        print("os guardas percebem sua chegada, mas você consegue avançar até o salão principal.")
        confronto_comandante()
    elif opcao == 2:
        print("você encontra uma abertura atrás das ruínas e entra sem ser percebido.")
        print("lá dentro, escuta um comandante falando sobre um novo ataque ao reino.")
        confronto_comandante()
    else:
        print("opção não encontrada!")
        fortaleza_das_sombras()


def confronto_comandante():
    print("no salão principal, você encontra um comandante inimigo diante de vários mapas.")
    print("ele percebe que seus planos foram descobertos.")
    print('"vocês chegaram tarde demais. o ataque já está sendo preparado."')
    print("você exige saber por que ele recebeu informações sobre as defesas do reino.")
    print('"o conselheiro nos contou algumas coisas, mas ele não é quem comanda tudo."')
    print("o comandante se recusa a revelar o nome de seu superior.")
    print("-" * 50)
    print("1 - prender o comandante e levar os documentos ao Rei")
    print("2 - tentar convencê-lo a revelar mais informações")
    print("-" * 50)
    opcao = int(input("o que você faz?: "))
    print("-" * 50)
    if opcao == 1:
        print("você recolhe os mapas e impede o comandante de fugir.")
        fim_da_missao_nova()
    elif opcao == 2:
        print("você mostra ao comandante que os planos dele foram descobertos.")
        print("ele revela que uma pessoa ainda mais poderosa está por trás da invasão.")
        print('"procure o símbolo da coroa partida. ele vai mostrar quem dá as ordens."')
        fim_da_missao_nova()
    else:
        print("opção não encontrada!")
        confronto_comandante()


def fim_da_missao_nova():
    print("-" * 50)
    print("VOCÊ DESCOBRIU UMA PARTE DA CONSPIRAÇÃO!")
    print("os documentos provam que o reino está sendo ameaçado por uma organização maior.")
    print("agora o Rei precisa ser avisado antes que o próximo ataque aconteça.")
    print("a identidade do verdadeiro líder ainda é um mistério.")
    print("-" * 50)
    print("FIM DESTA PARTE DA AVENTURA.")
    print("A PRÓXIMA MISSÃO SERÁ DESCOBRIR QUEM USA O SÍMBOLO DA COROA PARTIDA.")


# TELA INICIAL

while True:
    letreiro = r"""
     _____    _____    _____
    |  _  \  |  _  \  |     \
    | |_)  | | |_)  | |  ___/
    |  _  /  |  ___/  | | ___
    | | \ \  | |      | | |  |
    | |  \ | | |      | |_|  |
    |_|   \| |_|      |______|
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
        exit()
    else:
        print("opção não encontrada!")

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
                    print("fim da aventura.")
                    print("-" * 50)
                    break
                if castelo():
                    if a_aventura_começa():
                        a_cruzada_da_indecisão()
                break
        elif caminho == 2:
            tem_ovo = caverna(tem_ovo)
            if tem_ovo is None:
                print("-" * 50)
                print("VOCÊ MORREU!")
                print("fim da aventura.")
                print("-" * 50)
                break
            if tem_ovo:
                print("você agora possui o ovo de dragão.")
                print("ainda precisa encontrar uma maneira de chegar ao castelo.")
                print("-" * 50)
                passou, tem_ovo = ponte_em_um_penhasco(tem_ovo)
                if passou:
                    depois_da_ponte()
                    sobreviveu = acampamento_goblim()
                    if not sobreviveu:
                        print("-" * 50)
                        print("VOCÊ MORREU!")
                        print("fim da aventura.")
                        print("-" * 50)
                        break
                    if castelo():
                        if a_aventura_começa():
                            a_cruzada_da_indecisão()
                    break
            else:
                print("sem o ovo, o goblin continua bloqueando a ponte.")
                print("você volta para a floresta e precisa escolher novamente.")
                print("-" * 50)
        else:
            print("não tem esse caminho!")
            print("escolha novamente!")
