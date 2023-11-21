#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Definition de fonctions utiles dans les exercices du chapitre "Scipy"
"""

# Importation des librairies
import numpy as np

# Definition des fonctions
def Cx(Re):
   """ Coefficient de trainee Cx d'une sphere, en fonction du nombre de Reynolds """
   # Convert argument to np.array as np.piecewise does not work with scalar...
   if not isinstance(Re, np.ndarray):
      Re = np.array([Re])
   # As tabulated by Clift, Grace & Weber
   f0 = lambda x: 0.
   fa = lambda x: 3./16 + 24./x
   fb = lambda x: 24./x * (1.+0.1315*x**(0.82-0.05*np.log10(x)))
   fc = lambda x: 24./x * (1+0.1935*x**0.6305)
   fd = lambda x: 10.**(np.polyval([0.1558, -1.1242, 1.6435],np.log10(x)))
   fe = lambda x: 10.**(np.polyval([0.1049, -0.9295, 2.5558, -2.4571],np.log10(x)))
   ff = lambda x: 10.**(np.polyval([-0.0636, 0.6370, -1.9181],np.log10(x)))
   fg = lambda x: 10.**(np.polyval([-0.1546, 1.5809, -4.3390],np.log10(x)))
   fh = lambda x: 29.78 -5.3*np.log10(x)
   fi = lambda x: 0.1*np.log10(x) -0.49
   fj = lambda x: 0.19-8.e4/x
   Cx = np.piecewise(Re, [Re==0.,(Re>0.)*(Re<0.01), (0.01 <= Re)*(Re <20), (20 <= Re)*(Re <260), \
                          (260 <= Re)*(Re < 1500), (1500 <= Re)*(Re < 1.2e4), \
                          (1.2e4 <= Re)*(Re < 4.4e4), (4.4e4 <= Re)*(Re < 3.38e5), \
                          (3.38e5 <= Re)*(Re < 4.e5), (4.e5 <= Re)*(Re < 1.e6), \
                          1.e6 <= Re], \
                         [f0,fa, fb, fc, fd, fe, ff, fg, fh, fi, fj])
   return Cx
   
# Programme principal
if __name__ == "__main__":
   test = Cx(float(2018))
   print(test)
