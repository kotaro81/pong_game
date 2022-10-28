import pygame
BLACK = (0,0,0)

class Paddle(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        #call the parent class(Sprite) constructor
        super().__init__()
        #create a surface:pygame object for representing images
        self.image = pygame.Surface([width,height])
        #set the background color and set it to be transparent
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        #draw the paddle
        pygame.draw.rect(self.image,color,[0,0,width,height])

        #get the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

    
    def moveUp(self,pixels):
        self.rect.y -= pixels
        if self.rect.y<0:
            self.rect.y=0
        
    
    def moveDown(self,pixels):
        self.rect.y+=pixels
        if self.rect.y>400:
            self.rect.y=400
