import sys, pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Perguntas Sobre Redes")

Bebas_Font = pygame.font.Font('Font/BEBAS-REGULAR.otf', 40)

config = pygame.image.load('Imagens/gear.svg')

black = (0, 0, 0)
red = (255, 0, 0)
blue = (109,144,202)
white = (255,255,255)

dark_blue = (42,58,93)
bright_green = (0, 255, 0)

def interface():
    while True:
        screen.fill((white))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(mouse):
                    start_game()

        mouse = pygame.mouse.get_pos()

        def iniciar(x, y):
            score = Bebas_Font.render("Iniciar", True, black)
            screen.blit(score, (x, y))
        
        def cadastrar(x, y):
            score = Bebas_Font.render("Cadastrar", True, black)
            screen.blit(score, (x, y))

        def titulo(x, y):
            score = Bebas_Font.render("[TITULO]", True, black)
            screen.blit(score, (x, y))

        button1 = pygame.Rect(150, 300, 200, 100)
        pygame.draw.rect(screen, blue, (150, 300, 200, 100))

        button2 = pygame.Rect(450, 300, 200, 100)
        pygame.draw.rect(screen, blue, (450, 300, 200, 100))

        if 150+200 > mouse[0] > 150 and 300+100 > mouse[1] > 300:
            def iniciar(x, y):
                score = Bebas_Font.render("Iniciar", True, white)
                screen.blit(score, (x, y))
            pygame.draw.rect(screen, dark_blue, (150, 300, 200, 100))
        
        if 450+200 > mouse[0] > 450 and 300+100 > mouse[1] > 300:
            def cadastrar(x, y):
                score = Bebas_Font.render("Cadastrar", True, white)
                screen.blit(score, (x, y))
            pygame.draw.rect(screen, dark_blue, (450, 300, 200, 100))

        screen.blit(config, (20, 20))
        iniciar(200, 325)
        cadastrar(475, 325)
        titulo(340, 100)

        pygame.display.update()

interface()