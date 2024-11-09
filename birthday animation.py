import pygame 
pygame.init()

#screen dimensions and title
WIDTH = 600
HEIGHT = 600
TITLE = "Birthday animation"

#setting up the screen and title
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)
#functions
bg1 = pygame.image.load("bday background.jpg")
bg2 = pygame.image.load("cake.jpg")
bg3 = pygame.image.load("present.jpg")

run = True
#while loop
while run == True:
    #image 1
    screen.blit(bg1,(0,0))
    font = pygame.font.SysFont("Arial",35)
    text = font.render("Happy birthday Owen!",True,"cyan")
    screen.blit(text,(170,270))
    pygame.display.update()
    pygame.time.delay(4000)
    
    #image 2
    screen.blit(bg2,(0,0))
    font = pygame.font.SysFont("Verdana",40)
    text = font.render("Enjoy this cake!",True,"green")
    screen.blit(text,(130,220))
    pygame.display.update()
    pygame.time.delay(4000)

    #image 3
    screen.blit(bg3,(0,0))
    font = pygame.font.SysFont("Times new roman",30)
    text = font.render("Hope you have a great year and a merry christmas!",True,"turquoise")
    screen.blit(text,(105,220))
    pygame.display.update()
    pygame.time.delay(4000)

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    pygame.display.update()