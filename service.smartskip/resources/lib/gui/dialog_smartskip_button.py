# -*- coding: utf-8 -*-
import xbmcgui
import xbmc
import time
import threading
import xbmcaddon

# Lokalisierung vorbereiten
ADDON = xbmcaddon.Addon()
_ = lambda x: ADDON.getLocalizedString(x)

def is_debug_enabled():
    try:
        return ADDON.getSettingBool("enable_debug_logging")
    except Exception:
        return False

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
        xbmc.log("[SmartSkip] %s" % _(32021), xbmc.LOGINFO)
        self._start_time = time.time()
        try:
            label_control = self.getControl(101)
            label_control.setLabel(f"{self.label} " + xbmc.getLocalizedString(30017))
        except Exception as e:
            xbmc.log("[SmartSkip] %s" % (_(32011) % str(e)), xbmc.LOGERROR)

        self._fade_thread = threading.Thread(target=self._update_progress)
        self._fade_thread.start()

    def onClick(self, controlId):
        if is_debug_enabled():
            xbmc.log("[SmartSkip] %s %d" % (_(32022), controlId), xbmc.LOGDEBUG)
        if controlId == 100:
            self.should_skip = True
            self._stop = True
            self.close()

    def onAction(self, action):
        if action.getId() in (xbmcgui.ACTION_PREVIOUS_MENU, xbmcgui.ACTION_NAV_BACK):
            if is_debug_enabled():
                xbmc.log("[SmartSkip] %s" % _(32023), xbmc.LOGDEBUG)
            self._stop = True
            self.close()

    def _update_progress(self):
        fade_duration = self.timeout

        try:
            fade_bar = self.getControl(1002)
            total_width = fade_bar.getWidth()
            if is_debug_enabled():
                xbmc.log("[SmartSkip] %s %d" % (_(32024), total_width), xbmc.LOGDEBUG)
        except Exception as e:
            xbmc.log("[SmartSkip] %s" % (_(32025) % str(e)), xbmc.LOGERROR)
            return

        while not self._stop:
            elapsed = time.time() - self._start_time
            if elapsed >= fade_duration:
                break

            progress = max(0.0, 1.0 - (elapsed / fade_duration))
            current_width = int(total_width * progress)

            try:
                fade_bar.setWidth(current_width)
                if is_debug_enabled():
                    xbmc.log("[SmartSkip] %s: %.2f, %s: %d" % (_(32029), progress, _(32030), current_width), xbmc.LOGDEBUG)
            except Exception as e:
                xbmc.log("[SmartSkip] %s" % (_(32027) % str(e)), xbmc.LOGERROR)

            xbmc.sleep(100)

        if not self.should_skip:
            if is_debug_enabled():
                xbmc.log("[SmartSkip] %s" % _(32028), xbmc.LOGDEBUG)
            self.close()
