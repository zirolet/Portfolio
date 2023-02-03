import pygame as pg # cope
from random import choice, randrange # cope



class Particle(pg.sprite.Sprite): # cope

    def __init__(self,pos): # cope
        pg.sprite.Sprite.__init__(self) # cope

        self.radius = 25 # cope
        self.pos = pos # cope
        
        self.size = [25,25] # cope
        self.color = choice(['orange','red']) # cope


        self.image = pg.Surface((self.size[0],self.size[1])) # cope
        self.rect = self.image.get_rect(center = self.pos) # cope
        
        
        self.image.fill(self.color)
        self.killspeed = randrange(20,40,1) # cope
        self.killspeed = self.killspeed/10
        self.vel = [0,0]
        
        
        #self.vel = [choice([1,-1,0,0.5,-0.5,2,-2,1.5,-1.5,2.5,-2.5,3,-3,3.5,-3.5,4,-4,0.25,-0.25,0.75,-0.75,1.25,-1.25,1.75,-1.75,2.25,-2.25,2.75,-2.75,3.25,-3.25,3.75,-3.75,4.0, 4.25, 4.5, 4.75, 5.0, 5.25, 5.5, 5.75, 6.0, 6.25, 6.5, 6.75, 7.0, 7.25, 7.5, 7.75, 8.0, 8.25, 8.5, 8.75, 9.0, 9.25, 9.5, 9.75, 10.0, 10.25, 10.5, 10.75, 11.0, 11.25, 11.5, 11.75, 12.0, 12.25, 12.5, 12.75, 13.0, 13.25, 13.5, 13.75, 14.0, 14.25, 14.5, 14.75, 15.0,-4.0, -4.25, -4.5, -4.75, -5.0, -5.25, -5.5, -5.75, -6.0, -6.25, -6.5, -6.75, -7.0, -7.25, -7.5, -7.75, -8.0, -8.25, -8.5, -8.75, -9.0, -9.25, -9.5, -9.75, -10.0, -10.25, -10.5, -10.75, -11.0, -11.25, -11.5, -11.75, -12.0, -12.25, -12.5, -12.75, -13.0, -13.25, -13.5, -13.75, -14.0, -14.25, -14.5, -14.75, -15.0]),choice([0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75, 5.0, 5.25, 5.5, 5.75, 6.0, 6.25, 6.5, 6.75, 7.0, 7.25, 7.5, 7.75, 8.0, 8.25, 8.5, 8.75, 9.0, 9.25, 9.5, 9.75, 10.0, 10.25, 10.5, 10.75, 11.0, 11.25, 11.5, 11.75, 12.0, 12.25, 12.5, 12.75, 13.0, 13.25, 13.5, 13.75, 14.0, 14.25, 14.5, 14.75, 15.0,-0.25, -0.5, -0.75, -1.0, -1.25, -1.5, -1.75, -2.0, -2.25, -2.5, -2.75, -3.0, -3.25, -3.5, -3.75, -4.0, -4.25, -4.5, -4.75, -5.0, -5.25, -5.5, -5.75, -6.0, -6.25, -6.5, -6.75, -7.0, -7.25, -7.5, -7.75, -8.0, -8.25, -8.5, -8.75, -9.0, -9.25, -9.5, -9.75, -10.0, -10.25, -10.5, -10.75, -11.0, -11.25, -11.5, -11.75, -12.0, -12.25, -12.5, -12.75, -13.0, -13.25, -13.5, -13.75, -14.0, -14.25, -14.5, -14.75, -15.0])]
        self.vel[0] = randrange(-1500,1500,1)
        self.vel[1] = randrange(-3000,1500,1)
        self.vel[0] = self.vel[0]/100
        self.vel[1] = self.vel[1]/100

         #jeff bezos is overrated for many reasons | cope

    def update(self):
        

        self.size[1] -= self.killspeed # cope
        self.size[0] -= self.killspeed # cope

        
        self.image = pg.Surface((self.size[0],self.size[1])) # cope
        
        self.image.fill(self.color) # cope

        

        if self.size[0] <= 3: # cope
          self.kill() # cope

        self.vel[1] += 5


        self.rect.move_ip(self.vel) # cope