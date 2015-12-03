# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Jurassic Health 
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.jurassic-health'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "Blender"
YOUTUBE_CHANNEL_ID_2 = "robin"
YOUTUBE_CHANNEL_ID_3 = "girls"
YOUTUBE_CHANNEL_ID_4 = "zumba"
YOUTUBE_CHANNEL_ID_5 = "BeFit"
YOUTUBE_CHANNEL_ID_6 = "runtastic"
YOUTUBE_CHANNEL_ID_7 = "Perfect"
YOUTUBE_CHANNEL_ID_8 = "popsugar"
YOUTUBE_CHANNEL_ID_9 = "bodybuilding"
YOUTUBE_CHANNEL_ID_10 = "superhero"
YOUTUBE_CHANNEL_ID_11 = "STORYOFSHIRTLESS"
YOUTUBE_CHANNEL_ID_12 = "TheQuestForFitness"
YOUTUBE_CHANNEL_ID_13 = "fit"
YOUTUBE_CHANNEL_ID_14 = "shauntfitness"

# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Blender",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://icons.iconarchive.com/icons/icons8/ios7/128/Sports-Exercise-icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="robin",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://icons.iconarchive.com/icons/sportsbettingspot/summer-olympics/128/weightlifting-icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Girls",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="http://icons.iconarchive.com/icons/sonya/swarm/128/gym-icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Zumba",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="http://s3.postimg.org/lhzsp1h1f/zumba.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Fit",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="http://icons.iconarchive.com/icons/icons-land/metro-raster-sport/128/Fitness-Hand-Grippers-icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Runtastic",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="http://icons.iconarchive.com/icons/sonya/swarm/128/Running-icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Perfect",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="http://icons.iconarchive.com/icons/sportsbettingspot/summer-olympics/128/weightlifting-icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="pop sugar",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="http://icons.iconarchive.com/icons/hopstarter/3d-cartoon-vol3/128/Yahoo-Messenger-icon.png",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="bodybuild",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="http://icons.iconarchive.com/icons/sonya/swarm/128/Running-icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="super hero",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="http://icons.iconarchive.com/icons/icons8/ios7/128/Sports-Exercise-icon.png",
        folder=True )                

    plugintools.add_item( 
        #action="", 
        title="Fit Media",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="http://icons.iconarchive.com/icons/iconsmind/outline/128/Bodybuilding-icon.png",
        folder=True )    

    plugintools.add_item( 
        #action="", 
        title="Jon Venus",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="http://icons.iconarchive.com/icons/tribalmarkings/colorflow/128/bodybuilding-icon.png",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="FiT – Global",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="http://icons.iconarchive.com/icons/iconsmind/outline/128/weight-Lift-icon.png",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Shaun",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="http://icons.iconarchive.com/icons/icons8/ios7/128/Sports-Exercise-icon.png",
        folder=True ) 
		
           
   	
run()
