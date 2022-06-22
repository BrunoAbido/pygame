import pygame
import random
pygame.init()
largura = 1000
altura = 606
tamanho = (largura, altura)
pygameDisplay = pygame.display
pygameDisplay.set_caption("WarPlane")
gameDisplay = pygame.display.set_mode(tamanho)


background = pygame.image.load("assets/background.png")
background_destroy = pygame.image.load("assets/explosao.png")
# Aqui Começa o jogo

explosaoSound = pygame.mixer.Sound("assets/explosao.wav")
explosaoSound.set_volume(1)
black = (0, 0, 0)
white = (255, 255, 255)
clock = pygame.time.Clock()
gameEvents = pygame.event


def dead(pontos):
    gameDisplay.blit(background_destroy, (150, 150)) ## posição da explosão 
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(explosaoSound)
    fonte = pygame.font.Font("freesansbold.ttf", 50)
    fonteContinue = pygame.font.Font("freesansbold.ttf", 25)
    texto = fonte.render("GAME OVER " + "Score: " + str(pontos)
                         , True, black)
    textoContinue = fonteContinue.render(
        "Press enter to continue...", True, white)
    gameDisplay.blit(textoContinue, (50, 200))
    gameDisplay.blit(texto, (50, 100))
    pygameDisplay.update()


def jogo():
    posicaoX = 0
    posicaoY = random.randrange(0, altura)
    direcao = True
    velocidade = 10
    posicaoXaviao = 500
    posicaoYaviao = 100
    movimentoXaviao = 0
    movimentoYaviao = 0
    pontos = 0
    missile = pygame.image.load("assets/missile.png")
    aviao = pygame.image.load("assets/aviao (2).png")
    missile = pygame.transform.flip(missile, True, False)
    pygame.mixer.music.load("assets/trilha.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1)

    missileSound = pygame.mixer.Sound("assets/missile.wav")
    missileSound.set_volume(1)
    pygame.mixer.Sound.play(missileSound)

    alturaaviao = 124
    larguraaviao = 400
    alturaMissel = 52
    larguraMissel = 150
    dificuldade = 50
    jogando = True
    while True:
        # aqui é lido os eventos da tela
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    jogo()
                if event.key == pygame.K_LEFT:
                    movimentoXaviao = - 10
                elif event.key == pygame.K_RIGHT:
                    movimentoXaviao = 10
                elif event.key == pygame.K_UP:
                    movimentoYaviao = -10
                elif event.key == pygame.K_DOWN:
                    movimentoYaviao = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    movimentoXaviao = 0
                    movimentoYaviao = 0

        if jogando == True:
            # travando o movimento na tela
            posicaoXaviao = posicaoXaviao + movimentoXaviao
            posicaoYaviao = posicaoYaviao + movimentoYaviao
            if posicaoXaviao < 0:
                posicaoXaviao = 0
            elif posicaoXaviao >= largura - larguraaviao:
                posicaoXaviao = largura - larguraaviao

            if posicaoYaviao < 0:
                posicaoYaviao = 0
            elif posicaoYaviao >= altura - alturaaviao:
                posicaoYaviao = altura - alturaaviao

            # aqui termina a leitura de eventos
            gameDisplay.blit(background, (0, 0))

            if direcao == True:
                if posicaoX < largura-150:
                    posicaoX = posicaoX + velocidade
                else:
                    pygame.mixer.Sound.play(missileSound)
                    # direcao = False
                    posicaoX = 0
                    posicaoY = random.randrange(0, altura)
                    velocidade = velocidade + 1
                    pontos = pontos + 1
            else:
                if posicaoX >= 0:
                    posicaoX = posicaoX - velocidade
                else:
                    pygame.mixer.Sound.play(missileSound)
                    direcao = True
                    posicaoY = random.randrange(0, altura)
                    velocidade = velocidade + 1
                    missile = pygame.transform.flip(missile, True, False)
                    pontos = pontos + 1

            gameDisplay.blit(missile, (posicaoX, posicaoY))
            gameDisplay.blit(aviao, (posicaoXaviao, posicaoYaviao))
            fonte = pygame.font.Font("freesansbold.ttf", 20)
            texto = fonte.render("Pontos: "+str(pontos), True, white)
            gameDisplay.blit(texto, (20, 20))


            pixelsYAviao = list(
                range(posicaoYaviao, posicaoYaviao + alturaaviao))
            pixelsXAviao = list(
                range(posicaoXaviao, posicaoXaviao + larguraaviao))

            pixelsYMissel = list(range(posicaoY, posicaoY+alturaMissel+1))
            pixelsXMissel = list(range(posicaoX, posicaoX+larguraMissel+1))

            if len(list(set(pixelsYMissel) & set(pixelsYAviao))) > dificuldade:
                if len(list(set(pixelsXMissel) & set(pixelsXAviao))) > dificuldade:
                    jogando = False
                    dead(pontos)

        pygameDisplay.update()
        clock.tick(60)


jogo()