#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np

from vpython import *

#GlowScript 3.2 VPython
scene.width = scene.height = 600
scene.background = color.white
scene.range = 10
scene.forward = vector(0,1,0)
scene.up=vector(0,0,1)
# Display frames per second and render time:
scene.append_to_title("<div id='fps'/>")

from vpython.no_notebook import stop_server
run = True
#run = False
def Runbutton(b):
    global run
    if b.text == 'Pause':
        run = False
        b.text = 'Run'
    else:
        run = True
        b.text = 'Pause'

def killbutton(b):
    stop_server()


button(text='Pause', bind=Runbutton)
button(text='Stop', bind=killbutton)
scene.append_to_caption("""
To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate.""")


C = sphere(pos=vector(0,0,0),color=color.gray(0.1) )
H1=sphere(pos=vector(-1,0,-1),radius=0.75)
H2=sphere(pos=vector(1,0,-1),radius=0.75)
Cl1=sphere(pos=vector(0,-1,1),radius=0.75,color=color.green)
Cl2=sphere(pos=vector(0,1,1),radius=0.75,color=color.green)


C2 = curve(vector(0,0,-5), vector(0,0,7),color=color.green,radius=0.1)
Tc = text(text='C2',align='center', color=color.black,pos=vector(0,0,7),axis=vector(1,0,0),up=vector(0,0,1))
#sigmaV =quad( vs=[vector(-5,0,-5), vector(-5,0,5), vector(5,0,-5),vector(5,0,5)])     

a = vertex( pos=vector(-5,0,-5) ,color=color.purple,opacity=0.5)
b = vertex( pos=vector(-5,0,5) ,color=color.purple,opacity=0.5)
d = vertex( pos=vector(5,0,-5) ,color=color.purple,opacity=0.5)
c = vertex( pos=vector(5,0,5) ,color=color.purple,opacity=0.5)
SigmaV = quad(vs= [a,b,c,d] ,opacity=0.5 )

Tv = text(text='σv',align='center', color=color.black,pos=vector(-4,0,4),axis=vector(1,0,0),up=vector(0,0,1))


a1 = vertex( pos=vector(0,-5,-5) ,color=color.blue,opacity=0.5)
b1 = vertex( pos=vector(0,-5,5) ,color=color.blue,opacity=0.5)
d1 = vertex( pos=vector(0,5,-5) ,color=color.blue,opacity=0.5)
c1 = vertex( pos=vector(0,5,5) ,color=color.blue,opacity=0.5)
SigmaD = quad(vs= [a1,b1,c1,d1],opacity=0.5 )
 
Td = text(text='σd',align='center', color=color.black,pos=vector(0,-4,4),axis=vector(0,1,0),up=vector(0,0,1))

while True:
    rate(5)
    if run: # Currently there isn't a way to rotate a points object, so rotate scene.forward:
        scene.forward = scene.forward.rotate(angle=-np.pi/50, axis=vec(0,0,1))
