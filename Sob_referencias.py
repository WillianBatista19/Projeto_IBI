import pygame
import funcoes

from funcoes import *
from pygame.locals import *

#Definindo tamanho da tela
tela = tamanho_tela()

#Adicionando nome a tela
nome_tela("Referências")

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
    for event in pygame.event.get():
        if event.type == QUIT:
            event.quit()

    #Fundo de tela
    fundo_tela(tela)

    #Botão voltar
    botao_voltar(tela)

    #botão retorna direto para o menu
    botao_menu(tela)
    
    #Definindo as fontes, tamanhos e atribuindo a variavéis
    linha_Sysfont = fonte_linha()
    titulo_Sysfont = fonte_titulo()

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

    #Atualizando tela
    atualiza()