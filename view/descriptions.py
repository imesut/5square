from utils.pathUtils import *

def textForPath(path : str) -> str:
    array = splitPathStr(path)
    if len(array) == 6:
        # Menu Item Details
        if array[1] == "vn_ctgs":
            text = """
            MENU ITEM
            <a href="https://mesut.me/mesut_hu2fddfd419dc2cee2cacb3ffab07e7266_283976_288x288_fill_q75_box_smart1.jpg">·</a>
            <a href="https://developer.apple.com/augmented-reality/quick-look/models/meringue/pie_lemon_meringue.usdz">View 3D Model</a>
            MENU ITEM
            PRICE: 18.99 $
            """
            return text
    else:
        return "path"