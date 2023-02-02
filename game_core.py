import pygame
import numpy as np


MAX_RADIUS_SNOW = 2
MIN_RADIUS_SNOW = 1
SNOW_FREQUENCY = 5
counter = 0

WIDTH = 1920
HEIGHT = 1080

MAX_HEIGHT = 50



class Snow:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

class SnowGenerator:
    def __init__(self):
        self.snow = []
    def gen(self):
        self.snow.append(Snow(np.random.randint(WIDTH),
         -np.random.randint(MAX_HEIGHT), MIN_RADIUS_SNOW + np.random.randint(MAX_RADIUS_SNOW)))
        

pygame.init()

screen = pygame.display.set_mode((1920, 1080))

running = True

weather = 'snow'

snow_gen = SnowGenerator()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Fill the screen with white
    
    if (weather == 'snow'):
        for i in snow_gen.snow:
            pygame.draw.circle(screen, (0, 0, 0), (i.x, i.y), i.r)
            # not working
            if i.y != HEIGHT - 50:
                i.y += 1


    pygame.display.update()

    counter += 1

    if counter % SNOW_FREQUENCY == 0:
        snow_gen.gen()

pygame.quit()
