# ======================================================================
#
# Brad T. Aagaard, U.S. Geological Survey
#
# ======================================================================
"""Additional tiles from USGS National Map.
"""

import cartopy.crs as ccrs
from cartopy.io.img_tiles import GoogleTiles

class USGS(GoogleTiles):
    """USGS National Map imagery, hydrology, shaded relief, and topo tiles.
    """

    def __init__(self, desired_tile_form="RGB", style="imagerytopo"):
        """Constructor.

        :type desired_tile_form: str
        :param desired_tile_form: PIL image mode (e.g., L, RGB, RGBA,
        CMYK, HSV, I, F)

        :type style: str
        :param style: Stamen flavor
            ("imagery", "shadedrelief", "hydrography", "topo", "imagerytopo")
        """
        styles = {
            "imagery": "USGSImageryOnly",
            "shadedrelief": "USGSShadedReliefOnly",
            "hydrography": "USGSHydroCached",
            "topo": "USGSTopo",
            "imagerytopo": "USGSImageryTopo",
            }
        if style not in styles:
            msg = "Invalid style '%s'. Valid styles: %s" % (style, ", ".join(styles.keys()))
            raise ValueError(msg)

        self.desired_tile_form = desired_tile_form
        self.style = style
        self.imgs = []
        self.crs = ccrs.Mercator.GOOGLE

        self.url = "http://basemap.nationalmap.gov/arcgis/rest/services/{}/MapServer/tile/%d/%d/%d".format(styles[style])

        self.attribution = ""

        return

    def _image_url(self, tile):
        """
        """
        x, y, z = tile
        return self.url % (z, y, x)

# End of file
