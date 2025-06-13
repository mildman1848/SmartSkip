# -*- coding: utf-8 -*-
import xbmcaddon
import importlib
import sys
import xbmc

def get_settings():
    # Addon-Modul neu laden, um Settings-Aktualisierungen sicherzustellen
    if "xbmcaddon" in sys.modules:
        importlib.reload(sys.modules["xbmcaddon"])

    addon = xbmcaddon.Addon(id='plugin.video.smartskip')

    skip_mode_index = addon.getSetting("skip_mode")
    xbmc.log(f"[SmartSkip] getSetting('skip_mode') = {skip_mode_index}", xbmc.LOGDEBUG)

    skip_mode_map = {
        "0": "Automatic",
        "1": "Manual"
    }
    skip_mode = skip_mode_map.get(skip_mode_index, "Manual")

    return {
        "skip_mode": skip_mode,
        "enable_intro_skip": addon.getSettingBool("enable_intro_skip"),
        "enable_recap_skip": addon.getSettingBool("enable_recap_skip"),
        "enable_outro_skip": addon.getSettingBool("enable_outro_skip"),
        "enable_preview_skip": addon.getSettingBool("enable_preview_skip"),
        "enable_credits_skip": addon.getSettingBool("enable_credits_skip")
    }
