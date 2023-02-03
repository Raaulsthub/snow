import pygame
import numpy as np
import threading
from speech_recog import SpeechRecognition

class Weather:
    def __init__(self):
        self.current = 'sunny'

def new_weather(recog, weather):
    weather.current = recog.record_recognize()

    


# snow
MAX_RADIUS_SNOW = 2
MIN_RADIUS_SNOW = 1
SNOW_FREQUENCY = 5

# rain
MAX_LENGHT_RAIN = 3
MIN_LENGHT_RAIN = 1
RAIN_FREQUENCY = 10

# sun
WAVE_FREQUENCY = 20

# screen
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

class Rain:
    def __init__(self, x, y, l):
        self.x = x
        self.y = y
        self.l = l

class RainGenerator:
    def __init__(self):
        self.rain = []
    def gen(self):
        self.rain.append(Rain(np.random.randint(WIDTH), -np.random.randint(MAX_HEIGHT),
         MIN_LENGHT_RAIN + np.random.randint(MAX_LENGHT_RAIN)))



counter = 0

recog = SpeechRecognition('./audio/audio.wav')

pygame.init()

screen = pygame.display.set_mode((1920, 1080))

running = True

weather = Weather()

snow_gen = SnowGenerator()
rain_gen = RainGenerator()

# Create a snow_grad surface
snow_grad = pygame.Surface((WIDTH, HEIGHT))
rain_grad = pygame.Surface((WIDTH, HEIGHT))
sunny_grad = pygame.Surface((WIDTH, HEIGHT))

for y in range(HEIGHT):
    color = (0, 0, 255 - (y * 255 // HEIGHT))
    snow_grad.fill(color, (0, y, WIDTH, 1))
    color = (255 - (y * 255 // HEIGHT), 255 - (y * 255 // HEIGHT), 255 - (y * 255 // HEIGHT))
    rain_grad.fill(color, (0, y, WIDTH, 1))
    color = (100, 150, 255 - (y * 255 // HEIGHT))
    sunny_grad.fill(color, (0, y, WIDTH, 1))

sea_height = 0


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                thread = threading.Thread(target=new_weather, args=(recog, weather))
                thread.start()

    if (weather.current == 'snow'):
        screen.blit(snow_grad, (0, 0))
    if (weather.current == 'rain'):
        screen.blit(rain_grad, (0, 0))
    if (weather.current == 'sunny'):
        screen.blit(sunny_grad, (0, 0))

    if (weather.current == 'snow'):
        for i in snow_gen.snow:
            pygame.draw.circle(screen, (255, 255, 255), (i.x, i.y), i.r)
            if i.y < HEIGHT - 100:
                i.y += 1
        pygame.draw.rect(screen, (255, 255, 255), (0, HEIGHT-100, WIDTH, HEIGHT))
        if counter % SNOW_FREQUENCY == 0:
            snow_gen.gen()
    elif (weather.current == 'rain'):
        for i in rain_gen.rain:
            #pygame.draw.rect(screen, (211, 211, 211), (i.x, i.y, i.x+1, i.y+i.l))
            pygame.draw.circle(screen, (211, 211, 211), (i.x, i.y), i.l)
            i.y += 5
            if (i.y > HEIGHT - 100):
                i.y = -50
        pygame.draw.rect(screen, (211, 211, 211), (0, HEIGHT-100, WIDTH, HEIGHT))
        if counter % RAIN_FREQUENCY == 0 and len(rain_gen.rain) < 3000:
            rain_gen.gen()   
    elif (weather.current == 'sunny'):
        if counter % WAVE_FREQUENCY == 0:
            sea_height = 600 + np.random.randint(100)

        pygame.draw.circle(screen, (255, 255, 0), (500, 100), 50) # sun
        pygame.draw.rect(screen, (0, 105, 148), (0, sea_height, WIDTH, HEIGHT-300)) # sea
        pygame.draw.rect(screen, (194, 178, 128), (0, HEIGHT-300, WIDTH, HEIGHT)) # sands

    pygame.display.update()

    counter += 1


pygame.quit()
