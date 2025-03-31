import pygame, time #library to create a timer and use time functions

pygame.font.init() #function to use and display text in pygame

class Timer:
    def __init__(self):
        self.startTime=None #originally set to None because timer hasn't started yet
        self.elapsedTime =0 #stores amount of time passed since the timer started
        self.font = pygame.font.SysFont("Agency FB",30)
        self.timer_colour = pygame.Color("#0A5E59")

    #starting the timer and sets startTime to current time
    def startTimer(self):
        self.startTime = time.time() #function called from time library to start timer

    #Update the timer
    def updateTimer(self):
        if self.startTime is not None:
            self.elapsedTime = time.time() - self.startTime #subtracts start time from current time
    
    #displaying timer on screen with minutes and seconds
    def displayTimer(self):
        seconds = int(self.elapsedTime %60)
        minutes = int(self.elapsedTime / 60)
        myTime = self.font.render(f"{minutes:02}:{seconds:02}",True,self.timer_colour)
        return myTime

    #Stop timer
    def stopTimer(self):
        self.startTime = None
