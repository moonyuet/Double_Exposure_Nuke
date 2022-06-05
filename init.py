import nuke
import sys

CURRENT_PATH = "C:/Users/Kayla/Desktop/w8/" #change to your path
sys.path.append(CURRENT_PATH)

nuke.pluginAddPath(CURRENT_PATH)

import de_toolbar

def init():
    de_toolbar.add_toolbar(CURRENT_PATH)
    
init()