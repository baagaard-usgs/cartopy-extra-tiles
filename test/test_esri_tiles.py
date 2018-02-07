#!/usr/bin/env python
# ======================================================================
#
# Brad T. Aagaard, U.S. Geological Survey
#
# ======================================================================
""" Test of ESRI map tiles.
"""

import sys

import matplotlib.pyplot as plt

sys.path.append("../cartopy_extra_tiles")
from cached_tiler import CachedTiler
from esri_tiles import ESRI

styles = (
    "imagery",
    "shadedrelief",
    "streetmap",
    "terrain",
    "topo",
    "natgeo",
    )
for style in styles:
    tiler = CachedTiler(ESRI(style=style), cache_dir="~/data_scratch/images/tiles")
    ax = plt.axes(projection=tiler.crs)
    ax.set_extent([-123, -121.5, 37, 38.5])
    ax.add_image(tiler, 8)
    plt.show()
