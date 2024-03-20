import pygame 

pygame.init()

screen=pygame.display.set_mode((400,600))
game=True
x=30
y=30
fps=30
clock=pygame.time.Clock()
color = (255, 100, 0)
while game:
   
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False

    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        if y>20:
         y-=3
    if pressed[pygame.K_DOWN]:
        if y<580:
         y+=3
    if pressed[pygame.K_LEFT]:
        if x>20:
         x-=3
    if pressed[pygame.K_RIGHT]:
        if x<380:
         x+=3

    screen.fill((1,2,0))

    pygame.draw.circle(screen,color,(x,y),25,25)
    clock.tick(60)
    pygame.display.update()


   
 

