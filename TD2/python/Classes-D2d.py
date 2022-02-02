#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import Matrices


np.set_printoptions(precision=0,floatmode='fixed',suppress=True)
if __name__ == '__main__':
    operations = [] 
    #E
    operations.append(np.matrix([[1,0,0,0],
                                [0,1,0,0],
                                [0,0,1,0],
                                [0,0,0,1]]))
    #C2
    operations.append(np.matrix([[0,1,0,0],
                                [1,0,0,0],
                                [0,0,1,0],
                                [0,0,0,1]]))
    #S4
    operations.append(np.matrix([[0,0,1,0],
                                [0,0,0,1],
                                [0,1,0,0],
                                [1,0,0,0]]))   
    #S4-1
    operations.append(np.matrix([[0,0,0,1],
                                [0,0,1,0],
                                [1,0,0,0],
                                [0,1,0,0]]))
    #C2y 
    operations.append(np.matrix([[0,0,1,0],
                                [0,0,0,1],
                                [1,0,0,0],
                                [0,1,0,0]]))
    #C2x
    operations.append(np.matrix([[0,0,0,1],
                                [0,0,1,0],
                                [0,1,0,0],
                                [1,0,0,0]]))
    #sig xy'
    operations.append(np.matrix([[1,0,0,0],
                                [0,1,0,0],
                                [0,0,0,1],
                                [0,0,1,0]]))
    #sig xy
    operations.append(np.matrix([[0,1,0,0],
                                [1,0,0,0],
                                [0,0,1,0],
                                [0,0,0,1]]))   

    operationsname = ['E','C2z','S4','S4-1','C2y','C2x','sigxy\'','sigxy']


    #matrice de passage dans la base t et son invers
    P = np.matrix([[0.5,0.5,1/np.sqrt(2),0],
                   [0.5,0.5,-1/np.sqrt(2),0],
                   [0.5,-0.5,0,1/np.sqrt(2)],
                   [0.5,-0.5,0,-1/np.sqrt(2)]])

    P1 = P.T
    #vérification que la matrice inverse est bonne
    #print(np.matmul(P,P1))

#On affiche la matrice des opérateurs dans chacune des bases.
    for i,op in enumerate(operations):
        print('{}'.format(operationsname[i]))
        print('base {s}')
        print(op)
        print('base {t}')
        print(Matrices.matmul3(P1,op,P)) 
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
