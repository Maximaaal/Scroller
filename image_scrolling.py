from random import randint
import pygame
import sys


exit = False

SIZE = width, height = 800, 600
BG_COLOR = (0, 0, 0)
fullscreen = True

images = []
i = 0
while len(images) < 97:
    images.append("images/img%d.jpeg" % i)
    i += 1
print(images)

# images = ["img1.png", "img2.jpeg", "img3.png", "img4.png"]
# yPos = [-454, -1798, -1126, -1220]

currentImage = 0
image = pygame.image.load(images[currentImage])

border1 = pygame.image.load('border1.png')
border2 = pygame.image.load('border2.png')

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
y_speed = 10

print(img_height)
print(img_width)

# img_names = []
# j = 0
# while len(img_names) < 39:
#     images.append("border/border_%d.jpg" % j)
#     j += 1

# all_imgs = []
# for img in img_names:
#     all_imgs[img] = pygame.image.load(img)

# for img in img_names:
#     screen.blit(all_imgs[img], (0, 0))


def move(x, y):
    screen.blit(border2, (0, 0))
    screen.blit(image, (x, y))
    screen.blit(border1, (0, 512))
    


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

    if y > 2048:
        # y = 0 - img_height
        currentImage = randint(0, 96)
        image = pygame.image.load(images[currentImage])
        y = (0 - image.get_rect().height) - 100
        

    # if currentImage >= 3:
    #     currentImage = 0        
    
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