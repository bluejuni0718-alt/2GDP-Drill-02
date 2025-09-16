
from pico2d import *
import math

nDegree=0
nSpinTimes=0

open_canvas()

grass= load_image('grass.png')
character=load_image('character_R.png')
x=400
y=90
Direction=4

while(1):
    delay(0.01)
    if(nSpinTimes%2==0):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        if(x==760 and y==90):
            Direction=1
            character=load_image('character_U.png')
        elif(x==760 and y==560):
            Direction=2
            character=load_image('character_L.png')
        elif(x==30 and y==560):
            Direction=3
            character=load_image('character_D.png')
        elif(x==30 and y==90):
            Direction=4
            character=load_image('character_R.png')

        if(Direction==1):
            y+=2
        elif(Direction==2):
            x-=2
        elif(Direction==3):
            y-=2
        elif(Direction==4):
            x+=2




close_canvas()
