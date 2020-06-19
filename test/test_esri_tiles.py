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
import cartopy.crs as ccrs

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
    ["dark", "dark-labels"],
    ["gray", "gray-labels"],
    ["ocean", "ocean-labels"],
    ["imagery", "labels1"],
    ["imagery", "labels2"],
    ["imagery", "labels3"],
    )

for style in styles:

    fig, ax = plt.subplots(1, 1, subplot_kw={'projection': ccrs.PlateCarree()})
    ax.set_extent([-123, -121.5, 37, 38.5])

    style = [style] if isinstance(style, str) else style

    for s in style:
        tiler = CachedTiler(ESRI(desired_tile_form='RGBA', style=s),
                            cache_dir="~/data_scratch/images/tiles")
        ax.add_image(tiler, 8)

    ax.set_title(style)
    plt.show()

    fig.savefig('/tmp/example_' + '_'.join(style) + '.png', bbox_inches='tight')
