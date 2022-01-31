#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
np.set_printoptions(precision=3,floatmode='fixed',suppress=True)
if __name__ == '__main__':
    E = np.matrix([[1,0,0],
                   [0,1,0],
                   [0,0,1]])
    theta = 2*np.pi/3
    C3 = np.matrix([[np.cos(theta),-np.sin(theta),0],
                    [np.sin(theta),np.cos(theta),0],
                    [0,0,1]])
    C32 = np.matrix([[np.cos(2*theta),-np.sin(2*theta),0],
                    [np.sin(2*theta),np.cos(2*theta),0],
                    [0,0,1]])

    inv1 = np.matrix([[1,0,0],
                    [0,-1,0],
                    [0,0,1]])
    inv2 = np.matmul(inv1,C3)
    inv3 = np.matmul(inv1,C32)

    N = np.matrix([[0],[0],[0]])
    H1 = np.matrix([[1],[0],[-1]])
    H2 = np.matmul(C3,H1)
    H3 = np.matmul(C3,H2)
    coords = np.concatenate((N,H1,H2,H3),axis=1)
    print('coords')
    print(coords)
    
    operations = [E,C3,C32,inv1,inv2,inv3]
    operationsname = ['E','C3','C32','inv1','inv2','inv3']
    
###
#En passant par les coordonnées
###
#coordonnées des atomes après chaque opération
    aftercoords = []
    for i,op in enumerate(operations):
        after = np.matmul(op,coords)
        aftercoords.append(after)
        print(operationsname[i])
        print(after)


#coordonnées des atomes après les deux opérations
    matmulNH3 = [[]] * len(operations)
    for i in range(len(operations)):
        matmulNH3[i]=[[]]*len(operations)
    print(matmulNH3)
    for i,op1 in enumerate(operations):
        before = np.matmul(op1,coords)
        for j,op2 in enumerate(operations):
            after = np.matmul(op2,before)
            print('{} x {}'.format(operationsname[j],operationsname[i]))
            print(after)
            #on regarde parmis les coordonnées calculées au début quelles sont celles qui sont le plus proche de la nouvelle matrice pour trouver à quelle transformation simple correspond le produit des deux transformations
            mins = np.zeros(len(operations))
            for k,coord in enumerate(aftercoords):
                mins[k]=np.sum(np.abs(coord-after))
            idx=np.argmin(mins) 
            matmulNH3[i][j]=operationsname[idx]
            print('{}'.format(operationsname[idx]))
    print(np.asarray(operationsname)) 
    print(np.transpose(np.asarray(matmulNH3,dtype='str')))


#######
##En passant par les matrices de transformation
#######
    for i,op in enumerate(operations):
        print(operationsname[i])
        print(op)
    
    
    matmulNH32 = [[]] * len(operations)
    for i in range(len(operations)):
        matmulNH32[i]=[[]]*len(operations)
    for i,op1 in enumerate(operations):
        for j,op2 in enumerate(operations):
            after = np.matmul(op2,op1)
            print('{} x {}'.format(operationsname[j],operationsname[i]))
            print(after)
            mins = np.zeros(len(operations))
            #on trouve l'opération 3 qui a la matrice égale au produit des deux opérations 
            for k,op3 in enumerate(operations):
                mins[k]=np.sum(np.abs(op3-after))
            idx=np.argmin(mins) 
            print('{}'.format(operationsname[idx]))
            matmulNH32[i][j]=operationsname[idx]
    print(np.transpose(np.asarray(matmulNH32,dtype='str')))
