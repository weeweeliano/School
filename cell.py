import pygame
from random import choice

#test code for the draw() function

walls_direction = {
    "top": True,
    "right": True,
    "bottom": True,
    "left": True
}  #i have created walls_direction and tile outside of the Cell class
  #This is so i can test the draw() function by itself
thickness = 4

class Cell:

    def __init__(self, x, y, thickness):
        self.x = x  #takes the x and y coordinates as parameters
        self.y = y
        self.walls_direction = {
            'top': True,
            'right': True,
            'bottom': True,
            'left': True
        }
        self.thickness = thickness
        self.visited = False

    def draw(self,screen,tile):  #drawing the cell walls
        x = self.x * tile
        y = self.y * tile
        if self.walls_direction['top']: #the code here checks if the key 'top' exists in the dictionary, as well as what the value is of that key, e.g. True or False
            pygame.draw.line(
                screen, pygame.Color("#0A5E59"), (x, y), (x + tile, y),
                thickness
            )  #thickness is 4  #used to update the screen every time something new happens
        if self.walls_direction['right']:#the code here checks if the key 'right' exists in the dictionary, as well as what the value is of that key, e.g. True or False
            pygame.draw.line(screen, pygame.Color("#0A5E59"), (x + tile, y),
                             (x + tile, y + tile), thickness)

        if self.walls_direction['bottom']: #the code here checks if the key 'bottom' exists in the dictionary, as well as what the value is of that key, e.g. True or False
            pygame.draw.line(screen, pygame.Color("#0A5E59"),
                             (x + tile, y + tile), (x, y + tile), thickness)

        if self.walls_direction['left']: ##the code here checks if the key 'left' exists in the dictionary, as well as what the value is of that key, e.g. True or False
            pygame.draw.line(screen, pygame.Color("#0A5E59"), (x, y + tile), (x, y), thickness)

    def check_cell(self, x, y, cols, rows, grid_cells):
        find_index = lambda x, y: x + y * cols
        #The lambda function does a calculation with two unknown variables, x and y
        if x < 0 or x > cols - 1 or y < 0 or y > rows - 1: #if the x and y coordinates are out of range then false is returned since the cell does not exist 
            return False
        return grid_cells[find_index(x, y)] #returns whether the cell looked at exists or not 
        #check_cell finds the index of the cell looked at in grid_cells and if the x and y coordinates are smaller than 0 or larger than the maximum number of rows and columns then the cell does not exist in the grid_cells array. 
    def check_neighbours(
        self, cols, rows, grid_cells
    ):  #checks the neighbours of cells to see if they're visited or not
        neighbours = []  #creates an array
        top = self.check_cell(self.x, self.y - 1, cols, rows, grid_cells)
        right = self.check_cell(self.x + 1, self.y, cols, rows, grid_cells)
        bottom = self.check_cell(self.x, self.y + 1, cols, rows, grid_cells)
        left = self.check_cell(self.x - 1, self.y, cols, rows, grid_cells)

        if top and not top.visited:
            neighbours.append(top)
        if right and not right.visited:
            neighbours.append(right)
        if bottom and not bottom.visited:
            neighbours.append(bottom)
        if left and not left.visited:
            neighbours.append(left)
        #If direction exists(True) and has not been visited(False) then the cell is appended to neighbours.
        return choice(neighbours) if neighbours else False

