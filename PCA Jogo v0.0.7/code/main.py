import pygame
import json
with open('data/data.json') as f:
    data = json.load(f)

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("TI LEARNING")

Bebas_Font = pygame.font.Font('font/BEBAS-REGULAR.otf', 40)

Genuine = pygame.font.Font('font/GENUINE.TTF', 52)

Bebas_Font24 = pygame.font.Font('font/BEBAS-REGULAR.otf', 24)

Berlin = pygame.font.Font('font/BRLNSR.TTF', 30)

inputFont = pygame.font.Font(None, 32)

pontosFont = pygame.font.Font('font/BRLNSR.TTF', 20)

config = pygame.image.load('images/gear.svg')

question = pygame.image.load('images/questao.svg')

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
                if button2.collidepoint(mouse):
                    rankingUser()
                if button3.collidepoint(mouse):
                    cadastro()
                if button4.collidepoint(mouse):
                    logar()
                if button5.collidepoint(mouse):
                    ajuda()

        def iniciar(x, y):
            font = Bebas_Font.render("Iniciar", True, black)
            screen.blit(font, (x, y))
        
        def loginMensagem(x, y):
            font = Berlin.render("Cadastre-se ou acesse sua conta!", True, black)
            screen.blit(font, (x, y))
        
        def ranking(x, y):
            font = Bebas_Font.render("Ranking", True, black)
            screen.blit(font, (x, y))
        
        def cadastrar(x, y):
            font = Bebas_Font24.render("CADASTRO", True, black)
            screen.blit(font, (x, y))
        
        def login(x, y):
            font = Bebas_Font24.render("LOGIN", True, black)
            screen.blit(font, (x, y))
            
        def titulo(x, y):
            font = Genuine.render("TI   LEARNING", True, black)
            screen.blit(font, (x, y))

        button1 = pygame.Rect(150, 300, 200, 100)
        pygame.draw.rect(screen, blue, (button1))

        button2 = pygame.Rect(450, 300, 200, 100)
        pygame.draw.rect(screen, blue, (button2))

        button3 = pygame.Rect(300, 500, 100, 50)
        pygame.draw.rect(screen, blue, (button3))

        button4 = pygame.Rect(420, 500, 100, 50)
        pygame.draw.rect(screen, blue, (button4))

        button5 = pygame.Rect(730, 20, 100, 50)

        if 150+200 > mouse[0] > 150 and 300+100 > mouse[1] > 300:
            def iniciar(x, y):
                font = Bebas_Font.render("Iniciar", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (button1))
        
        if 450+200 > mouse[0] > 450 and 300+100 > mouse[1] > 300:
            def ranking(x, y):
                font = Bebas_Font.render("Ranking", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (button2))
        
        if 300+100 > mouse[0] > 300 and 500+50 > mouse[1] > 500:
            def cadastrar(x, y):
                font = Bebas_Font24.render("CADASTRO", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (button3))
        
        if 420+100 > mouse[0] > 420 and 500+50 > mouse[1] > 500:
            def login(x, y):
                font = Bebas_Font24.render("LOGIN", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (button4))

        screen.blit(question, (730, 20))
        loginMensagem(210, 440)
        cadastrar(310, 510)
        login(445, 510)
        iniciar(200, 325)
        ranking(490, 325)
        titulo(270, 100)

        pygame.display.update()

def interfaceLogin():

    while True:
        screen.fill((white))

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(mouse):
                    choose_levelLogin()
                if button2.collidepoint(mouse):
                    rankingUserLogado()
                if button3.collidepoint(mouse):
                    interface()
                if button4.collidepoint(mouse):
                    ajudaLogin()
                

        def checarNome(nome):
            for item in data['players']:
                if nome in item['nome']:
                    def pontosUsuario(x, y):
                        font = Berlin.render(f"Seus pontos: {item['pontos']}", True, black)
                        screen.blit(font, (x, y))
                    pontosUsuario(300, 520)

        def logout(x, y):
            font = Bebas_Font24.render("Logout", True, black)
            screen.blit(font, (x, y))

        def iniciar(x, y):
            font = Bebas_Font.render("Iniciar", True, black)
            screen.blit(font, (x, y))
        
        def loginMensagem(x, y):
            font = Berlin.render(f"Bem vindo, {user_textLog}!", True, black)
            screen.blit(font, (x, y))
        
        def ranking(x, y):
            font = Bebas_Font.render("Ranking", True, black)
            screen.blit(font, (x, y))
            
        def titulo(x, y):
            font = Genuine.render("TI   LEARNING", True, black)
            screen.blit(font, (x, y))

        button1 = pygame.Rect(150, 300, 200, 100)
        pygame.draw.rect(screen, blue, (button1))

        button2 = pygame.Rect(450, 300, 200, 100)
        pygame.draw.rect(screen, blue, (button2))

        button3 = pygame.Rect(20, 530, 100, 50)
        pygame.draw.rect(screen, blue, (button3))

        button4 = pygame.Rect(730, 20, 100, 50)

        if 150+200 > mouse[0] > 150 and 300+100 > mouse[1] > 300:
            def iniciar(x, y):
                font = Bebas_Font.render("Iniciar", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (button1))
        
        if 450+200 > mouse[0] > 450 and 300+100 > mouse[1] > 300:
            def ranking(x, y):
                font = Bebas_Font.render("Ranking", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (button2))
        
        if 20+100 > mouse[0] > 20 and 530+50 > mouse[1] > 530:
            def logout(x, y):
                font = Bebas_Font24.render("Logout", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (button3))

        screen.blit(question, (730, 20))
        loginMensagem(270, 480)
        iniciar(200, 325)
        ranking(490, 325)
        titulo(270, 100)
        logout(35, 540)
        checarNome(user_textLog)

        pygame.display.update()

