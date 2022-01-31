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


ori = vector(0,0,0)
N = sphere(pos=vector(0,0,0),color=color.blue)
posH1 = vector(1,0,-1)
H1 = sphere(pos = posH1,radius=0.75)

posH2 = posH1.rotate(angle=2*np.pi/3,axis=vector(0,0,1))
H2 = sphere(pos=posH2,radius=0.75)

posH3 = posH1.rotate(angle=-2*np.pi/3,axis=vector(0,0,1))
H3 = sphere(pos = posH3,radius=0.75)



C3 = curve(vector(0,0,-5), vector(0,0,7),color=color.green,radius=0.1)
Tc = text(text='C3',align='center', color=color.black,pos=vector(0,0,7),axis=vector(1,0,0),up=vector(0,0,1))
#sigmaV =quad( vs=[vector(-5,0,-5), vector(-5,0,5), vector(5,0,-5),vector(5,0,5)])     


p = [vector(-5,0,-5),vector(-5,0,5),vector(5,0,5),vector(5,0,-5),vector(-4,0,4),vector(1,0,0),vector(0,0,1)]

verticis=[]
vecs=[]
for i,point in enumerate(p):
    vecs.append(point)
    verticis.append(vertex(pos=vecs[i],color=color.purple,opacity=0.5))
SigmaV = quad(vs= [verticis[0],verticis[1],verticis[2],verticis[3]] ,opacity=0.5 )
Tv1 = text(text='σv1',align='center', color=color.black,pos=vecs[4],axis=vecs[5],up=vecs[6])

verticis=[]
vecs=[]
for i,point in enumerate(p):
    vecs.append(point.rotate(angle=2*np.pi/3,axis=vector(0,0,1)) )
    verticis.append(vertex(pos=vecs[i],color=color.red,opacity=0.5))
SigmaV = quad(vs= [verticis[0],verticis[1],verticis[2],verticis[3]] ,opacity=0.5 )
Tv1 = text(text='σv2',align='center', color=color.black,pos=vecs[4],axis=vecs[5],up=vecs[6])

verticis=[]
vecs=[]
for i,point in enumerate(p):
    vecs.append(point.rotate(angle=-2*np.pi/3,axis=vector(0,0,1)) )
    verticis.append(vertex(pos=vecs[i],color=color.blue,opacity=0.5))
SigmaV = quad(vs= [verticis[0],verticis[1],verticis[2],verticis[3]] ,opacity=0.5 )
Tv1 = text(text='σv3',align='center', color=color.black,pos=vecs[4],axis=vecs[5],up=vecs[6])


 

while True:
    rate(5)
    if run: # Currently there isn't a way to rotate a points object, so rotate scene.forward:
        scene.forward = scene.forward.rotate(angle=-np.pi/50, axis=vec(0,0,1))
