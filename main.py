import pygame,sys
from paddle import Paddle
from ball import Ball

#initialise pygame
pygame.init()

#colors
BLACK = (0,0,0)
WHITE = (255,255,255)

#open a new window
size=(700,500) #width,height
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

#the clock will be used to control the framerate
clock = pygame.time.Clock()

#instantiating the class "Paddle" and defining parameters
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x=20
paddleA.rect.y=200

paddleB = Paddle(WHITE, 10,100)
paddleB.rect.x=670
paddleB.rect.y=200

#instantiating the class "Ball"
ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195 


#a list that will contain all the sprites
all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

#initialise player scores
scoreA = 0
scoreB = 0


#-main game loop-
while True:
    #-main event loop-
    for event in pygame.event.get(): #user did something
        if event.type==pygame.QUIT: #if user clicked close
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x: #if press the x key will quit the game
                pygame.quit()
                sys.exit()

    #moving the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)
    
    
    #-game logic-
    all_sprites_list.update()

    #check if the ball is bouncing against any of the 4 walls and the logic of scores
    if ball.rect.x>=690: #690 is because of the ball size(10)
        ball.velocity[0] = -ball.velocity[0]
        scoreA+=1
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
        scoreB+=1
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]

    if scoreA==11 or scoreB ==11:
        scoreA = 0
        scoreB = 0
        ball.rect.x = 345
        ball.rect.y = 195 
        all_sprites_list.update()

    #detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball,paddleA) or  pygame.sprite.collide_mask(ball,paddleB):
        ball.bounce()

   
        

    #-drawing code-

    #first,clear the screen to black
    screen.fill(BLACK)
    #draw the net
    pygame.draw.line(screen,WHITE,[349,0],[349,500],5)

    #draw all the sprites
    all_sprites_list.draw(screen)

    #display scores
    font = pygame.font.Font(None,74)
    text = font.render(str(scoreA),1,WHITE)
    screen.blit(text,(250,10))
    text = font.render(str(scoreB),1,WHITE)
    screen.blit(text,(420,10))



    #update the screen
    pygame.display.flip()

    #fps
    clock.tick(60)


    