import pygame
from pygame.locals import *
import json

def write_json(new_data, filename='data/data_teste.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["players"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

def name():
    pygame.init()
    screen = pygame.display.set_mode((480, 360))
    name = ""
    font = pygame.font.Font(None, 50)

    y = {
        "nome":name,
        "pontos": 50
    }
    
    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    name += evt.unicode
                elif evt.key == K_BACKSPACE:
                    name = name[:-1]
                elif evt.key == K_RETURN:
                    print(name)
                    write_json(y)
            elif evt.type == QUIT:
                return
        screen.fill ((0, 0, 0))
        block = font.render(name, True, (255, 255, 255))
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        pygame.display.flip()
 
if __name__ == "__main__":
    name()