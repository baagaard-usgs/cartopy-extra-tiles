#!/usr/bin/env python
# ======================================================================
#
# Brad T. Aagaard, U.S. Geological Survey
#
# ======================================================================
"""Test tile caching using GoogleTiles.
"""

import sys

import matplotlib.pyplot as plt
from cartopy.io.img_tiles import GoogleTiles

sys.path.append("../cartopy_extra_tiles")
from cached_tiler import CachedTiler

tiler = CachedTiler(GoogleTiles(), cache_dir="~/data_scratch/images/tiles")
ax = plt.axes(projection=tiler.crs)
ax.set_extent([-123, -121.5, 37, 38.5])
ax.add_image(tiler, 8)
plt.show()

# End of file
