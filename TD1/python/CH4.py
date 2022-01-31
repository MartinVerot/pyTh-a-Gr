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

def showC2():
    for i,el in enumerate(C2s):
        el.visible=not(el.visible)

def showsigma():
    for i,el in enumerate(sigmas):
        for j,vert in enumerate(el[0]):
            vert.opacity=0.5-vert.opacity
        el[2].opacity=0
        el[2].visible=False


def showC3():
    for i,el in enumerate(C3s):
        el.visible=not(el.visible)


def rotateCoord(p,angle,axe):
    vecs=[]
    for i,point in enumerate(p):
        vecs.append(point.rotate(angle=angle,axis=axe) )
    return vecs

def PlotRotatedPlane(p,angle,axe,t,col):
    verticis=[]
    vecs = rotateCoord(p,angle,axe)
    for i,point in enumerate(vecs):
        verticis.append(vertex(pos=vecs[i],color=col,opacity=0.5))
    plan =  quad(vs= [verticis[0],verticis[1],verticis[2],verticis[3]] ,opacity=0.5 )
    #texte = text(text=t,align='center', color=color.black,opacity=0.5,pos=vecs[4],axis=vecs[5],up=vecs[6])
    return verticis,plan,text,vecs


button(text='Pause', bind=Runbutton)
button(text='Stop', bind=killbutton)
button(text='C2', bind=showC2)
button(text='sigma', bind=showsigma)
button(text='C3', bind=showC3)
scene.append_to_caption("""
To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate.""")


C = sphere(pos=vector(0,0,0),color=color.gray(0.15) )
H1=sphere(pos=vector(1,-1,1),radius=0.75)
H2=sphere(pos=vector(-1,1,1),radius=0.75)
H3=sphere(pos=vector(-1,-1,-1),radius=0.75)
H4=sphere(pos=vector(1,1,-1),radius=0.75)

#3 C2
C2s= []
axis=[vector(0,0,-5),vector(0,0,7),vector(1,0,0),vector(0,0,1)]
C2s.append(curve(axis[0],axis[1] ,color=color.green,radius=0.1))
#Tc = text(text='C2',align='center', color=color.black,pos=axis[1],axis=axis[2],up=axis[3])

newaxis=[]
for i,point in enumerate(axis):
    newaxis.append(point.rotate(angle=np.pi/2,axis=vector(0,1,0)) )
C2s.append(curve(newaxis[0],newaxis[1] ,color=color.green,radius=0.1))
#Tc = text(text='C2',align='center', color=color.black,pos=newaxis[1],newaxis=newaxis[2],up=newaxis[3])


newaxis=[]
for i,point in enumerate(axis):
    newaxis.append(point.rotate(angle=np.pi/2,axis=vector(1,0,0)) )
C2s.append(curve(newaxis[0],newaxis[1] ,color=color.green,radius=0.1))
#Tc = text(text='C2',align='center', color=color.black,pos=newaxis[1],newaxis=newaxis[2],up=newaxis[3])

#3 C3
C3s= []
axis=[vector(5,-5,5),vector(-5,5,-5),vector(-5,5,-5),vector(5,-5,5)]
C3s.append(curve(axis[0],axis[1] ,color=color.blue,radius=0.1))
#Tc = text(text='C3',align='center', color=color.black,pos=axis[1],axis=axis[2],up=axis[3])

axis=[vector(-5,5,5),vector(5,-5,-5),vector(5,-5,-5),vector(-5,5,5)]
C3s.append(curve(axis[0],axis[1] ,color=color.blue,radius=0.1))
#Tc = text(text='C3',align='center', color=color.black,pos=axis[1],axis=axis[2],up=axis[3])

axis=[vector(-5,-5,-5),vector(5,5,5),vector(5,5,5),vector(-5,-5,-5)]
C3s.append(curve(axis[0],axis[1] ,color=color.blue,radius=0.1))
#Tc = text(text='C3',align='center', color=color.black,pos=axis[1],axis=axis[2],up=axis[3])

axis=[vector(5,5,-5),vector(-5,-5,5),vector(-5,-5,5),vector(5,5,-5)]
C3s.append(curve(axis[0],axis[1] ,color=color.blue,radius=0.1))
#Tc = text(text='C3',align='center', color=color.black,pos=axis[1],axis=axis[2],up=axis[3])









#Sigmas
sigmas=[]
vert = []
Ts = []

p = [vector(-5,0,-5),vector(-5,0,5),vector(5,0,5),vector(5,0,-5),vector(-4,0,4),vector(1,0,0),vector(0,0,1)]
sigmas.append( PlotRotatedPlane(p,np.pi/4,vector(0,0,1),'σv1',color.purple))
sigmas.append( PlotRotatedPlane(p,-np.pi/4,vector(0,0,1),'σv2',color.purple))
sigmas.append( PlotRotatedPlane(p,-np.pi/4,vector(1,0,0),'σv3',color.green))
sigmas.append( PlotRotatedPlane(p,np.pi/4,vector(1,0,0),'σv4',color.green))
p2 = rotateCoord(p,np.pi/2,vector(0,0,1))
sigmas.append( PlotRotatedPlane(p2,np.pi/4,vector(0,1,0),'σv5',color.red))
sigmas.append( PlotRotatedPlane(p2,-np.pi/4,vector(0,1,0),'σv6',color.red))




while True:
    rate(5)
    if run: # Currently there isn't a way to rotate a points object, so rotate scene.forward:
        scene.forward = scene.forward.rotate(angle=-np.pi/50, axis=vec(0,0,1))
