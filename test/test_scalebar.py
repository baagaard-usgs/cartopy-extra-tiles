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
from cartopy import crs

sys.path.append("../cartopy_extra_tiles")
import scale_bar

ax = plt.axes(projection=crs.PlateCarree())
ax.set_extent([-123, -121.5, 37, 38.5])
scale_bar.scale_bar(ax, (0.25, 0.1), 50)
plt.show()
