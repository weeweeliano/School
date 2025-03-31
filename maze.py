import pygame
from cell import Cell

pygame.init()


class Maze:

    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.thickness = 4
        self.grid_cells = [Cell(col, row, self.thickness) for row in range(self.rows) for col in range(self.cols)]

    def get_grid(self):
        grid_cells = self.grid_cells
        print(grid_cells)

    def wall_remove(self, current, next):  #carving the cell walls
        diff_x = current.x - next.x  #next.x is a function which will look at cell next to current one either to left or right

        if diff_x == 1:  #will happen if next cell to the left of current cell
            current.walls_direction['left'] = False  #the left wall of the current cell is removed so that there is a path between the two cells
            next.walls_direction['right'] = False  #right wall of next wall is removed
        elif diff_x == -1:  #happens if next cell is to the right of current cell
            current.walls_direction['right'] = False
            next.walls_direction['left'] = False
        diff_y = current.y - next.y
        if diff_y == 1:
            current.walls_direction['top'] = False
            next.walls_direction['bottom'] = False
        elif diff_y == -1:
            current.walls_direction['bottom'] = False
            next.walls_direction['top'] = False

    def generate_maze(self):  #generating the maze
        current_cell = self.grid_cells[0]  #makes current_cell the item at self.grid_cells[0]
        array = []
        maximum = 1
        while maximum != len(self.grid_cells):  #while end is not equal to the number of cells in self.grid_cells
            current_cell.visited = True  #because the current cell is currently being visited it is set to true
            next_cell = current_cell.check_neighbours(self.cols, self.rows,
                                                      self.grid_cells)
            if next_cell:
                next_cell.visited = True
                maximum = maximum + 1
                array.append(current_cell)
                self.wall_remove(current_cell, next_cell)
                current_cell = next_cell
            elif array:
                current_cell = array.pop()

        return self.grid_cells
