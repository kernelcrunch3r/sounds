import pygame

pygame.init()

# font=pygame.font.SysFont(None,25)
# def printScore (p1, p2, color):
#   score=font.render((p1,True,color))

# Initialize the joysticks.
pygame.joystick.init()

# sounds setup
hitSound = pygame.mixer.Sound('sounds\\blip.wav')
scoreSound = pygame.mixer.Sound('sounds\\score.wav')
music = pygame.mixer.music.load('sounds\\music.mp3')
# start background music
pygame.mixer.music.play(-1)

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
gameSizeHeight = 800
gameSizeWidght = 800
win = pygame.display.set_mode((gameSizeWidght, gameSizeHeight))
pygame.display.set_caption("Pong")

# make character move
# player 1
p1x = 50
p1y = 50
p1width = 10
p1height = 100
# player 2
p2x = 750
p2y = 50
p2width = 10
p2height = 100
vel = 5
vel = 5
# ball
bx = 400
by = 400
bleft = True
bdown = True
hits = 0
bspeed = 2

p1Score = 0
p2Score = 0

run = True

while run:
    pygame.time.delay(10)
    ###joystick trial
    for event in pygame.event.get():  # User did something.
        if event.type == pygame.QUIT:  # If user clicked close.
            run = False  # Flag that we are done so we exit this loop.
        elif event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
            by -= vel

        elif event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")

    ###
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # if keys[pygame.K_LEFT]:
    #   x-=vel
    # if keys[pygame.K_RIGHT]:
    #   x+=vel
    if keys[pygame.K_q]:  # add the limits for the game size

        p1y -= vel
    if keys[pygame.K_a]:
        p1y += vel

    # controls p2
    if keys[pygame.K_UP]:  # add the limits for the game size

        p2y -= vel
    if keys[pygame.K_DOWN]:
        p2y += vel
    win.fill((0, 0, 0))

    # direction of balll
    if (bx == p1x + p1width and by >= p1y and by <= p1y + p1height):
        bleft = False
        # play a sound effect
        hitSound.play()

    elif (bx == p2x and by >= p2y and by <= p2y + p2height):
        bleft = True
        hitSound.play()

    elif (bx < p1x - 20 or bx > p2x + 20):  # put the ball back in the middle after a score
        # play score sound
        scoreSound.play()
        if (bleft == True):
            p2Score += 1
        else:
            p1Score += 1
        bx = 400
        by = 400
        print("PLayer 1: ", p1Score, " Player 2: ", p2Score, "Speed: ", bspeed)
    else:
        if (bdown == True):
            by += bspeed
        elif (bdown == False):
            by -= bspeed

    # hits top or bottom
    if (by <= 0):
        bdown = True
    elif (by >= gameSizeHeight):
        bdown = False

    # move ball
    if (bleft == True):
        bx -= bspeed
    else:
        bx += bspeed

    pygame.draw.rect(win, (255, 0, 0), (p1x, p1y, p1width, p1height))
    pygame.draw.rect(win, (255, 0, 0), (p2x, p2y, p2width, p2height))
    # pygame.draw.circle(win,(255,0,0),(x,y),radius)
    pygame.draw.circle(win, (0, 255, 0), (bx, by), 20)
    pygame.display.update()
pygame.quit()






