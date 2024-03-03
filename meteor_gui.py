'''
@author: Esther Asuquo(eoa4)
@author: Noro Dung (ned24)
@Date: Spring, 2022

'''

from guizero import App, Drawing, PushButton, Box, Picture
from random import randint
from meteor_particle import Meteor
from Gun_class import Gun, Bullet
from meteor_helpers import distance


class MeteorAnimation:
    """Runs a meteor game on the GUI app."""

    def __init__(self, app):
        """Instantiate the meteor on the GUI app."""
        
        app.title = 'Meteor Blast'
        UNIT = 500
        CONTROL_UNIT = 50
        app.width = UNIT
        app.height = UNIT + CONTROL_UNIT
        self.app = app
        self.score = 0
        self.drop_count = 0
        

        # widgets for the game.
        #box = Box(app, layout='grid', width=UNIT, height=UNIT + CONTROL_UNIT)
        self.drawing = Drawing(app, width=UNIT, height=UNIT + CONTROL_UNIT)
        self.drawing.bg = 'black'
        
        quit_button = PushButton(app, text = 'Quit', align= "bottom", command = app.destroy)
        self.restart = PushButton(app, text="Restart", align = 'bottom', command = self.restart_game)
        self.restart.visible = True
        self.picture = Picture(app, image="YouLose.jpeg", width = 450, height = 550, enabled= 'drawing', align = 'top')
        self.picture.visible = False

    
        self.meteors = [Meteor()]
       
        
        self.gun = Gun()
        app.when_key_pressed = self.process_key
        
        
        self.bullet = Bullet()
        
        app.repeat(50, self.draw_frame)
        

    def draw_frame(self):
        '''Draws the frame and moves the meteor'''
        
        self.drawing.clear()
        
        #Draw the line at the bottom of the screen and the stars. 
        self.drawing.line(0, 450, 500, 450, color = 'red')
        
        
        
        #Inserts the text at the specified x and y location
        self.drawing.text (10, 10, text = 'Score: ' + str(self.score), color = 'red')
        self.drawing.text (10,30, text ='Miss: ' + str(self.drop_count), color = 'red')
        
        # Updates the meteor
        if randint(0, 50) == 1:
            self.meteors.append(Meteor(x = randint(0,450)))
            
       
        # update gun and bullets
        self.gun.draw(self.drawing)
        self.bullet.draw (self.drawing)
        self.bullet.move()
        
        # update meteors
        for meteor in self.meteors:
            meteor.move(self.drawing)
            meteor.draw(self.drawing)
            if meteor.y >= 450:
                self.meteors.remove(meteor)
                self.drop_count += 1                    
        
        # check for collision between all meteors and bullet here and updates the score
        for meteor in self.meteors:
            if meteor.x < self.bullet.x< meteor.x+ 20 and meteor.y <self.bullet.y <meteor.y + 20 or meteor.x == self.bullet.x :
                self.meteors.remove(meteor)
                self.score += 1
                
         #keeps track of meteors that fall shows if you loose 
        if self.drop_count == 5:
            self.drawing.hide()
            self.restart.visible = True
            self.picture.visible = True
            

    def process_key(self, event):
        #Event keys for the game
         if event.key == 'a':
           self.gun.move(-8) 
         elif event.key == 's':
            self.gun.move(+8)
         elif event.key == ' ':
            self.bullet.x = self.gun.x
            self.bullet.y = 450
        
    def restart_game(self):
        #To restart the game
        self.picture.visible = False
        self.restart.visible = False
        self.drawing.show()
        self.score = 0
        self.drop_count = 0
        
        

if __name__ == '__main__':
    app = App(title='Meteor Blast')
    meteor_cpp = MeteorAnimation(app)
    app.display()
    