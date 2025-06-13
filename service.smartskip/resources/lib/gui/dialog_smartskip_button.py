# -*- coding: utf-8 -*-
import xbmcgui
import xbmc
import time
import threading

class SmartSkipButton(xbmcgui.WindowXMLDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = "Segment"
        self.timeout = 5
        self.should_skip = False
        self._start_time = None
        self._fade_thread = None
        self._stop = False

    def set_segment_label(self, label):
        self.label = label

    def set_timeout(self, timeout):
        self.timeout = timeout

    def onInit(self):
        xbmc.log("[SmartSkipButton] Init – Starte Button-Anzeige", xbmc.LOGINFO)
        self._start_time = time.time()
        try:
            label_control = self.getControl(101)  # Label
            label_control.setLabel(f"{self.label} " + xbmc.getLocalizedString(30017))  # z. B. "Intro überspringen"
        except Exception as e:
            xbmc.log(f"[SmartSkipButton] Fehler beim Setzen des Labels: {e}", xbmc.LOGERROR)

        self._fade_thread = threading.Thread(target=self._update_progress)
        self._fade_thread.start()

    def onClick(self, controlId):
        xbmc.log(f"[SmartSkipButton] Klick erkannt auf Control-ID: {controlId}", xbmc.LOGDEBUG)
        if controlId == 100:
            self.should_skip = True
            self._stop = True
            self.close()

    def onAction(self, action):
        if action.getId() in (xbmcgui.ACTION_PREVIOUS_MENU, xbmcgui.ACTION_NAV_BACK):
            xbmc.log("[SmartSkipButton] Benutzer hat zurück gedrückt", xbmc.LOGDEBUG)
            self._stop = True
            self.close()

    def _update_progress(self):
        fade_duration = self.timeout

        try:
            fade_bar = self.getControl(1002)  # Fortschrittsbalken
            total_width = fade_bar.getWidth()
            xbmc.log(f"[SmartSkipButton] Starte Fortschrittsanzeige – Breite: {total_width}", xbmc.LOGDEBUG)
        except Exception as e:
            xbmc.log(f"[SmartSkipButton] Fehler beim Zugriff auf Fortschrittsbalken: {e}", xbmc.LOGERROR)
            return

        while not self._stop:
            elapsed = time.time() - self._start_time
            if elapsed >= fade_duration:
                break

            progress = max(0.0, 1.0 - (elapsed / fade_duration))
            current_width = int(total_width * progress)

            try:
                fade_bar.setWidth(current_width)
                xbmc.log(f"[SmartSkipButton] Fortschritt: {progress:.2f}, Breite: {current_width}", xbmc.LOGDEBUG)
            except Exception as e:
                xbmc.log(f"[SmartSkipButton] Fehler beim Setzen der Breite: {e}", xbmc.LOGERROR)

            xbmc.sleep(100)

        if not self.should_skip:
            xbmc.log("[SmartSkipButton] Timeout erreicht – schließe Dialog", xbmc.LOGDEBUG)
            self.close()
