#!/usr/bin/env python
# ======================================================================
#
# Brad T. Aagaard, U.S. Geological Survey
#
# ======================================================================
""" Test of Stamen map tiles.
"""

import sys

import numpy
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from cartopy import crs

sys.path.append("../cartopy_extra_tiles")
from cached_tiler import CachedTiler
from stamen_tiles import Stamen

background = "terrain-background"

styles = (
    "terrain-labels",
    "terrain-lines",
    "toner-labels",
    "toner-lines",
    )

tilerBg = CachedTiler(Stamen(desired_tile_form="L", style=background), cache_dir="./tiles")

cmap = plt.cm.gray
mask = cmap(numpy.arange(cmap.N))
mask[:,-1] = mask[:,0] > 0.5
mask_cmap = ListedColormap(mask)
modelCRS = crs.PlateCarree()

for style in styles:
    ax = plt.axes(projection=tilerBg.crs)
    ax.set_extent([-123, -121.5, 37, 38.5])
    ax.add_image(tilerBg, 8, cmap="gray")
    tiler = CachedTiler(Stamen(desired_tile_form="RGBA", style=style), cache_dir="./tiles")
    ax.add_image(tiler, 8)
    plt.show()
