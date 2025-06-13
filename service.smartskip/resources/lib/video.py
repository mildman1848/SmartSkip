# -*- coding: utf-8 -*-
import os
import xbmcvfs

def get_video_duration(path):
    try:
        import ffprobe3  # simuliert, da wir keine externen Module nutzen
        return ffprobe3.get_duration(path)
    except:
        return 0.0
