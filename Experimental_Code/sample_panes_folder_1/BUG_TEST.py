import pygame

pygame.init()
screen = pygame.display.set_mode((2560, 1440),  pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.SRCALPHA)

# Simple test with a transparent rectangle
test_surface = pygame.Surface((100, 100), pygame.SRCALPHA)
test_surface.fill((255, 0, 0, 128))  # Semi-transparent red

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # White background
    screen.blit(test_surface, (100, 100))
    pygame.display.flip()

pygame.quit()
