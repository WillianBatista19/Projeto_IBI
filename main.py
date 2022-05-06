# Importações da tela
import pygame, sys
import funcoes
import jogoJerry
#import jogoWill
import ponte

from pygame.locals import *
from funcoes import *
from jogoJerry import *
#from jogoWill import *
from ponte import *

'''# Definindo uma logo (32x32) para a janela
logo = pygame.image.load("imagens/logo.png")
pygame.display.set_icon(logo)'''

'''# Transforma o cursor em uma mão
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)'''


# Criação das telas e definição do seus tamanhos
telainicial = tamanho_tela()

# Definindo uma logo
logo = pygame.image.load("imagens/icon.png")
pygame.display.set_icon(logo)

# Dando um nome a tela
nome_tela("Menu principal") 

# Definindo local de origem do botão(Margem esquerda, Margem superior, Tamanho Horinzontal, Tamanho Vertical)
botaoJogar = pygame.Rect((640/2 - 75), 150, 150, 45)
botaoSobre = pygame.Rect((640/2 - 75), 220, 150, 45)
botaoEquipe = pygame.Rect((640/2 - 75), 290, 150, 45)
#botaoOpcoes = pygame.Rect(20, 415, 150, 45)

# Retangulo que cobre toda a tela
#limpatela = pygame.Rect(0, 0, larguratela, alturatela)    

# Definindo cores
for i in range(1,2):
    cor_azulClaro = (0, 128, 255)
    cor_verde = (88, 159, 100)
    cor_verdeClaro = (0, 255, 0)
    cor_vermelho = (255, 0, 0)
    cor_azul = (0, 0, 255)
    cor_rosa = (255, 0, 128)
    cor_roxo = (128, 0, 128)
    cor_cinza = (192, 192, 192)
    cor_branco = (255, 255, 255)
    cor_preto = (0, 0, 0)

# Mouse
#pygame.mouse.set_system_cursor(mouse)

# Caregando imagens
for i in range(1,2):
    bg = pygame.image.load("imagens/bg3.jpeg")
    bgJogos1 = pygame.image.load("imagens/bgJogos.jpeg")
    botaoJogar1 = pygame.image.load("imagens/btJogar.png")
    botaoSobre1 = pygame.image.load("imagens/btSobre.png")
    #botaoOpcoes1 = pygame.image.load("imagens/btOpcoes.png")
    botaoEquipe1 = pygame.image.load("imagens/btEquipe.png")
    botaoVoltar1 = pygame.image.load("imagens/btMenu.png")
    botaoProx1 = pygame.image.load("imagens/btPoximo.png")
    botaoAnt1 = pygame.image.load("imagens/btAnterior.png")
    botaoJogo11 = pygame.image.load("imagens/btJogo1.png")
    botaoJogo22 = pygame.image.load("imagens/btJogo2.png")

# Carregando as imagens dos membros da equipe
for i in range(1,2):
    imagemDavid = pygame.image.load("imagens/David.jpeg")
    imagemRafael = pygame.image.load("imagens/Rafael.jpeg")
    imagemVicente = pygame.image.load("imagens/Vicente.jpeg")
    imagemVictor = pygame.image.load("imagens/Victor.jpeg")
    imagemWillian = pygame.image.load("imagens/Willian.jpeg")
    imagem_fundo_sobre = pygame.image.load("imagens/bg4.jpeg")
    imagem_fundo_equipe = pygame.image.load("imagens/bg5.jpeg")

# Mudando o tamanho das imagens 
for i in range(1,2):
    bgnovo = pygame.transform.scale(bg,(640,480))
    bgJogos = pygame.transform.scale(bgJogos1,(640,480))
    imgbotaoJogar = pygame.transform.scale(botaoJogar1,(150,45))
    imgbotaoSobre = pygame.transform.scale(botaoSobre1,(150,45))
    #imgbotaoOpcoes = pygame.transform.scale(botaoOpcoes1,(150,45))
    imgbotaoEquipe = pygame.transform.scale(botaoEquipe1,(150,45))
    imgbotaoVoltar = pygame.transform.scale(botaoVoltar1,(150,45))
    imgbotaoProx = pygame.transform.scale(botaoProx1,(45,45))
    imgbotaoAnt = pygame.transform.scale(botaoAnt1,(45,45))
    imgbotaoJogar1 = pygame.transform.scale(botaoJogo11,(150,45))
    imgbotaoJogar2 = pygame.transform.scale(botaoJogo22,(150,45))

    fotoDavid = pygame.transform.scale(imagemDavid, (150, 130))
    fotoRafael = pygame.transform.scale(imagemRafael, (150, 130))
    fotoVicente = pygame.transform.scale(imagemVicente, (150, 130))
    fotoVictor = pygame.transform.scale(imagemVictor, (150, 130))
    fotoWillian = pygame.transform.scale(imagemWillian, (150, 130))

# Definindo fonte(tipo, tamanho, negrito, italico)
fonteTitulo = fonte_titulo_inicial()

fonteTituloEquipe = fonte_titulo_equipe()

