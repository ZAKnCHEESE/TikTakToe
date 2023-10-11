import pygame,sys   

pygame.init()

clock =  pygame.time.Clock()
screen = pygame.display.set_mode((700,700))

running = True

player_turn = "X"
player_x_score = 0
player_O_score = 0  



def creating_assets():
    global playing_square,vertical_line,horizontal_line, font,font2

    #the middle square where game will be played
    playing_square = pygame.Surface((500,500))
    playing_square.fill((47,79,79))

    #basic lines for visuals
    vertical_line = pygame.Surface((5,500))
    vertical_line.fill((0,0,0))

    horizontal_line = pygame.Surface((500,5))
    horizontal_line.fill((0,0,0))

    font = pygame.font.Font("luckiest-guy/LuckiestGuy.ttf",50)
    font2 = pygame.font.Font("luckiest-guy/LuckiestGuy.ttf",200)
    
    

def visuals():
    global big_o,big_x
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

    big_x = font2.render("X",True,(0,0,0))
    big_o = font2.render("O",True,(0,0,0))

def playing_field():
    global rect_0_0,rect_0_1, rect_0_2
    global rect_1_0,rect_1_1,rect_1_2
    global rect_2_0,rect_2_1,rect_2_2

    # first row of squares
    rect_0_0 = pygame.Rect(100,100,167,167)
    rect_0_1 = pygame.Rect(266,100,167,167)
    rect_0_2 = pygame.Rect(432,100,167,167)
    # second row
    rect_1_0 = pygame.Rect(100,266,167,167)
    rect_1_1 = pygame.Rect(266,266,167,167)
    rect_1_2 = pygame.Rect(432,266,167,167)
    #third row
    rect_2_0 = pygame.Rect(100,432,167,167)
    rect_2_1 = pygame.Rect(266,432,167,167)
    rect_2_2 = pygame.Rect(432,432,167,167)

creating_assets()
playing_field()


while running:
    visuals()
    #screen.fill((47,79,79))
    pygame.draw.rect(screen,(0,0,0),rect_2_2)
    screen.blit(big_x,rect_0_0)
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

    if rect_0_0.collidepoint(pygame.mouse.get_pos()):
        print(1)

    pygame.display.update()
    clock.tick(60)
