# -*- coding: utf-8 -*-
from imagekit import ImageSpec
from imagekit.processors import Thumbnail as PilThumbnail


class Thumbnail(ImageSpec):
    processors = [PilThumbnail(420, 230)]
    format = 'JPEG'
    options = {'quality': 60}
