# ======================================================================
#
# Brad T. Aagaard, U.S. Geological Survey
#
# ======================================================================
"""
Adapted from CachedTiler posted by pelson on
https://github.com/SciTools/cartopy/issues/732

Additional features:
  * Cache directory is specified via argument to the constructor.
  * Filename extension for image is determined at runtime.
"""

import os
import types

import requests
import PIL


class CachedTiler(object):
    """Augments other tilers with ability to cache tiles localy to disk
    in user-specified directory.
    """

    def __init__(self, tiler, cache_dir):
        """Constructor.

        :type tiler: GoogleTiles
        :param tiler: Tiler to use.

        :type cache_dir: str
        :param cache_dir: Path to directory for caching tiles locally on disk.
        """
        self.tiler = tiler
        tileset_name = '{}-{}'.format(self.tiler.__class__.__name__.lower(), self.tiler.style)
        self.cache_dir = os.path.expanduser(os.path.join(cache_dir, tileset_name))
        return

    def __getattr__(self, name):
        """Mimic the tiler interface.

        For methods ensure that the "self" passed through continues to
        be CachedTiler, not underlying tiler (self.tiler).

        :type name: str
        :param name: Name of attribute/method.
        """
        attr = getattr(self.tiler, name, None)
        if isinstance(attr, types.MethodType):
            attr = types.MethodType(attr.__func__, self)
        return attr

    def get_image(self, tile):
        """Get image, using local cache if possible.

        :type tile: tuple
        :param tile: Tuple of tile x,y,z.
        """

        # Create cache directory if necessary.
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

        # Get extension for filename based on URL.
        url = self._image_url(tile)
        if url.lower().endswith("png"):
            fname_extension = ".png"
        elif url.lower().endswith("jpg"):
            fname_extension = ".jpg"
        elif url.endswith("s=G"):
            fname_extension = ".png"
        elif "nationalmap.gov" in url:
            fname_extension = ".png"
        else:
            msg = "Could not detect filename extension from url '{}'.".format(url)
            raise ValueError(msg)

        tile_fname = os.path.join(self.cache_dir, "_".join(str(v) for v in tile) + fname_extension)
        if not os.path.exists(tile_fname):
            response = requests.get(url, stream=True)
            with open(tile_fname, "wb") as fh:
                for chunk in response:
                    fh.write(chunk)
        with open(tile_fname, 'rb') as fh:
            img = PIL.Image.open(fh)
            img = img.convert(self.desired_tile_form)

        return img, self.tileextent(tile), 'lower'

# End of file
