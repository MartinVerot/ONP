#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


import cv2 as cv
import sys


# Programme principal
if __name__ == "__main__":
    #ouverture de l'image
    img = cv.imread("exo9-peach.png")
    
    #conversion en tableau numpy
    img_arr = np.array(img)
    
    print(img_arr.shape)
    #l'axe zéro correspond donc à la hauteur, l'axe 1 à la largeur, et l'axe 2 aux composantes RGB
    
    #conversion en binaire, l'option expand_dims permet d'augmenter d'une dimension pour chaque composante
    #puis de convertir chaque octet en binaire
    img_bin = np.unpackbits(np.expand_dims(img_arr,axis=-1),axis=-1)
    print(img_bin.shape)
    
    
    img_cachee_bin = np.zeros_like(img_bin) 
    img_cachee_bin[:,:,:,0:4] = img_bin[:,:,:,4:8]
    img_cachee = np.packbits(img_cachee_bin,axis=-1)
    #À ce stade, on a une dimension en trop que l'on va éliminer avec np.squeeze
    print(img_cachee.shape)
    img_cachee = np.squeeze(img_cachee)
    cv.imshow("Display window", img_cachee)
    k = cv.waitKey(0)
