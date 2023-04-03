import pygame

pygame.init()

WIDTH = 900
HEIGHT = 950
screen  = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 20)

# Load the sprite for monsters
wall_sprite = pygame.image.load("img/Monstruo.png")

run = True
while run:
    timer.tick(fps)
    screen.fill('black')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()
pygame.quit()
