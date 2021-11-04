#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Here we calculate the grating dispersion of an Acton spectrometer.
"""
import numpy as np
import matplotlib.pyplot as plt
def linear_dispersion(w, f=750, phi=-6, m=1, gr=300):
    """dlambda / dx
    Default values correspond to Acton 750i
    Parameters
    ----------
    f: focal length (mm)
         default 750 (SpectraPro 2750i)
    phi: angle in degrees (°)
        default 9
    m: order of dispersion
        default 1
    gr: grooves spacing (gr/mm)
        default 300
    """
    # correct units:
    phi *= 2 * np.pi / 360
    d = 1e-3 / gr
    disp = w / (2 * f) * (np.tan(phi) + np.sqrt((2 * d / m / (w * 1e-9) * np.cos(phi)) ** 2 - 1))
    return disp  # to nm/mm


W = np.linspace(300,800,50)     # nm
f = 500       # mm
gr = 2400     # gr/mm
phi = -9.2     # °

disp = linear_dispersion(W,f,phi,m=1,gr=gr)


plt.figure('Grating dispersion')
plt.plot(W,disp)
plt.xlabel('Wavelength (nm)'),plt.ylabel('Spectrometer reciprocal function (nm/mm)')
plt.ylim(ymin=0)


l_pix = 19    # µm  # pixel size
N_pix = 512   # Number of pixels
plt.figure('Spectral range')
plt.plot(W,disp*N_pix*l_pix*1e-3)
plt.xlabel('Wavelength (nm)'),plt.ylabel('Spectral range (nm)')