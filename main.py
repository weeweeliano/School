import pygame, sys # sys is a module called in to create an exit function

from maze import Maze
from player import Player
from game import Game # importing all the classes
from timer import Timer

pygame.init()
pygame.font.init()

tile = 30 
window_size = (500,500) #tuple that takes 500,500 as values
screen = (window_size[0]+200,window_size[1]) #screen is a tuple that takes the first item of window_size (500) and the last item of window_size(500)
screen = pygame.display.set_mode(screen)
# main class
class Main():
    def __init__(self,screen):
        self.screen = screen
        self.running = True #keeps the screen running
        self.game_over = False
        self.FPS = pygame.time.Clock() #changes the number of frames per second

    def all_draw(self,maze,tile,player,game,timer):
        #drawing the maze
        [cell.draw(screen,tile) for cell in maze.grid_cells]
        game.goal(self.screen)
        player.draw_(self.screen)
        player.update_player()
        #Draw player by creating an instance of Player called player1
        if self.game_over:
            timer.stopTimer()
        else:
            timer.updateTimer()
        self.screen.blit(timer.displayTimer(),(500,50))
        setting_icon = pygame.draw.rect(screen,'#00FFE0',[500,150,60,60])
        ffont = pygame.font.SysFont('Agency FB',35)
        quit = ffont.render('QUIT',True,'black')
        screen.blit(quit,(505,160))
        pygame.display.flip()
        

    def main(self,frame_size,tile): #the main loop
        cols,rows = frame_size[0]//tile,frame_size[-1]//tile 
        maze = Maze(cols,rows)
        game = Game(maze.grid_cells[-1],tile)
        player = Player(tile//3,tile//3)
        maze.generate_maze()
        timer = Timer()
        timer.startTimer()
        while self.running:
            self.screen.fill("white")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 500 <= mouse[0]<= 560 and 150 <= mouse[1]<= 210:#if the mouse is touching the settings button when clicked 
                        settings()
            mouse = pygame.mouse.get_pos()#stores coordinates of mouse
            if event.type == pygame.KEYDOWN: #calls the built in pygame function that allows for keyboard inputs
                if not self.game_over:
                    if event.key == pygame.K_LEFT: #the built-in code for the left key
                        player.left_pressed = True
                    if event.key == pygame.K_RIGHT: #the built-in code for the right key
                        player.right_pressed = True
                    if event.key == pygame.K_UP: #the built-in code for the up key
                        player.top_pressed = True
                    if event.key == pygame.K_DOWN: #the built-in code for the down key
                        player.bottom_pressed = True
                    player.check_move(tile, maze.grid_cells, maze.thickness)
            # If pressed key released
            if event.type == pygame.KEYUP: #once the key has stop being pressed the arrow key pressed value is set to false again
                if not self.game_over:
                    if event.key == pygame.K_LEFT:
                        player.left_pressed = False
                    if event.key == pygame.K_RIGHT:
                        player.right_pressed = False
                    if event.key == pygame.K_UP:
                        player.top_pressed = False
                    if event.key == pygame.K_DOWN:
                        player.bottom_pressed = False
                    player.check_move(tile, maze.grid_cells, maze.thickness)
            if game.isgame_over(player): #if the game is over then self.game_over set to true and the arrows being pressed reset to false
                self.game_over = True
                game_screen()
                player.left_pressed = False
                player.right_pressed = False
                player.top_pressed = False
                player.bottom_pressed = False
            self.all_draw(maze, tile, player, game,timer)
            self.FPS.tick(60)

def mazescreen():
    if __name__ == "__main__": #the main game loop
        window_size = (500,500) #tuple that takes 500,500 as values
        screen = (window_size[0]+200,window_size[1]) #screen is a tuple that takes the first item of window_size (500) and the last item of window_size(500)
        tile_size = 30
        screen = pygame.display.set_mode(screen)
        pygame.display.set_caption("Maze Game")

        game = Main(screen)
        game.main(window_size,tile)

def settings():
    pygame.display.set_caption("Settings")
    screen_size = (800,800)
    screen = pygame.display.set_mode(screen_size)
    background = ("white")
    textcolour = ("#0A5E59")
    ffont = pygame.font.SysFont('Agency FB',35)
    bigfont = pygame.font.SysFont('Agency FB', 80)
    width = screen.get_width()
    height = screen.get_height()
    setting_text = bigfont.render('SETTINGS',True,textcolour)
    new_game = ffont.render('NEW GAME',True,textcolour)#creates the text for the play button
    exit = ffont.render('HOME',True,textcolour)
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            #if the mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if width/2-70 <= mouse[0]<= width/2+140 and height/2-100 <= mouse[1]<= height/2:
                    mazescreen()#maze game starts
                elif width/2-19 <= mouse[0]<= width/2 and height/2 < mouse[1]<= height/2+150:
                    home_screen()
        screen.fill('white')
        mouse = pygame.mouse.get_pos()#stores coordinates of mouse
    #when mouse hovers over play button it changes to the hover colour
        if width/2-70 <= mouse[0] <= width/2+140 and height/2-100 <= mouse[1] <= height/2:
            pygame.draw.rect(screen,"#00FFE0",[width/2-70,height/2-100,140,40])
        else:
            pygame.draw.rect(screen,"white",[width/2-70,height/2-100,140,40])
        screen.blit(new_game, (width/2-63,height/2-100))
        screen.blit(exit, (width/2-32,height/2+50))#+50 to width
        screen.blit(setting_text,(width/2-125, height/2-300))
        pygame.display.update()


#creating the home screen

def home_screen():
    pygame.display.set_caption("Home Screen")#names screen
    screen_size = (800,800)
    screen = pygame.display.set_mode(screen_size)
    colour = ("white")#colour of the text
    colour_hover = ("#00FFE0")#when the cursor touches the box it will turn this colour 
    play_colour = ("black")
    exit_colour = ("#00FFE0")
    ffont = pygame.font.SysFont('Agency FB',35)#the font i am using
    mazefont = pygame.font.SysFont('Agency FB', 80)
    width = screen.get_width()
    height = screen.get_height()
    play = ffont.render('PLAY',True,play_colour)#creates the text for the play button
    exit = ffont.render('Exit',True,exit_colour)
    mazee = mazefont.render("MAZE GAME",True,"#00FFE0")

    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            #if the mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if width/2-70 <= mouse[0]<= width/2+140 and height/2-100 <= mouse[1]<= height/2: #if the mouse clicks in the area of the button 
                    mazescreen()#maze game starts
                elif width/2-19 <= mouse[0]<= width/2 and height/2 < mouse[1]<= height/2+150:
                    pygame.quit() #if exit button pressed then program terminates
        screen.fill('black')
        mouse = pygame.mouse.get_pos()#stores coordinates of mouse
    #when mouse hovers over play button it changes to the hover colour
        if width/2-70 <= mouse[0] <= width/2+140 and height/2-100 <= mouse[1] <= height/2: #if mouse is in the ranges
            pygame.draw.rect(screen,colour_hover,[width/2-70,height/2-100,140,40])#a blue rectangle is drawn over the white one
        else:
            pygame.draw.rect(screen,colour,[width/2-70,height/2-100,140,40])#the white rectangle stays drawn
        screen.blit(play, (width/2-25,height/2-100))#displays all the text
        screen.blit(exit, (width/2-19,height/2+50))
        screen.blit(mazee,(width/2-135, height/2-300))
        pygame.display.update()

def game_screen():
    pygame.display.flip
    pygame.time.delay(2500) #2.5 second delay
    pygame.display.set_caption("Game Over")
    screen_size = (800,800)
    screen = pygame.display.set_mode(screen_size)
    background = ("white")
    textcolour = ("#0A5E59")
    ffont = pygame.font.SysFont('Agency FB',35)
    bigfont = pygame.font.SysFont('Agency FB', 80)
    width = screen.get_width()
    height = screen.get_height()
    congrats = bigfont.render('Congratulations!',True,textcolour)#creates the text for the play button
    message = ffont.render('You have successfully completed the maze! ',True,textcolour)
    retry = ffont.render('PLAY AGAIN',True,textcolour)
    home = ffont.render('Home',True,textcolour)
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            #If the mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if width/2-70 <= mouse[0]<= width/2+140 and height/2-100 <= mouse[1]<= height/2:
                    mazescreen()#maze game starts
                elif width/2-19 <= mouse[0]<= width/2 and height/2 < mouse[1]<= height/2+150:
                    home_screen()
        screen.fill('white')
        mouse = pygame.mouse.get_pos()#stores coordinates of mouse
    #When mouse hovers over play button it changes to the hover colour
        if width/2-70 <= mouse[0] <= width/2+140 and height/2-100 <= mouse[1] <= height/2:
            pygame.draw.rect(screen,"#00FFE0",[width/2-70,height/2-100,140,40])
        else:
            pygame.draw.rect(screen,"white",[width/2-70,height/2-100,140,40])
        screen.blit(retry, (width/2-63,height/2-100))
        screen.blit(home, (width/2-32,height/2+50))#+50 to width
        screen.blit(congrats,(width/2-200, height/2-300))
        screen.blit(message, (width/2-225,height/2-200))
        pygame.display.update()

home_screen()

