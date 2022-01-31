#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


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
def InvY():
    return np.matrix([[1,0,0],
                      [0,-1,0],
                      [0,0,1]])


def InvX():
    return np.matrix([[-1,0,0],
                      [0,1,0],
                      [0,0,1]])
def InvZ():
    return np.matrix([[1,0,0],
                      [0,1,0],
                      [0,0,-1]])
def centreInv():
    return np.matrix([[-1,0,0],
                      [0,-1,0],
                      [0,0,-1]])

if __name__ == '__main__':
    pass