# Definindo textos
#nomeEquipe = fonteTituloEquipe.render("Nome da Equipe", True, cor_preto)
for i in range(1,2):
    nomeDavid = fonteTituloEquipe.render("David Waters Teixeira Rodrigues", True, cor_preto)
    nomeRafael = fonteTituloEquipe.render("Rafael Pereira de Souza", True, cor_preto)
    nomeVicente = fonteTituloEquipe.render("Vicente de Paulo Vidal Alencar", True, cor_preto)
    nomeVictor = fonteTituloEquipe.render("Victor Jerrysson Gama Bastos", True, cor_preto)
    nomeWillian = fonteTituloEquipe.render("Willian Alves Batista", True, cor_preto)
    funcaoDavid = fonteTituloEquipe.render("Função: menu inicial", True, cor_preto)
    funcaoRafael = fonteTituloEquipe.render("Função: tela da equipe", True, cor_preto)
    funcaoVicente = fonteTituloEquipe.render("Função: tela sobre", True, cor_preto)
    funcaoVictor = fonteTituloEquipe.render("Função: jogo", True, cor_preto)
    funcaoWillian = fonteTituloEquipe.render("Função: jogo", True, cor_preto)
    emailDavid = fonteTituloEquipe.render("Email: davidwaters503@gmail.com", True, cor_preto)
    emailRafael = fonteTituloEquipe.render("Email: rafaelpereirasouza15@gmail.com", True, cor_preto)
    emailVicente = fonteTituloEquipe.render("Email: vicente050paulo@gmail.com", True, cor_preto)
    emailVictor = fonteTituloEquipe.render("Email: victorjerrysson@gmail.com", True, cor_preto)
    emailWillian = fonteTituloEquipe.render("Email: willianmoreira.2000.19@gmail.com", True, cor_preto)
    menu = fonteTituloEquipe.render("Menu", True, cor_preto)    

# Função da tela inicial
def telaInicial():
    # Definindo um nome de tela
    nome_tela("Menu Principal")
    # Loop para deixar a aplicação aberta
    while True:
        


        # Colocando imagem como backgroud
        telainicial.blit(bgnovo, (0, 0))
        
        # Colocando imagens para representar o botão
        telainicial.blit(imgbotaoJogar, ((640/2 - 75),150))
        telainicial.blit(imgbotaoSobre, ((640/2 - 75),220))
        telainicial.blit(imgbotaoEquipe, ((640/2 - 75),290))
        #telainicial.blit(imgbotaoOpcoes, (20,415))
        #telainicial.blit(imgbotaoVoltar, (20,415))

        

        # Dando uma cor para o fundo
        #telainicial.fill(cor_branco)

        # Verificando se o usuário está executando algum elvento
        for evento in pygame.event.get():
            # Se o evento for de fechar então deve ser fechada a aplicação
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            # Cliques do mouse
            if evento.type == MOUSEBUTTONDOWN and evento.button == 1:
                # Pegando valor X do mouse
                x_mouse = pygame.mouse.get_pos()[0]
                # Pegando valor Y do mouse
                y_mouse = pygame.mouse.get_pos()[1]

                #Verificando se o Mouse está clicando na área onde está a imagem do botão
                if x_mouse > (640/2 - 75) and y_mouse > 150 and x_mouse < (640/2 - 75 + 150) and y_mouse < 195:
                    telaJogos()
                    break
                if x_mouse > (640/2 - 75) and y_mouse > 220 and x_mouse < (640/2 - 75 + 150) and y_mouse < 265:
                    telaSobreInicial()
                    break
                if x_mouse > (640/2 - 75) and y_mouse > 290 and x_mouse < (640/2 - 75 + 150) and y_mouse < 335:
                    telaEquipe1()
                    break
                '''if x_mouse > 20 and y_mouse > 415 and x_mouse < (20 + 150) and y_mouse < (415 + 45):
                    telaTesteAzul()
                    break'''

        # Colocando texto
            # nome da variavel, recebe a fonte pré definida com (texto, True/False, cor)
        textoTitulo = fonteTitulo.render("Ibi - Natureza é Vida", True, cor_preto)
        
            # Superficie onde será pregado o texto, depis escolhe o texto e onde ele vai aparecer
        telainicial.blit(textoTitulo, [10, 10])

        # Atualizando a tela
        atualiza()

def telaJogos():
    
    tela = tamanho_tela()

    #Adicionando nome a tela
    nome_tela("Escolha o Jogo")
    
    while True:
        # Colocando imagem como backgroud
        tela.blit(bgJogos, (0, 0))
        
        # Colocando imagens para representar o botão
        tela.blit(imgbotaoJogar1, ((640/2 - 75),150))
        tela.blit(imgbotaoJogar2, ((640/2 - 75),220))
        tela.blit(imgbotaoVoltar, (20,415))

        # Verificando se o usuário está executando algum elvento
        for evento in pygame.event.get():
            # Se o evento for de fechar então deve ser fechada a aplicação
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            # Cliques do mouse
            if evento.type == MOUSEBUTTONDOWN and evento.button == 1:
                # Pegando valor X do mouse
                x_mouse = pygame.mouse.get_pos()[0]
                # Pegando valor Y do mouse
                y_mouse = pygame.mouse.get_pos()[1]

                #Verificando se o Mouse está clicando na área onde está a imagem do botão
                if x_mouse > (640/2 - 75) and y_mouse > 150 and x_mouse < (640/2 - 75 + 150) and y_mouse < 195:
                    tamanho_telaJogoJerry()
                    telaPrincipal()
                    break
                    break
                if x_mouse > (640/2 - 75) and y_mouse > 220 and x_mouse < (640/2 - 75 + 150) and y_mouse < 265:
                    tamanho_telaJogoWill()
                    jogosoldadinho()
                    break
                if x_mouse > 20 and y_mouse > 415 and x_mouse < (20 + 150) and y_mouse < (415 + 45):
                    telaInicial()
                    break
        # Atualizando a tela
        atualiza()

