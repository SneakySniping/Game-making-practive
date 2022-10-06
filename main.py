from random import random
from pygame_objects import *
from colours import *
import random
import pygame
import time

class Game:
    def __init__(self):
        self.state = "main"
        self.leaderboard = "leaderboard.txt"
        self.logins = "logins.txt"
        self.assign()
    
    def assign(self):
        if self.state == "main":
            self.main()
        elif self.state == "game":
            self.game()
    
    def main(self):
        WIDTH, HEIGHT, FPS = 500, 500, 60
        pygame.display.set_caption("Main screen")
        win = pygame.display.set_mode((WIDTH, HEIGHT))
        clock = pygame.time.Clock()

        background = pygame.image.load("Assets/Images/Background.png")
        main_screen_image = pygame.image.load("Assets/Images/Main screen title.png")
        
        play_button = Button(win, 100, 50, 250, 150, "Arial", 20, "Play", BLACK, 15, MAGENTA, True, MAGENTA_HOVER, True, CYAN, (-10, 10), True)
        character_button = Button(win, 100, 50, 250, 225, "Arial", 20, "Character", BLACK, 15, MAGENTA, True, MAGENTA_HOVER, True, CYAN, (-10, 10), True)
        leaderboard_button = Button(win, 100, 50, 250, 300, "Arial", 20, "Leaderboard", BLACK, 15, MAGENTA, True, MAGENTA_HOVER, True, CYAN, (-10, 10), True)
        quit_button = Button(win, 100, 50, 250, 375, "Arial", 20, "Quit", BLACK, 15, MAGENTA, True, MAGENTA_HOVER, True, CYAN, (-10, 10), True)


        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            win.fill(BG_YELLOW)
            #win.blit(background, (0, 0))
            win.blit(main_screen_image, (200, 50))

            play_button.draw()
            leaderboard_button.draw()
            character_button.draw()
            quit_button.draw()

            if play_button.check_left_click():
                self.state = "game"
                pygame.quit()
                self.assign()
            if character_button.check_left_click():
                print("CHaracter button pressed")
            if leaderboard_button.check_left_click():
                print("Leaderboard button pressed")
            if quit_button.check_left_click():
                self.state = "QUIT"
                running = False

            pygame.display.update()
            clock.tick(FPS)

        pygame.quit()
        quit()

    def game(self):
        WIDTH, HEIGHT, FPS = 700, 700, 100
        pygame.display.set_caption("Game")
        win = pygame.display.set_mode((WIDTH, HEIGHT))
        clock = pygame.time.Clock()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            win.fill(BG_YELLOW)

            pygame.display.update()
            clock.tick(FPS)

        pygame.quit()
        quit()

Game()