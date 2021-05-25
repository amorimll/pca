import sys, pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Perguntas Sobre Redes")

Bebas_Font = pygame.font.Font('Font/BEBAS-REGULAR.otf', 40)

Genuine = pygame.font.Font('Font/GENUINE.TTF', 52)

Berlin = pygame.font.Font('Font/BRLNSR.TTF', 30)

pontosFont = pygame.font.Font('Font/BRLNSR.TTF', 20)

config = pygame.image.load('Imagens/gear.svg')

question = pygame.image.load('Imagens/questao.svg')

pontosCount = 0

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
            font = Bebas_Font.render("Iniciar", True, black)
            screen.blit(font, (x, y))
        
        def cadastrar(x, y):
            font = Bebas_Font.render("Cadastrar", True, black)
            screen.blit(font, (x, y))

        def titulo(x, y):
            font = Genuine.render("TI   LEARNING", True, black)
            screen.blit(font, (x, y))

        button1 = pygame.Rect(150, 300, 200, 100)
        pygame.draw.rect(screen, blue, (150, 300, 200, 100))

        button2 = pygame.Rect(450, 300, 200, 100)
        pygame.draw.rect(screen, blue, (450, 300, 200, 100))

        if 150+200 > mouse[0] > 150 and 300+100 > mouse[1] > 300:
            def iniciar(x, y):
                font = Bebas_Font.render("Iniciar", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (150, 300, 200, 100))
        
        if 450+200 > mouse[0] > 450 and 300+100 > mouse[1] > 300:
            def cadastrar(x, y):
                font = Bebas_Font.render("Cadastrar", True, white)
                screen.blit(font, (x, y))
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
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button2.collidepoint(mouse):
                    python_level_pergunta_1()

        
        def redes(x, y):
                font = Bebas_Font.render("Redes", True, black)
                screen.blit(font, (x, y))
        
        def python(x, y):
                font = Bebas_Font.render("Python", True, black)
                screen.blit(font, (x, y))
        
        def SQL(x, y):
                font = Bebas_Font.render("SQL", True, black)
                screen.blit(font, (x, y))
        
        def escolha(x, y):
                font = Genuine.render("ESCOLHA UM TEMA", True, black)
                screen.blit(font, (x, y))

        button1 = pygame.Rect(300, 150, 200, 100)
        pygame.draw.rect(screen, blue, (300, 150, 200, 100))

        button2 = pygame.Rect(300, 265, 200, 100)
        pygame.draw.rect(screen, blue, (300, 265, 200, 100))

        button3 = pygame.Rect(300, 380, 200, 100)
        pygame.draw.rect(screen, blue, (300, 380, 200, 100))

        if 300+200 > mouse[0] > 300 and 150+100 > mouse[1] > 150:
            def redes(x, y):
                font = Bebas_Font.render("Redes", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (300, 150, 200, 100))
        
        if 300+200 > mouse[0] > 300 and 265+100 > mouse[1] > 265:
            def python(x, y):
                font = Bebas_Font.render("Python", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (300, 265, 200, 100))
        
        if 300+200 > mouse[0] > 300 and 380+100 > mouse[1] > 380:
            def SQL(x, y):
                font = Bebas_Font.render("SQL", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (300, 380, 200, 100))
        
        redes(360, 175)
        python(350, 290)
        SQL(375, 405)
        escolha(215, 50)

        pygame.display.update()

