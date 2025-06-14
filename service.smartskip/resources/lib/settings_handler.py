# -*- coding: utf-8 -*-
import xbmcaddon
import importlib
import sys
import xbmc

# Lokalisierungsfunktion holen
ADDON = xbmcaddon.Addon()
_ = lambda x: ADDON.getLocalizedString(x)

def get_settings():
    """
    Liest und verarbeitet die SmartSkip-Addon-Einstellungen.
    Dies umfasst die Konvertierung des Skip-Modus und das Abrufen
    der Booleschen Optionen zum Aktivieren von Segment-Sprüngen.
    """
    # Addon-Modul neu laden, falls es bereits im Speicher ist (z. B. bei Settings-Wechseln)
    if "xbmcaddon" in sys.modules:
        importlib.reload(sys.modules["xbmcaddon"])

    addon = xbmcaddon.Addon(id='service.smartskip')

    # Skip-Modus abrufen und zu lesbarem String konvertieren
    skip_mode_index = addon.getSetting("skip_mode")
    xbmc.log(f"[SmartSkip] getSetting('skip_mode') = {skip_mode_index}", xbmc.LOGDEBUG)

    skip_mode_map = {
        "0": "Automatic",
        "1": "Manual"
    }
    skip_mode = skip_mode_map.get(skip_mode_index, "Manual")

    # Debug-Logging-Einstellung
    debug_logging = addon.getSettingBool("enable_debug_logging")
    if debug_logging:
        xbmc.log(_(32004), xbmc.LOGDEBUG)  # "Settings loaded"

    # Alle Einstellungen zusammenstellen
    return {
        "skip_mode": skip_mode,
        "enable_intro_skip": addon.getSettingBool("enable_intro_skip"),
        "enable_recap_skip": addon.getSettingBool("enable_recap_skip"),
        "enable_outro_skip": addon.getSettingBool("enable_outro_skip"),
        "enable_preview_skip": addon.getSettingBool("enable_preview_skip"),
        "enable_credits_skip": addon.getSettingBool("enable_credits_skip"),
        "enable_debug_logging": debug_logging
    }
