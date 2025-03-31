import pygame

class Game:
    def __init__(self,goal_cell,tile):
        self.tile = tile
        self.goal_cell = goal_cell

    def goal(self,screen):
        image = pygame.image.load("Images\Goal.png").convert()
        image = pygame.transform.scale(image,(self.tile,self.tile))#makes the image fit to the scale of the maze
        screen.blit(image,(self.goal_cell.x*self.tile,self.goal_cell.y*self.tile))#outputss the goal cell

    def isgame_over(self,player):
        goal_cell_abs_x = self.goal_cell.x*self.tile
        goal_cell_abs_y = self.goal_cell.y*self.tile
        if player.x >= goal_cell_abs_x and player.y >= goal_cell_abs_y:
            return True
        else:
            return False