def python_level_pergunta_1():

    global pontosCount

    while True:
        screen.fill((white))

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button3.collidepoint(mouse):
                    pontosCount+=1
                    python_level_pergunta_2()
                
                if button1.collidepoint(mouse):
                    python_level_pergunta_2()

        
        def respostaA(x, y):
                font = Bebas_Font.render("A. Lista", True, black)
                screen.blit(font, (x, y))
        
        def respostaB(x, y):
                font = Bebas_Font.render("B. Operador", True, black)
                screen.blit(font, (x, y))
        
        def respostaC(x, y):
                font = Bebas_Font.render("C. Tupla", True, black)
                screen.blit(font, (x, y))
        
        def respostaD(x, y):
                font = Bebas_Font.render("D. Classe", True, black)
                screen.blit(font, (x, y))
        
        def pergunta(x, y):
                font = Berlin.render("1. Na linguagem de programação Python, existem 3 estruturas", True, black)
                screen.blit(font, (x, y))

        def perguntaEx(x, y):
                font = Berlin.render("para armazenar dados indexados. A estrutura cujos valores ", True, black)
                screen.blit(font, (x, y))
        
        def perguntaEx2(x, y):
                font = Berlin.render("são imutáveis depois de sua criação é conhecida como: ", True, black)
                screen.blit(font, (x, y))
        
        def pontos(x, y):
                font = pontosFont.render("Pontos: " + str(pontosCount) + "/5", True, black)
                screen.blit(font, (x, y))
            
        button1 = pygame.Rect(100, 250, 250, 120)
        pygame.draw.rect(screen, blue, (100, 250, 250, 120))

        button2 = pygame.Rect(100, 400, 250, 120)
        pygame.draw.rect(screen, blue, (100, 400, 250, 120))

        button3 = pygame.Rect(450, 400, 250, 120)
        pygame.draw.rect(screen, blue, (450, 400, 250, 120))

        button4 = pygame.Rect(450, 250, 250, 120)
        pygame.draw.rect(screen, blue, (450, 250, 250, 120))

        if 100+250 > mouse[0] > 100 and 250+120 > mouse[1] > 250:
            def respostaA(x, y):
                font = Bebas_Font.render("A. Lista", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (100, 250, 250, 120))
        
        if 100+250 > mouse[0] > 100 and 400+120 > mouse[1] > 400:
            def respostaB(x, y):
                font = Bebas_Font.render("B. Operador", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (100, 400, 250, 120))
        
        if 450+250 > mouse[0] > 450 and 400+120 > mouse[1] > 400:
            def respostaC(x, y):
                font = Bebas_Font.render("C. Tupla", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (450, 400, 250, 120))
        
        if 450+250 > mouse[0] > 450 and 250+120 > mouse[1] > 250:
            def respostaD(x, y):
                font = Bebas_Font.render("D. Classe", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (450, 250, 250, 120))
        
        respostaA(150, 280)
        respostaB(150, 430)
        respostaC(500, 430)
        respostaD(500, 280)
        pergunta(10, 50)
        perguntaEx(30, 90)
        perguntaEx2(30, 130)
        pontos(10, 20)
        pygame.display.update()
        print(pontosCount)

def python_level_pergunta_2():

    global pontosCount

    while True:
        screen.fill((white))

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button3.collidepoint(mouse):
                    pontosCount+=1
                    python_level_pergunta_2()
                
                if button1.collidepoint(mouse):
                    python_level_pergunta_2()

        
        def respostaA(x, y):
                font = Bebas_Font.render("A. Lista", True, black)
                screen.blit(font, (x, y))
        
        def respostaB(x, y):
                font = Bebas_Font.render("B. Operador", True, black)
                screen.blit(font, (x, y))
        
        def respostaC(x, y):
                font = Bebas_Font.render("C. Tupla", True, black)
                screen.blit(font, (x, y))
        
        def respostaD(x, y):
                font = Bebas_Font.render("D. Classe", True, black)
                screen.blit(font, (x, y))
        
        def pergunta(x, y):
                font = Berlin.render("1.", True, black)
                screen.blit(font, (x, y))

        def perguntaEx(x, y):
                font = Berlin.render("", True, black)
                screen.blit(font, (x, y))
        
        def perguntaEx2(x, y):
                font = Berlin.render("", True, black)
                screen.blit(font, (x, y))
        
        def pontos(x, y):
                font = pontosFont.render("Pontos: " + str(pontosCount) + "/5", True, black)
                screen.blit(font, (x, y))
            
        button1 = pygame.Rect(100, 250, 250, 120)
        pygame.draw.rect(screen, blue, (100, 250, 250, 120))

        button2 = pygame.Rect(100, 400, 250, 120)
        pygame.draw.rect(screen, blue, (100, 400, 250, 120))

        button3 = pygame.Rect(450, 400, 250, 120)
        pygame.draw.rect(screen, blue, (450, 400, 250, 120))

        button4 = pygame.Rect(450, 250, 250, 120)
        pygame.draw.rect(screen, blue, (450, 250, 250, 120))

        if 100+250 > mouse[0] > 100 and 250+120 > mouse[1] > 250:
            def respostaA(x, y):
                font = Bebas_Font.render("A. Lista", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (100, 250, 250, 120))
        
        if 100+250 > mouse[0] > 100 and 400+120 > mouse[1] > 400:
            def respostaB(x, y):
                font = Bebas_Font.render("B. Operador", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (100, 400, 250, 120))
        
        if 450+250 > mouse[0] > 450 and 400+120 > mouse[1] > 400:
            def respostaC(x, y):
                font = Bebas_Font.render("C. Tupla", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (450, 400, 250, 120))
        
        if 450+250 > mouse[0] > 450 and 250+120 > mouse[1] > 250:
            def respostaD(x, y):
                font = Bebas_Font.render("D. Classe", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (450, 250, 250, 120))
        
        respostaA(150, 280)
        respostaB(150, 430)
        respostaC(500, 430)
        respostaD(500, 280)
        pergunta(10, 50)
        perguntaEx(30, 90)
        perguntaEx2(30, 130)
        pontos(10, 20)
        pygame.display.update()

interface()