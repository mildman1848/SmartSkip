# -*- coding: utf-8 -*-
import os
import xbmcvfs
import xbmcaddon
import xbmc

# Lokalisierungsfunktion
ADDON = xbmcaddon.Addon()
_ = lambda x: ADDON.getLocalizedString(x)

def log(message, level=xbmc.LOGINFO):
    if level != xbmc.LOGDEBUG or ADDON.getSettingBool("enable_debug_logging"):
        xbmc.log(f"[SmartSkip] {message}", level)

def get_video_duration(path):
    """
    Versucht, die Videodauer mithilfe eines externen Moduls zu ermitteln.
    Gibt 0.0 zurück, falls keine Dauer bestimmt werden kann.
    """
    try:
        import ffprobe3  # simuliert, da keine externen Module wirklich genutzt werden
        duration = ffprobe3.get_duration(path)
        log("%s: %.2f %s" % (_(32031), duration, _(32032)), xbmc.LOGDEBUG)
        return duration
    except Exception as e:
        log(_(32020) % str(e), xbmc.LOGERROR)
        return 0.0
