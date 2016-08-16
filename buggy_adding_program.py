#! python3
#projectile_simulation.py - Gets the maximum height and travel distance of a projectile depending on the initial velocity and angle.
import math
import matplotlib.pyplot as plt
from numpy import *
def projectile_propreties(v_0,t,g = 9.8):
  t =math.radians(t)
  v_x = (math.cos(t)*v_0)
  v_y = (math.sin(t)*v_0)
  
  x_max = ((2*v_y)/(v_x *(g/v_x**2)))      #travel distance
  b = v_y/g
  y_max = -0.5*g*(b**2)+v_y*b   #max height
  
  t_flight=x_max/v_x
  x_coor=linspace(0,x_max)
  c = x_coor/v_x
  y_coor = (-0.5*g)*c**2+v_y*c
  plt.plot(x_coor,y_coor)
  return x_max,y_max,t_flight
  
x,y,t = projectile_propreties(12, 45)
t= round(t, 2)
x= round(x, 2)
y= round(y,2)
print('The projectile will travel %s meters' %(x))
print('The projectile will reach a height of %s meters' %(y))
print('The projectile will spend %s seconds in the air' %(t))


