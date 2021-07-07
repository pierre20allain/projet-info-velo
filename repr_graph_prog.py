#from planning4mois.py import planning #je pense que ça marchera pas

#bon faut partir du principe qu'on met ça après dans planning4mois

#planning = [date de début, (ftp_max, ftp_min), ....]

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm
from PIL import Image

def repr_entr(planning):
    nb_jour = len(planning)
        
    for i in range(nb_jour):
        #If the value is (0,0), there is no training
        if len(planning[i][0]) == 1:
            new_im = Image.new('RGB', (100,100), (255,255,255))
            new_im.save(f'static/img_{i}_1.png', "PNG")
            new_im.save(f'static/img_{i}_2.png', 'PNG')
        

        #Else, the training is saved as an image in the static folder
        else:
            imgpil = Image.open("static/cycl.png")
            img = np.array(imgpil)
            plt.imshow(img)
            plt.savefig(f"static/img_{i}_1")

            ftp_max = planning[i][0]
            ftp_min = planning[i][1]
            duree = np.arange(0, len(ftp_max), 1)//6

            points = np.array([duree, ftp_min]).T.reshape(-1, 1, 2)
            segments = np.concatenate([points[:-1], points[1:]], axis=1)

            fig, axs = plt.subplots()
            norm = plt.Normalize(ftp_min.min(), ftp_min.max())
            lc = LineCollection(segments, cmap='RdPu', norm=norm)

            # Set the values used for colormapping
            lc.set_array(ftp_min)
            lc.set_linewidth(2)
            line_min = axs.add_collection(lc)

            points_max = np.array([duree, ftp_max]).T.reshape(-1, 1, 2)
            segments_max = np.concatenate([points_max[:-1], points_max[1:]], axis=1)


            lc_max = LineCollection(segments_max, cmap='RdPu', norm=norm)
            
            # Set the values used for colormapping
            lc_max.set_array(ftp_min)
            lc_max.set_linewidth(2)
            line_max = axs.add_collection(lc_max)
            fig.colorbar(line_min, ax=axs)


            # set the limits
            axs.set_xlim(duree.min(), duree.max())
            axs.set_ylim(0, ftp_min.max()+10)

            plt.fill_between(duree, ftp_max, alpha=0.2, color='green')
            plt.fill_between(duree, ftp_min, ftp_max, alpha=0.7, color='purple')

            plt.ylabel("Puissance (W)")
            plt.xlabel("Temps (min)")
            plt.title(f"Entraînement du jour")

            axs.yaxis.grid(linestyle='dashed')
            plt.gca().xaxis.set_ticks(range(0, len(duree)//6, 10), minor = True)
            plt.gca().xaxis.grid(True, which = 'both', color = 'gray', zorder = 0)

            plt.savefig(f"static/img_{i}_2")
            plt.clf()
            plt.cla()
