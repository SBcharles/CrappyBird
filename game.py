import sys
import pygame

pygame.init()


class Config:
    window_size = window_width, window_height = 288, 512
    scroll_speed = -1


screen = pygame.display.set_mode(Config.window_size)
clock = pygame.time.Clock()

background = pygame.image.load("assets/background-day.png")
background_rect = background.get_rect()

bird = pygame.image.load("assets/yellowbird-midflap.png")
bird_rect = bird.get_rect(center=(Config.window_width / 2, Config.window_height / 2))

floor = pygame.image.load("assets/base.png")
floor_rect = floor.get_rect(bottomleft=(0, Config.window_height))
floor_rect2 = floor.get_rect(bottomleft=(Config.window_width, Config.window_height))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    floor_rect = floor_rect.move(Config.scroll_speed, 0)
    floor_rect2 = floor_rect2.move(Config.scroll_speed, 0)

    screen.blit(background, background_rect)
    screen.blit(bird, bird_rect)
    screen.blit(floor, floor_rect)
    screen.blit(floor, floor_rect2)
    pygame.display.flip()
    clock.tick(60)
