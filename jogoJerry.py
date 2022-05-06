import pygame
from pygame.locals import *
from sys import exit
from random import *

pygame.init()

LARGURA = 800
ALTURA = 600

marrom_claro = (188, 94, 0)
marrom = (88,42,3)
verde_claro = (38,117,1)

fogo_x = randint(800, 950)
gota_x = randint(900, 960)

while gota_x == fogo_x or gota_x < fogo_x - 90:
    fogo_x = randint(800, 950)
    gota_x = randint(900, 960)

end_game = False

velocidade_jogo = 10

#CONSTANTE ARMAZENANDO A POSIÇÃ O Y DO CHÃO
pos_chao = ALTURA - 195

pulo = False

vida = 3
pontos = 0
fonte = pygame.font.SysFont('comicsansms', 40, bold=True, italic=False)#VARIÁVEL COM O TIPO DE FONTE

#DECLARANDO VARIÁVEL QUE ARMAZENARÁ A IMAGEM DE FUNDO
fundo = pygame.image.load("imagens/Burning Forest Background.jpg")

#DECLARANDO VARIÁVEL QUE ARMAZENARÁ O SOM DE VITÓRIA
som_vitoria = pygame.mixer.Sound('sons/Victory Sound.wav')
som_vitoria.set_volume(0.2)

#DECLARANDO VARIÁVEL QUE ARMAZENARÁ O SOM DE COLISÃO
som_colisao = pygame.mixer.Sound('sons/smw_yoshi_spit.wav')
som_colisao.set_volume(1.0)

#DECLARANDO VARIÁVEL QUE ARMAZENARÁ O SOM DOS PONTOS
som_pontos = pygame.mixer.Sound('sons/gota.ogg')
som_pontos.set_volume(1.0)

#VÁRIAVEL RECEBENDO O 'CLOCK' DO JOGO
relogio = pygame.time.Clock()
tela = pygame.display.set_mode((LARGURA,ALTURA))
tela_Endgame = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("Jogo Horizontal")

sprite_sheet_aventureiro = pygame.image.load('sprites/MainGuySpriteSheet_2.png')
sprite_aventureiroFront = pygame.image.load('sprites/PrincipalFront.png')

class Aventureiro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites_aventureiro = []
        for i in range(3):
            img = sprite_sheet_aventureiro.subsurface((i * 41,0), (41,36))
            img = pygame.transform.scale(img, (41*2, 36*2))
            self.sprites_aventureiro.append(img)
        self.index_lista = 0
        self.image = self.sprites_aventureiro[self.index_lista]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = 60, ALTURA - 90
        self.pos_y_inicial = ALTURA - 90 - 46//2
        self.pulo = False

    def pular(self):
        self.pulo = True

    def update(self):

        if self.pulo == True:
            self.rect.y -= 20
            if self.rect.y <= 240:
                self.pulo = False
        else:
            if self.rect.y < self.pos_y_inicial:
                self.rect.y += 20
            else:
                self.rect.y = self.pos_y_inicial

        self.index_lista += 0.05
        if self.index_lista >= 3:
            self.index_lista = 0
        self.image = self.sprites_aventureiro[int(self.index_lista)]

class AventureiroFront(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites_aventureiro = []
        for i in range(3):
            img = sprite_aventureiroFront.subsurface((i * 41,0), (41,36))
            img = pygame.transform.scale(img, (41*2, 36*2))
            self.sprites_aventureiro.append(img)
        self.index_lista = 0
        self.image = self.sprites_aventureiro[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = 410, 400
        self.pos_y_inicial = ALTURA - 90 - 46//2

    def update(self):

        self.index_lista += 0.1
        if self.index_lista >= 3:
            self.index_lista = 0
        self.image = self.sprites_aventureiro[int(self.index_lista)]

class Fogo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/fire_0.png'))
        self.sprites.append(pygame.image.load('sprites/fire_1.png'))
        self.sprites.append(pygame.image.load('sprites/fire_2.png'))
        self.sprites.append(pygame.image.load('sprites/fire_3.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (32*3, 32*3))

        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = LARGURA, ALTURA - 70
        self.pulo = False

    def pular(self):
        self.pulo = True

    def update(self):
        if self.pulo == True:
            self.rect.y -= 20
            if self.rect.y <= 200:
                self.pulo = False
        self.atual += 0.2
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (32*3, 32*3))

        if self.rect.topright[0] < 0:
            self.rect.x = fogo_x
        self.rect.x -= velocidade_jogo

class Gota(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = pygame.image.load('sprites/gota.png')
        self.image = self.sprite
        self.image = pygame.transform.scale(self.image, (32*2, 32*2))

        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = LARGURA + 150, ALTURA - 70

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = gota_x
        self.rect.x -= velocidade_jogo

def exibe_mensagem(msg, tamanho, cor):
    fonte = pygame.font.SysFont('comicsansms', tamanho, True, False)
    mensagem = f'{msg}'
    texto_formatado = fonte.render(mensagem, True, cor)
    return texto_formatado

def reiniciar_jogo():
    global pontos, vida, end_game, velocidade_jogo
    pontos = 0
    vida = 3
    velocidade_jogo = 10
    end_game = False
    fogo.rect.x = LARGURA
    gota.rect.x = gota_x
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1.0)

def fadeOut(width, height): 
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        todas_as_sprites.draw(tela)
        tela.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)

def fadeOutEndgame(width, height):
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 200):
        fade.set_alpha(alpha)
        tela.blit(fade, (0,0))
        pygame.display.flip()
        pygame.time.delay(5)

def fadeIn(width,height):
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 100):
        fade.set_alpha(200 - alpha)
        tela.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)

