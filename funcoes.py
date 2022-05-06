import pygame
from pygame.locals import *

pygame.font.init()

'''# Definindo cores
cor_azulClaro = (0, 128, 255)
cor_verdeClaro = (0, 255, 0)
cor_vermelho = (255, 0, 0)
cor_azul = (0, 0, 255)
cor_rosa = (255, 0, 128)
cor_roxo = (128, 0, 128)
cor_cinza = (192, 192, 192)
cor_branco = (255, 255, 255)
cor_preto = (0, 0, 0)'''

# Tamanho da tela padrão dos menus
def tamanho_tela():
    largura = 640
    altura = 480
    tela = pygame.display.set_mode((largura,altura))
    return tela
def tamanho_telaJogoJerry():
    largura = 800
    altura = 600
    tela = pygame.display.set_mode((largura,altura))
    return tela
def tamanho_telaJogoWill():
    largura = 560
    altura = 750
    tela = pygame.display.set_mode((largura,altura))
    return tela

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def fundo_tela(tela):
    tela.fill((192,192,192))

# Aplica um nome a tela
def nome_tela(nome):
    pygame.display.set_caption(nome)    

# Fonte padrão e tamanho padrão dos textos
def fonte_linha():
    fonteSys_linha = pygame.font.SysFont("Times New Roman", 16)
    return fonteSys_linha

# Fonte padrão e tamanho padrão para os títulos
def fonte_titulo():
    fonteSys_titulo = pygame.font.SysFont("Times New Roman", 18)
    return fonteSys_titulo

# Fonte padrão e tamanho padrão para os títulos
def fonte_titulo_inicial():
    fonteSys_titulo = pygame.font.SysFont("Times New Roman", 35, bold=True, italic=False)
    return fonteSys_titulo

def fonte_titulo_equipe():
    fonteSys_titulo = pygame.font.SysFont("Times New Roman", 20)
    return fonteSys_titulo

# Atualiza a tela, por estar em um while ela sempre é atualizada
def atualiza():
    pygame.display.update()
