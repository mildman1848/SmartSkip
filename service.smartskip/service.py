# -*- coding: utf-8 -*-
import xbmc
from resources.lib.player_monitor import SmartSkipPlayer

if __name__ == "__main__":
    xbmc.log("[SmartSkip] Service gestartet", xbmc.LOGINFO)

    # Leere Einstellungen beim Initialisieren übergeben – sie werden später dynamisch geladen
    player = SmartSkipPlayer({})
    monitor = xbmc.Monitor()

    while not monitor.abortRequested():
        xbmc.sleep(1000)

    xbmc.log("[SmartSkip] Service beendet", xbmc.LOGINFO)
