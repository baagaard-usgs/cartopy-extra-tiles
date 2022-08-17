#!/usr/bin/env python
# ======================================================================
#
# Brad T. Aagaard, U.S. Geological Survey
#
# ======================================================================
""" Test of ESRI map tiles.
"""

import sys

import cartopy.crs as ccrs
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
    ("dark", "dark-labels"),
    ("gray", "gray-labels"),
    ("ocean", "ocean-labels"),
    ("imagery", "world-labels"),
    ("imagery", "world-alt-labels"),
    ("shadedrelief", "world-overlay"),
    )
for style in styles:
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_extent([-123, -121.5, 37, 38.5])

    styles = [style] if isinstance(style, str) else style
    for s in styles:
        tiler = CachedTiler(ESRI(style=s, desired_tile_form='RGBA'), cache_dir="~/data_scratch/images/tiles")
        ax.add_image(tiler, 8)
    ax.set_title(style)
    plt.show()
