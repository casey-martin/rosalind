# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:09:03 2016

@author: martincg
"""
import scipy
from scipy import ndimage

eb_neuro = scipy.misc.imread('88339 ChR5 S2R CamKII 10x_c1+2+3.png')
label_im, nb_labels = ndimage.label(eb_neuro)

from PIL import Image

foo = Image.open('88339 ChR5 S2R CamKII 10x_c1+2+3.png').convert('RGB').getcolors()




