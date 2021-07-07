import sqlite3
import matplotlib.pyplot as plt
import numpy as np

from classes import Individu, Endurance, Sprint, Tempo, Sweet_spot, Capacite_aerobie, Capacite_anaerobie, Seuil, Recup_active
from programmevelo import fct_entrainement_ftp_max, fct_entrainement_ftp_min


def fct_planning(username):
        # Recuperation d'un individu dans la bdd :
        conn = sqlite3.connect('personnes.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT* FROM personnes WHERE username= ?""",(username,))
        personne = cursor.fetchone()
        conn.close()
        print(personne)
        individu = Individu(personne[1],personne[2],personne[3],personne[4],personne[5],personne[6],personne[7])
        print(individu)

        # Les différentes classes d'intervalles :

        endurance = Endurance(individu)
        sprint = Sprint(individu)
        tempo = Tempo(individu)
        sweet_spot = Sweet_spot(individu)
        seuil = Seuil(individu)
        capacite_aerobie = Capacite_aerobie (individu)
        capacite_anaerobie = Capacite_anaerobie (individu)
        recup_active = Recup_active(individu)


        # On définit les entraînements spécifiques aux semaines de récupération :

        fct_recup1_min = np.zeros((360))
        fct_recup1_max = np.zeros((360))
        fct_recup1_max[0:359] = 0.55*individu.FTP

        fct_recup2_min = np.zeros((660))
        fct_recup2_max = np.zeros((660))
 
        fct_recup2_min[91:210] = 0.56*individu.FTP
        fct_recup2_min[211:216] = 1.5*individu.FTP
        fct_recup2_min[217:246] = 0.56*individu.FTP
        fct_recup2_min[247:252] = 1.5*individu.FTP
        fct_recup2_min[253:282] = 0.56*individu.FTP
        fct_recup2_min[283:288] = 1.5*individu.FTP
        fct_recup2_min[289:318] = 0.56*individu.FTP
        fct_recup2_min[319:438] = 0.56*individu.FTP
        fct_recup2_min[439:441] = 1.5*individu.FTP
        fct_recup2_min[442:466] = 0.56*individu.FTP
        fct_recup2_min[467:469] = 1.5*individu.FTP
        fct_recup2_min[470:494] = 0.56*individu.FTP
        fct_recup2_min[495:497] = 1.5*individu.FTP
        fct_recup2_min[498:522] = 0.56*individu.FTP

        fct_recup2_max[91:210] = 0.75*individu.FTP
        fct_recup2_max[211:216] = 3*individu.FTP
        fct_recup2_max[217:246] = 0.75*individu.FTP
        fct_recup2_max[247:252] = 2*individu.FTP
        fct_recup2_max[253:282] = 0.75*individu.FTP
        fct_recup2_max[283:288] = 2*individu.FTP
        fct_recup2_max[289:318] = 0.75*individu.FTP
        fct_recup2_max[319:438] = 0.75*individu.FTP
        fct_recup2_max[439:441] = 2*individu.FTP
        fct_recup2_max[442:466] = 0.75*individu.FTP
        fct_recup2_max[467:469] = 2*individu.FTP
        fct_recup2_max[470:494] = 0.75*individu.FTP
        fct_recup2_max[495:497] = 2*individu.FTP
        fct_recup2_max[498:522] = 0.75*individu.FTP

        fct_recup3_min = np.zeros((1080))
        fct_recup3_max = np.zeros((1080))

      
        fct_recup3_min[91:451] = 0.56*individu.FTP

        fct_recup3_max[0:1079] = 0.56*individu.FTP
        fct_recup3_max[91:451] = 0.75*individu.FTP

        planning = []  # contiendra en  premier argument le jour exact de début de l'entraînement, puis à l'indice n de la liste correspond l'entrainement (ou le repos) du nème jour du programme

        x=personne[-1]

        nb_cycles = 122 // individu.duree  # 122 jours pour 2 mois à 31 jours et 2 mois à 30 jours
        first_day = x  # jour où la personne commence l'entraînement
        for i in range(x) : 
            planning.append((np.array([0]),np.array([0])))

    
        periode_non_repos = individu.duree - 7  # Nombre de jours d'entraînement en enlevant la semaine de repos/récup
        nb_sem_a_cy = periode_non_repos / 7  # nombre de semaines actives par cycle
        jour = 0  # numéro du nème jour du programme

        conn = sqlite3.connect('entrainements.db')
        cursor = conn.cursor()

        while jour < 121:
            num_cycle = (jour+first_day) // individu.duree
            num_sem = ((jour+first_day) % individu.duree) // 7
            if (first_day + jour)%7 == 0 or (first_day + jour)%7 == 2 or (first_day + jour)%7 == 4:
                planning.append((np.array([0]),np.array([0]))) # Les lundi, mercredi et vendredi : repos (caractérisé par un tupple de np.array(0,0)
                print(f'jour={jour}, num_cycle={num_cycle}, num_sem={num_sem}, seance = repos')
                jour += 1
                

            if (first_day + jour)%7 == 1:  # Les mardi : intensité avec du sprint
                if num_cycle == 0 and num_sem == 0:   
                    cursor.execute("""SELECT* FROM entrainements WHERE label LIKE '%Sp1'""")
                    entrainement = cursor.fetchone()
                    
                    Seance = eval(entrainement[2])
                    Repet = eval(entrainement[4])
                    Duree = eval(entrainement[3])

                    print(f'jour={jour}, num_cycle={num_cycle}, num_sem={num_sem}, seance = {entrainement}')

                    planning.append((fct_entrainement_ftp_min(Seance, Duree, Repet, individu), fct_entrainement_ftp_max(Seance, Duree, Repet, individu)))
                    jour += 1
                    
                elif (jour % individu.duree) <= periode_non_repos :
                    a = 148 + 10*num_cycle + 10*num_sem  # on code ici la progression entre les différentes semaines : on mutliplie a et b par des facteurs de num_cycle et num_semaines
                    b = 148 + 70*num_cycle + 70*num_sem # les facteurs 10 et 70 sont arbitraires, ils fonctionnent bien ici avec les intensité des entrainements 
                    
                    cursor.execute("""SELECT* FROM entrainements WHERE label LIKE 'SP%' AND intensite BETWEEN ? AND ? """, (a,b))
                    entrainement = cursor.fetchone()
                    Seance = eval(entrainement[2])
                    Repet = eval(entrainement[4])
                    Duree = eval(entrainement[3])

                    print(f'jour={jour}, num_cycle={num_cycle}, num_sem={num_sem}, seance = {entrainement}')

                    planning.append((fct_entrainement_ftp_min(Seance, Duree, Repet, individu), fct_entrainement_ftp_max(Seance, Duree, Repet, individu)))
                    jour += 1
                else:
                    planning.append((fct_recup1_min, fct_recup1_max))
                    jour += 1
                    # entrainement en semaine de repos



            if (first_day + jour)%7 == 3:  # Les) jeudi : intensité avec de la PMA
                if num_cycle == 0 and num_sem == 0:   
                    cursor.execute("""SELECT* FROM entrainements WHERE label LIKE '%PMA1'""")
                    entrainement = cursor.fetchone()
                    Seance = eval(entrainement[2])
                    Duree = eval(entrainement[3])
                    Repet = eval(entrainement[4])

                    print(f'jour={jour},num_cycle={num_cycle}, num_sem={num_sem}, seance = {entrainement}')
                    
                    planning.append((fct_entrainement_ftp_min(Seance, Duree, Repet, individu), fct_entrainement_ftp_max(Seance, Duree, Repet, individu)))
                    jour +=1
                elif (jour % individu.duree) <= periode_non_repos :
                    a = 83 + 5*num_cycle + 5*num_sem
                    b = 83 + 30*num_cycle + 30*num_sem
                    cursor.execute("""SELECT* FROM entrainements WHERE label LIKE 'PMA%' AND intensite BETWEEN ? AND ? """, (a,b))
                    entrainement = cursor.fetchone()
                    if entrainement == None :
                        a = 83 + 5*num_cycle + 5*num_sem
                        b = 83 + 30*num_cycle + 30*num_sem
                        cursor.execute("""SELECT* FROM entrainements WHERE intensite BETWEEN ? AND ? """, (a,b))
                        entrainement = cursor.fetchone()
                    Seance = eval(entrainement[2])
                    Duree = eval(entrainement[3])
                    Repet = eval(entrainement[4])

                    print(f'jour={jour},num_cycle={num_cycle}, num_sem={num_sem}, seance = {entrainement}')
                    
                    planning.append((fct_entrainement_ftp_min(Seance, Duree, Repet, individu), fct_entrainement_ftp_max(Seance, Duree, Repet, individu)))
                    jour +=1
                else:
                    planning.append((np.array([0]), np.array([0])))
                    jour += 1
                

            if (first_day + jour)%7 == 5:  # Les samedi : endurance light  
                if (jour % individu.duree) <= periode_non_repos :
                    
                    cursor.execute("""SELECT* FROM entrainements WHERE label LIKE '%L1'""") 
                    entrainement = cursor.fetchone()
                    Seance = eval(entrainement[2])
                    Duree = eval(entrainement[3])
                    Repet = eval(entrainement[4])

                    print(f'jour={jour}, num_cycle={num_cycle}, num_sem={num_sem},  seance = {entrainement}')
                    planning.append((fct_entrainement_ftp_min(Seance, Duree, Repet, individu), fct_entrainement_ftp_max(Seance, Duree, Repet, individu)))
                    jour +=1
                else:
                    planning.append((fct_recup2_min, fct_recup2_max))
                    jour += 1
                

            if (first_day + jour)%7 == 6:  # Les dimanche : endurance longue (Temp)
                if num_cycle == 0 and num_sem == 0:   
                    
                    cursor.execute("""SELECT* FROM entrainements WHERE label LIKE '%TEMP4'""")
                    entrainement = cursor.fetchone()
                    Seance = eval(entrainement[2])
                    Duree = eval(entrainement[3])
                    Repet = eval(entrainement[4])


                    print(f'jour={jour}, num_cycle={num_cycle}, num_sem={num_sem}, seance = {entrainement}')
                    planning.append((fct_entrainement_ftp_min(Seance, Duree, Repet, individu), fct_entrainement_ftp_max(Seance, Duree, Repet, individu)))
                    jour +=1
                elif (jour % individu.duree) <= periode_non_repos :
                    a = 104 + 10*num_cycle + 10*num_sem
                    b = 104 + 70*num_cycle + 70*num_sem
                    cursor.execute("""SELECT* FROM entrainements WHERE label LIKE 'TEMP%' AND intensite BETWEEN ? AND ? """, (a,b)) 
                    entrainement = cursor.fetchone()
                    Seance = eval(entrainement[2])
                    Duree = eval(entrainement[3])
                    Repet = eval(entrainement[4])


                    print(f'jour={jour}, num_cycle={num_cycle}, num_sem={num_sem}, seance = {entrainement}')
                    planning.append((fct_entrainement_ftp_min(Seance, Duree, Repet, individu), fct_entrainement_ftp_max(Seance, Duree, Repet, individu)))
                    jour +=1
                else:
                    planning.append((fct_recup3_min, fct_recup3_max))
                    jour += 1

                

        conn.close()
        

        return planning