def telaSobreInicial():
    #Definindo tamanho da tela
    tela = tamanho_tela()

    tela.blit(imagem_fundo_sobre, (0, 0))

    #Adicionando nome a tela
    nome_tela("Agenda ONU")

    #Textos informativos a serem utilizados nas tela
    for i in range(1,2):    
        titulo = "Agenda ONU para 2030"
        linha1 = "'Em setembro de 2015, representantes dos 193 Estados-membros da ONU se reuniram em Nova "
        linha2 = "York e reconheceram que a erradicação da pobreza em todas as suas formas e dimensões, incluindo"
        linha3 = "a pobreza extrema, é o maior desafio global e um requisito indispensável para o desenvolvimento'."

        linha4 = "A Agenda 2030 é um plano de ação que busca fortalecer a paz mundial, indica os 17 Objetivos de"
        linha5 = "Desenvolvimento Sustentável para erradicar a pobreza e promover vida digna para todas as pessoas,"
        linha6 = "dentro dos limites do planeta. Dentre eles, o objetivo 15 - Vida Terrestre, com a finalidade de prote-"
        linha7 = "ger, recuperar e promover o uso sustentável dos ecossistemas  terrestres."

        linha8 = "Algumas metas do Objetivo 15:"
        linha9 = "15.2: Até 2020, promover a implementação da gestão sustentável de todos os tipos de flo-"
        linha10 = "restas, deter o desmatamento, restaurar florestas degradadas e aumentar substancialmente o "
        linha11 = "florestamento e o reflorestamento global."

        linha12 = "15.3: Até 2030, combater a desertificação, restaurar a terra e o solo degradado, incluindo terre-"
        linha13 = "nos afetados pela desertificação, secas e inundações, e lutar para alcançar um mundo neutro em"
        linha14 = "termos de degradação do solo."

        linha15 = "15.4: Até 2030, assegurar a conservação dos ecossistemas de montanha, incluindo a sua biodiver-"
        linha16 = "sidade, para melhorar a sua capacidade de proporcionar benefícios, que são essenciais para o desen-"
        linha17 = "volvimento sustentável."

    while True:

        

        for evento in pygame.event.get():
            # Se o evento for de fechar então deve ser fechada a aplicação
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            
            # Cliques do mouse
            if evento.type == MOUSEBUTTONDOWN and evento.button == 1:
                # Pegando valor X do mouse
                x_mouse = pygame.mouse.get_pos()[0]
                # Pegando valor Y do mouse
                y_mouse = pygame.mouse.get_pos()[1]
                
                # Colidindo na area do botão avançar
                if x_mouse > 590 and y_mouse > 240-22.5 and x_mouse < (590 + 45) and y_mouse < ((240-22.5) + 45):
                    telaSobreCha()
                    break
                
                # Colidindo na area do botão voltar ao menu
                if x_mouse > 20 and y_mouse > 415 and x_mouse < (20 + 150) and y_mouse < (415 + 45):
                    telaInicial()
                    break

        #Adicionando cor ao fundo da tela
        #fundo_tela(tela)

        #Definindo as fontes, tamanhos e atribuindo a variavéis
        fonteSys_linha = fonte_linha()
        fonteSys_titulo = fonte_titulo()

        #Adicionando o resumo e o título a tela e formatando(qual o texto, se serrilhado, cor)
        for i in range(1,2):      
            titulo_tela = fonteSys_titulo.render(titulo, True, (0,0,0,))
            linha1_tela = fonteSys_linha.render(linha1, True, (0,0,0))
            linha2_tela = fonteSys_linha.render(linha2, True, (0,0,0))
            linha3_tela = fonteSys_linha.render(linha3, True, (0,0,0))

            linha4_tela = fonteSys_linha.render(linha4, True, (0,0,0))
            linha5_tela = fonteSys_linha.render(linha5, True, (0,0,0))
            linha6_tela = fonteSys_linha.render(linha6, True, (0,0,0))
            linha7_tela = fonteSys_linha.render(linha7, True, (0,0,0))

            linha8_tela = fonteSys_linha.render(linha8, True, (0,0,0))
            linha9_tela = fonteSys_linha.render(linha9, True, (0,0,0))
            linha10_tela = fonteSys_linha.render(linha10, True, (0,0,0))

            linha11_tela = fonteSys_linha.render(linha11, True, (0,0,0))
            linha12_tela = fonteSys_linha.render(linha12, True, (0,0,0))
            linha13_tela = fonteSys_linha.render(linha13, True, (0,0,0))
            linha14_tela = fonteSys_linha.render(linha14, True, (0,0,0))

            linha15_tela = fonteSys_linha.render(linha15, True, (0,0,0))
            linha16_tela = fonteSys_linha.render(linha16, True, (0,0,0))
            linha17_tela = fonteSys_linha.render(linha17, True, (0,0,0))
    
        #Definindo as posições dos textos na tela 
        for i in range(1,2):  
            tela.blit(titulo_tela,(240,15))
            tela.blit(linha1_tela,(20,40))
            tela.blit(linha2_tela,(10,60))
            tela.blit(linha3_tela,(10,80))

            tela.blit(linha4_tela,(20,105))
            tela.blit(linha5_tela,(10,125))
            tela.blit(linha6_tela,(10,145))
            tela.blit(linha7_tela,(10,165))

            tela.blit(linha8_tela,(35,195))
            tela.blit(linha9_tela,(20,225))
            tela.blit(linha10_tela,(10,245))
            tela.blit(linha11_tela,(10,265))
            
            tela.blit(linha12_tela,(20,285))
            tela.blit(linha13_tela,(10,305))
            tela.blit(linha14_tela,(10,325))

            tela.blit(linha15_tela,(20,345))
            tela.blit(linha16_tela,(10,365))
            tela.blit(linha17_tela,(10,385))
        
        # Imagem que representa o botão para voltar ao menu e para adiar a próxima tela
        tela.blit(imgbotaoEquipe, (20,415))
        tela.blit(imgbotaoProx, (590,240-22.5))

        #Atualizando tela
        atualiza()

