# importando bibliotecas
import pygame, random, sys
from pygame.locals import *

# Criando variáveis da tela e jogo
SCREEN_WIDTH = 560 
SCREEN_HEIGHT = 750
SPEED = 0
GRAVITY = 0
GAME_SPEED = 0
COLIDIR = False
VIDAS = 2

GROUND_WIDTH = 2 * SCREEN_WIDTH
GROUND_HEIGHT = 100

PIPE_WIDTH = 80
PIPE_HEIGHT = 500

PIPE_GAP = 150

tutorial = True

#Adicionando nome na janela
pygame.display.set_caption('IBI - Flappy Bird')

#iniciando fontes de texto np pygame
pygame.font.init()

pontos = 0
#Definindo as primeiras fontes
fonte = pygame.font.SysFont('arial', 40, True, True)

#criando função para mensagens
def exibe_mensagem(msg, tamanho, cor):
    fonte = pygame.font.SysFont('comicsansms', tamanho, True, False)
    mensagem = f'{msg}'
    texto_formatado = fonte.render(mensagem, True, cor)
    return texto_formatado

#Criando classe do pássaro
class Bird(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
#adicionando as imagens do pássaro
        self.images = [pygame.image.load('sprites/redbird-upflap.png').convert_alpha(),
                       pygame.image.load('sprites/redbird-midflap.png').convert_alpha(),
                       pygame.image.load('sprites/redbird-downflap.png').convert_alpha()]
        
        self.speed = SPEED

        self.current_image = 0               

        self.image = pygame.image.load('sprites/redbird-upflap.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
# Adicionando posição do pássaro
        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_WIDTH / 5
        self.rect[1] = SCREEN_HEIGHT / 2

    def update(self):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[ self.current_image ] 

        self.speed +=  GRAVITY

        self.rect[1] += self.speed
# Configurando pulo
    def bump(self):
        self.speed = -SPEED

#Criando classe dos canos
class Pipe(pygame.sprite.Sprite):

    def __init__(self, inverted, xpos, ysize):
        pygame.sprite.Sprite.__init__(self)
# adicionando imagem do cano
        self.image = pygame.image.load('sprites\pipe-red.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (PIPE_WIDTH,PIPE_HEIGHT))
#Adicionando posição do cano 
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
#Adicionado posição do cano invertido
        if inverted:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect[1] = - (self.rect[3] - ysize)
        else:
            self.rect[1] = SCREEN_HEIGHT - ysize
        
        self.mask = pygame.mask.from_surface(self.image)
    
    def update(self):
        self.rect[0] -= GAME_SPEED

#Criando classe do chão
class Ground(pygame.sprite.Sprite):

    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
#Adicionando imagem do chão
        self.image = pygame.image.load('sprites/base.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (GROUND_WIDTH, GROUND_HEIGHT))

        self.mask = pygame.mask.from_surface(self.image)
#Ajustando posição do chão
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = SCREEN_HEIGHT - GROUND_HEIGHT

    def update(self):
        self.rect[0] -= GAME_SPEED
#Apagando chão em desuso
def is_off_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])

#Gerando canos aleatoriamente
def get_random_pipes(xpos):
    size = random.randint(200, 560)
    pipe = Pipe(False, xpos, size)
    pipe_inverted = Pipe(True, xpos, SCREEN_HEIGHT - size - PIPE_GAP)
    return (pipe, pipe_inverted)

#iniciando o pygame e criando sua janela
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#Colocando imagem de fundo
BACKGROUND = pygame.image.load('sprites/fundofloresta.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH,SCREEN_HEIGHT))

#Adicionado pássaro ao jogo
bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)

ground_group = pygame.sprite.Group()
#Adicionado chão ao jogo
for i in range(2):
    ground = Ground(GROUND_WIDTH * i)
    ground_group.add(ground)

pipe_group = pygame.sprite.Group() 
#Adicionado canos ao jogo
for i in range(2):
    pipes = get_random_pipes(SCREEN_WIDTH * i + 700)
    pipe_group.add(pipes[0])
    pipe_group.add(pipes[1])

#Criando função para iniciar o jogo
def iniciar():
    global SPEED, GAME_SPEED, GRAVITY
    SPEED = 10
    GRAVITY = 1
    GAME_SPEED = 10

#Criando função para reiniciar o jogo
def reiniciar_jogo():
    global pontos, SPEED, COLIDIR, GAME_SPEED, GRAVITY, VIDAS, Chances
    VIDAS -= 1

    for i in range(2):
        pipes = get_random_pipes(SCREEN_WIDTH * i + 700)

    pipe_group.add(pipes[0])
    pipe_group.add(pipes[1])
    bird.rect.y = SCREEN_HEIGHT/2
    bird.rect.x = SCREEN_WIDTH/5
    pipe_group.remove(pipe_group.sprites()[0])
    pipe_group.remove(pipe_group.sprites()[0])
    SPEED = 10
    GRAVITY = 1
    GAME_SPEED = 10
    COLIDIR = False
#Para ajuste de fps
clock = pygame.time.Clock()

#Criando laço principal do jogo
while True:
    pygame.display.set_caption("Jogo II")

    clock.tick(30)
    #Criando eventos/ ajustes de botões
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                bird.bump()    

            if event.key == K_i:
                tutorial = False
                iniciar()

            if event.key == K_r and SPEED == 0 and VIDAS > 0:
                reiniciar_jogo()

            if event.key == K_s and VIDAS == 0:
                pygame.quit()
                sys.exit()
    
    pygame.font.init()
    mensagem = f'{pontos}'
    texto_formatado = fonte.render(mensagem, False, (255,255,255))
    screen.blit(BACKGROUND, (0,0))

#Preparando mensagens ('texto', tamanho, (Cor))
    ensinar = exibe_mensagem('Aperte a tecla Space para pular', 20, (0,0,0))
    aperte_i = exibe_mensagem('Aperte I para começar', 20, (0,0,0))
    game_over = pygame.image.load('sprites/gameover.png')
    restart = exibe_mensagem('Pressione R para reiniciar', 20, (0,0,0))
    Chances = exibe_mensagem(f'Você tem {VIDAS} Chances', 20, (0,0,0))
# Configurando Fim de Jogo    
    if VIDAS == 0:
        restart = exibe_mensagem('Pressione S para sair', 20, (0,0,0))
        Chances = exibe_mensagem('Suas chances acabaram', 20, (0,0,0))
        pass

#Configurando pausa de inicio de jogo   
    if (tutorial == True):
        screen.blit(aperte_i, (155, 570))  
        screen.blit(ensinar, (110, 600))

#Removendo chão de fora da tela
    if is_off_screen(ground_group.sprites()[0]):
        ground_group.remove(ground_group.sprites()[0])

#Gerando novo chão na tela
        new_ground = Ground(GROUND_WIDTH - 20)
        ground_group.add(new_ground)

#Removendo canos de fora da tela
    if is_off_screen(pipe_group.sprites()[0]):
        pipe_group.remove(pipe_group.sprites()[0])  
        pipe_group.remove(pipe_group.sprites()[0])  

#Gerando novos canos na tela
        pipes = get_random_pipes(SCREEN_WIDTH * 2)

        pipe_group.add(pipes[0])
        pipe_group.add(pipes[1])

#Adicionando pontos no placar
        pontos += 1

#Desenhando pássaro,canos e chão na tela
    bird_group.draw(screen)
    pipe_group.draw(screen)
    ground_group.draw(screen)

#Criando siuação de colisão
    if (pygame.sprite.groupcollide(bird_group, ground_group, False, False, pygame.sprite.collide_mask) or pygame.sprite.groupcollide(bird_group, pipe_group, False, False, pygame.sprite.collide_mask)):
        COLIDIR = True

    if (COLIDIR == True):    
        screen.blit(game_over, (300, 400))
        screen.blit(restart, (300, 460))
        screen.blit(Chances, (300, 490))
        SPEED = 0
        GRAVITY = 0
        GAME_SPEED = 0
        pass
    else:
        bird_group.update()
        ground_group.update()
        pipe_group.update()

#Atualizando tela do jogo
    screen.blit(texto_formatado, (20, 20))
    pygame.display.update()