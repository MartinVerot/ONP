#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Definition de fonctions pour faire l'analyse d'une simulation MD
"""

# Importation des librairies
import numpy as np
import matplotlib.pyplot as plt

# Definition des fonctions
def extract_data(filename, nb_mol=64, nb_atom_per_mol=3, nb_spatial_dim=3):
   """Extract raw positions from an MD output file in .xyz format generated by CP2K, and reshape it into a 4D array for easier manipulation.
        
   Parameters:
           filename (str): path to the positions .xyz file.
           
           nb_mol (int, optional): number of molecules simulated.
           
           nb_atom_per_mol (int, optional): number of atoms per molecule (Beware: assuming same molecules).
           
           nb_spatial_dim (int, optional): number of spatial dimensions to consider.
     
   Returns:
           data (4D float array): Numpy array containing the coordinates of all atoms for every step of the MD.
                Notes: data[i, j, k, l] is the l-th coordinate of the k-th atom of the j-th molecule of water at the i-th step.

   Credit : R. Staub
   """

   # Load raw coordinates into memory, discard comments lines and only consider the coordinate columns
   data = np.loadtxt(filename, comments=(' i =', '     {}'.format(nb_mol*nb_atom_per_mol)), usecols=range(1,4))

   # Reshape data with dimensions (nb_steps, nb_mol, nb_atom_per_mol, nb_spatial_dim)
   data = data.reshape(-1, nb_mol, nb_atom_per_mol, nb_spatial_dim)

   return(data)

def plot_1D(affine_fit, linear_fit, *args, **kwargs):
   """ Routine de plot pour l'exercice de MD
   **kwargs permet de passer les titres des plots sous la forme d'un dictionnaire, et eventuellement sauver le resultat.
   Les booleens affine_fit et linear_fit permettent de superposer eventuellement aux donnees des fits affine et lineaire """
   # Determine le nombre de plot
   nplot = len(args)
   # Recupere les clefs des commentaires
   if kwargs:
      keys = kwargs.keys()
   # Creation du support de l'oeuvre (unites = pouces!)
   fig = plt.figure(figsize=(4*nplot, 4))
   # Creation de l'oeuvre
   iplot = 1
   for arg in args:
      axe = plt.subplot(1,nplot,iplot)
      plt.plot(arg)
      if affine_fit: # add a affine fit
         time = np.arange(arg.shape[0])
         coeff = np.polyfit(time, arg, 1)
         plt.plot(np.polyval(coeff,time))
      if True:#linear_fit: # add a linear fit
         # https://fr.wikipedia.org/wiki/Ajustement_affine
         coeff = time.dot(arg)/time.dot(time)
         print('Dlin {}'.format(coeff))
         plt.plot(time,coeff*time,linestyle='dotted')
      # Les titres
      axe.set_xlabel('Time step')
      key_title = 'Title{}'.format(iplot)
      if kwargs and key_title in keys:
         plt.title(kwargs[key_title])
         
      iplot += 1
   # Sauvegarde
   if True:
      key_savepng = 'Pngname'
      if kwargs and key_title in keys:
         plt.savefig(kwargs[key_savepng])
   # Visualisation
   plt.show()
   return

# Programme principal
if __name__ == "__main__":
   pass

