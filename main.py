import pygame

# size = 45
# WIDTH = size * 12
# HEIGHT = size * 10

WIDTH = 640
HEIGHT = 420

FPS = 60
WHITE_COLOR = (255, 255, 255)
GRAY_COLOR = (177, 177, 177)
BLACK_COLOR = (0, 0, 0)
RED_COLOR = (255, 0, 0)
ORANGE_COLOR = (241, 141, 24)
GREEN_COLOR = (102,   235, 82)
BLUE_COLOR = (0,   0,   255)
WHITE_BLUE_COLOR = (65, 189, 236)
YELLOW_COLOR = (255, 255, 51)
PURPLE_COLOR = (209, 82, 235)
PURPLE_COLOR2 = (141, 9, 156)
PURPLE_COLOR3 = (215, 123, 226)

pygame.init()
clock = pygame.time.Clock()
surface = pygame.display.set_mode((WIDTH, HEIGHT))
surface.fill(WHITE_COLOR)
pygame.display.set_caption("Первая программа на PyGame")
pygame.display.set_icon(pygame.image.load("rocket.png"))

size = 75
left = WIDTH//2 - size//2
top = HEIGHT//2 - size//2

# КРУЖКА
# r1 = pygame.draw.rect(surface, PURPLE_COLOR, (left, top, size, 100))
# pygame.draw.ellipse(surface, PURPLE_COLOR, (left, top+70, 75, 50))
# pygame.draw.ellipse(surface, PURPLE_COLOR3, (left, top-12, 75, 25))
# pygame.draw.ellipse(surface, PURPLE_COLOR, (left+35, top+15, 70, 70), 8)

# РАДУГА
# pygame.draw.ellipse(surface, RED_COLOR, (-35, top-69, WIDTH+70, HEIGHT+100), 35)
# pygame.draw.ellipse(surface, ORANGE_COLOR, (-17, top-35, WIDTH+35, HEIGHT+100), 35)
# pygame.draw.ellipse(surface, YELLOW_COLOR, (0, top, WIDTH, HEIGHT+100), 35)
# pygame.draw.ellipse(surface, GREEN_COLOR, (17, top+35, WIDTH-35, HEIGHT+100), 35)
# pygame.draw.ellipse(surface, WHITE_BLUE_COLOR, (35, top+70, WIDTH-70, HEIGHT+100), 35)
# pygame.draw.ellipse(surface, BLUE_COLOR, (52, top+105, WIDTH-105, HEIGHT+100), 35)
# pygame.draw.ellipse(surface, PURPLE_COLOR, (69, top+140, WIDTH-140, HEIGHT+100), 35)

# ШАХМАТНАЯ ДОСКА
# colors = [WHITE_COLOR, BLACK_COLOR]
# pygame.draw.rect(surface, GRAY_COLOR, (size, 0, size*10, size*10), 5)
# for i in range(8):
#     for j in range(8):
#         pygame.draw.rect(surface, colors[j%2], (size*j+size*2, size*i+size, size, size))
#     colors[0], colors[1] = colors[1], colors[0]
#
# pygame.draw.rect(surface, BLACK_COLOR, (size*2, size, size*8, size*8), 5)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.update()
    clock.tick(FPS)



