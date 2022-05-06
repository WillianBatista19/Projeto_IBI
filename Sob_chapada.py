import pygame
import funcoes

from funcoes import *
from pygame.locals import *

#Definindo tamanho da tela
tela = tamanho_tela()

#Adicionando nome a tela
nome_tela("Chapada do Araripe")

titulo = "Informações Chapada do Araripe"
linha1 = "A Chapada do Araripe é uma formação geográfica que abrange os estados do Ceará, Piauí e Per-"
linha2 = "nambuco, caracteriza-se por oferecer uma enorme quantidade de riquezas fósseis, vegetais e animais, contribuindo"
linha3 = "para a formação de aquíferos que abastecem as localidades. Formando um clima tropical úmido mas"
linha4 = "com chuvas irregulares, sendo as mais significativas durante o mês de fevereiro."

linha5 = "Abriga uma fauna e flora destacáveis, criando um microclima local no semiárido, com uma flora"
linha6 = "forte capaz de sustentar o solo e evitar deslizamentos, em conjunto com sua fauna trabalham em e-"
linha7 = "quilíbrio para manter o ecossistema local, de onde várias pessoas tiram sua renda, remédios ou ou-"
linha8 = "tros recursos."

linha9 = "A quantidade de vestígios arqueológicos surpreende também pela sua qualidade, com rochas de"
linha10 = "cerca de 110 milhões de anos que conservam diversos animais, sendo os grupos de fósseis mais en-"
linha11 = "contrados: vegetais, invertebrados, peixes anfíbios, quelônios, Pterossauros e outros dinossauros."

linha12 = "A região abriga o Parque dos Pterossauros, a quatro quilômetros de Santana do Cariri, com répli-"
linha13 = "cas artísticas desses répteis; sendo um terço de todos os exemplares fósseis já achados dessa ave,"
linha14 = "presente na Chapada do Araripe."

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

    tela.blit(titulo_tela,(200,40))
    tela.blit(linha1_tela,(20,70))
    tela.blit(linha2_tela,(10,90))
    tela.blit(linha3_tela,(10,110))
    tela.blit(linha4_tela,(10,130))
    
    tela.blit(linha5_tela,(20,160))
    tela.blit(linha6_tela,(10,180))
    tela.blit(linha7_tela,(10,200))
    tela.blit(linha8_tela,(10,220))
    
    tela.blit(linha9_tela,(20,250))
    tela.blit(linha10_tela,(10,270))
    tela.blit(linha11_tela,(10,290))

    tela.blit(linha12_tela,(20,320))
    tela.blit(linha13_tela, (10,340))
    tela.blit(linha14_tela, (10,360))

    #Atualizar tela
    atualiza()