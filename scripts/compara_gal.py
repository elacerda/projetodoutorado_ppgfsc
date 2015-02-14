#!/usr/bin/python
# -*- coding: utf-8 -*-
from os.path import expanduser
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from pycasso import fitsQ3DataCube

outputImgSuffix = 'pdf'

fitsv13 = '/Users/lacerda/CALIFA/gal_fits/v20_q036.d13c/K0119_synthesis_eBR_v20_q036.d13c512.ps03.k2.mC.CCM.Bgsd61.fits'
fitsv14 = '/Users/lacerda/CALIFA/gal_fits/v20_q043.d14a/K0119_synthesis_eBR_v20_q043.d14a512.ps03.k1.mE.CCM.Bgsd6e.fits'
galaxyImgFile = '/Users/lacerda/CALIFA/images/K0119.jpg'

Kv13 = fitsQ3DataCube(fitsv13)
Kv14 = fitsQ3DataCube(fitsv14)

f, axArr = plt.subplots(3, 2)
f.set_size_inches((10, 12))

for ax in f.axes:
    ax.set_axis_off()

galimg = plt.imread(galaxyImgFile)
ax = axArr[0, 0]
ax.set_axis_on()
plt.setp(ax.get_xticklabels(), visible = False)
plt.setp(ax.get_yticklabels(), visible = False)
ax.imshow(galimg)

ax = axArr[0, 1]
textbox = dict(boxstyle = 'round', facecolor = 'wheat', alpha = 0.)
txt = 'CALIFA 119 - %s\n\nHubble Type: S0\n\n$\logM_\star\ =\ 11.47$\n\n$z\ =\ 0.01645$' % Kv13.galaxyName
ax.text(0.1, 0.9, txt,
        fontsize = 18,
        transform = ax.transAxes,
        verticalalignment = 'top',
        bbox = textbox)

ax = axArr[1, 0]
ax.set_axis_on()
ax.set_title(r'v1.3c - $\langle \log\ t \rangle_L\ [yr]$')
im = ax.imshow(Kv13.at_flux__yx, origin = 'lower', interpolation = 'nearest', aspect = 'auto', cmap = 'hot_r')
f.colorbar(ax = ax, mappable = im, use_gridspec = True)

ax = axArr[1, 1]
ax.set_axis_on()
ax.set_title(r'v1.4a - $\langle \log\ t \rangle_L\ [yr]$')
im = ax.imshow(Kv14.at_flux__yx, origin = 'lower', interpolation = 'nearest', aspect = 'auto', cmap = 'hot_r')
f.colorbar(ax = ax, mappable = im, use_gridspec = True)

ax = axArr[2, 0]
ax.set_axis_on()
ax.set_title(r'v1.3c - $A_V^\star\ [mag]$')
im = ax.imshow(Kv13.A_V__yx, origin = 'lower', interpolation = 'nearest', aspect = 'auto', cmap = 'hot_r')
f.colorbar(ax = ax, mappable = im, use_gridspec = True)

ax = axArr[2, 1]
ax.set_axis_on()
ax.set_title(r'v1.4a - $A_V^\star\ [mag]$')
im = ax.imshow(Kv14.A_V__yx, origin = 'lower', interpolation = 'nearest', aspect = 'auto', cmap = 'hot_r')
f.colorbar(ax = ax, mappable = im, use_gridspec = True)

# plt.suptitle(r'%s - %s' % (K.galaxyName, K.califaID))
f.savefig('%s-compv13v14-atflux_AV.%s' % (Kv13.califaID, outputImgSuffix))
