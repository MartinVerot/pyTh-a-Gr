#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import Matrices


np.set_printoptions(precision=3,floatmode='fixed',suppress=True)
if __name__ == '__main__':
    operations = [] 
    #E
    operations.append(Matrices.Identity())
    #C3
    theta = 2*np.pi/3
    operations.append(Matrices.RotationC3(theta,np.array([1,1,1])))
    operations.append(Matrices.RotationC3(-theta,np.array([1,1,1])))
    operations.append(Matrices.RotationC3(theta,np.array([1,-1,1])))
    operations.append(Matrices.RotationC3(-theta,np.array([1,-1,1])))
    operations.append(Matrices.RotationC3(theta,np.array([-1,1,1])))
    operations.append(Matrices.RotationC3(-theta,np.array([-1,1,1])))
    operations.append(Matrices.RotationC3(theta,np.array([-1,-1,1])))
    operations.append(Matrices.RotationC3(-theta,np.array([-1,-1,1])))

    #C2
    theta = np.pi
    operations.append(Matrices.RotationX(theta))
    operations.append(Matrices.RotationY(theta))
    operations.append(Matrices.RotationZ(theta))
    
    #sigma_h 
    invx=Matrices.InvX()
    invy=Matrices.InvY()
    invz=Matrices.InvZ()
    #C4
    theta = np.pi/2
    C4x =  Matrices.RotationX(theta)
    C4x2 =  Matrices.RotationX(-theta)
    C4y =  Matrices.RotationY(theta)
    C4y2 =  Matrices.RotationY(-theta)
    C4z =  Matrices.RotationZ(theta)
    C4z2 =  Matrices.RotationZ(-theta)
    #C8
    theta = np.pi/4
    C8x =  Matrices.RotationX(theta)
    C8x2 =  Matrices.RotationX(-theta)
    C8y =  Matrices.RotationY(theta)
    C8y2 =  Matrices.RotationY(-theta)
    C8z =  Matrices.RotationZ(theta)
    C8z2 =  Matrices.RotationZ(-theta)

    #sigma_v
    operations.append(Matrices.classe(C8z,invy))
    operations.append(Matrices.classe(C8z2,invy))
    operations.append(Matrices.classe(C8y,invx))
    operations.append(Matrices.classe(C8y2,invx))
    operations.append(Matrices.classe(C8x,invz))
    operations.append(Matrices.classe(C8x2,invz))

    #S4
    operations.append(np.matmul(invx,C4x))
    operations.append(np.matmul(invx,C4x2))
    operations.append(np.matmul(invy,C4y))
    operations.append(np.matmul(invy,C4y2))
    operations.append(np.matmul(invz,C4z))
    operations.append(np.matmul(invz,C4z2))


    operationsname = ['E','aC3','aC32','bC3','bC32','cC3','cC32','dC3','dC32','C2x','C2y','C2z','sigx1','sigx2','sigy1','sigy2','sigz1','sigz2','S6x1','S6x2','S6y1','S6y2','S6z1','S6z2']
    for i,op in enumerate(operations):
        print(operationsname[i])
        print(op)   
        for j,op2 in enumerate(operations):
            if np.allclose(op2,op) and i!=j:
                print('bug {} {}'.format(operationsname[i],operationsname[j]))

#######
##Détermination des classes d'opérateurs
#######
    
    
    for i,op1 in enumerate(operations):
        classe=[operationsname[i]]
        for j,op2 in enumerate(operations):
            #on essaye de voir si op1 et op2 sont conjuguées
            #print('{}  {}'.format(operationsname[i],operationsname[j]))
            prod1 = np.matmul(op1,op2)
            after = np.matmul(op2.T,prod1)
            for k,op3 in enumerate(operations):
                if np.allclose(after,op3):
                    #print('{} via {} donne {}'.format(operationsname[i],operationsname[j],operationsname[k]))
                    if not(operationsname[k] in classe):
                        classe.append(operationsname[k])
        print('classe de {}'.format(operationsname[i]))
        print(classe)
