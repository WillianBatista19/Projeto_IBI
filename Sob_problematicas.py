import pygame
import funcoes

from funcoes import *
from pygame.locals import *

#Definindo tamanho da tela
tela = tamanho_tela()

#Adicionando nome a tela
nome_tela("Fauna e Flora")

titulo = "Fauna, Flora e Problemáticas da Chapada do Araripe"
linha1 = "A Chapada do Araripe abriga uma vida terrestre extremamente rica, com uma riqueza vegetal que "
linha2 = "abriga 516 espécies de flora nativa, só de samambaias são 39 espécies e 56 espécies de fungos mico-"
linha3 = "rrízicos e 71 fungos basidiomicetos; possui uma fauna com cerca de 483 espécies de vertebrados sil-"
linha4 = "vestres, sendo 298 aves, 90 mamíferos, 71 répteis e 24 anfíbios."

linha5 = "Com destaque para uma espécie exclusiva da região,  o soldadinho-do-araripe, restrita a uma faixa"
linha6 = "pequena de território cearense nos municípios de Barbalha, Crato e Missão Velha, criticamente ame-"
linha7 = "açada de extinção."

linha8 = "A interferência humana na APA(Área de Proteção Ambiental), é o seu maior problema, a prepara-"
linha9 = "ção do solo para plantação, se utiliza muitas vezes do fogo, que se alastra muito rapidamente pelo te-"
linha10 = "rritório por ser uma região de caatinga e comumente seca, em 2008 a unidade chegou a apresentar "
linha11 = "1400 focos de calor no ano."

linha12 = "Também, enfrenta outros problemas, por ser uma área rica em minério muitas empresas realizam a"
linha13 = "extração, obras de infraestrutura como rodovias e o desmatamento contribuem para limitar o uso da"
linha14 = "própria unidade pelos animais e alterar o ecossistema local."

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    #Fundo de tela
    fundo_tela(tela)

    #Botões avançar e voltar
    botoes_avancar_voltar(tela)

    #botão retorna direto para o menu
    botao_menu(tela)

    #Definindo as fontes, tamanhos e atribuindo a variavéis
    fonteSys_linha = fonte_linha()
    fonteSys_titulo = fonte_titulo()

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

    tela.blit(titulo_tela,(140,40))
    tela.blit(linha1_tela,(20,70))
    tela.blit(linha2_tela,(10,90))
    tela.blit(linha3_tela,(10,110))
    tela.blit(linha4_tela,(10,130))
    
    tela.blit(linha5_tela,(20,160))
    tela.blit(linha6_tela,(10,180))
    tela.blit(linha7_tela,(10,200))
    
    tela.blit(linha8_tela,(20,230))
    tela.blit(linha9_tela,(10,250))
    tela.blit(linha10_tela,(10,270))
    tela.blit(linha11_tela,(10,290))
    
    tela.blit(linha12_tela,(20,320))
    tela.blit(linha13_tela, (10,340))
    tela.blit(linha14_tela, (10,360))

    #Atualizando tela
    atualiza()