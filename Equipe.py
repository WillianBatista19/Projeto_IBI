# Importando a biblioteca
import pygame, sys
from pygame.locals import *

# Iniciando pygame
pygame.init()

# Criando a tela e definindo seu tamanho
larguraTela, alturaTela = (640, 480)
tela = pygame.display.set_mode((larguraTela, alturaTela))

# Delimitando o local de surgimento do botão
# Rect(left, top, width, height)
botaoMenu= pygame.Rect(20, 415, 150, 45)
setaEsquerda = pygame.Rect(10, 280, 45, 45)
setaDireita = pygame.Rect(580, 280, 45, 45)

# Colocando um nome para a janela
pygame.display.set_caption("Equipe")

# Colocando cores
verdeEscuro = (2, 30, 1)
verdeEsc = (12, 63, 3)
verde = (38, 117, 1)
verdeClaro = (105, 189, 16)
marrom = (88, 42, 3)
branco = (255, 255, 255) 
preto = (0, 0, 0)

# Adicionando fonte
# SysFont(name, size, bold=False, italic=False) -> Font
fonte = pygame.font.SysFont('Times New Roman', 20)

# Adicionando texto
# render(text, antialias, color, background=None) -> Surface
nomeEquipe = fonte.render("Nome da Equipe", True, preto)
nomeDavid = fonte.render("David Waters Teixeira Rodrigues", True, preto)
nomeRafael = fonte.render("Rafael Pereira de Souza", True, preto)
nomeVicente = fonte.render("Vicente de Paulo Vidal Alencar", True, preto)
nomeVictor = fonte.render("Victor Jerrysson Gama Bastos", True, preto)
nomeWillian = fonte.render("Willian Alves Batista", True, preto)
funcaoDavid = fonte.render("Função: menu inicial", True, preto)
funcaoRafael = fonte.render("Função: tela da equipe", True, preto)
funcaoVicente = fonte.render("Função: tela sobre", True, preto)
funcaoVictor = fonte.render("Função: jogo", True, preto)
funcaoWillian = fonte.render("Função: jogo", True, preto)
emailDavid = fonte.render("Email: davidwaters503@gmail.com", True, preto)
emailRafael = fonte.render("Email: rafaelpereirasouza15@gmail.com", True, preto)
emailVicente = fonte.render("Email: vicente050paulo@gmail.com", True, preto)
emailVictor = fonte.render("Email: victorjerrysson@gmail.com", True, preto)
emailWillian = fonte.render("Email: willianmoreira.2000.19@gmail.com", True, preto)
menu = fonte.render("Menu", True, preto)

# Carregando as imagens dos membros da equipe
imagemDavid = pygame.image.load("imagens/David.jpeg")
imagemRafael = pygame.image.load("imagens/Rafael.jpeg")
imagemVicente = pygame.image.load("imagens/Vicente.jpeg")
imagemVictor = pygame.image.load("imagens/Victor.jpeg")
imagemWillian = pygame.image.load("imagens/Willian.jpeg")
imagem_fundo = pygame.image.load("imagens/bg2.png") 

# Alterando o tamanho das imagens
fotoDavid = pygame.transform.scale(imagemDavid, (150, 130))
fotoRafael = pygame.transform.scale(imagemRafael, (150, 130))
fotoVicente = pygame.transform.scale(imagemVicente, (150, 130))
fotoVictor = pygame.transform.scale(imagemVictor, (150, 130))
fotoWillian = pygame.transform.scale(imagemWillian, (150, 130))
imagem_fundo = pygame.transform.scale(imagem_fundo, (640, 480))

# Definindo uma logo (32x32) para a janela
logo = pygame.image.load("imagens/logo.png")
pygame.display.set_icon(logo)

# Transforma o cursor em uma mão
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

# Carrega o arquivo de som
#pygame.mixer.music.load("som/Ednaldo-Pereira-beatbox-animado.ogg")

# Toca a som carregada (loop = -1 para tocar repetidamente)
#pygame.mixer.music.play(-1)

# Define o volume do som
#pygame.mixer.music.set_volume(1.0)

# Função da telaEquipe
def telaEquipe():
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
                    pygame.quit()
                if x_mouse > 580 and y_mouse > 280 and x_mouse < (580 + 45) and y_mouse < (280 + 45):
                    telaEquipe2()

        # Colocando imagens na tela
        tela.blit(imagem_fundo, (0, 0))
        tela.blit(fotoDavid, (10, 70))
        
        # Colocando o botão(retângulo) na tela
        pygame.draw.rect(tela, verde, botaoMenu)
        pygame.draw.rect(tela, verde, setaDireita)
                
        # Adicionando texto na superfície e escolhendo o local
        tela.blit(nomeEquipe, (larguraTela/2.5, 0))
        tela.blit(nomeDavid, (10, 50))
        tela.blit(funcaoDavid, (10, 200))   
        tela.blit(emailDavid, (10, 225))
        tela.blit(menu, (73, 425))

        # Atualizando a tela
        pygame.display.update()

