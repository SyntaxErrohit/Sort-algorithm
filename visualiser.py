import pygame
pygame.init()

display_width = 451
display_height = 451
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Sort visualiser")

l = [5, 6, 3, 9, 4, 2, 7, 8]



running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
