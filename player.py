import pygame

class Player:
    def __init__(self,x,y):
        self.x = int(x) #assigns self.x and self.y to parameters called.
        self.y = int(y)
#The pathway of the image
        self.velX = 0
        self.velY = 0 # vertical and horizontal velocities set to 0
        self.player_size = 10
        self.left_pressed = False #creates a variable that shows whether or not a key has been pressed
        self.right_pressed = False
        self.top_pressed = False
        self.bottom_pressed = False #arrow keys pressed set to false because no keys have been pressed yet
        self.speed = 4 #speed of the avatar
        self.rectangle = pygame.Rect(self.x,self.y,self.player_size,self.player_size)

    def get_player_position(self,x,y,grid_cells): #getting current cell position of the player
        for cell in grid_cells:
            if cell.x == x and cell.y == y: #iterates through grid_cells until the x and y coordinates of the player is found in grid_cells
                return cell
            
    def check_move(self,tile,grid_cells,thickness): #checks if a player can move to another cell without there being a wall in the way
        current_cell_x, current_cell_y = self.x//tile, self.y//tile #work out the current x coordinate of the cell that the player is in
        #works out the current y coordinate of the cell that the player is in
        current_cell  = self.get_player_position(current_cell_x,current_cell_y, grid_cells) # calls the function and takes the current cell attributes as parameters
        current_cell_abs_x, current_cell_abs_y = current_cell_x * tile, current_cell_y * tile #calculates the absolute value of the current cell
        if self.left_pressed: #if the left key is pressed 
            if current_cell.walls_direction['left']:#if the left wall is in the wall array that means it exists, and the player is blocked in that direction
                if self.x <= current_cell_abs_x + thickness: # works out how far away the player is from the wall and if they are too close to the wall
                    self.left_pressed = False # then left_pressed is set to false so the player doesn't move
        if self.right_pressed:
            if current_cell.walls_direction['right']: #does same thing
                if self.x >= current_cell_abs_x + tile - (self.player_size + thickness): 
                    self.right_pressed = False
        if self.top_pressed:
            if current_cell.walls_direction['top']: #does same thing
                if self.y <= current_cell_abs_y + thickness:
                    self.top_pressed = False
        if self.bottom_pressed:
            if current_cell.walls_direction['bottom']: #does same thing
                if self.y >= current_cell_abs_y + tile - (self.player_size + thickness):
                    self.bottom_pressed = False
    
    def draw_(self, screen):
        pygame.draw.rect(screen,"#0A5E59",self.rectangle) #creates a rectangle that will be the player's avatar

    def update_player(self): #updates the player's position on the screen
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed #if left key pressed and right key not: horizontal velocity set to negative
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed #if right key pressed and left key not: horizontal velocity set to positive
        if self.top_pressed and not self.bottom_pressed:
            self.velY = -self.speed #if up key pressed and down key not: vertical velocity set to negative
        if self.bottom_pressed and not self.top_pressed:
            self.velY = self.speed #if down key pressed and up key not: vertical velocity set to positive
        self.x += self.velX # changes x to x + velocity of x
        self.y += self.velY # changes y to y + velocity of y
        self.rectangle = pygame.Rect(int(self.x),int(self.y),self.player_size, self.player_size) #moves the rectangle to the position the user wants the avatar to move

