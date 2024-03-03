'''
@author: Esther Asuquo(eoa4)
@author: Noro Dung (ned24)
@Date: Spring, 2022
'''

from meteor_helpers import distance


class Meteor:
    """ This models a meteor that is drawn to a canvas. """

    def __init__(self, x=50, y=50, vel_x=1, vel_y=5, radius=20, color="grey"):
        """Instantiate a particle object."""
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.radius = radius
        self.color = color

    def draw (self, drawing):
        #This draws the meteor and the stars
        
        drawing.oval (self.x - self.radius,
             self.y - self.radius,
             self.x + self.radius,
             self.y + self.radius,
             color=self.color
             )
      
    def move (self,drawing):
        #This code was gotten form simulation particle (lab 11)
        self.x = self.x + self.vel_x
        self.y = self.y + self.vel_y
       
        if self.x < 0 and self.vel_x < 0:
            self.vel_x = self.vel_x * -1
        if self.y < 0 and self.vel_y < 0:
            self.vel_y = self.vel_y *-1
            
        if self.x < 0 and self.vel_x < 0:
            self.vel_x = 500
        if self.y < 0 and self.vel_y < 0:
            self.vel_y = 250
                  
     
if __name__ == '__main__':
    m = Meteor()
    assert m.x == 50
    assert m.y == 50
    assert m.radius == 20
    assert m.color == 'grey'



   