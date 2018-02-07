#!/usr/bin/env python
# ======================================================================
#
# Brad T. Aagaard, U.S. Geological Survey
#
# ======================================================================
""" Test of Stamen map tiles.
"""

import sys

import matplotlib.pyplot as plt

sys.path.append("../cartopy_extra_tiles")
from cached_tiler import CachedTiler
from stamen_tiles import Stamen

styles = (
    "terrain-standard",
    "terrain-labels",
    "terrain-lines",
    "terrain-background",
    "toner-standard",
    "toner-hybrid",
    "toner-labels",
    "toner-lines",
    "toner-background",
    "toner-lite",
    )
for style in styles:
    tiler = CachedTiler(Stamen(style=style), cache_dir="~/data_scratch/images/tiles")
    ax = plt.axes(projection=tiler.crs)
    ax.set_extent([-123, -121.5, 37, 38.5])
    ax.add_image(tiler, 8)
    plt.show()
