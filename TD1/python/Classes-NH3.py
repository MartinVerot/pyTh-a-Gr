#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import Matrices
np.set_printoptions(precision=3,floatmode='fixed',suppress=True)
if __name__ == '__main__':
    E =  Matrices.Identity()
    theta = 2*np.pi/3
    C3 = Matrices.RotationZ(theta)
    C32 = Matrices.RotationZ(2*theta)
    inv1 = Matrices.InvY()
    invC3 =  C32
    invC32 =  C3
    inv2 = np.matmul(C3,np.matmul(inv1,invC3))
    inv3 = np.matmul(C32,np.matmul(inv1,invC32))
    
    operations = [E,C3,C32,inv1,inv2,inv3]
    invoperations = [E,C32,C3,inv1,inv2,inv3]
    operationsname = ['E','C3','C32','inv1','inv2','inv3']


#######
##Détermination des classes d'opérateurs
#######
    
    
    for i,op1 in enumerate(operations):
        classe=[operationsname[i]]
        for j,op2 in enumerate(operations):
            #on essaye de voir si op1 et op2 sont conjuguées
            #print('{}  {}'.format(operationsname[i],operationsname[j]))
            prod1 = np.matmul(op1,operations[j])
            after = np.matmul(invoperations[j],prod1)
            for k,op3 in enumerate(operations):
                if np.allclose(after,op3):
                    print('{} via {} donne {}'.format(operationsname[i],operationsname[j],operationsname[k]))
                    if not(operationsname[k] in classe):
                        classe.append(operationsname[k])
        print('classe de {}'.format(operationsname[i]))
        print(classe)
