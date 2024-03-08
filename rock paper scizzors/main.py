
import random
import pygame 
import User


def create_start_menu(game_state):
    screen.fill("light blue")
    font = pygame.font.SysFont('purisa',40)
    title = font.render('Rock Paper Scizzors', True, (0,0,0))
    screen.blit(title, (screen.get_width()/2-title.get_width()/2, screen.get_height()/2-title.get_height()/2))
    font = pygame.font.SysFont('purisa',32)
    instructions = font.render('Press SPACE To Start', True, (0,0,0))
    screen.blit(instructions, (screen.get_width()/2-instructions.get_width()/2,screen.get_height()/2-instructions.get_height()/2+30))
    pressed_space = pygame.key.get_pressed()
    if pressed_space[pygame.K_SPACE] == True:
        game_state = "game_mode"
        return game_state
    return game_state


#setting up game 
pygame.init();
pygame.display.set_caption('Rock Paper Scissors')
screen = pygame.display.set_mode((1500,900))
clock = pygame.time.Clock()
running = True 
weaponChoice = ""
weaponChoice2 = ""
clicking = False
mousePos = pygame.mouse.get_pos()

player1 = User.Player("p1",0,"")
player2 = User.Player("p2",0,"")

game_state = "start_menu"

i = 0

rock = pygame.image.load('rock.png').convert()
rock_rect = rock.get_rect()
rock_rect.center = (422,585)

paper = pygame.image.load('paper.png').convert()
paper_rect = paper.get_rect()
paper_rect.center = (729,565)

scissors = pygame.image.load('scissors.png').convert()
scissors_rect = scissors.get_rect()
scissors_rect.center = (995,553)

while running:
    #print(mousePos)
    mousePos = pygame.mouse.get_pos()
    weaponChoice = player1.weapon
    weaponChoice2 = player2.weapon
    if game_state == "start_menu":
        game_state = create_start_menu(game_state)
    
    elif game_state == "game_mode" and weaponChoice == "":
        scissors_rect.center = (995,553)
        paper_rect.center = (729,565)
        rock_rect.center = (422,585)

        screen.fill("#F5F4F0")
        font = pygame.font.SysFont('purisa',32)
        title = font.render("Player 1's Turn", True, (0,0,0))
        screen.blit(title, (screen.get_width()/2-title.get_width()/2, screen.get_height()/2-title.get_height()/2-100))
        screen.blit(rock,rock_rect)
        screen.blit(paper,paper_rect)
        screen.blit(scissors,scissors_rect)
        #screen.blit(rock,(300-rock_rect.x/2,screen.get_height()/2-rock_rect.x/2))
        #screen.blit(paper,(610-paper_rect.x/2,screen.get_height()/2-paper_rect.x/2-50))
       #screen.blit(scissors, (900-scissors_rect.x/2,screen.get_height()/2-scissors_rect.x/2-50))

        if clicking == True and weaponChoice == "":
            if rock_rect.collidepoint(mousePos) == True:
                player1.weapon = "rock"
            if paper_rect.collidepoint(mousePos) == True:
                player1.weapon = "paper"
            if scissors_rect.collidepoint(mousePos) == True:
                player1.weapon = "scissors"
        clicking = False
        weaponChoice = player1.weapon
        #print("player 1 chose " + player1.weapon)

    
    elif game_state == "game_mode" and weaponChoice2 == "":
        screen.fill("#F5F4F0")
        font = pygame.font.SysFont('purisa',32)
        title = font.render("Player 2's Turn", True, (0,0,0))
        screen.blit(title, (screen.get_width()/2-title.get_width()/2, screen.get_height()/2-title.get_height()/2-100))
        screen.blit(rock,rock_rect)
        screen.blit(paper,paper_rect)
        screen.blit(scissors,scissors_rect)
        if clicking == True and weaponChoice2 == "":
            if rock_rect.collidepoint(mousePos) == True:
                player2.weapon = "rock"
            if paper_rect.collidepoint(mousePos) == True:
                player2.weapon = "paper"
            if scissors_rect.collidepoint(mousePos) == True:
                player2.weapon = "scissors"
            clicking = False 
            weaponChoice2 = player2.weapon
            #print("player 2 chose " + player2.weapon)
            game_state = "results"


    elif weaponChoice2 != "" and weaponChoice != "":
        screen.fill("#F5F4F0")
        font = pygame.font.SysFont('purisa',32)
        title = font.render("Player 1's Choice", True, (0,0,0))
        screen.blit(title, (screen.get_width()/2-title.get_width()/2-350, screen.get_height()/2-title.get_height()/2-100))
        title2 = font.render("Player 2's Choice",True, (0,0,0))
        screen.blit(title2, (screen.get_width()/2-title2.get_width()/2+350, screen.get_height()/2-title.get_height()/2-100))
        
        dW = ""
        tie = True

        if player1.weapon == "rock" and player2.weapon == "paper":
            dW = "player 2 wins"
            tie = False
        if player1.weapon == "paper" and player2.weapon == "scissors":
            dW = "player 2 wins"
            tie = False
        if player1.weapon == "scissors" and player2.weapon == "rock":
            dW = "player 2 wins"
            tie = False
        
        if player1.weapon == "paper" and player2.weapon == "rock":
            dW = "player 1 wins"
            tie = False
        if player1.weapon == "scissors" and player2.weapon == "paper":
            dW = "player 1 wins"
            tie = False
        if player1.weapon == "rock" and player2.weapon == "scissors":
            dW = "player 1 wins"
            tie = False

        elif tie == True: 
            dW = "player 1 and 2 have tied"
        

        
        decider = font.render(dW, True, (0,0,0))
        screen.blit(decider, (screen.get_width()/2-decider.get_width()/2, screen.get_height()/2-decider.get_height()/2))
        instructions = font.render('Press Space To Restart', True, (0,0,0))
        screen.blit(instructions, (screen.get_width()/2-instructions.get_width()/2,screen.get_height()/2-instructions.get_height()/2+30))
        
        if player1.weapon == "rock":
            rock_rect.center = (400, 560)
            screen.blit(rock,rock_rect)
        elif player1.weapon == "paper":
            paper_rect.center = (385, 560)
            screen.blit(paper,paper_rect)
        elif player1.weapon == "scissors":
            scissors_rect.center = (400, 560)
            screen.blit(scissors,scissors_rect)

        if player2.weapon == "rock":
            rock_rect.center = (400+700, 560)
            screen.blit(rock,rock_rect)
        elif player2.weapon == "paper":
            paper_rect.center = (385+700, 560)
            screen.blit(paper,paper_rect)
        elif player2.weapon == "scissors":
            scissors_rect.center = (400+700, 560)
            screen.blit(scissors,scissors_rect)

        pressed_space = pygame.key.get_pressed()
        if pressed_space[pygame.K_SPACE] == True:
            player1.weapon = ""
            player2.weapon = ""
            game_state = "game_mode"
            

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicking = True
                
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                clicking = False
                
                
 

            
            

            

    pygame.display.update()
    clock.tick(60)