def telaSobreCha():
    #Definindo tamanho da tela
    tela = tamanho_tela()

    tela.blit(imagem_fundo_sobre, (0, 0))

    #Adicionando nome a tela
    nome_tela("Chapada do Araripe")

    for i in range(1,2):

        titulo = "Informações Chapada do Araripe"
        linha1 = "A Chapada do Araripe é uma formação geográfica que abrange os estados do Ceará, Piauí e Per-"
        linha2 = "nambuco, caracteriza-se por oferecer uma enorme quantidade de riquezas fósseis, vegetais e animais, contribuindo"
        linha3 = "para a formação de aquíferos que abastecem as localidades. Formando um clima tropical úmido mas"
        linha4 = "com chuvas irregulares, sendo as mais significativas durante o mês de fevereiro."

        linha5 = "Abriga uma fauna e flora destacáveis, criando um microclima local no semiárido, com uma flora"
        linha6 = "forte capaz de sustentar o solo e evitar deslizamentos, em conjunto com sua fauna trabalham em e-"
        linha7 = "quilíbrio para manter o ecossistema local, de onde várias pessoas tiram sua renda, remédios ou ou-"
        linha8 = "tros recursos."

        linha9 = "A quantidade de vestígios arqueológicos surpreende também pela sua qualidade,"
        linha10 = "com rochas de cerca de 110 milhões de anos que conservam diversos animais, sendo"
        linha11 = "os grupos de fósseis mais encontrados: vegetais, invertebrados, peixes anfíbios, quelônios, Pterossa-"
        linha12 = "uros e outros dinossauros."

        linha13 = "A região abriga o Parque dos Pterossauros, a quatro quilômetros de Santana do Cariri, com répli-"
        linha14 = "cas artísticas desses répteis; sendo um terço de todos os exemplares fósseis já achados dessa ave,"
        linha15 = "presente na Chapada do Araripe."

    while True:
        for evento in pygame.event.get():
            # Se o evento for de fechar então deve ser fechada a aplicação
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            
            # Cliques do mouse
            if evento.type == MOUSEBUTTONDOWN and evento.button == 1:
                # Pegando valor X do mouse
                x_mouse = pygame.mouse.get_pos()[0]
                # Pegando valor Y do mouse
                y_mouse = pygame.mouse.get_pos()[1]
                
                # Colidindo na area do botão avançar
                if x_mouse > 590 and y_mouse > 240-22.5 and x_mouse < (590 + 45) and y_mouse < ((240-22.5) + 45):
                    telaSobrePro()
                    break
                
                # Colidindo na area do botão voltar
                if x_mouse > 5 and y_mouse > 240-22.5 and x_mouse < (5 + 45) and y_mouse < ((240-22.5) + 45):
                    telaSobreInicial()
                    break

                # Colidindo na area do botão voltar ao menu
                if x_mouse > 20 and y_mouse > 415 and x_mouse < (20 + 150) and y_mouse < (415 + 45):
                    telaInicial()
                    break

        #Fundo de tela
        #fundo_tela(tela)

        #Definindo as fontes, tamanhos e atribuindo a variavéis
        fonteSys_linha = fonte_linha()
        fonteSys_titulo = fonte_titulo()
        
        for i in range(1,2):

            titulo_tela = fonteSys_titulo.render(titulo, True, (0,0,0))
            linha1_tela = fonteSys_linha.render(linha1,True, (0,0,0))
            linha2_tela = fonteSys_linha.render(linha2, True, (0,0,0))
            linha3_tela = fonteSys_linha.render(linha3, True, (0,0,0))
            linha4_tela = fonteSys_linha.render(linha4, True, (0,0,0))
            
            linha5_tela = fonteSys_linha.render(linha5, True, (0,0,0))
            linha6_tela = fonteSys_linha.render(linha6, True, (0,0,0))
            linha7_tela = fonteSys_linha.render(linha7, True, (0,0,0))
            linha8_tela = fonteSys_linha.render(linha8, True, (0,0,0))

            linha9_tela = fonteSys_linha.render(linha9, True, (0,0,0))
            linha10_tela = fonteSys_linha.render(linha10, True, (0,0,0))
            linha11_tela = fonteSys_linha.render(linha11, True, (0,0,0))
            linha12_tela = fonteSys_linha.render(linha12, True, (0,0,0))

            linha13_tela = fonteSys_linha.render(linha13, True, (0,0,0))
            linha14_tela = fonteSys_linha.render(linha14, True, (0,0,0))
            linha15_tela = fonteSys_linha.render(linha15, True, (0,0,0))

            tela.blit(titulo_tela,(200,20))
            tela.blit(linha1_tela,(20,50))
            tela.blit(linha2_tela,(10,70))
            tela.blit(linha3_tela,(10,90))
            tela.blit(linha4_tela,(10,110))
            
            tela.blit(linha5_tela,(20,140))
            tela.blit(linha6_tela,(10,160))
            tela.blit(linha7_tela,(10,180))
            tela.blit(linha8_tela,(10,200))
            
            tela.blit(linha9_tela,(70,230))
            tela.blit(linha10_tela,(55,250))
            tela.blit(linha11_tela,(10,270))
            tela.blit(linha12_tela,(10,290))

            tela.blit(linha13_tela,(20,320))
            tela.blit(linha14_tela, (10,340))
            tela.blit(linha15_tela, (10,360))

                # Imagem que representa o botão para voltar ao menu e para adiar a próxima tela
        
        tela.blit(imgbotaoEquipe, (20,415))
        tela.blit(imgbotaoProx, (590,240-22.5))
        tela.blit(imgbotaoAnt, (5,240-22.5))

        #Atualizar tela
        atualiza()

