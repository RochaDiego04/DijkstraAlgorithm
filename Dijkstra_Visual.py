from Board import board
import pygame

pygame.init()

WIDTH = 900
HEIGHT = 950
screen  = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60
level = board

# BOARD specifications
HORIZONTAL = 4
VERTICAL = 4

font = pygame.font.Font('freesansbold.ttf', 20)


def draw_board():
    num1 = ((HEIGHT - 50) // VERTICAL)
    num2 = (WIDTH // HORIZONTAL)
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 0:
                x = (j * num2 + (0.5*num2))
                y = (i * num1 + (0.5*num1))
                #screen.blit(monster_sprite,(x, y))
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5*num2), i * num1 + (0.5*num1)), 4)
        

# Load the sprite for monsters
monster_sprite = pygame.image.load("img/Monstruo.png")

run = True
while run:
    timer.tick(fps)
    screen.fill('black')
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()
pygame.quit()
