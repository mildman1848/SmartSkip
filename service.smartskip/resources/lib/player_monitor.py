# -*- coding: utf-8 -*-
import xbmc
import xbmcgui
import xbmcvfs
import xbmcaddon
import os
from .edl_handler import parse_edl_file, should_skip_automatically
from .settings_handler import get_settings
from .gui.dialog_smartskip_button import SmartSkipButton

ADDON = xbmcaddon.Addon()
_ = lambda x: ADDON.getLocalizedString(x)

def log(message, level=xbmc.LOGINFO):
    if ADDON.getSettingBool("enable_debug_logging") or level != xbmc.LOGDEBUG:
        xbmc.log(f"[SmartSkip] {message}", level)


class SmartSkipMonitor(xbmc.Monitor):
    def __init__(self, player):
        super().__init__()
        self.player = player

    def onSettingsChanged(self):
        log(_(32006), xbmc.LOGINFO)  # Settings changed – refreshing
        self.player.settings = get_settings()


class SmartSkipPlayer(xbmc.Player):
    def __init__(self, settings):
        super().__init__()
        self.settings = settings
        self.edl_segments = []
        self.monitor = SmartSkipMonitor(self)
        self.skipped_segments = set()
        self.skip_auto = False

    def onAVStarted(self):
        log(_(32007), xbmc.LOGINFO)  # Playback started

        if not self.isPlayingVideo():
            return

        video_path = self.getPlayingFile()
        log(_(32008) % video_path, xbmc.LOGINFO)

        self.settings = get_settings()
        self.skip_auto = should_skip_automatically(self.settings.get("skip_mode"))
        self.edl_segments = parse_edl_file(video_path)
        self.skipped_segments = set()  # Reset segments per playback

        log(_(32009) % len(self.edl_segments), xbmc.LOGINFO)

        if not self.edl_segments:
            return

        log(_(32002), xbmc.LOGDEBUG)  # Monitoring started
        self._monitor_loop()

    def _monitor_loop(self):
        while not self.monitor.abortRequested() and self.isPlaying():
            try:
                time = self.getTime()

                for start, end, seg_type in self.edl_segments:
                    if (start, end) in self.skipped_segments:
                        continue
                    if not self._is_segment_enabled(seg_type):
                        continue
                    if not (start <= time < end if self.skip_auto else start <= time <= start + 1.5):
                        continue

                    label = self._get_label_for_type(seg_type)

                    if self.skip_auto:
                        log(_(30020) % (label, start, end), xbmc.LOGINFO)
                        self.seekTime(end)
                    else:
                        log(_(30021) % (label, start, end), xbmc.LOGINFO)

                        try:
                            timeout = int(self.settings.get("manual_skip_timeout", 3))
                            dialog = SmartSkipButton(
                                "DialogSmartSkipButton.xml",
                                ADDON.getAddonInfo("path"),
                                "default",
                                "1080i"
                            )
                            dialog.set_segment_label(label)
                            dialog.set_timeout(timeout)
                            dialog.doModal()
                            if dialog.should_skip:
                                log(_(30023) % (label, start, end), xbmc.LOGINFO)
                                self.seekTime(end)
                            dialog.close()
                            del dialog
                        except Exception as e:
                            log(_(32011) % str(e), xbmc.LOGERROR)

                    self.skipped_segments.add((start, end))
                    break

                xbmc.sleep(500 if not self.skip_auto else 1000)

            except Exception as e:
                log(_(32012) % str(e), xbmc.LOGERROR)
                break

    def _is_segment_enabled(self, seg_type):
        seg_type = (seg_type or "unknown").lower()
        return {
            "intro": self.settings.get("enable_intro_skip", True),
            "recap": self.settings.get("enable_recap_skip", True),
            "outro": self.settings.get("enable_outro_skip", True),
            "preview": self.settings.get("enable_preview_skip", True),
            "credits": self.settings.get("enable_credits_skip", True),
            "unknown": False
        }.get(seg_type, False)

    def _get_label_for_type(self, seg_type):
        seg_type = (seg_type or "unknown").lower()
        labels = {
            "intro": _(30011),
            "recap": _(30012),
            "outro": _(30013),
            "preview": _(30014),
            "credits": _(30015),
            "unknown": _(30016)
        }
        return labels.get(seg_type, seg_type.capitalize())

    def onPlayBackEnded(self):
        log(_(32013), xbmc.LOGINFO)

    def onPlayBackStopped(self):
        log(_(32014), xbmc.LOGINFO)

    def onPlayBackError(self):
        log(_(32015), xbmc.LOGERROR)  # Playback error
