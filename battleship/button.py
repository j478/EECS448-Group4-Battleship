import pygame

class button():
    # initializes any variables needed for button
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    # Creates the button on screen
    def draw(self, win):
        #draws button
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        #draws text
        if self.text !- '':
            font = pygame.font.SysFont('Arial',60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 -text.get_height()/2)))

    # returns a boolean of if the mouse is over the button
    def hover():
        if pos[0] > self.x and pos[0] <self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False