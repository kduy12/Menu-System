import pygame
from menu import *
from mybutton import Button



button_font_path = "8-BIT WONDER.TTF"  # Replace with your font file path
button1 = Button(50, 500, 200, 50, "OCEAN", font=button_font_path, font_size=24)
button2 = Button(300, 500, 200, 50, "GROUND", font=button_font_path, font_size=24)
button3 = Button(550, 500, 200, 50, "UNIVERSE", font=button_font_path, font_size=24)

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.CLICKED = False
        self.DISPLAY_W, self.DISPLAY_H = 800, 600
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = '8-BIT WONDER.TTF'
        #self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

    def game_loop(self):
        while self.playing:
            pos = pygame.mouse.get_pos()
            self.check_events()
            if self.START_KEY:
                self.playing= False
            self.display.fill(self.BLACK)

            button1.draw(self.display)
            button2.draw(self.display)
            button3.draw(self.display)

            if self.CLICKED:
                self.draw_text("BACKGROUND SELECTED", 40, self.DISPLAY_W / 2, self.DISPLAY_H / 2)
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()



    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button1.is_clicked(mouse_pos) or button2.is_clicked(mouse_pos) or button3.is_clicked(mouse_pos):
                    self.CLICKED = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)




