import pygame as pg
import json
with open('data/data_teste.json') as f:
        data = json.load(f)

def write_form(new_data, filename='data/form.json'):
    with open(filename,'r+') as h:
        form = json.load(h)
        form["nome"] = new_data
        h.seek(0)
        json.dump(form, h, indent = 4)

def write_data(new_data, filename='data/data_teste.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        temp = file_data["players"]
        temp.append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

def main():
    with open('data/form.json') as h:
        form = json.load(h)
    screen = pg.display.set_mode((800, 600))
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    input_box = pg.Rect(400, 100, 140, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    y = {"nome":form["nome"],
     "pontos": form["pontos"]
    }

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        write_form(text)
                        print(text)
                        write_data(y)
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()