def telaEquipe2():
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
                    pygame.quit()
                if x_mouse > 580 and y_mouse > 280 and x_mouse < (580 + 45) and y_mouse < (280 + 45):
                    telaEquipe3()
                if x_mouse > 10 and y_mouse > 280 and x_mouse < (10 + 45) and y_mouse < (280 + 45):
                    telaEquipe()
                
        # Colocando imagens na tela
        tela.blit(imagem_fundo, (0, 0))
        tela.blit(fotoRafael, (10, 70))

        # Colocando o botão(retângulo) na tela
        pygame.draw.rect(tela, verde, botaoMenu)
        pygame.draw.rect(tela, verde, setaDireita)
        pygame.draw.rect(tela, verde, setaEsquerda)

        # Adicionando texto na superfície e escolhendo o local
        tela.blit(nomeEquipe, (larguraTela/2.5, 0))
        tela.blit(nomeRafael, (10, 50))
        tela.blit(funcaoRafael, (10, 200))   
        tela.blit(emailRafael, (10, 225))
        tela.blit(menu, (73, 425))

        # Atualizando a tela
        pygame.display.update()

def telaEquipe3():
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
                    pygame.quit()
                if x_mouse > 580 and y_mouse > 280 and x_mouse < (580 + 45) and y_mouse < (280 + 45):
                    telaEquipe4()
                if x_mouse > 10 and y_mouse > 280 and x_mouse < (10 + 45) and y_mouse < (280 + 45):
                    telaEquipe2()

        # Colocando imagens na tela
        tela.blit(imagem_fundo, (0, 0))
        tela.blit(fotoVicente, (10, 70))
        
        # Colocando o botão(retângulo) na tela
        pygame.draw.rect(tela, verde, botaoMenu)
        pygame.draw.rect(tela, verde, setaDireita)
        pygame.draw.rect(tela, verde, setaEsquerda)

        # Adicionando texto na superfície e escolhendo o local
        tela.blit(nomeEquipe, (larguraTela/2.5, 0))
        tela.blit(nomeVicente, (10, 50))
        tela.blit(funcaoVicente, (10, 200))   
        tela.blit(emailVicente, (10, 225))
        tela.blit(menu, (73, 425))

        # Atualizando a tela
        pygame.display.update()

def telaEquipe4():
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
                    pygame.quit()
                if x_mouse > 580 and y_mouse > 280 and x_mouse < (580 + 45) and y_mouse < (280 + 45):
                    telaEquipe5()
                if x_mouse > 10 and y_mouse > 280 and x_mouse < (10 + 45) and y_mouse < (280 + 45):
                    telaEquipe3()

        # Colocando imagens na tela
        tela.blit(imagem_fundo, (0, 0))
        tela.blit(fotoVictor, (10, 70))
        
        # Colocando o botão(retângulo) na tela
        pygame.draw.rect(tela, verde, botaoMenu)
        pygame.draw.rect(tela, verde, setaDireita)
        pygame.draw.rect(tela, verde, setaEsquerda)

        # Adicionando texto na superfície e escolhendo o local
        tela.blit(nomeEquipe, (larguraTela/2.5, 0))
        tela.blit(nomeVictor, (10, 50))
        tela.blit(funcaoVictor, (10, 200))   
        tela.blit(emailVictor, (10, 225))
        tela.blit(menu, (73, 425))

        # Atualizando a tela
        pygame.display.update()

def telaEquipe5():
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
                    pygame.quit()
                if x_mouse > 10 and y_mouse > 280 and x_mouse < (10 + 45) and y_mouse < (280 + 45):
                    telaEquipe4()
        
        # Colocando imagens na tela
        tela.blit(imagem_fundo, (0, 0))
        tela.blit(fotoWillian, (10, 70))

        # Colocando o botão(retângulo) na tela
        pygame.draw.rect(tela, verde, botaoMenu)
        pygame.draw.rect(tela, verde, setaEsquerda)

        # Adicionando texto na superfície e escolhendo o local
        tela.blit(nomeEquipe, (larguraTela/2.5, 0))
        tela.blit(nomeWillian, (10, 50))
        tela.blit(funcaoWillian, (10, 200))   
        tela.blit(emailWillian, (10, 225))
        tela.blit(menu, (73, 425))

        # Atualizando a tela
        pygame.display.update()

# Invocando a função          
telaEquipe()