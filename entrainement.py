import sqlite3
import matplotlib.pyplot as plt
import numpy as np

from classes import Individu, Endurance, Sprint, Tempo, Sweet_spot, Capacite_aerobie, Capacite_anaerobie, Seuil, Recup_active
from programmevelo import fct_entrainement_ftp_max, fct_entrainement_ftp_min



# Recuperation d'un individu dans la bdd :
conn = sqlite3.connect('personnes.db')
cursor = conn.cursor()
cursor.execute("""SELECT* FROM personnes WHERE id=1""")
personne = cursor.fetchone()
conn.close()
individu = Individu(personne[1],personne[2],personne[3],personne[4],personne[5],personne[6],personne[7])

endurance = Endurance(individu)
sprint = Sprint(individu)
tempo = Tempo(individu)
sweet_spot = Sweet_spot(individu)
seuil = Seuil(individu)
capacite_aerobie = Capacite_aerobie (individu)
capacite_anaerobie = Capacite_anaerobie (individu)
recup_active = Recup_active(individu)


# Recupération d'un entrainement dans la bdd :


conn = sqlite3.connect('entrainements.db')
cursor = conn.cursor()
cursor.execute("""SELECT* FROM entrainements WHERE label='SP3'""") 
entrainement = cursor.fetchone() 
conn.close()

Seance = eval(entrainement[2])
Duree = eval(entrainement[3])


print(entrainement)

Repet = eval(entrainement[4])




power_max=fct_entrainement_ftp_max(Seance, Duree, Repet, individu)
power_min=fct_entrainement_ftp_min(Seance, Duree, Repet, individu)

N=len(power_max)
plt.plot(np.arange(0, N, 1), power_max)
plt.plot(np.arange(0, N, 1), power_min)
plt.show()
