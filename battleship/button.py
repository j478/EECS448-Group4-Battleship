import pygame
pygame.init()


class Button():
#@pre - none
#
#@param - color of button, position, deminsions and text
#         
#@post - defines the passed in variables
#
#@return - none
# 
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

#@pre - the button needs to be defined  
#
#@param - window to draw on
#         
#@post - draws the button
#
#@return - none
#
    def draw(self, win):
        #draws button
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        #draws text
        if self.text != '':
            font = pygame.font.SysFont('Arial',60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 -text.get_height()/2)))

#@pre - button needs to be defined
#
#@param - position of mouse
#         
#@post - checks if mouse is over button
#
#@return - boolean of whether over position
#
    def hover(self, pos):
        if pos[0] > self.x and pos[0] <self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False