def telaSobrePro():

    #Definindo tamanho da tela
    tela = tamanho_tela()
    tela.blit(imagem_fundo_sobre, (0, 0))

    #Adicionando nome a tela
    nome_tela("Fauna e Flora")
    for i in range(1,2):
            
        titulo = "Fauna, Flora e Problemáticas da Chapada do Araripe"
        linha1 = "A Chapada do Araripe abriga uma vida terrestre extremamente rica, com uma riqueza vegetal que "
        linha2 = "abriga 516 espécies de flora nativa, só de samambaias são 39 espécies e 56 espécies de fungos mico-"
        linha3 = "rrízicos e 71 fungos basidiomicetos; possui uma fauna com cerca de 483 espécies de vertebrados sil-"
        linha4 = "vestres, sendo 298 aves, 90 mamíferos, 71 répteis e 24 anfíbios."

        linha5 = "Com destaque para uma espécie exclusiva da região,  o soldadinho-do-araripe, restrita a uma faixa"
        linha6 = "pequena de território cearense nos municípios de Barbalha, Crato e Missão Velha, criticamente ame-"
        linha7 = "açada de extinção."

        linha8 = "A interferência humana na APA(Área de Proteção Ambiental), é o seu maior pro-"
        linha9 = "blema, a preparação do solo para plantação, se utiliza muitas vezes do fogo, que se"
        linha10 = "alastra muito rapidamente pelo território por ser uma região de caatinga e comumen-"
        linha11 = "te seca, em 2008 a unidade chegou a apresentar 1400 focos de calor no ano."

        linha12 = "Também, enfrenta outros problemas, por ser uma área rica em minério muitas empresas realizam a"
        linha13 = "extração, obras de infraestrutura como rodovias e o desmatamento contribuem para limitar o uso da"
        linha14 = "própria unidade pelos animais e alterar o ecossistema local."

    while True:
        for evento in pygame.event.get():
            # Se o evento for de fechar então deve ser fechada a aplicação
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            
            # Cliques do mouse
            if evento.type == MOUSEBUTTONDOWN and evento.button == 1:
                # Pegando valor X do mouse
                x_mouse = pygame.mouse.get_pos()[0]
                # Pegando valor Y do mouse
                y_mouse = pygame.mouse.get_pos()[1]
                
                # Colidindo na area do botão avançar
                if x_mouse > 590 and y_mouse > 240-22.5 and x_mouse < (590 + 45) and y_mouse < ((240-22.5) + 45):
                    telaSobreRef()
                    break
                
                # Colidindo na area do botão avançar
                if x_mouse > 5 and y_mouse > 240-22.5 and x_mouse < (5 + 45) and y_mouse < ((240-22.5) + 45):
                    telaSobreCha()
                    break

                # Colidindo na area do botão voltar ao menu
                if x_mouse > 20 and y_mouse > 415 and x_mouse < (20 + 150) and y_mouse < (415 + 45):
                    telaInicial()
                    break

        #Fundo de tela
        #fundo_tela(tela)

        #Definindo as fontes, tamanhos e atribuindo a variavéis
        fonteSys_linha = fonte_linha()
        fonteSys_titulo = fonte_titulo()

        for i in range(1,2):
                
            titulo_tela = fonteSys_titulo.render(titulo, True, (0,0,0))
            linha1_tela = fonteSys_linha.render(linha1, True, (0,0,0))
            linha2_tela = fonteSys_linha.render(linha2, True, (0,0,0))
            linha3_tela = fonteSys_linha.render(linha3, True, (0,0,0))
            linha4_tela = fonteSys_linha.render(linha4, True, (0,0,0))
            
            linha5_tela = fonteSys_linha.render(linha5, True, (0,0,0))
            linha6_tela = fonteSys_linha.render(linha6, True, (0,0,0))
            linha7_tela = fonteSys_linha.render(linha7, True, (0,0,0))
            linha8_tela = fonteSys_linha.render(linha8, True, (0,0,0))

            linha9_tela = fonteSys_linha.render(linha9, True, (0,0,0))
            linha10_tela = fonteSys_linha.render(linha10, True, (0,0,0))
            linha11_tela = fonteSys_linha.render(linha11, True, (0,0,0))

            linha12_tela = fonteSys_linha.render(linha12, True, (0,0,0))
            linha13_tela = fonteSys_linha.render(linha13, True, (0,0,0))
            linha14_tela = fonteSys_linha.render(linha14, True, (0,0,0))

            tela.blit(titulo_tela,(140,20))
            tela.blit(linha1_tela,(20,50))
            tela.blit(linha2_tela,(10,70))
            tela.blit(linha3_tela,(10,90))
            tela.blit(linha4_tela,(10,110))
            
            tela.blit(linha5_tela,(20,140))
            tela.blit(linha6_tela,(10,160))
            tela.blit(linha7_tela,(10,180))
            
            tela.blit(linha8_tela,(70,210))
            tela.blit(linha9_tela,(60,230))
            tela.blit(linha10_tela,(60,250))
            tela.blit(linha11_tela,(10,270))
            
            tela.blit(linha12_tela,(20,300))
            tela.blit(linha13_tela, (10,320))
            tela.blit(linha14_tela, (10,340))

        # Imagem que representa o botão para voltar ao menu e para adiar a próxima tela
        tela.blit(imgbotaoEquipe, (20,415))
        tela.blit(imgbotaoProx, (590,240-22.5))
        tela.blit(imgbotaoAnt, (5,240-22.5))

        #Atualizando tela
        atualiza()

