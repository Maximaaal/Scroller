from random import randint
import pygame
import sys

exit = False

SIZE = width, height = 800, 600
BG_COLOR = (0, 0, 0)
fullscreen = True

# load random image
images = []
i = 0
while len(images) < 97:
    images.append("images/img%d.jpg" % i)
    i += 1
print(images)

currentImage = 0
image = pygame.image.load(images[randint(0, 96)])

# borders and background
bgNative = pygame.image.load('bg/native_background.png')
bgBinary = pygame.image.load('bg/binary_background.png')
nativeTop = pygame.image.load('bg/native-border_top-min.png')
nativeBottom = pygame.image.load('bg/native-border_bottom-min.png')
binaryTop = pygame.image.load('bg/binary-border_top.png')
binaryBottom = pygame.image.load('bg/binary-border_bottom.png')

#screen setup
clock = pygame.time.Clock()
img_size = image.get_rect().size
img_height = image.get_rect().height
img_width = image.get_rect().width
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Scroller')

if fullscreen:
    DISPLAYSURF = pygame.display.set_mode((1280, 2048), pygame.FULLSCREEN)
    pygame.mouse.set_visible(False)

# img movement
x = 640 - (img_width/2)
y = 0 - (img_height/2)
x_speed = 0
y_speed = 3

print(img_height)
print(img_width)

# if image is too big then resize
if img_width > 900:
    newImg_width = img_width/1.5
    newImg_width = int(newImg_width)
    newImg_height = img_height/1.5
    newImg_height = int(newImg_height)
    image = pygame.transform.scale(image, (newImg_width, newImg_height))

# blit
def move(x, y):
    screen.blit(bgNative, (0, 0))
    screen.blit(bgBinary, (0, 1024)) 
    screen.blit(image, (x, y))
    # screen.blit(nativeTop, (0, 0))
    # screen.blit(nativeBottom, (0, 0))
    # screen.blit(binaryBottom, (0, 0))
    
while exit == False:
    
    screen.fill(BG_COLOR)

    x += x_speed
    y += y_speed

    move(x, y)
    print("y=", y)
    print("img_height=", img_height)

    # get image size
    img_size = image.get_rect().size
    img_height = image.get_rect().height
    img_width = image.get_rect().width

    # place image in middle
    x = 640 - (img_width/2)

    # after image is off screen then load next random image
    if y > 2048:
        currentImage = randint(0, 96)
        image = pygame.image.load(images[currentImage])
        if img_width > 900:
            img_width = img_width/1.5
        y = (0 - image.get_rect().height) - 100

    # if image is too big then resize
    if img_width > 900:
        newImg_width = img_width/1.5
        newImg_width = int(newImg_width)
        newImg_height = img_height/1.5
        newImg_height = int(newImg_height)
        image = pygame.transform.scale(image, (newImg_width, newImg_height))

    # esc killswitch
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
                       
    pygame.display.update()
    clock.tick(30)
    
pygame.quit()
sys.exit()