todas_as_sprites = pygame.sprite.Group()
grupo_vitoria = pygame.sprite.Group()
grupo_inimigo = pygame.sprite.Group()
grupo_pontuacao = pygame.sprite.Group()


principal = Aventureiro()
principalFront = AventureiroFront()
fogo = Fogo()
gota = Gota()

todas_as_sprites.add(principal)
todas_as_sprites.add(fogo)
todas_as_sprites.add(gota)
grupo_vitoria.add(principalFront)

grupo_inimigo.add(fogo)
grupo_pontuacao.add(gota)

#DEF DO LOOP PRINCIPAL
def telaPrincipal():
    pygame.display.set_caption("Jogo I")

    global velocidade_jogo
    pygame.mixer.music.load('sons/Firescape.ogg')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1.0)

    tela_x = 0
    while True:
        relogio.tick(40)#FPS
        tela.blit(fundo, (0,0))

        #EFEITO DE MOVIMENTO DO BACKGROUND
        rel_x = tela_x % fundo.get_rect().width
        tela.blit(fundo, (rel_x - fundo.get_rect().width, 0))
        if  rel_x < LARGURA:
            tela.blit(fundo, (rel_x, 0))
        tela_x -= 5

        #MENSAGENS DA TELA
        global pontos,vida
        mensg_vida = f'VIDA: {vida}'
        mensg_pontos = f'PONTOS: {pontos}'
        texto_vida = fonte.render(mensg_vida, True, verde_claro)
        texto_pontos = fonte.render(mensg_pontos, True, marrom_claro)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_r and end_game == True:
                    reiniciar_jogo()
                if event.key == K_SPACE:
                    if principal.rect.y != principal.pos_y_inicial:
                        pass
                    else:
                        principal.pular()
    
        #CHECANDO SE O PERSONAGEM ESTÁ COM 0 DE VIDA / VENCEU O JOGO
        if vida <= 0:
            fadeOut(800,600)
            pygame.mixer.music.stop()
            telaGameover()
        
        elif pontos == 5:
            fadeOut(800,600)
            pygame.mixer.music.stop()
            telaVenceu()
        else:
            todas_as_sprites.update()

        todas_as_sprites.draw(tela)

        #COLISÃO ENTRE O RETÂNGULO E A SPRITE FOGO

        colisao_fogo = pygame.sprite.spritecollide(principal, grupo_inimigo, False, pygame.sprite.collide_mask)
        colisao_gota = pygame.sprite.spritecollide(principal, grupo_pontuacao, False, pygame.sprite.collide_mask)

        if colisao_fogo:
            fogo_x = randint(800, 950)
            fogo.rect.x = fogo_x
            vida -= 1
            som_colisao.play()

        if colisao_gota:
            gota_x = randint(900, 960)
            gota.rect.x = gota_x
            pontos += 1
            som_pontos.play()
            if velocidade_jogo >= 15:
                velocidade_jogo += 0
            else:
                velocidade_jogo += 2

        tela.blit(texto_vida, (20,40))#MOSTRANDO NA TELA A VIDA DO JOGADOR
        tela.blit(texto_pontos, (20,90))#MOSTRANDO NA TELA A PONTUAÇÃO DO JOGADOR
        pygame.display.flip()

#DEF DA TELA DO VENCEDOR
def telaVenceu():
    fundo = pygame.image.load("imagens/tilesetOpenGameBackground.png")
    tela_Endgame.blit(fundo, (0,0))
    pygame.mixer.music.load('sons/JRPG OST (Rev 2)/17 - Victory.ogg')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1.0)
    fadeIn(800, 600)
    tela_x = 0

    while True:
        tela_Endgame.blit(fundo, (0,0))

        #EFEITO DE MOVIMENTO DO FUNDO
        rel_x = tela_x % fundo.get_rect().width
        tela.blit(fundo, (rel_x - fundo.get_rect().width, 0))
        if  rel_x < LARGURA:
            tela.blit(fundo, (rel_x, 0))
        tela_x -= 5

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    reiniciar_jogo()
                    pygame.mixer.music.stop()
                    fadeOutEndgame(800, 600)
                    telaPrincipal()

        grupo_vitoria.draw(tela)
        grupo_vitoria.update()

        venceu = exibe_mensagem(' VOCÊ APAGOU O INCÊNDIO', 30, (marrom))
        tela_Endgame.blit(venceu, (200,200))
        restart = exibe_mensagem('Pressione r para reiniciar', 20, (marrom))
        tela_Endgame.blit(restart, (300, 260))

        pygame.display.flip()

#DEF DA TELA DE GAME OVER
def telaGameover():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('sons/JRPG OST (Rev 2)/09 - Z 339 - Here the Deities approve.ogg')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1.0)
    fadeIn(800, 600)

    while True:
        tela_Endgame.blit(fundo, (0,0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    reiniciar_jogo()
                    pygame.mixer.music.stop()
                    fadeOutEndgame(800, 600)
                    telaPrincipal()

        gameover = exibe_mensagem('A FLORESTA ESTÁ EM CINZAS', 30, (255,255,255))
        tela_Endgame.blit(gameover, (150,200))
        restart = exibe_mensagem('Pressione r para reiniciar', 20, (255,255,255))
        tela_Endgame.blit(restart, (300, 260))

        pygame.display.flip()

#EXECUTANDO FUNÇÃO DA TELA PRINCIPAL
#telaPrincipal()