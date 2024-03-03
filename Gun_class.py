'''
@author: Esther Asuquo(eoa4)
@author: Noro Dung (ned24)
@Date: Spring, 2022

'''
from meteor_helpers import distance

class Gun:
   def __init__(self, x=230, y=450, velocity=5, body_color='blue'):
        #Create a gun object with the given location and color
        self.x = x
        self.y = y
        self.velocity = velocity
        self.vertical_velocity = 0        
        self.body_color = body_color
    
   def move(self, delta_x):
        #Move the gun based on the horizontal velocity.
        
        if self.x < 500:
            self.x += delta_x
            
   def draw(self, drawing):
       # Draws the gun
       drawing.rectangle(self.x , self.y, self.x+ 10, self.y + 50, color=self.body_color)
    
#This next section of the code was inspired by the flying car sample code
class Bullet:
    #Create a Bullet
    def __init__(self, x= 0, y=450, velocity = 5):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.delta = velocity
        
    def draw (self, drawing):
        #draws the bullet
        drawing.oval(self.x - 10, self.y, self.x + 5, self.y + 10, color = 'green')
        
    def move(self):
        # move the bullet based on the horizontal velocity
        self.y -= self.delta
        
if __name__ == '__main__':
    g = Gun()
    b = Bullet()
    assert g.x == 230 and b.x == 0
    assert g.y == 450 and b.y == 450
    assert g.velocity == 5
    

 