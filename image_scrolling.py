from random import randint
import pygame
import sys

exit = False

SIZE = width, height = 800, 600
BG_COLOR = (0, 0, 0)
fullscreen = True

images = ["img1.png", "img2.jpeg", "img3.png", "img4.png"]
yPos = [-454, -1798, -1126, -1220]

currentImage = 0
image = pygame.image.load(images[currentImage])

clock = pygame.time.Clock()
img_size = image.get_rect().size
img_height = image.get_rect().height
img_width = image.get_rect().width
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Scroller')
if fullscreen:
    DISPLAYSURF = pygame.display.set_mode((1280, 2048), pygame.FULLSCREEN)
    pygame.mouse.set_visible(False)


# x = randint(0, width)
x = 640 - (img_width/2)
y = 0 - (img_height + 500)
x_speed = 0
y_speed = 2

print(img_height)
print(img_width)


def move(x, y):
    screen.blit(image, (x, y))

while exit == False:
    
    
    screen.fill(BG_COLOR)

    x += x_speed
    y += y_speed

    move(x, y)
    print("y=", y)
    print("img_height=", img_height)

    img_size = image.get_rect().size
    img_height = image.get_rect().height
    img_width = image.get_rect().width

    x = 640 - (img_width/2)

    if y == 2048:
        # y = 0 - img_height
        currentImage = randint(0, 3)
        image = pygame.image.load(images[currentImage])
        y = (yPos[currentImage] - img_height)
        

    if currentImage >= 3:
        currentImage = 0        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
                
    pygame.display.update()
    clock.tick(60)
    

pygame.quit()
sys.exit()