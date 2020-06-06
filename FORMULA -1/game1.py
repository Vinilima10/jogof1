import pygame
from random import randint

pygame.init()
x = 490  #minimo 255 maximo 550
y = 350   #min 0 maximo 400
pos_x = 300
pos_y = 0
pos2_x = 450
pos2_y = -1000
timer = 0
tempo_segundo = 0

velocidade = 7
velocidade_outros = 6
velocidade_outros2 = 6

vidas = 3


fundo = pygame.image.load('ROAD.png')
carro = pygame.image.load('CAR.png')
carro2 = pygame.image.load('CAR2.png')
carro3 = pygame.image.load('CAR3.png')

font = pygame.font.SysFont('arial black', 30)
texto = font.render('Pontos: ', True,  (255, 255, 255), (0,0,0))
texto2 = font.render('Vidas: ', True,  (255, 0, 0), (0,0,0))
pos_texto = texto.get_rect()
pos_texto2 = texto2.get_rect()
pos_texto.center = (65,50)
pos_texto2.center = (53,90)



#TAMANHO DA JANELA
janela = pygame.display.set_mode((902,543))
pygame.display.set_caption('FORMULA 1 OSASCOCORP LMTD©')

janela_aberta = True
while janela_aberta :
    pygame.time.delay(10)#FRAMES DA TELA

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         janela_aberta = False
    
    comandos = pygame.key.get_pressed()# COMANDOS DE MOVIMENTACAO
    if comandos[pygame.K_UP] and y >= 0:
        y-= velocidade
    if comandos[pygame.K_DOWN] and y <= 400:
        y+= velocidade
    if comandos[pygame.K_RIGHT] and x<= 550:
        x+= velocidade
    if comandos[pygame.K_LEFT] and x>= 255:
        x-= velocidade    

    #DETECTA COLISAO
    if (x +55 > pos2_x - 100  and y  + 153  > pos2_y):
        vidas = vidas - 1
        texto2 = font.render('Vidas: ' + str(vidas), True,  (255, 255, 255), (0,0,0))
    
    if  (pos_y >= 1000):
        pos_y = randint(-1000,-200)
        

    if (pos2_y>= 1000):
        pos2_y = randint(-1000,-300)
   
    if (timer <20):
        timer +=1
    else:
        tempo_segundo +=1
        texto = font.render('Pontos: ' + str(tempo_segundo), True,  (255, 255, 255), (0,0,0))
        timer = 0


    
        

    pos_y += velocidade_outros
    pos2_y += velocidade_outros2

    janela.blit(fundo,(0, 0))# fundo
    janela.blit(carro,(x, y))#carro
    janela.blit(carro2,(pos_x, pos_y))
    janela.blit(carro3,(pos2_x, pos2_y))
    janela.blit(texto,pos_texto)
    janela.blit(texto2,pos_texto2)

    pygame.display.update()


pygame.quit()
