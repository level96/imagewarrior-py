from imagewarrior import Gravity
from imagewarrior import Resize
from imagewarrior import Ext


def imagewarrior(request):
    return {
        'GRAVITY_SMART': Gravity.SMART,
        'GRAVITY_NORTH': Gravity.NORTH,
        'GRAVITY_SOUTH': Gravity.SOUTH,
        'GRAVITY_EAST': Gravity.EAST,
        'GRAVITY_WEST': Gravity.WEST,
        'GRAVITY_CENTER': Gravity.CENTER,
        'GRAVITY_NORTH_EAST': Gravity.NORTH_EAST,
        'GRAVITY_NORTH_WEST': Gravity.NORTH_WEST,
        'GRAVITY_SOUTH_EAST': Gravity.SOUTH_EAST,
        'GRAVITY_SOUTH_WEST': Gravity.SOUTH_WEST,
        'GRAVITY_FOCUS': Gravity.FOCUS,
        # Resize
        'RESIZE_FIT': Resize.FIT,
        'RESIZE_FILL': Resize.FILL,
        'RESIZE_CROP': Resize.CROP,
        # File Extension
        'EXT_JPEG': Ext.JPEG,
        'EXT_PNG': Ext.PNG,
        'EXT_GIF': Ext.GIF,
        'EXT_WEBP': Ext.WEBP,
        'EXT_ICO': Ext.ICO,
    }