def telaSobreRef():

    #Definindo tamanho da tela
    tela = tamanho_tela()
    tela.blit(imagem_fundo_sobre, (0, 0))

    #Adicionando nome a tela
    nome_tela("Referências")

    for i in range(1,2):
        titulo = "Referências"
        linha1 = "https://www.icmbio.gov.br/portal/unidadesdeconservacao/biomas-brasileiros/caatinga"
        linha2 = "http://www.urca.br/hcdal/site/index.php/2016/09/12/site-oficial-do/"
        linha3 = "https://meioambiente.culturamix.com/natureza/chapada-do-araripe-caracteristicas-gerais"
        linha4 = "https://cienciahoje.org.br/coluna/bacia-do-araripe-uma-viagem-ao-passado/"
        linha5 = "https://pesquisa-apa-araripe.webnode.com/apa-chapada-do-araripe/"
        linha6 = "https://uc.socioambiental.org/pt-br/noticia/163778"
        linha7 = "https://sae.museunacional.ufrj.br/museu-de-curiosidades-2-2/"
        linha8 = "http://panoramacultural.com.br/ameacas-a-chapada-do-araripe/"
        linha9 = "http://www.agenda2030.org.br/ods/15/"

    while True:
        for evento in pygame.event.get():
            # Se o evento for de fechar então deve ser fechada a aplicação
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            
            # Cliques do mouse
            if evento.type == MOUSEBUTTONDOWN and evento.button == 1:
                # Pegando valor X do mouse
                x_mouse = pygame.mouse.get_pos()[0]
                # Pegando valor Y do mouse
                y_mouse = pygame.mouse.get_pos()[1]
                
                # Colidindo na area do botão avançar
                if x_mouse > 5 and y_mouse > 240-22.5 and x_mouse < (5 + 45) and y_mouse < ((240-22.5) + 45):
                    telaSobrePro()
                    break

                # Colidindo na area do botão voltar ao menu
                if x_mouse > 20 and y_mouse > 415 and x_mouse < (20 + 150) and y_mouse < (415 + 45):
                    telaInicial()
                    break

        #Fundo de tela
        #fundo_tela(tela)
        
        #Definindo as fontes, tamanhos e atribuindo a variavéis
        linha_Sysfont = fonte_linha()
        titulo_Sysfont = fonte_titulo()

        for i in range(1,2):

            titulo_tela = titulo_Sysfont.render(titulo, True, (0,0,0))
            linha1_tela = linha_Sysfont.render(linha1, True, (0,0,0))
            linha2_tela = linha_Sysfont.render(linha2, True, (0,0,0))
            linha3_tela = linha_Sysfont.render(linha3, True, (0,0,0))
            linha4_tela = linha_Sysfont.render(linha4, True, (0,0,0))
            linha5_tela = linha_Sysfont.render(linha5, True, (0,0,0))
            linha6_tela = linha_Sysfont.render(linha6, True, (0,0,0))
            linha7_tela = linha_Sysfont.render(linha7, True, (0,0,0))
            linha8_tela = linha_Sysfont.render(linha8, True, (0,0,0))
            linha9_tela = linha_Sysfont.render(linha9, True, (0,0,0))
            
            tela.blit(titulo_tela,(280,100))
            tela.blit(linha1_tela,(60,140))
            tela.blit(linha2_tela,(60,160))
            tela.blit(linha3_tela,(60,180))
            tela.blit(linha4_tela,(60,200))
            tela.blit(linha5_tela,(60,220))
            tela.blit(linha6_tela,(60,240))
            tela.blit(linha7_tela,(60,260))
            tela.blit(linha8_tela,(60,280))
            tela.blit(linha9_tela,(60,300))

        # Imagem que representa o botão para voltar ao menu e para adiar a próxima tela
        tela.blit(imgbotaoEquipe, (20,415))
        tela.blit(imgbotaoAnt, (5,240-22.5))

        #Atualizando tela
        atualiza()

