import sqlite3

import numpy as np
import matplotlib.pyplot as plt


def fct_entrainement_ftp_max(seance, Duree, repet, individu):

    L= 6*np.array(Duree)
    duree= np.array(L, dtype = "int") # on met en bonne dimension

    N = 25  # +25 pour les 15min d'échauffement et 10 de récup
    for tps, rep in zip(duree, repet):
        N += tps*rep[0]

    fct = np.zeros(int(N))
    n = 0
    fct[0:5] = 0.56*individu.FTP  # Partie échauffement...
    fct[5:10] = 0.7*individu.FTP
    fct[10:15] = 0.75*individu.FTP
    n +=15  # ...jusque là
    for i in range(len(seance)):
        if repet[i][1] == 0:
            fct[n:(n+duree[i])] = seance[i].FTPplus
            n += duree[i]
        elif repet[i][1] != 0:
            k = repet[i][0]
            while k > 0:
                if repet[i][1]!=-1 :
                    fct[n:(n+duree[i])] = seance[i].FTPplus
                    n += duree[i]
                    fct[n:(n+duree[i+1])] = seance[i+1].FTPplus

                    n += duree[i+1]
                    k -= 1
                if repet[i][1]==-1 : k-=1

    fct[n:(n+10)] = 0.7*individu.FTP  # partie récup
    return fct
            
    
def fct_entrainement_ftp_min(seance, Duree, repet, individu):

    L= 6*np.array(Duree)
    duree= np.array(L, dtype = "int") # on met en bonne dimension

    N = 25  # +25 pour les 15min d'échauffement et 10 de récup
    for tps, rep in zip(duree, repet):
        N += tps*rep[0]

    fct = np.zeros(int(N))
    n = 0
    fct[0:5] = 0
    fct[5:10] = 0.56*individu.FTP
    fct[10:15] = 0.65*individu.FTP
    n +=15
    for i in range(len(seance)):
        if repet[i][1] == 0:
            fct[n:(n+duree[i])] = seance[i].FTPmoins
            n += duree[i]
        elif repet[i][1] != 0:
            k = repet[i][0]
            while k > 0:
                if repet[i][1]!=-1 :
                    fct[n:(n+duree[i])] = seance[i].FTPmoins
                    n += duree[i]
                    fct[n:(n+duree[i+1])] = seance[i+1].FTPmoins

                    n += duree[i+1]
                    k -= 1
                if repet[i][1]==-1 : k-=1
    fct[n:(n+10)] = 0.4*individu.FTP
    return fct



