import sys, pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Perguntas Sobre Redes")

Bebas_Font = pygame.font.Font('Font/BEBAS-REGULAR.otf', 40)

Genuine = pygame.font.Font('Font/GENUINE.TTF', 52)

config = pygame.image.load('Imagens/gear.svg')

question = pygame.image.load('Imagens/questao.svg')

black = (0, 0, 0)
red = (255, 0, 0)
blue = (109,144,202)
white = (255,255,255)

dark_blue = (42,58,93)
bright_green = (0, 255, 0)

def interface():
    while True:
        screen.fill((white))

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(mouse):
                    choose_level()

        def iniciar(x, y):
            score = Bebas_Font.render("Iniciar", True, black)
            screen.blit(score, (x, y))
        
        def cadastrar(x, y):
            score = Bebas_Font.render("Cadastrar", True, black)
            screen.blit(score, (x, y))

        def titulo(x, y):
            score = Genuine.render("TI   LEARNING", True, black)
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

        screen.blit(question, (730, 20))
        screen.blit(config, (20, 20))
        iniciar(200, 325)
        cadastrar(475, 325)
        titulo(270, 100)

        pygame.display.update()

def choose_level():
    while True:
        screen.fill((white))

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        def redes(x, y):
                score = Bebas_Font.render("Redes", True, black)
                screen.blit(score, (x, y))
        
        def python(x, y):
                score = Bebas_Font.render("Python", True, black)
                screen.blit(score, (x, y))
        
        def SQL(x, y):
                score = Bebas_Font.render("SQL", True, black)
                screen.blit(score, (x, y))
        
        def escolha(x, y):
                score = Genuine.render("ESCOLHA UM TEMA", True, black)
                screen.blit(score, (x, y))

        button1 = pygame.Rect(300, 150, 200, 100)
        pygame.draw.rect(screen, blue, (300, 150, 200, 100))

        button2 = pygame.Rect(300, 265, 200, 100)
        pygame.draw.rect(screen, blue, (300, 265, 200, 100))

        button3 = pygame.Rect(300, 380, 200, 100)
        pygame.draw.rect(screen, blue, (300, 380, 200, 100))

        if 300+200 > mouse[0] > 300 and 150+100 > mouse[1] > 150:
            def redes(x, y):
                score = Bebas_Font.render("Redes", True, white)
                screen.blit(score, (x, y))
            pygame.draw.rect(screen, dark_blue, (300, 150, 200, 100))
        
        if 300+200 > mouse[0] > 300 and 265+100 > mouse[1] > 265:
            def python(x, y):
                score = Bebas_Font.render("Python", True, white)
                screen.blit(score, (x, y))
            pygame.draw.rect(screen, dark_blue, (300, 265, 200, 100))
        
        if 300+200 > mouse[0] > 300 and 380+100 > mouse[1] > 380:
            def SQL(x, y):
                score = Bebas_Font.render("SQL", True, white)
                screen.blit(score, (x, y))
            pygame.draw.rect(screen, dark_blue, (300, 380, 200, 100))
        
        redes(360, 175)
        python(350, 290)
        SQL(375, 405)
        escolha(215, 50)

        pygame.display.update()

interface()