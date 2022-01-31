#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Point group C2v

Symmetry elements and operations, done with vpython and numpy

requires Matrices.py 

Informations
------------
Author : Martin Vérot  from the ENS de Lyon, France
Licence : Creative Commons CC-BY-NC-SA 4.0 

"""
import Matrices
import numpy as np
import time

from vpython import *

#GlowScript 3.2 VPython
scene.width = scene.height = 600
scene.background = color.white
scene.range = 10
scene.forward = vector(0,1,0)
scene.up=vector(0,0,1)
scene.title = 'Molécule d\'eau - groupe C2v'
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

def showsigmay():
    Matrices.TogglePlane(sigmay)

def showsigmax():
    Matrices.TogglePlane(sigmax)

def showC2():
    C2.visible=not(C2.visible) 

def ResetPos():
    global coords 
    for u in range(coords.shape[1]):
        atoms[u].pos = vector(*initialcoords[:,u])
    coords = np.copy(initialcoords)



def applyE():
    pass

def applyC2():
    global coords 
    rate(5)
    for i in range(250):
        time.sleep(0.01)
        newcoords = np.matmul(Matrices.RotationZ(i*np.pi/249),coords)
        for u in range(coords.shape[1]):
             atoms[u].pos = vector(*newcoords[:,u])
    coords = newcoords

def applysigmay():
    global coords 
    rate(5)
    for i in range(250):
        time.sleep(0.01)
        newcoords = np.matmul(Matrices.InvY(i/249),coords)
        for u in range(coords.shape[1]):
             atoms[u].pos = vector(*newcoords[:,u])
    coords = newcoords
    
def applysigmax():
    global coords 
    rate(5)
    for i in np.linspace(-1,1,250):
        time.sleep(0.01)
        newcoords = np.matmul(Matrices.InvX(i),coords)
        for u in range(coords.shape[1]):
             atoms[u].pos = vector(*newcoords[:,u])
    coords = newcoords



scene.append_to_caption('\n<h2>Éléments de symétrie</h2>')
button(text='C2', bind=showC2)
button(text='sigmay', bind=showsigmay)
button(text='sigmax', bind=showsigmax)
scene.append_to_caption('<h2>Opérations</h2>')

button(text='Reset', bind=ResetPos)
button(text='E', bind=applyE)
button(text='C2', bind=applyC2)
button(text='sigmay', bind=applysigmay)
button(text='sigmax', bind=applysigmax)

scene.append_to_caption('<h3>Contrôle</h3>')
button(text='Pause', bind=Runbutton)
scene.append_to_caption("""\n
To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate.""")


E =  Matrices.Identity()
theta = 2*np.pi/2
C2 = Matrices.RotationZ(theta)
invy = Matrices.InvY()
invx = Matrices.InvX()

O = np.matrix([[0],[0],[0]])
H1 = np.matrix([[1],[0],[-1]])
H2 = np.matmul(C2,H1)
initialcoords = np.concatenate((O,H1,H2),axis=1)
coords = np.copy(initialcoords)
print(coords)


colors = Matrices.AtomColors()
colors2 = Matrices.OperatorColors()

radii = [1,0.75,0.75]
atoms=[]
for u in range(coords.shape[1]):
    atoms.append(sphere(pos=vector(*coords[:,u]),color=colors[u],radius=radii[u]))

C2 = curve(vector(0,0,-5), vector(0,0,7),color=colors2[0],radius=0.1)

p = [vector(-5,0,-5),vector(-5,0,5),vector(5,0,5),vector(5,0,-5),vector(-4,0,4),vector(1,0,0),vector(0,0,1)]
sigmay = Matrices.PlotRotatedPlane(p,0,vector(0,0,1),'σv1',colors2[2])
sigmax = Matrices.PlotRotatedPlane(p,np.pi/2,vector(0,0,1),'σv1',colors2[3])
      

while True:
    rate(5)
    if run: # Currently there isn't a way to rotate a points object, so rotate scene.forward:
        scene.forward = scene.forward.rotate(angle=-np.pi/100, axis=vec(0,0,1))
