# -*- coding: utf-8 -*-
import xbmc
import xbmcaddon
import traceback

from resources.lib.player_monitor import SmartSkipPlayer
from resources.lib.settings_handler import get_settings

# Addon-Instanz und Logging-Tag definieren
addon = xbmcaddon.Addon()
LOG_TAG = f"[{addon.getAddonInfo('name')} {addon.getAddonInfo('version')}]"

def log(msg, level=xbmc.LOGDEBUG):
    """
    Protokolliert eine Nachricht mit dem Kodi-Logging-System.

    :param msg: Die zu protokollierende Nachricht
    :param level: Das Log-Level
    """
    try:
        debug_enabled = addon.getSettingBool("enable_debug_logging")
    except Exception:
        debug_enabled = addon.getSetting("enable_debug_logging") == "true"

    if level != xbmc.LOGDEBUG or debug_enabled:
        xbmc.log(f"{LOG_TAG} {msg}", level)

if __name__ == "__main__":
    # Service-Startmeldung
    log(addon.getLocalizedString(32000), xbmc.LOGINFO)  # "Service gestartet"

    try:
        # Einstellungen aus settings_handler abrufen
        settings = get_settings()
        log(addon.getLocalizedString(32004), xbmc.LOGDEBUG)  # "Einstellungen geladen"
        log(f"[Debug] Aktuelle Einstellungen: {settings}", xbmc.LOGDEBUG)

        # SmartSkipPlayer mit geladenen Einstellungen initialisieren
        player = SmartSkipPlayer(settings)
        log(addon.getLocalizedString(32001), xbmc.LOGDEBUG)  # "SmartSkipPlayer initialisiert"

        # Monitor-Instanz erstellen, um Service-Lifecycle zu beobachten
        monitor = xbmc.Monitor()
        log(addon.getLocalizedString(32002), xbmc.LOGDEBUG)  # "Monitor gestartet, Warte auf Beenden..."

        # Warte auf Beenden-Signal von Kodi
        while not monitor.abortRequested():
            xbmc.sleep(1000)

        # Service wurde beendet
        log(addon.getLocalizedString(32003), xbmc.LOGINFO)  # "Service beendet"

    except Exception as e:
        # Allgemeiner Fehler-Logger mit vollständigem Stacktrace
        log(f"{addon.getLocalizedString(32005)}: {str(e)}", xbmc.LOGERROR)  # "Fehler im Service"
        log(traceback.format_exc(), xbmc.LOGERROR)
