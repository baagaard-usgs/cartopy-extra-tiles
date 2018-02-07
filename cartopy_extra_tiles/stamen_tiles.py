# ======================================================================
#
# Brad T. Aagaard, U.S. Geological Survey
#
# ======================================================================
"""Additional tiles from http://maps.stamen.com.
"""

import cartopy.crs as ccrs
from cartopy.io.img_tiles import GoogleTiles

class Stamen(GoogleTiles):
    """Stamen terrain and toner tiles.

    http://maps.stamen.com/#terrain
    http://maps.stamen.com/#toner

    Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap,
    under ODbL.
    """

    def __init__(self, desired_tile_form="RGB", style="standard"):
        """Constructor.

        :type desired_tile_form: str
        :param desired_tile_form: PIL image mode (e.g., L, RGB, RGBA, CMYK, HSV, I, F)

        :type style: str
        :param style: Stamen flavor (e.g., "terrain-standard", "toner-standard", "toner-lite")
        """
        styles = {
            "terrain-standard": "terrain",
            "terrain-labels": "terrain-labels",
            "terrain-lines": "terrain-lines",
            "terrain-background": "terrain-background",
            "toner-standard": "toner",
            "toner-hybrid": "toner-hybrid",
            "toner-labels": "toner-labels",
            "toner-lines": "toner-lines",
            "toner-background": "toner-background",
            "toner-lite": "toner-lite",
            }
        if style not in styles:
            msg = "Invalid style '%s'. Valid styles: %s" % (style, ", ".join(styles.keys()))
            raise ValueError(msg)

        self.desired_tile_form = desired_tile_form
        self.style = style
        self.imgs = []
        self.crs = ccrs.Mercator.GOOGLE

        self.url = "http://tile.stamen.com/{}/%s/%s/%s.png".format(styles[style])

        self.attribution = "Map tiles by Stamen Design, under CC BY 3.0." \
          "Data by OpenStreetMap, under ODbL."

        return

    def _image_url(self, tile):
        """
        """
        x, y, z = tile
        return self.url % (z, x, y)

# End of file
