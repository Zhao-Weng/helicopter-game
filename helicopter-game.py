import pygame
import time
from random import *

sunset = (253, 72,47)
greenyellow = (184,255,0)
brightblue = (47,228,253)
orange = (255, 113,0)
yellow = (255,236,0)
purple = (252,67, 255)

colorChoices = [greenyellow, brightblue,orange,yellow,purple]

black = (0,0,0)
white = (255, 255,255)
surfaceHeight = 500
surfaceWidth = 800

imageHeight = 99
imageWidth = 199

pygame.init()
#init the class
surface = pygame.display.set_mode((800, 600)) #set the display mode
pygame.display.set_caption('Helicopter') #change the name to be helicopter
#set frame per second
img = pygame.image.load('Helicopter.png')
clock = pygame.time.Clock()


def level(level):
    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("Level: " + level,True, black)
    surface.blit(text,[0,30])

def score(count):
    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("Score: " + str(count),True, black)
    surface.blit(text,[0,0])
    

def blocks(x_block,y_block,block_width, block_height, gap,blockColor):
    
    pygame.draw.rect(surface, blockColor, [x_block, y_block, block_width,block_height]);
    pygame.draw.rect(surface, blockColor, [x_block, y_block + block_height+ gap, block_width,surfaceHeight]);

def helicopter(x, y, image):
	#place the helicopter
    surface.blit(img, (x, y))





def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP,pygame.QUIT]):
        if event.type ==pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type ==pygame.KEYDOWN:
            continue
        print("1")
        return event.key
    return None
        

def makeTextObjs(text,font):
    textSurface = font.render(text, True,sunset)
    return textSurface,textSurface.get_rect()
    

def msgSurface(text):
        smallText = pygame.font.Font('freesansbold.ttf',20)#use pygame to set font
        largeText = pygame.font.Font('freesansbold.ttf',150)
        titleTextSurf, titleTextRect = makeTextObjs(text,largeText)
        titleTextRect.center = surfaceWidth /2,surfaceHeight/2
        surface.blit(titleTextSurf,titleTextRect)

        typeTextSurf,typeTextRect = makeTextObjs('Press any key to continue', smallText)
        typeTextRect.center = surfaceWidth /2,(surfaceHeight/2 + 100)
        surface.blit(typeTextSurf, typeTextRect)

        pygame.display.update()
        time.sleep(1)

        while replay_or_quit() == None:
            clock.tick()

        main()


        
    

def gameOver():
    msgSurface('BOOM!')




def main():
    game_over = False
    x = 150
    y = 200
    y_move = 5

    current_score = 0
    current_level = "you are just a beginner"

    x_block = surfaceWidth
    y_block = 0
    block_width = 75
    block_height = randint(0, surfaceHeight/2)
    gap = imageHeight * 3
    block_move = 3
    blockColor = colorChoices[randrange(0, len(colorChoices))]
    
    
    while not game_over:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#pygame event type
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -5
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 5
        
        y += y_move


        surface.fill(white)
        helicopter(x, y, img)


        
        blocks(x_block, y_block, block_width, block_height, gap,blockColor)
        score(current_score)
        level(current_level)
        x_block -= block_move
        #draw the block 

        if y > surfaceHeight  or y <0 :
            gameOver()

        if x_block < (-1* block_width):
            x_block = surfaceWidth
        #block and helicopter can be off the surface
            block_height = randint(0, surfaceHeight /2 )
            blockColor = colorChoices[randrange(0, len(colorChoices))]
            #change the color
            current_score +=5
            #increment the score


        if x + imageWidth > x_block and x < x_block + block_width:
            #pass the pass or not
            if y < block_height:
                gameOver()

        if x + imageWidth > x_block and x < x_block + block_width:
            if y + imageHeight> block_height + gap:
                gameOver()

        
            

        if 15 <= current_score  <=25:
            gap = imageHeight * 2.5
            block_move = 5
            current_level = "you are good"
        if 30 <= current_score:
            gap = imageHeight * 2
            block_move = 7
            current_level = "you are master!"
        
        pygame.display.update()
                
                
            #dipslay.flip updates the whole surface, 
            #display.update can update a specific area
        clock.tick(60)
            #20-30 normal human eye fluent
            #>30 no difference, waste graphic computation
            #60 frame per second




main()
pygame.quit()
quit() #quit the program
