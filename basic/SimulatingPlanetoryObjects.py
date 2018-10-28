import math
from turtle import *

#The gravitational constant
#G=6.67428e -11

#Assumed scale : 100 pixels = 1AU
AU=(149.6e6 * 1000) #149.6 million km, in meters.
SCALE=250/AU

class Body(Turtle):
    """Subclass of Turtle representing a gravitationally-acting body.
    Extra attributes:
    mass : mass in kg
    vx, vy: x, y velocities in m/s
    px, py: x, y positions in m
    """
    name= 'Body'
    mass=None
    vx = vy=0.0
    px=py=0.0

    def attraction(self,other):
        if self is other:
            raise ValueError("Attraction of object %r to itself requested" %self.name)
        sx,sy=self.px,self.py
        ox,oy=other.px,other.py
        dx=(ox-sx)
        dy=(oy-sy)
        d=math.sqrt(dx**2+dy**2)
        if d == 0:
            raise ValueError("Collision between objects %r and %r" % (self.name, other.name))

      #  f=g.self.mass * other.mass/(d**2)