def rankingUser():

    while True:
        screen.fill((white))

        mouse = pygame.mouse.get_pos()

        ranking = pygame.image.load('images/ranking.png')

        screen.blit(ranking, (-500, -200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(mouse):
                    interface()
        
        def topCinco():
            data['players'] = sorted(data['players'], key=lambda x : x['pontos'], reverse = True)


        def rankUm(x, y):
            font = Bebas_Font24.render(f"1: {data['players'][0]['nome']}, {data['players'][0]['pontos']}", True, black)
            screen.blit(font, (x, y))
        
        def rankDois(x, y):
            font = Bebas_Font24.render(f"2: {data['players'][1]['nome']}, {data['players'][1]['pontos']}", True, black)
            screen.blit(font, (x, y))
        
        def rankTres(x, y):
            font = Bebas_Font24.render(f"3: {data['players'][2]['nome']}, {data['players'][2]['pontos']}", True, black)
            screen.blit(font, (x, y))
        
        def rankQuatro(x, y):
            font = Bebas_Font24.render(f"4: {data['players'][3]['nome']}, {data['players'][3]['pontos']}", True, black)
            screen.blit(font, (x, y))
        
        def rankCinco(x, y):
            font = Bebas_Font24.render(f"5: {data['players'][4]['nome']}, {data['players'][4]['pontos']}", True, black)
            screen.blit(font, (x, y))
        
        def rankSeis(x, y):
            font = Bebas_Font24.render(f"6: {data['players'][5]['nome']}, {data['players'][5]['pontos']}", True, black)
            screen.blit(font, (x, y))
        
        def rankSete(x, y):
            font = Bebas_Font24.render(f"7: {data['players'][6]['nome']}, {data['players'][6]['pontos']}", True, black)
            screen.blit(font, (x, y))
        
        def rankOito(x, y):
            font = Bebas_Font24.render(f"8: {data['players'][7]['nome']}, {data['players'][7]['pontos']}", True, black)
            screen.blit(font, (x, y))
        
        def rankNove(x, y):
            font = Bebas_Font24.render(f"9: {data['players'][8]['nome']}, {data['players'][8]['pontos']}", True, black)
            screen.blit(font, (x, y))
        
        def rankDez(x, y):
            font = Bebas_Font24.render(f"10: {data['players'][9]['nome']}, {data['players'][9]['pontos']}", True, black)
            screen.blit(font, (x, y))
            
        def titulo(x, y):
            font = Genuine.render("RANKING", True, black)
            screen.blit(font, (x, y))
        
        def voltar(x, y):
            font = Bebas_Font24.render("VOLTAR", True, black)
            screen.blit(font, (x, y))

        button1 = pygame.Rect(20, 20, 100, 50)
        pygame.draw.rect(screen, blue, (button1))

        if 20+100 > mouse[0] > 20 and 20+50 > mouse[1] > 20:
            def voltar(x, y):
                font = Bebas_Font24.render("VOLTAR", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (button1))


        topCinco()
        voltar(40, 30)
        rankUm(350, 150)
        rankDois(240, 220)
        rankTres(465, 285)
        rankQuatro(600, 150)
        rankCinco(600, 200)
        rankSeis(600, 250)
        rankSete(600, 300)
        rankOito(600, 350)
        rankNove(600, 400)
        rankDez(600, 450)
        titulo(300, 50)

        pygame.display.update()

def rankingUserLogado():

    while True:
        screen.fill((white))

        mouse = pygame.mouse.get_pos()

        ranking = pygame.image.load('images/ranking.png')

        screen.blit(ranking, (-500, -200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(mouse):
                    interfaceLogin()
        
        def topCinco():
            data['players'] = sorted(data['players'], key=lambda x : x['pontos'], reverse = True)


        def rankUm(x, y):
            font = Bebas_Font24.render(f"1: {data['players'][0]['nome']}, {data['players'][0]['pontos']}", True, black)
            screen.blit(font, (x, y))
        
        def rankDois(x, y):
            font = Bebas_Font24.render(f"2: {data['players'][1]['nome']}, {data['players'][1]['pontos']}", True, black)
            screen.blit(font, (x, y))
        
        def rankTres(x, y):
            font = Bebas_Font24.render(f"3: {data['players'][2]['nome']}, {data['players'][2]['pontos']}", True, black)
            screen.blit(font, (x, y))
        
        def rankQuatro(x, y):
            font = Bebas_Font24.render(f"4: {data['players'][3]['nome']}, {data['players'][3]['pontos']}", True, black)
            screen.blit(font, (x, y))
        
        def rankCinco(x, y):
            font = Bebas_Font24.render(f"5: {data['players'][4]['nome']}, {data['players'][4]['pontos']}", True, black)
            screen.blit(font, (x, y))
        
        def rankSeis(x, y):
            font = Bebas_Font24.render(f"6: {data['players'][5]['nome']}, {data['players'][5]['pontos']}", True, black)
            screen.blit(font, (x, y))
        
        def rankSete(x, y):
            font = Bebas_Font24.render(f"7: {data['players'][6]['nome']}, {data['players'][6]['pontos']}", True, black)
            screen.blit(font, (x, y))
        
        def rankOito(x, y):
            font = Bebas_Font24.render(f"8: {data['players'][7]['nome']}, {data['players'][7]['pontos']}", True, black)
            screen.blit(font, (x, y))
        
        def rankNove(x, y):
            font = Bebas_Font24.render(f"9: {data['players'][8]['nome']}, {data['players'][8]['pontos']}", True, black)
            screen.blit(font, (x, y))
        
        def rankDez(x, y):
            font = Bebas_Font24.render(f"10: {data['players'][9]['nome']}, {data['players'][9]['pontos']}", True, black)
            screen.blit(font, (x, y))
            
        def titulo(x, y):
            font = Genuine.render("RANKING", True, black)
            screen.blit(font, (x, y))
        
        def voltar(x, y):
            font = Bebas_Font24.render("VOLTAR", True, black)
            screen.blit(font, (x, y))

        button1 = pygame.Rect(20, 20, 100, 50)
        pygame.draw.rect(screen, blue, (button1))

        if 20+100 > mouse[0] > 20 and 20+50 > mouse[1] > 20:
            def voltar(x, y):
                font = Bebas_Font24.render("VOLTAR", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (button1))


        topCinco()
        voltar(40, 30)
        rankUm(350, 150)
        rankDois(240, 220)
        rankTres(465, 285)
        rankQuatro(600, 150)
        rankCinco(600, 200)
        rankSeis(600, 250)
        rankSete(600, 300)
        rankOito(600, 350)
        rankNove(600, 400)
        rankDez(600, 450)
        titulo(300, 50)

        pygame.display.update()

def cadastro():

    global user_textCad

    user_textCad = ''

    input_rect = pygame.Rect(310, 220, 140, 32)

    color_ativo = pygame.Color('lightskyblue3')

    color_desativo = pygame.Color('gray15')

    color = color_desativo

    ativo = False

    def registrar(new_data, filename='data/data.json'):
        with open(filename,'r+') as h:
            form = json.load(h)
            form["players"].append({
            "nome": user_textCad,
            "pontos":0
            })
            h.seek(0)
            json.dump(form, h, indent = 4)

    def checarCadastro(nome):
        for item in data['players']:
            if nome in item['nome']:
                cadastroExiste()

            if nome not in item['nome']:
                registrar(nome)
                interface()

    while True:
        screen.fill((white))

        pygame.draw.rect(screen, color, input_rect, 1)

        text_surface = inputFont.render(user_textCad, True, black)

        input_rect.w = max(200, text_surface.get_width() + 10)

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if ativo == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_textCad = user_textCad[: -1]
                    else:
                        user_textCad += event.unicode
                
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    ativo = True
                else:
                    ativo = False

                if button1.collidepoint(mouse):
                    checarCadastro(user_textCad)

                if button2.collidepoint(mouse):
                    interface()
            
        def cadastrar(x, y):
            font = Bebas_Font.render("REGISTRAR", True, black)
            screen.blit(font, (x, y))
        
        def cadastroMensagem(x, y):
            font = Berlin.render("Escolha seu novo nome de usuário!", True, black)
            screen.blit(font, (x, y))
            
        def cadastro(x, y):
            font = Genuine.render("CADASTRE-SE", True, black)
            screen.blit(font, (x, y))

        def voltar(x, y):
            font = Bebas_Font24.render("VOLTAR", True, black)
            screen.blit(font, (x, y))

        button1 = pygame.Rect(310, 300, 200, 100)
        pygame.draw.rect(screen, blue, (button1))

        button2 = pygame.Rect(20, 20, 100, 50)
        pygame.draw.rect(screen, blue, (button2))

        if 310+200 > mouse[0] > 310 and 300+100 > mouse[1] > 300:
            def cadastrar(x, y):
                font = Bebas_Font.render("REGISTRAR", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (310, 300, 200, 100))
        
        if 20+100 > mouse[0] > 20 and 20+50 > mouse[1] > 20:
            def voltar(x, y):
                font = Bebas_Font24.render("VOLTAR", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (button2))

        if ativo:
            color = color_ativo
        else:
            color = color_desativo

        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        cadastroMensagem(210, 120)
        cadastrar(340, 325)
        cadastro(270, 50)
        voltar(40, 30)

        pygame.display.update()

def cadastroExiste():

    global user_textCad

    user_textCad = ''

    input_rect = pygame.Rect(310, 220, 140, 32)

    color_ativo = pygame.Color('lightskyblue3')

    color_desativo = pygame.Color('gray15')

    color = color_desativo

    ativo = False

    def registrar(new_data, filename='data/data.json'):
        with open(filename,'r+') as h:
            form = json.load(h)
            form["players"].append({
            "nome": user_textCad,
            "pontos":0
            })
            h.seek(0)
            json.dump(form, h, indent = 4)

    def checarCadastro(nome):
        for item in data['players']:
            if nome in item['nome']:
                cadastroExiste()

            if nome not in item['nome']:
                registrar(nome)
                interface()

    while True:
        screen.fill((white))

        pygame.draw.rect(screen, color, input_rect, 1)

        text_surface = inputFont.render(user_textCad, True, black)

        input_rect.w = max(200, text_surface.get_width() + 10)

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if ativo == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_textCad = user_textCad[: -1]
                    else:
                        user_textCad += event.unicode
                
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    ativo = True
                else:
                    ativo = False

                if button1.collidepoint(mouse):
                    checarCadastro(user_textCad)

                if button2.collidepoint(mouse):
                    interface()
            
        def cadastrar(x, y):
            font = Bebas_Font.render("REGISTRAR", True, black)
            screen.blit(font, (x, y))
        
        def cadastroMensagem(x, y):
            font = Berlin.render("Escolha seu novo nome de usuário!", True, black)
            screen.blit(font, (x, y))
        
        def usuarioExiste(x, y):
            font = Berlin.render("Usuario ja existente.", True, black)
            screen.blit(font, (x, y))
            
        def cadastro(x, y):
            font = Genuine.render("CADASTRE-SE", True, black)
            screen.blit(font, (x, y))

        def voltar(x, y):
            font = Bebas_Font24.render("VOLTAR", True, black)
            screen.blit(font, (x, y))

        button1 = pygame.Rect(310, 300, 200, 100)
        pygame.draw.rect(screen, blue, (button1))

        button2 = pygame.Rect(20, 20, 100, 50)
        pygame.draw.rect(screen, blue, (button2))

        if 310+200 > mouse[0] > 310 and 300+100 > mouse[1] > 300:
            def cadastrar(x, y):
                font = Bebas_Font.render("REGISTRAR", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (310, 300, 200, 100))
        
        if 20+100 > mouse[0] > 20 and 20+50 > mouse[1] > 20:
            def voltar(x, y):
                font = Bebas_Font24.render("VOLTAR", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (button2))

        if ativo:
            color = color_ativo
        else:
            color = color_desativo

        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        cadastroMensagem(210, 120)
        cadastrar(340, 325)
        cadastro(270, 50)
        usuarioExiste(290, 450)
        voltar(40, 30)

        pygame.display.update()

def logar():

    global user_textLog

    user_textLog = ''

    input_rect = pygame.Rect(310, 220, 140, 32)

    color_ativo = pygame.Color('lightskyblue3')

    color_desativo = pygame.Color('gray15')

    color = color_desativo

    ativo = False

    while True:
        screen.fill((white))

        pygame.draw.rect(screen, color, input_rect, 1)

        text_surface = inputFont.render(user_textLog, True, black)

        input_rect.w = max(200, text_surface.get_width() + 10)

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if ativo == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_textLog = user_textLog[: -1]
                    else:
                        user_textLog += event.unicode
                
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    ativo = True
                else:
                    ativo = False

                if button1.collidepoint(mouse):

                    def checarLogin(nome):
                        global userLogin

                        userLogin = False
                        for item in data['players']:
                            if nome in item['nome']:
                                userLogin = True
                            
                        if userLogin == True:
                            interfaceLogin()
                        else:
                            cadastro()
                    
                    checarLogin(user_textLog)

                if button2.collidepoint(mouse):
                    interface()
            
        def logar(x, y):
            font = Bebas_Font.render("LOGAR", True, black)
            screen.blit(font, (x, y))
        
        def loginMensagem(x, y):
            font = Berlin.render("Digite seu nome de usuário!", True, black)
            screen.blit(font, (x, y))
            
        def login(x, y):
            font = Genuine.render("LOGIN", True, black)
            screen.blit(font, (x, y))
        
        def voltar(x, y):
            font = Bebas_Font24.render("VOLTAR", True, black)
            screen.blit(font, (x, y))

        button1 = pygame.Rect(310, 300, 200, 100)
        pygame.draw.rect(screen, blue, (button1))

        button2 = pygame.Rect(20, 20, 100, 50)
        pygame.draw.rect(screen, blue, (button2))

        if 310+200 > mouse[0] > 310 and 300+100 > mouse[1] > 300:
            def logar(x, y):
                font = Bebas_Font.render("LOGAR", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (button1))
        
        if 20+100 > mouse[0] > 20 and 20+50 > mouse[1] > 20:
            def voltar(x, y):
                font = Bebas_Font24.render("VOLTAR", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (button2))

        if ativo:
            color = color_ativo
        else:
            color = color_desativo

        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        loginMensagem(240, 120)
        logar(365, 325)
        login(345, 50)
        voltar(40, 30)

        pygame.display.update()

def ajuda():

    while True:
        screen.fill((white))

        mouse = pygame.mouse.get_pos()

        ajudaImg = pygame.image.load('images/ajuda.png')

        screen.blit(ajudaImg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(mouse):
                    interface()

        
        def voltar(x, y):
            font = Bebas_Font24.render("VOLTAR", True, black)
            screen.blit(font, (x, y))

        button1 = pygame.Rect(20, 20, 100, 50)
        pygame.draw.rect(screen, blue, (button1))

        
        if 20+100 > mouse[0] > 20 and 20+50 > mouse[1] > 20:
            def voltar(x, y):
                font = Bebas_Font24.render("VOLTAR", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (button1))

        voltar(40, 30)

        pygame.display.update()

def ajudaLogin():

    while True:
        screen.fill((white))

        mouse = pygame.mouse.get_pos()

        ajudaImg = pygame.image.load('images/ajuda.png')

        screen.blit(ajudaImg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(mouse):
                    interfaceLogin()

        def voltar(x, y):
            font = Bebas_Font24.render("VOLTAR", True, black)
            screen.blit(font, (x, y))

        button1 = pygame.Rect(20, 20, 100, 50)
        pygame.draw.rect(screen, blue, (button1))

        
        if 20+100 > mouse[0] > 20 and 20+50 > mouse[1] > 20:
            def voltar(x, y):
                font = Bebas_Font24.render("VOLTAR", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (button1))

        voltar(40, 30)

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
                if button4.collidepoint(mouse):
                    interface()

        
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
        
        def voltar(x, y):
            font = Bebas_Font24.render("VOLTAR", True, black)
            screen.blit(font, (x, y))

        button4 = pygame.Rect(20, 20, 100, 50)
        pygame.draw.rect(screen, blue, (button4))

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
        
        if 20+100 > mouse[0] > 20 and 20+50 > mouse[1] > 20:
            def voltar(x, y):
                font = Bebas_Font24.render("VOLTAR", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (button4))
        
        redes(360, 175)
        python(350, 290)
        SQL(375, 405)
        escolha(215, 50)
        voltar(40, 30)

        pygame.display.update()

def choose_levelLogin():

    while True:
        screen.fill((white))

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button2.collidepoint(mouse):
                    python_level_pergunta_1Login()
                if button4.collidepoint(mouse):
                    interfaceLogin()

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
        
        def voltar(x, y):
            font = Bebas_Font24.render("VOLTAR", True, black)
            screen.blit(font, (x, y))

        button4 = pygame.Rect(20, 20, 100, 50)
        pygame.draw.rect(screen, blue, (button4))

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
        
        if 20+100 > mouse[0] > 20 and 20+50 > mouse[1] > 20:
            def voltar(x, y):
                font = Bebas_Font24.render("VOLTAR", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (button4))
        
        redes(360, 175)
        python(350, 290)
        SQL(375, 405)
        escolha(215, 50)
        voltar(40, 30)

        pygame.display.update()

def python_level_pergunta_1():

    global pontosCount

    while True:

        pontosCount = 0

        screen.fill((white))

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if button1.collidepoint(mouse):
                    python_level_pergunta_2()

                if button2.collidepoint(mouse):
                    python_level_pergunta_2()

                if button3.collidepoint(mouse):
                    python_level_pergunta_2()

                if button4.collidepoint(mouse):
                    pontosCount+=1
                    python_level_pergunta_2()

        
        def respostaA(x, y):
                font = Bebas_Font.render("A. Lista", True, black)
                screen.blit(font, (x, y))
        
        def respostaB(x, y):
                font = Bebas_Font.render("C. Operador", True, black)
                screen.blit(font, (x, y))
        
        def respostaC(x, y):
                font = Bebas_Font.render("D. Tupla", True, black)
                screen.blit(font, (x, y))
        
        def respostaD(x, y):
                font = Bebas_Font.render("B. Classe", True, black)
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

        button2 = pygame.Rect(450, 250, 250, 120)
        pygame.draw.rect(screen, blue, (450, 250, 250, 120))

        button3 = pygame.Rect(100, 400, 250, 120)
        pygame.draw.rect(screen, blue, (100, 400, 250, 120))

        button4 = pygame.Rect(450, 400, 250, 120)
        pygame.draw.rect(screen, blue, (450, 400, 250, 120))

        if 100+250 > mouse[0] > 100 and 250+120 > mouse[1] > 250:
            def respostaA(x, y):
                font = Bebas_Font.render("A. Lista", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (100, 250, 250, 120))
        
        if 100+250 > mouse[0] > 100 and 400+120 > mouse[1] > 400:
            def respostaB(x, y):
                font = Bebas_Font.render("C. Operador", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (100, 400, 250, 120))
        
        if 450+250 > mouse[0] > 450 and 400+120 > mouse[1] > 400:
            def respostaC(x, y):
                font = Bebas_Font.render("D. Tupla", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (450, 400, 250, 120))
        
        if 450+250 > mouse[0] > 450 and 250+120 > mouse[1] > 250:
            def respostaD(x, y):
                font = Bebas_Font.render("B. Classe", True, white)
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

def python_level_pergunta_1Login():

    global pontosCount

    while True:

        pontosCount = 0

        screen.fill((white))

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if button1.collidepoint(mouse):
                    python_level_pergunta_2Login()

                if button2.collidepoint(mouse):
                    python_level_pergunta_2Login()

                if button3.collidepoint(mouse):
                    python_level_pergunta_2Login()

                if button4.collidepoint(mouse):
                    pontosCount+=1
                    python_level_pergunta_2Login()

        
        def respostaA(x, y):
                font = Bebas_Font.render("A. Lista", True, black)
                screen.blit(font, (x, y))
        
        def respostaB(x, y):
                font = Bebas_Font.render("C. Operador", True, black)
                screen.blit(font, (x, y))
        
        def respostaC(x, y):
                font = Bebas_Font.render("D. Tupla", True, black)
                screen.blit(font, (x, y))
        
        def respostaD(x, y):
                font = Bebas_Font.render("B. Classe", True, black)
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

        button2 = pygame.Rect(450, 250, 250, 120)
        pygame.draw.rect(screen, blue, (450, 250, 250, 120))

        button3 = pygame.Rect(100, 400, 250, 120)
        pygame.draw.rect(screen, blue, (100, 400, 250, 120))

        button4 = pygame.Rect(450, 400, 250, 120)
        pygame.draw.rect(screen, blue, (450, 400, 250, 120))

        if 100+250 > mouse[0] > 100 and 250+120 > mouse[1] > 250:
            def respostaA(x, y):
                font = Bebas_Font.render("A. Lista", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (100, 250, 250, 120))
        
        if 100+250 > mouse[0] > 100 and 400+120 > mouse[1] > 400:
            def respostaB(x, y):
                font = Bebas_Font.render("C. Operador", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (100, 400, 250, 120))
        
        if 450+250 > mouse[0] > 450 and 400+120 > mouse[1] > 400:
            def respostaC(x, y):
                font = Bebas_Font.render("D. Tupla", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (450, 400, 250, 120))
        
        if 450+250 > mouse[0] > 450 and 250+120 > mouse[1] > 250:
            def respostaD(x, y):
                font = Bebas_Font.render("B. Classe", True, white)
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

def python_level_pergunta_2():

    global pontosCount

    while True:
        screen.fill((white))

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(mouse):
                    python_level_pergunta_3()
                
                if button2.collidepoint(mouse):
                    python_level_pergunta_3()
                
                if button3.collidepoint(mouse):
                    pontosCount+=1
                    python_level_pergunta_3()
                
                if button4.collidepoint(mouse):
                    python_level_pergunta_3()

        
        def respostaA(x, y):
                font = Bebas_Font.render("A. IF", True, black)
                screen.blit(font, (x, y))
        
        def respostaB(x, y):
                font = Bebas_Font.render("C. FOR", True, black)
                screen.blit(font, (x, y))
        
        def respostaC(x, y):
                font = Bebas_Font.render("D. WHILE", True, black)
                screen.blit(font, (x, y))
        
        def respostaD(x, y):
                font = Bebas_Font.render("B. PRINT", True, black)
                screen.blit(font, (x, y))
        
        def pergunta(x, y):
                font = Berlin.render("2. Qual comando do Python 3 que realiza para cada lista", True, black)
                screen.blit(font, (x, y))

        def perguntaEx(x, y):
                font = Berlin.render("uma atribuição do elemento corrente à variável definida ", True, black)
                screen.blit(font, (x, y))
        
        def perguntaEx2(x, y):
                font = Berlin.render("no comando e executa o bloco de código associado", True, black)
                screen.blit(font, (x, y))
        
        def perguntaEx3(x, y):
                font = Berlin.render("a essa variável disponível?", True, black)
                screen.blit(font, (x, y))
        
        def pontos(x, y):
                font = pontosFont.render("Pontos: " + str(pontosCount) + "/5", True, black)
                screen.blit(font, (x, y))
            
        button1 = pygame.Rect(100, 250, 250, 120)
        pygame.draw.rect(screen, blue, (100, 250, 250, 120))

        button2 = pygame.Rect(450, 250, 250, 120)
        pygame.draw.rect(screen, blue, (450, 250, 250, 120))

        button3 = pygame.Rect(100, 400, 250, 120)
        pygame.draw.rect(screen, blue, (100, 400, 250, 120))

        button4 = pygame.Rect(450, 400, 250, 120)
        pygame.draw.rect(screen, blue, (450, 400, 250, 120))

        if 100+250 > mouse[0] > 100 and 250+120 > mouse[1] > 250:
            def respostaA(x, y):
                font = Bebas_Font.render("A. IF", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (100, 250, 250, 120))
        
        if 100+250 > mouse[0] > 100 and 400+120 > mouse[1] > 400:
            def respostaB(x, y):
                font = Bebas_Font.render("C. FOR", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (100, 400, 250, 120))
        
        if 450+250 > mouse[0] > 450 and 400+120 > mouse[1] > 400:
            def respostaC(x, y):
                font = Bebas_Font.render("D. WHILE", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (450, 400, 250, 120))
        
        if 450+250 > mouse[0] > 450 and 250+120 > mouse[1] > 250:
            def respostaD(x, y):
                font = Bebas_Font.render("B. PRINT", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (450, 250, 250, 120))
        
        respostaA(150, 280)
        respostaB(150, 430)
        respostaC(500, 430)
        respostaD(500, 280)
        pergunta(10, 50)
        perguntaEx(30, 90)
        perguntaEx2(30, 130)
        perguntaEx3(30, 170)
        pontos(10, 20)
        pygame.display.update()

def python_level_pergunta_2Login():

    global pontosCount

    while True:
        screen.fill((white))

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(mouse):
                    python_level_pergunta_3Login()
                
                if button2.collidepoint(mouse):
                    python_level_pergunta_3Login()
                
                if button3.collidepoint(mouse):
                    pontosCount+=1
                    python_level_pergunta_3Login()
                
                if button4.collidepoint(mouse):
                    python_level_pergunta_3Login()

        
        def respostaA(x, y):
                font = Bebas_Font.render("A. IF", True, black)
                screen.blit(font, (x, y))
        
        def respostaB(x, y):
                font = Bebas_Font.render("C. FOR", True, black)
                screen.blit(font, (x, y))
        
        def respostaC(x, y):
                font = Bebas_Font.render("D. WHILE", True, black)
                screen.blit(font, (x, y))
        
        def respostaD(x, y):
                font = Bebas_Font.render("B. PRINT", True, black)
                screen.blit(font, (x, y))
        
        def pergunta(x, y):
                font = Berlin.render("2. Qual comando do Python 3 que realiza para cada lista", True, black)
                screen.blit(font, (x, y))

        def perguntaEx(x, y):
                font = Berlin.render("uma atribuição do elemento corrente à variável definida ", True, black)
                screen.blit(font, (x, y))
        
        def perguntaEx2(x, y):
                font = Berlin.render("no comando e executa o bloco de código associado", True, black)
                screen.blit(font, (x, y))
        
        def perguntaEx3(x, y):
                font = Berlin.render("a essa variável disponível?", True, black)
                screen.blit(font, (x, y))
        
        def pontos(x, y):
                font = pontosFont.render("Pontos: " + str(pontosCount) + "/5", True, black)
                screen.blit(font, (x, y))
            
        button1 = pygame.Rect(100, 250, 250, 120)
        pygame.draw.rect(screen, blue, (100, 250, 250, 120))

        button2 = pygame.Rect(450, 250, 250, 120)
        pygame.draw.rect(screen, blue, (450, 250, 250, 120))

        button3 = pygame.Rect(100, 400, 250, 120)
        pygame.draw.rect(screen, blue, (100, 400, 250, 120))

        button4 = pygame.Rect(450, 400, 250, 120)
        pygame.draw.rect(screen, blue, (450, 400, 250, 120))

        if 100+250 > mouse[0] > 100 and 250+120 > mouse[1] > 250:
            def respostaA(x, y):
                font = Bebas_Font.render("A. IF", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (100, 250, 250, 120))
        
        if 100+250 > mouse[0] > 100 and 400+120 > mouse[1] > 400:
            def respostaB(x, y):
                font = Bebas_Font.render("C. FOR", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (100, 400, 250, 120))
        
        if 450+250 > mouse[0] > 450 and 400+120 > mouse[1] > 400:
            def respostaC(x, y):
                font = Bebas_Font.render("D. WHILE", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (450, 400, 250, 120))
        
        if 450+250 > mouse[0] > 450 and 250+120 > mouse[1] > 250:
            def respostaD(x, y):
                font = Bebas_Font.render("B. PRINT", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (450, 250, 250, 120))
        
        respostaA(150, 280)
        respostaB(150, 430)
        respostaC(500, 430)
        respostaD(500, 280)
        pergunta(10, 50)
        perguntaEx(30, 90)
        perguntaEx2(30, 130)
        perguntaEx3(30, 170)
        pontos(10, 20)
        pygame.display.update()

def python_level_pergunta_3():

    global pontosCount

    while True:
        screen.fill((white))

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(mouse):
                    python_level_pergunta_4()
                
                if button2.collidepoint(mouse):
                    pontosCount+=1
                    python_level_pergunta_4()
                
                if button3.collidepoint(mouse):
                    python_level_pergunta_4()
                
                if button4.collidepoint(mouse):
                    python_level_pergunta_4()

        
        def respostaA(x, y):
                font = Bebas_Font.render("A. Lista", True, black)
                screen.blit(font, (x, y))
        
        def respostaB(x, y):
                font = Bebas_Font.render("C. Dicionario", True, black)
                screen.blit(font, (x, y))
        
        def respostaC(x, y):
                font = Bebas_Font.render("D. Operador", True, black)
                screen.blit(font, (x, y))
        
        def respostaD(x, y):
                font = Bebas_Font.render("B. Tupla", True, black)
                screen.blit(font, (x, y))
        
        def pergunta(x, y):
                font = Berlin.render("3. Na linguagem de programação Python, existem 3 estruturas ", True, black)
                screen.blit(font, (x, y))

        def perguntaEx(x, y):
                font = Berlin.render("para armazenar dados indexados. A estrutura cujos valores", True, black)
                screen.blit(font, (x, y))
        
        def perguntaEx2(x, y):
                font = Berlin.render("são imutáveis depois de sua criação é conhecida como:", True, black)
                screen.blit(font, (x, y))
        
        def perguntaEx3(x, y):
                font = Berlin.render("", True, black)
                screen.blit(font, (x, y))
        
        def pontos(x, y):
                font = pontosFont.render("Pontos: " + str(pontosCount) + "/5", True, black)
                screen.blit(font, (x, y))
            
        button1 = pygame.Rect(100, 250, 250, 120)
        pygame.draw.rect(screen, blue, (100, 250, 250, 120))

        button2 = pygame.Rect(450, 250, 250, 120)
        pygame.draw.rect(screen, blue, (450, 250, 250, 120))

        button3 = pygame.Rect(100, 400, 250, 120)
        pygame.draw.rect(screen, blue, (100, 400, 250, 120))

        button4 = pygame.Rect(450, 400, 250, 120)
        pygame.draw.rect(screen, blue, (450, 400, 250, 120))

        if 100+250 > mouse[0] > 100 and 250+120 > mouse[1] > 250:
            def respostaA(x, y):
                font = Bebas_Font.render("A. Lista", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (100, 250, 250, 120))
        
        if 100+250 > mouse[0] > 100 and 400+120 > mouse[1] > 400:
            def respostaB(x, y):
                font = Bebas_Font.render("C. Dicionario", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (100, 400, 250, 120))
        
        if 450+250 > mouse[0] > 450 and 400+120 > mouse[1] > 400:
            def respostaC(x, y):
                font = Bebas_Font.render("D. Operador", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (450, 400, 250, 120))
        
        if 450+250 > mouse[0] > 450 and 250+120 > mouse[1] > 250:
            def respostaD(x, y):
                font = Bebas_Font.render("B. Tupla", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (450, 250, 250, 120))
        
        respostaA(150, 280)
        respostaB(150, 430)
        respostaC(500, 430)
        respostaD(500, 280)
        pergunta(10, 50)
        perguntaEx(30, 90)
        perguntaEx2(30, 130)
        perguntaEx3(30, 170)
        pontos(10, 20)
        pygame.display.update()

def python_level_pergunta_3Login():

    global pontosCount

    while True:
        screen.fill((white))

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(mouse):
                    python_level_pergunta_4Login()
                
                if button2.collidepoint(mouse):
                    pontosCount+=1
                    python_level_pergunta_4Login()
                
                if button3.collidepoint(mouse):
                    python_level_pergunta_4Login()
                
                if button4.collidepoint(mouse):
                    python_level_pergunta_4Login()

        
        def respostaA(x, y):
                font = Bebas_Font.render("A. Lista", True, black)
                screen.blit(font, (x, y))
        
        def respostaB(x, y):
                font = Bebas_Font.render("C. Dicionario", True, black)
                screen.blit(font, (x, y))
        
        def respostaC(x, y):
                font = Bebas_Font.render("D. Operador", True, black)
                screen.blit(font, (x, y))
        
        def respostaD(x, y):
                font = Bebas_Font.render("B. Tupla", True, black)
                screen.blit(font, (x, y))
        
        def pergunta(x, y):
                font = Berlin.render("3. Na linguagem de programação Python, existem 3 estruturas ", True, black)
                screen.blit(font, (x, y))

        def perguntaEx(x, y):
                font = Berlin.render("para armazenar dados indexados. A estrutura cujos valores", True, black)
                screen.blit(font, (x, y))
        
        def perguntaEx2(x, y):
                font = Berlin.render("são imutáveis depois de sua criação é conhecida como:", True, black)
                screen.blit(font, (x, y))
        
        def perguntaEx3(x, y):
                font = Berlin.render("", True, black)
                screen.blit(font, (x, y))
        
        def pontos(x, y):
                font = pontosFont.render("Pontos: " + str(pontosCount) + "/5", True, black)
                screen.blit(font, (x, y))
            
        button1 = pygame.Rect(100, 250, 250, 120)
        pygame.draw.rect(screen, blue, (100, 250, 250, 120))

        button2 = pygame.Rect(450, 250, 250, 120)
        pygame.draw.rect(screen, blue, (450, 250, 250, 120))

        button3 = pygame.Rect(100, 400, 250, 120)
        pygame.draw.rect(screen, blue, (100, 400, 250, 120))

        button4 = pygame.Rect(450, 400, 250, 120)
        pygame.draw.rect(screen, blue, (450, 400, 250, 120))

        if 100+250 > mouse[0] > 100 and 250+120 > mouse[1] > 250:
            def respostaA(x, y):
                font = Bebas_Font.render("A. Lista", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (100, 250, 250, 120))
        
        if 100+250 > mouse[0] > 100 and 400+120 > mouse[1] > 400:
            def respostaB(x, y):
                font = Bebas_Font.render("C. Dicionario", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (100, 400, 250, 120))
        
        if 450+250 > mouse[0] > 450 and 400+120 > mouse[1] > 400:
            def respostaC(x, y):
                font = Bebas_Font.render("D. Operador", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (450, 400, 250, 120))
        
        if 450+250 > mouse[0] > 450 and 250+120 > mouse[1] > 250:
            def respostaD(x, y):
                font = Bebas_Font.render("B. Tupla", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (450, 250, 250, 120))
        
        respostaA(150, 280)
        respostaB(150, 430)
        respostaC(500, 430)
        respostaD(500, 280)
        pergunta(10, 50)
        perguntaEx(30, 90)
        perguntaEx2(30, 130)
        perguntaEx3(30, 170)
        pontos(10, 20)
        pygame.display.update()

def python_level_pergunta_4():


    global pontosCount

    while True:
        screen.fill((white))

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(mouse):
                    pontosCount+=1
                    python_level_pergunta_5()
                
                if button2.collidepoint(mouse):
                    python_level_pergunta_5()
                
                if button3.collidepoint(mouse):
                    python_level_pergunta_5()
                
                if button4.collidepoint(mouse):
                    python_level_pergunta_5()

        
        def respostaA(x, y):
                font = Bebas_Font.render("A. Unpacking", True, black)
                screen.blit(font, (x, y))
        
        def respostaB(x, y):
                font = Bebas_Font.render("C. Parametros", True, black)
                screen.blit(font, (x, y))
        
        def respostaC(x, y):
                font = Bebas_Font.render("D. Import", True, black)
                screen.blit(font, (x, y))
        
        def respostaD(x, y):
                font = Bebas_Font.render("B. Packing", True, black)
                screen.blit(font, (x, y))
        
        def pergunta(x, y):
                font = Berlin.render("4. Em Python 3, qual é o processo que é executado", True, black)
                screen.blit(font, (x, y))

        def perguntaEx(x, y):
                font = Berlin.render("dentro da função e não na chamada?", True, black)
                screen.blit(font, (x, y))
        
        def perguntaEx2(x, y):
                font = Berlin.render("", True, black)
                screen.blit(font, (x, y))
        
        def perguntaEx3(x, y):
                font = Berlin.render("", True, black)
                screen.blit(font, (x, y))
        
        def pontos(x, y):
                font = pontosFont.render("Pontos: " + str(pontosCount) + "/5", True, black)
                screen.blit(font, (x, y))
            
        button1 = pygame.Rect(100, 250, 250, 120)
        pygame.draw.rect(screen, blue, (100, 250, 250, 120))

        button2 = pygame.Rect(450, 250, 250, 120)
        pygame.draw.rect(screen, blue, (450, 250, 250, 120))

        button3 = pygame.Rect(100, 400, 250, 120)
        pygame.draw.rect(screen, blue, (100, 400, 250, 120))

        button4 = pygame.Rect(450, 400, 250, 120)
        pygame.draw.rect(screen, blue, (450, 400, 250, 120))

        if 100+250 > mouse[0] > 100 and 250+120 > mouse[1] > 250:
            def respostaA(x, y):
                font = Bebas_Font.render("A. Unpacking", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (100, 250, 250, 120))
        
        if 100+250 > mouse[0] > 100 and 400+120 > mouse[1] > 400:
            def respostaB(x, y):
                font = Bebas_Font.render("C. Parametros", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (100, 400, 250, 120))
        
        if 450+250 > mouse[0] > 450 and 400+120 > mouse[1] > 400:
            def respostaC(x, y):
                font = Bebas_Font.render("D. Import", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (450, 400, 250, 120))
        
        if 450+250 > mouse[0] > 450 and 250+120 > mouse[1] > 250:
            def respostaD(x, y):
                font = Bebas_Font.render("B. Packing", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (450, 250, 250, 120))
        
        respostaA(130, 280)
        respostaB(130, 430)
        respostaC(480, 430)
        respostaD(480, 280)
        pergunta(10, 50)
        perguntaEx(30, 90)
        perguntaEx2(30, 130)
        perguntaEx3(30, 170)
        pontos(10, 20)
        pygame.display.update()

def python_level_pergunta_4Login():


    global pontosCount

    while True:
        screen.fill((white))

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(mouse):
                    pontosCount+=1
                    python_level_pergunta_5Login()
                
                if button2.collidepoint(mouse):
                    python_level_pergunta_5Login()
                
                if button3.collidepoint(mouse):
                    python_level_pergunta_5Login()
                
                if button4.collidepoint(mouse):
                    python_level_pergunta_5Login()

        
        def respostaA(x, y):
                font = Bebas_Font.render("A. Unpacking", True, black)
                screen.blit(font, (x, y))
        
        def respostaB(x, y):
                font = Bebas_Font.render("C. Parametros", True, black)
                screen.blit(font, (x, y))
        
        def respostaC(x, y):
                font = Bebas_Font.render("D. Import", True, black)
                screen.blit(font, (x, y))
        
        def respostaD(x, y):
                font = Bebas_Font.render("B. Packing", True, black)
                screen.blit(font, (x, y))
        
        def pergunta(x, y):
                font = Berlin.render("4. Em Python 3, qual é o processo que é executado", True, black)
                screen.blit(font, (x, y))

        def perguntaEx(x, y):
                font = Berlin.render("dentro da função e não na chamada?", True, black)
                screen.blit(font, (x, y))
        
        def perguntaEx2(x, y):
                font = Berlin.render("", True, black)
                screen.blit(font, (x, y))
        
        def perguntaEx3(x, y):
                font = Berlin.render("", True, black)
                screen.blit(font, (x, y))
        
        def pontos(x, y):
                font = pontosFont.render("Pontos: " + str(pontosCount) + "/5", True, black)
                screen.blit(font, (x, y))
            
        button1 = pygame.Rect(100, 250, 250, 120)
        pygame.draw.rect(screen, blue, (100, 250, 250, 120))

        button2 = pygame.Rect(450, 250, 250, 120)
        pygame.draw.rect(screen, blue, (450, 250, 250, 120))

        button3 = pygame.Rect(100, 400, 250, 120)
        pygame.draw.rect(screen, blue, (100, 400, 250, 120))

        button4 = pygame.Rect(450, 400, 250, 120)
        pygame.draw.rect(screen, blue, (450, 400, 250, 120))

        if 100+250 > mouse[0] > 100 and 250+120 > mouse[1] > 250:
            def respostaA(x, y):
                font = Bebas_Font.render("A. Unpacking", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (100, 250, 250, 120))
        
        if 100+250 > mouse[0] > 100 and 400+120 > mouse[1] > 400:
            def respostaB(x, y):
                font = Bebas_Font.render("C. Parametros", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (100, 400, 250, 120))
        
        if 450+250 > mouse[0] > 450 and 400+120 > mouse[1] > 400:
            def respostaC(x, y):
                font = Bebas_Font.render("D. Import", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (450, 400, 250, 120))
        
        if 450+250 > mouse[0] > 450 and 250+120 > mouse[1] > 250:
            def respostaD(x, y):
                font = Bebas_Font.render("B. Packing", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (450, 250, 250, 120))
        
        respostaA(130, 280)
        respostaB(130, 430)
        respostaC(480, 430)
        respostaD(480, 280)
        pergunta(10, 50)
        perguntaEx(30, 90)
        perguntaEx2(30, 130)
        perguntaEx3(30, 170)
        pontos(10, 20)
        pygame.display.update()

def python_level_pergunta_5():

    global pontosCount

    while True:
        screen.fill((white))

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(mouse):
                    final()
                
                if button2.collidepoint(mouse):
                    pontosCount+=1
                    final()
                
                if button3.collidepoint(mouse):
                    final()
                
                if button4.collidepoint(mouse):
                    final()

        
        def respostaA(x, y):
                font = Bebas_Font.render("A. Arroba", True, black)
                screen.blit(font, (x, y))
        
        def respostaB(x, y):
                font = Bebas_Font.render("C. Cifrao", True, black)
                screen.blit(font, (x, y))
        
        def respostaC(x, y):
                font = Bebas_Font.render("D. Hashtag", True, black)
                screen.blit(font, (x, y))
        
        def respostaD(x, y):
                font = Bebas_Font.render("B. Percentual", True, black)
                screen.blit(font, (x, y))
        
        def pergunta(x, y):
                font = Berlin.render("5. Em Python 3, o que é utilizado para interpolar string?", True, black)
                screen.blit(font, (x, y))

        def perguntaEx(x, y):
                font = Berlin.render("", True, black)
                screen.blit(font, (x, y))
        
        def perguntaEx2(x, y):
                font = Berlin.render("", True, black)
                screen.blit(font, (x, y))
        
        def perguntaEx3(x, y):
                font = Berlin.render("", True, black)
                screen.blit(font, (x, y))
        
        def pontos(x, y):
                font = pontosFont.render("Pontos: " + str(pontosCount) + "/5", True, black)
                screen.blit(font, (x, y))
            
        button1 = pygame.Rect(100, 250, 250, 120)
        pygame.draw.rect(screen, blue, (100, 250, 250, 120))

        button2 = pygame.Rect(450, 250, 250, 120)
        pygame.draw.rect(screen, blue, (450, 250, 250, 120))

        button3 = pygame.Rect(100, 400, 250, 120)
        pygame.draw.rect(screen, blue, (100, 400, 250, 120))

        button4 = pygame.Rect(450, 400, 250, 120)
        pygame.draw.rect(screen, blue, (450, 400, 250, 120))

        if 100+250 > mouse[0] > 100 and 250+120 > mouse[1] > 250:
            def respostaA(x, y):
                font = Bebas_Font.render("A. Arroba", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (100, 250, 250, 120))
        
        if 100+250 > mouse[0] > 100 and 400+120 > mouse[1] > 400:
            def respostaB(x, y):
                font = Bebas_Font.render("C. Cifrao", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (100, 400, 250, 120))
        
        if 450+250 > mouse[0] > 450 and 400+120 > mouse[1] > 400:
            def respostaC(x, y):
                font = Bebas_Font.render("D. Hashtag", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (450, 400, 250, 120))
        
        if 450+250 > mouse[0] > 450 and 250+120 > mouse[1] > 250:
            def respostaD(x, y):
                font = Bebas_Font.render("B. Percentual", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (450, 250, 250, 120))
        
        respostaA(130, 280)
        respostaB(130, 430)
        respostaC(480, 430)
        respostaD(480, 280)
        pergunta(10, 50)
        perguntaEx(30, 90)
        perguntaEx2(30, 130)
        perguntaEx3(30, 170)
        pontos(10, 20)
        pygame.display.update()

def python_level_pergunta_5Login():

    global pontosCount

    while True:
        screen.fill((white))

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(mouse):
                    finalLogin()
                
                if button2.collidepoint(mouse):
                    pontosCount+=1
                    finalLogin()
                
                if button3.collidepoint(mouse):
                    finalLogin()
                
                if button4.collidepoint(mouse):
                    finalLogin()

        
        def respostaA(x, y):
                font = Bebas_Font.render("A. Arroba", True, black)
                screen.blit(font, (x, y))
        
        def respostaB(x, y):
                font = Bebas_Font.render("C. Cifrao", True, black)
                screen.blit(font, (x, y))
        
        def respostaC(x, y):
                font = Bebas_Font.render("D. Hashtag", True, black)
                screen.blit(font, (x, y))
        
        def respostaD(x, y):
                font = Bebas_Font.render("B. Percentual", True, black)
                screen.blit(font, (x, y))
        
        def pergunta(x, y):
                font = Berlin.render("5. Em Python 3, o que é utilizado para interpolar string?", True, black)
                screen.blit(font, (x, y))

        def perguntaEx(x, y):
                font = Berlin.render("", True, black)
                screen.blit(font, (x, y))
        
        def perguntaEx2(x, y):
                font = Berlin.render("", True, black)
                screen.blit(font, (x, y))
        
        def perguntaEx3(x, y):
                font = Berlin.render("", True, black)
                screen.blit(font, (x, y))
        
        def pontos(x, y):
                font = pontosFont.render("Pontos: " + str(pontosCount) + "/5", True, black)
                screen.blit(font, (x, y))
            
        button1 = pygame.Rect(100, 250, 250, 120)
        pygame.draw.rect(screen, blue, (100, 250, 250, 120))

        button2 = pygame.Rect(450, 250, 250, 120)
        pygame.draw.rect(screen, blue, (450, 250, 250, 120))

        button3 = pygame.Rect(100, 400, 250, 120)
        pygame.draw.rect(screen, blue, (100, 400, 250, 120))

        button4 = pygame.Rect(450, 400, 250, 120)
        pygame.draw.rect(screen, blue, (450, 400, 250, 120))

        if 100+250 > mouse[0] > 100 and 250+120 > mouse[1] > 250:
            def respostaA(x, y):
                font = Bebas_Font.render("A. Arroba", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (100, 250, 250, 120))
        
        if 100+250 > mouse[0] > 100 and 400+120 > mouse[1] > 400:
            def respostaB(x, y):
                font = Bebas_Font.render("C. Cifrao", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (100, 400, 250, 120))
        
        if 450+250 > mouse[0] > 450 and 400+120 > mouse[1] > 400:
            def respostaC(x, y):
                font = Bebas_Font.render("D. Hashtag", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (450, 400, 250, 120))
        
        if 450+250 > mouse[0] > 450 and 250+120 > mouse[1] > 250:
            def respostaD(x, y):
                font = Bebas_Font.render("B. Percentual", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (450, 250, 250, 120))
        
        respostaA(130, 280)
        respostaB(130, 430)
        respostaC(480, 430)
        respostaD(480, 280)
        pergunta(10, 50)
        perguntaEx(30, 90)
        perguntaEx2(30, 130)
        perguntaEx3(30, 170)
        pontos(10, 20)
        pygame.display.update()

def final():

    global pontosCount

    while True:
        screen.fill((white))

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(mouse):
                    interface()

        def botaoVoltar(x, y):
                font = Bebas_Font.render("Voltar", True, black)
                screen.blit(font, (x, y))

        def mensagem(x, y):
                font = Berlin.render(f"Voce acertou: {pontosCount} de 5 questoes!", True, black)
                screen.blit(font, (x, y))

        def perguntaEx(x, y):
                font = Berlin.render("", True, black)
                screen.blit(font, (x, y))
            
        button1 = pygame.Rect(280, 250, 250, 120)
        pygame.draw.rect(screen, blue, (280, 250, 250, 120))

        if 280+250 > mouse[0] > 280 and 250+120 > mouse[1] > 250:
            def botaoVoltar(x, y):
                font = Bebas_Font.render("Voltar", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (280, 250, 250, 120))
        
        botaoVoltar(350, 280)
        mensagem(220, 100)
        perguntaEx(30, 90)
        pygame.display.update()

def finalLogin():

    global pontosCount

    while True:
        screen.fill((white))

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(mouse):
                    somarPontos(user_textLog)
                    interfaceLogin()

        def somarPontos(nome):
            for item in data['players']:
                if nome in item['nome']:
                    item['pontos'] = item['pontos'] + pontosCount
                    f = open("data/data.json", "w")
                    json.dump(data, f, indent = 4)
                    f.close()

        def botaoVoltar(x, y):
                font = Bebas_Font.render("Voltar", True, black)
                screen.blit(font, (x, y))

        def mensagem(x, y):
                font = Berlin.render(f"Voce acertou: {pontosCount} de 5 questoes!", True, black)
                screen.blit(font, (x, y))

        def perguntaEx(x, y):
                font = Berlin.render("", True, black)
                screen.blit(font, (x, y))
            
        button1 = pygame.Rect(280, 250, 250, 120)
        pygame.draw.rect(screen, blue, (280, 250, 250, 120))

        if 280+250 > mouse[0] > 280 and 250+120 > mouse[1] > 250:
            def botaoVoltar(x, y):
                font = Bebas_Font.render("Voltar", True, white)
                screen.blit(font, (x, y))
            pygame.draw.rect(screen, dark_blue, (280, 250, 250, 120))
        
        botaoVoltar(350, 280)
        mensagem(220, 100)
        perguntaEx(30, 90)
        pygame.display.update()

interface()