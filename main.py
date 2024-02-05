from run import *

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        run(event)

    button()
    
    pygame.display.flip()

pygame.quit()
