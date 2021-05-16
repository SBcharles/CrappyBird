import sys
import pygame

pygame.init()

size = width, height = 288, 512

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

background = pygame.image.load("assets/background-day.png")
background_rect = background.get_rect()

bird = pygame.image.load("assets/yellowbird-midflap.png")
bird_rect = bird.get_rect(center=(width / 2, height / 2))

floor = pygame.image.load("assets/base.png")
floor_rect = floor.get_rect(bottomleft=(0, height))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(background, background_rect)
    screen.blit(bird, bird_rect)
    screen.blit(floor, floor_rect)
    pygame.display.flip()
    clock.tick(60)
