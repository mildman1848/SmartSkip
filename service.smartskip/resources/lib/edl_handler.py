# -*- coding: utf-8 -*-
import os
import xbmcvfs
import xbmc
import xbmcaddon

# Addon-Instanz und Logging-Tag
addon = xbmcaddon.Addon()
LOG_TAG = f"[{addon.getAddonInfo('name')} {addon.getAddonInfo('version')}]"


def log(msg, level=xbmc.LOGDEBUG):
    try:
        debug_enabled = addon.getSettingBool("enable_debug_logging")
    except Exception:
        debug_enabled = addon.getSetting("enable_debug_logging") == "true"

    if level != xbmc.LOGDEBUG or debug_enabled:
        xbmc.log(f"{LOG_TAG} {msg}", level)


def parse_edl_file(video_path):
    """
    Liest und parst eine EDL-Datei zum gegebenen Video.

    Gibt eine Liste von Segmenten zurück: (start, end, seg_type)
    """
    edl_path = os.path.splitext(video_path)[0] + ".edl"
    segments = []

    if not xbmcvfs.exists(edl_path):
        log(addon.getLocalizedString(33010) % edl_path, xbmc.LOGDEBUG)  # "Keine EDL-Datei gefunden: %s"
        return segments

    try:
        with xbmcvfs.File(edl_path) as f:
            lines = f.read().splitlines()
            for line in lines:
                line = line.strip()
                if not line:
                    continue

                # Kommentar mit Segmenttyp extrahieren (z. B. #intro)
                if "#" in line:
                    line, seg_type = line.split("#", 1)
                    seg_type = seg_type.strip().lower()
                else:
                    seg_type = "unknown"

                parts = line.strip().split()
                if len(parts) >= 2:
                    try:
                        start = float(parts[0])
                        end = float(parts[1])
                        segments.append((start, end, seg_type))
                        log(addon.getLocalizedString(33011) % (seg_type, start, end), xbmc.LOGDEBUG)  # "Segment erkannt: %s (%.1f → %.1f)"
                    except ValueError:
                        log(addon.getLocalizedString(33012) % line, xbmc.LOGWARNING)  # "Ungültige EDL-Zeile: %s"
                        continue
    except Exception as e:
        log(addon.getLocalizedString(33013) % str(e), xbmc.LOGERROR)  # "Fehler beim Lesen der EDL-Datei: %s"

    return segments


def should_skip_automatically(skip_mode):
    """
    Entscheidet, ob ein Segment automatisch übersprungen werden soll,
    basierend auf dem Skip-Modus ('Automatic' oder 'Manual').
    """
    if isinstance(skip_mode, int):
        mode_str = {0: "Automatic", 1: "Manual"}.get(skip_mode, "Unknown")
    elif isinstance(skip_mode, str):
        mode_str = skip_mode.strip().capitalize()
    else:
        mode_str = "Unknown"

    if mode_str == "Automatic":
        log(addon.getLocalizedString(33014), xbmc.LOGINFO)  # "Skip-Modus: Automatisch"
        return True
    elif mode_str == "Manual":
        log(addon.getLocalizedString(33015), xbmc.LOGINFO)  # "Skip-Modus: Manuell"
        return False
    else:
        log(addon.getLocalizedString(30033) % skip_mode, xbmc.LOGWARNING)  # "Warnung: Ungültiger Skip-Modus: %s"
        return False
