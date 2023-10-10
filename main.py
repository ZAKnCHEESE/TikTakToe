import pygame,sys   

pygame.init()

clock =  pygame.time.Clock()
screen = pygame.display.set_mode((700,700))

running = True

playing_square = pygame.Surface((500,500))
playing_square.fill((47,79,79))

vertical_line = pygame.Surface((5,500))
vertical_line.fill((0,0,0))

horizontal_line = pygame.Surface((500,5))
horizontal_line.fill((0,0,0))

def playing_field():
    screen.fill((105,105,105))
    screen.blit(playing_square,(100,100))

    screen.blit(vertical_line,(100,100))
    screen.blit(vertical_line,(595,100))

    screen.blit(vertical_line,(266,100))
    screen.blit(vertical_line,(432,100))

    screen.blit(horizontal_line,(100,100))
    screen.blit(horizontal_line,(100,595))

    screen.blit(horizontal_line,(100,266))
    screen.blit(horizontal_line,(100,432))




while running:
    playing_field()
    #screen.fill((47,79,79))
    for  event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)
