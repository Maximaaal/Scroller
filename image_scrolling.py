# https://github.com/Tomeczekqq/dvd-corner

from random import randint
import pygame
import sys

exit = False

# Settings
SIZE = width, height = 800, 600  # Resolution. (4:3)!
BG_COLOR = (0, 0, 0)  # Background color in RGB
fullscreen = True  # Fullscreen

images = ["img1.png", "img2.jpeg", "img3.jpeg"]
imageLength = 2

currentImage = 0
image = pygame.image.load(images[currentImage])

clock = pygame.time.Clock()
img_size = image.get_rect().size
img_height = image.get_rect().height
img_width = image.get_rect().width
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('DVD Corner')
if fullscreen:
    DISPLAYSURF = pygame.display.set_mode((1280, 2048), pygame.FULLSCREEN)
    pygame.mouse.set_visible(False)

# x = randint(0, width)
x = 640 - (img_width/2)
y = 0
x_speed = 0
y_speed = 10

print(img_height)
print(img_width)


def move(x, y):
    screen.blit(image, (x, y))


while exit == False:
    
    
    screen.fill(BG_COLOR)
#     if (x + img_size[0] >= width) or (x <= 0):
#         x_speed = -x_speed
#     if (y + img_size[1] >= height) or (y <= 0):
#         y_speed = -y_speed
    x += x_speed
    y += y_speed
    move(x, y)

    # for index, i in enumerate(images):
    #     print(i)
    print(currentImage)
    
    
    
#     if y > 2048:
#         y = - img_height
# #         image = pygame.image.load('bella2 .jpg')
#         image = pygame.image.load(images[0 + 1])
#         currentImage = currentImage + 1
    if y > 2048:
            y = - img_height
            currentImage = currentImage + 1
            image = pygame.image.load(images[currentImage])
            
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
                
    pygame.display.update()
    clock.tick(59)
    

pygame.quit()
sys.exit()