def telaEquipe1():
    nome_tela("Membro da equipe, David")
    
    tela = tamanho_tela()
    
    while True:
        # Permite sair da tela
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            # Adicionando clique do mouse (somente botão esquerdo)
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x_mouse = pygame.mouse.get_pos()[0]
                y_mouse = pygame.mouse.get_pos()[1]
                if x_mouse > 20 and y_mouse > 415 and x_mouse < (20 + 150) and y_mouse < (415 + 45):
                    telaInicial()
                    break
                if x_mouse > 590 and y_mouse > 240-22.5 and x_mouse < (590 + 45) and y_mouse < ((240-22.5) + 45):
                    telaEquipe2()
                    break

        # Colocando imagens na tela

        tela.blit(imagem_fundo_equipe, (0, 0))
        tela.blit(fotoDavid, (65, 70))
        tela.blit(imgbotaoProx, (590,240-22.5))
        tela.blit(imgbotaoVoltar, (20,415))

        # Colocando o botão(retângulo) na tela
        #pygame.draw.rect(tela, verde, botaoMenu)
        #setaDireita = pygame.Rect(580, 280, 45, 45)
        #pygame.draw.rect(tela, cor_verdeClaro, setaDireita)
                
        # Adicionando texto na superfície e escolhendo o local
        #tela.blit(nomeEquipe, (640/2.5, 0))
        tela.blit(nomeDavid, (65, 50))
        tela.blit(funcaoDavid, (65, 200))   
        tela.blit(emailDavid, (65, 225))
        #tela.blit(menu, (73, 425))
        atualiza()

def telaEquipe2():
        nome_tela("Membro da equipe, Rafael")

        tela = tamanho_tela()

        while True:
            for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    
                    # Adicionando clique do mouse (somente botão esquerdo)
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        x_mouse = pygame.mouse.get_pos()[0]
                        y_mouse = pygame.mouse.get_pos()[1]
                        if x_mouse > 20 and y_mouse > 415 and x_mouse < (20 + 150) and y_mouse < (415 + 45):
                            telaInicial()
                            break
                        if x_mouse > 590 and y_mouse > 240-22.5 and x_mouse < (590 + 45) and y_mouse < ((240-22.5) + 45):
                            telaEquipe3()
                            break
                        if x_mouse > 5 and y_mouse > 240-22.5 and x_mouse < (5 + 45) and y_mouse < ((240-22.5) + 45):
                            telaEquipe1()
                            break
                        
            # Colocando imagens na tela
            tela.blit(imagem_fundo_equipe, (0, 0))
            tela.blit(fotoRafael, (65, 70))

            # Colocando o botão(retângulo) na tela
            #pygame.draw.rect(tela, verde, botaoMenu)
            '''setaEsquerda = pygame.Rect(10, 280, 45, 45)
            setaDireita = pygame.Rect(580, 280, 45, 45)
            pygame.draw.rect(tela, cor_verdeClaro, setaDireita)
            pygame.draw.rect(tela, cor_verdeClaro, setaEsquerda)'''

            # Adicionando texto na superfície e escolhendo o local
            #tela.blit(nomeEquipe, (larguraTela/2.5, 0))
            tela.blit(imgbotaoVoltar, (20,415))
            tela.blit(imgbotaoProx, (590,240-22.5))
            tela.blit(imgbotaoAnt, (5,240-22.5))
            tela.blit(nomeRafael, (65, 50))
            tela.blit(funcaoRafael, (65, 200))   
            tela.blit(emailRafael, (65, 225))
            #tela.blit(menu, (73, 425))

            # Atualizando a tela
            atualiza()

