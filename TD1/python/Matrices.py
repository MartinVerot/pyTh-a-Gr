#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from vpython import *

def Identity():
    return np.matrix([[1,0,0],
                      [0,1,0],
                      [0,0,1]])

def RotationZ(theta):
    return np.matrix([[np.cos(theta),-np.sin(theta),0],
                    [np.sin(theta),np.cos(theta),0],
                    [0,0,1]])

def RotationY(theta):
    return np.matrix([[np.cos(theta),0,-np.sin(theta)],
                    [0,1,0],
                    [np.sin(theta),0,np.cos(theta)]])

def RotationX(theta):
    return np.matrix([[1,0,0],
                    [0,np.cos(theta),-np.sin(theta)],
                    [0,np.sin(theta),np.cos(theta)],
                    ])
def InvY(a=1):
    return np.matrix([[1,0,0],
                      [0,-a,0],
                      [0,0,1]])


def InvX(a=1):
    return np.matrix([[-a,0,0],
                      [0,1,0],
                      [0,0,1]])
def InvZ(a=1):
    return np.matrix([[1,0,0],
                      [0,1,0],
                      [0,0,-a]])
def centreInv(a=1):
    return np.matrix([[-a,0,0],
                      [0,-a,0],
                      [0,0,-a]])


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
    return verticis,plan,text,vecs

def TogglePlane(sigma):
    for j,vert in enumerate(sigma[0]):
        vert.opacity=0.5-vert.opacity

def AtomColors():
    return [vector(0.65098039,0.80784314,0.89019608),vector(0.12156863,0.47058824,0.70588235),vector(0.69803922,0.8745098,0.54117647),vector(0.2,0.62745098,0.17254902),vector(0.98431373,0.60392157,0.6,),vector(0.89019608,0.10196078,0.10980392),vector(0.99215686,0.74901961,0.43529412),vector(1.,0.49803922,0.,),vector(0.79215686,0.69803922,0.83921569),vector(0.41568627,0.23921569,0.60392157),vector(1.,1.,0.6,),vector(0.69411765,0.34901961,0.15686275)]

def OperatorColors():
    return [vector(0.55294118,0.82745098,0.78039216),vector(1.,1.,0.70196078),vector(0.74509804,0.72941176,0.85490196),vector(0.98431373,0.50196078,0.44705882),vector(0.50196078,0.69411765,0.82745098),vector(0.99215686,0.70588235,0.38431373),vector(0.70196078,0.87058824,0.41176471),vector(0.98823529,0.80392157,0.89803922),vector(0.85098039,0.85098039,0.85098039),vector(0.7372549,0.50196078,0.74117647),vector(0.8,0.92156863,0.77254902),vector(1.,0.92941176,0.43529412)]

if __name__ == '__main__':
    pass
