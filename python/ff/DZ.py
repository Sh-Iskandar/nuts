# -*- coding: utf-8 -*-
import random

import simple_draw as sd
sd.resolution=(1200,600)
sd.random_color()
point=sd.get_point(300,300)
radius=50
def bublle(point,step):
 radius = 50

 for _ in range(3):
  color = sd.random_color()
  sd.circle(center_position=point,radius=radius,color=color)
  radius+=step

for _ in range(100):
 step = random.randint(2, 10)
 point=sd.random_point()
 bublle(point,step)

#for x in range(100,1100,100):
 #for y in range(100,600,200):
  #point = sd.get_point(x, y)
  #bublle(point,step)











sd.pause()