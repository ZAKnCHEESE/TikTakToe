import pygame,sys   

pygame.init()

clock =  pygame.time.Clock()
screen = pygame.display.set_mode((700,700))

running = True

player_turn = "X"
player_x_score = 0
player_O_score = 0  



def creating_assets():
    global playing_square,vertical_line,horizontal_line, font
    playing_square = pygame.Surface((500,500))
    playing_square.fill((47,79,79))

    vertical_line = pygame.Surface((5,500))
    vertical_line.fill((0,0,0))

    horizontal_line = pygame.Surface((500,5))
    horizontal_line.fill((0,0,0))

    font = pygame.font.Font("luckiest-guy/LuckiestGuy.ttf",50)

    rect_00 = pygame.Rect()
    

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

    turn = font.render(f"Player turn: {player_turn}",True,(0,0,0))
    turn_rect = turn.get_rect(topleft = (140,630))

    screen.blit(turn,turn_rect)

    big_x = font.render("X",True,(0,0,0))
    big_o = font.render("O",True,(0,0,0))


creating_assets()

while running:
    playing_field()
    #screen.fill((47,79,79))
    for  event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if keys[pygame.K_SPACE]:
                print(player_turn)

                if player_turn == "X":
                    player_turn = "O"

                elif player_turn == "O":
                    player_turn = "X"
            

    pygame.display.update()
    clock.tick(60)
