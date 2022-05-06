import pygame 
import funcoes

from funcoes import *
from pygame.locals import *

#Definindo tamanho da tela
tela = tamanho_tela()

#Adicionando nome a tela
nome_tela("Agenda ONU")

#Textos informativos a serem utilizados nas tela
titulo = "Agenda ONU para 2030"
linha1 = "'Em setembro de 2015, representantes dos 193 Estados-membros da ONU se reuniram em Nova "
linha2 = "York e reconheceram que a erradicação da pobreza em todas as suas formas e dimensões, incluindo"
linha3 = "a pobreza extrema, é o maior desafio global e um requisito indispensável para o desenvolvimento'."

linha4 = "A Agenda 2030 é um plano de ação que busca fortalecer a paz mundial, indica os 17 Objetivos de"
linha5 = "Desenvolvimento Sustentável para erradicar a pobreza e promover vida digna para todas as pessoas,"
linha6 = "dentro dos limites do planeta. Dentre eles, o objetivo 15 - Vida Terrestre, com a finalidade de prote-"
linha7 = "ger, recuperar e promover o uso sustentável dos ecossistemas  terrestres."

linha8 = "Algumas metas do Objetivo 15:"
linha9 = "15.2: Até 2020, promover a implementação da gestão sustentável de todos os tipos de florestas, o"
linha10 = "desmatamento, restaurar florestas degradadas e aumentar substancialmente o florestamento e o reflo-"
linha11 = "restamento globalmente."

linha12 = "15.3: Até 2030, combater a desertificação, e restaurar a terra e o solo degradado, incluindo terrenos"
linha13 = "afetados pela desertificação, secas e inundações, e lutar para alcançar um mundo neutro em termos"
linha14 = "de degradação do solo."

linha15 = "15.4: Até 2030, assegurar a conservação dos ecossistemas de montanha, incluindo a sua biodiver-"
linha16 = "sidade, para melhorar a sua capacidade de proporcionar benefícios, que são essenciais para o desen-"
linha17 = "volvimento sustentável."

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    #Adicionando cor ao fundo da tela
    fundo_tela(tela)

    #Botões avançar e voltar    
    botoes_avancar_voltar(tela)

    #Definindo as fontes, tamanhos e atribuindo a variavéis
    fonteSys_linha = fonte_linha()
    fonteSys_titulo = fonte_titulo()

    #Adicionando o resumo e o título a tela e formatando(qual o texto, se serrilhado, cor)
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
    tela.blit(titulo_tela,(240,15))
    tela.blit(linha1_tela,(20,50))
    tela.blit(linha2_tela,(10,70))
    tela.blit(linha3_tela,(10,90))

    tela.blit(linha4_tela,(20,115))
    tela.blit(linha5_tela,(10,135))
    tela.blit(linha6_tela,(10,155))
    tela.blit(linha7_tela,(10,175))

    tela.blit(linha8_tela,(15,205))
    tela.blit(linha9_tela,(20,225))
    tela.blit(linha10_tela,(10,245))
    tela.blit(linha11_tela,(10,265))
    
    tela.blit(linha12_tela,(20,295))
    tela.blit(linha13_tela,(10,315))
    tela.blit(linha14_tela,(10,335))

    tela.blit(linha15_tela,(20,365))
    tela.blit(linha16_tela,(10,385))
    tela.blit(linha17_tela,(10,405))
    
    #Atualizando tela
    atualiza()