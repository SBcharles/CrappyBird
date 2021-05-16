import sys
import pygame

pygame.init()

size = width, height = 288, 512

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

background = pygame.image.load("assets/background-day.png")
background_rect = background.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(background, background_rect)
    pygame.display.flip()
    clock.tick(60)
