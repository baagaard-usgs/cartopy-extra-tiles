# ======================================================================
#
# Brad T. Aagaard, U.S. Geological Survey
#
# ======================================================================
"""Additional tiles from ESRI.
"""

import cartopy.crs as ccrs
from cartopy.io.img_tiles import GoogleTiles


class ESRI(GoogleTiles):
    """ESRI imagery, shaded relief, street map, terrain, topo,
        National Geographic, dark, dark-labels, gray, gray-labels, ocean,
        ocean-labels, labels1, labels2 and labels3 tiles.
    """

    def __init__(self, desired_tile_form="RGB", style="standard"):
        """Constructor.

        :type desired_tile_form: str
        :param desired_tile_form: PIL image mode (e.g., L, RGB, RGBA,
        CMYK, HSV, I, F)

        :type style: str
        :param style: ESRI flavor
            ("imagery", "shadedrelief", "streetmap", "terrain", "topo", "natgeo",
             "dark", "dark-labels", "gray", "gray-labels", "ocean", "ocean-labels",
             "labels1", "labels2", "labels3")
        """
        styles = {
            "imagery": "World_Imagery",
            "shadedrelief": "World_Shaded_Relief",
            "streetmap": "World_Street_Map",
            "terrain": "World_Terrain_Base",
            "topo": "World_Topo_Map",
            "natgeo": "NatGeo_World_Map",
            "dark": "Canvas/World_Dark_Gray_Base",
            "dark-labels": "Canvas/World_Dark_Gray_Reference",
            "gray": "Canvas/World_Light_Gray_Base",
            "gray-labels": "Canvas/World_Light_Gray_Reference",
            "ocean": "Ocean/World_Ocean_Base",
            "ocean-labels": "Ocean/World_Ocean_Reference",
            "labels1": "Reference/World_Boundaries_and_Places",
            "labels2": "Reference/World_Boundaries_and_Places_Alternate",
            "labels3": "Reference/World_Reference_Overlay",
        }
        if style not in styles:
            msg = "Invalid style '%s'. Valid styles: %s" % (style, ", ".join(styles.keys()))
            raise ValueError(msg)

        self.desired_tile_form = desired_tile_form
        self.style = style
        self.imgs = []
        self.crs = ccrs.Mercator.GOOGLE

        self.url = "http://server.arcgisonline.com/arcgis/rest/services/{}/MapServer/tile/%d/%d/%d.jpg".format(styles[style])

        self.attribution = ""

        return

    def _image_url(self, tile):
        """
        """
        x, y, z = tile
        return self.url % (z, y, x)

# End of file
