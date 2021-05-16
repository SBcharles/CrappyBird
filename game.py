import sys
import pygame

pygame.init()


class Config:
    window_size = window_width, window_height = 288, 512
    scroll_delta = -1


screen = pygame.display.set_mode(Config.window_size)
clock = pygame.time.Clock()

background = pygame.image.load("assets/background-day.png")
background_rect = background.get_rect()

bird = pygame.image.load("assets/yellowbird-midflap.png")
bird_rect = bird.get_rect(center=(Config.window_width / 2, Config.window_height / 2))

floor = pygame.image.load("assets/base.png")
floor1_rect = floor.get_rect(bottomleft=(0, Config.window_height))
floor2_rect = floor.get_rect(bottomleft=(floor.get_width(), Config.window_height))


def move_floor(floor_rect):
    floor_rect = floor_rect.move(Config.scroll_delta, 0)
    if floor_rect.right < 0:
        floor_rect = floor_rect.move(2*floor_rect.width, 0)
    return floor_rect


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    floor1_rect = move_floor(floor1_rect)
    floor2_rect = move_floor(floor2_rect)

    screen.blit(background, background_rect)
    screen.blit(bird, bird_rect)
    screen.blit(floor, floor1_rect)
    screen.blit(floor, floor2_rect)
    pygame.display.flip()
    clock.tick(300)