def telaEquipe3():
    nome_tela("Membro da equipe, Vicente")
    
    tela = tamanho_tela()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # Adicionando clique do mouse
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x_mouse = pygame.mouse.get_pos()[0]
                y_mouse = pygame.mouse.get_pos()[1]
                if x_mouse > 20 and y_mouse > 415 and x_mouse < (20 + 150) and y_mouse < (415 + 45):
                    telaInicial()
                    break
                if x_mouse > 590 and y_mouse > 240-22.5 and x_mouse < (590 + 45) and y_mouse < ((240-22.5) + 45):
                    telaEquipe4()
                    break
                if x_mouse > 5 and y_mouse > 240-22.5 and x_mouse < (5 + 45) and y_mouse < ((240-22.5) + 45):
                    telaEquipe2()
                    break

        # Colocando imagens na tela
        tela.blit(imagem_fundo_equipe, (0, 0))
        tela.blit(fotoVicente, (65, 70))
        
        # Colocando o botão(retângulo) na tela
        #pygame.draw.rect(tela, verde, botaoMenu)
        '''setaEsquerda = pygame.Rect(10, 280, 45, 45)
        setaDireita = pygame.Rect(580, 280, 45, 45)
        pygame.draw.rect(tela, cor_verdeClaro, setaDireita)
        pygame.draw.rect(tela, cor_verdeClaro, setaEsquerda)'''

        # Adicionando texto na superfície e escolhendo o local
        #tela.blit(nomeEquipe, (larguraTela/2.5, 0))
        tela.blit(imgbotaoVoltar, (20,415))
        tela.blit(imgbotaoProx, (590,240-22.5))
        tela.blit(imgbotaoAnt, (5,240-22.5))
        tela.blit(nomeVicente, (65, 50))
        tela.blit(funcaoVicente, (65, 200))   
        tela.blit(emailVicente, (65, 225))
        #tela.blit(menu, (73, 425))

        # Atualizando a tela
        atualiza()

def telaEquipe4():
    nome_tela("Membro da equipe, Victor")

    tela = tamanho_tela()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # Adicionando clique do mouse
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x_mouse = pygame.mouse.get_pos()[0]
                y_mouse = pygame.mouse.get_pos()[1]
                if x_mouse > 20 and y_mouse > 415 and x_mouse < (20 + 150) and y_mouse < (415 + 45):
                    telaInicial()
                    break
                if x_mouse > 590 and y_mouse > 240-22.5 and x_mouse < (590 + 45) and y_mouse < ((240-22.5) + 45):
                    telaEquipe5()
                    break
                if x_mouse > 5 and y_mouse > 240-22.5 and x_mouse < (5 + 45) and y_mouse < ((240-22.5) + 45):
                    telaEquipe3()
                    break

        # Colocando imagens na tela
        tela.blit(imagem_fundo_equipe, (0, 0))
        tela.blit(fotoVictor, (65, 70))
        
        # Colocando o botão(retângulo) na tela
        #pygame.draw.rect(tela, cor_verdeClaro, botaoMenu)
        '''setaEsquerda = pygame.Rect(10, 280, 45, 45)
        setaDireita = pygame.Rect(580, 280, 45, 45)
        pygame.draw.rect(tela, cor_verdeClaro, setaDireita)
        pygame.draw.rect(tela, cor_verdeClaro, setaEsquerda)'''

        # Adicionando texto na superfície e escolhendo o local
        #tela.blit(nomeEquipe, (larguraTela/2.5, 0))
        tela.blit(imgbotaoVoltar, (20,415))
        tela.blit(imgbotaoProx, (590,240-22.5))
        tela.blit(imgbotaoAnt, (5,240-22.5))

        tela.blit(nomeVictor, (65, 50))
        tela.blit(funcaoVictor, (65, 200))   
        tela.blit(emailVictor, (65, 225))
        #tela.blit(menu, (73, 425))

        # Atualizando a tela
        pygame.display.update()

def telaEquipe5():
    nome_tela("Membro da equipe, Willian")

    tela = tamanho_tela()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # Adicionando clique do mouse
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x_mouse = pygame.mouse.get_pos()[0]
                y_mouse = pygame.mouse.get_pos()[1]
                if x_mouse > 20 and y_mouse > 415 and x_mouse < (20 + 150) and y_mouse < (415 + 45):
                    telaInicial()
                    break
                if x_mouse > 5 and y_mouse > 240-22.5 and x_mouse < (5 + 45) and y_mouse < ((240-22.5) + 45):
                    telaEquipe4()
                    break
        
        # Colocando imagens na tela
        tela.blit(imagem_fundo_equipe, (0, 0))
        tela.blit(fotoWillian, (65, 70))

        # Colocando o botão(retângulo) na tela
        #pygame.draw.rect(tela, cor_verdeClaro, botaoMenu)
        #setaEsquerda = pygame.Rect(10, 280, 45, 45)
        #pygame.draw.rect(tela, cor_verdeClaro, setaEsquerda)

        # Adicionando texto na superfície e escolhendo o local
        #tela.blit(nomeEquipe, (larguraTela/2.5, 0))
        tela.blit(imgbotaoVoltar, (20,415))
        tela.blit(imgbotaoAnt, (5,240-22.5))
        tela.blit(nomeWillian, (65, 50))
        tela.blit(funcaoWillian, (65, 200))   
        tela.blit(emailWillian, (65, 225))
        #tela.blit(menu, (73, 425))

        # Atualizando a tela
        atualiza()

# Chamando a função da tela inicial
#print("Foi1")
telaInicial()
#print("Foi2")
