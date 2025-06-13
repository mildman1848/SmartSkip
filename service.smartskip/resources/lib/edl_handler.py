# -*- coding: utf-8 -*-
import os
import xbmcvfs
import xbmc

def parse_edl_file(video_path):
    edl_path = os.path.splitext(video_path)[0] + ".edl"
    segments = []

    if not xbmcvfs.exists(edl_path):
        return segments

    try:
        with xbmcvfs.File(edl_path) as f:
            lines = f.read().splitlines()
            for line in lines:
                line = line.strip()
                if not line:
                    continue

                # Kommentar mit Segmenttyp extrahieren (z. B. #intro)
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
                    except ValueError:
                        continue
    except Exception as e:
        xbmc.log(f"[SmartSkip] Fehler beim Lesen der EDL-Datei: {str(e)}", xbmc.LOGERROR)

    return segments


def should_skip_automatically(skip_mode):
    """
    Entscheidet, ob ein Segment automatisch übersprungen werden soll,
    basierend auf dem Skip-Modus.
    Erwartet: 'Automatic' / 'Manual' (string) oder 0 / 1 (int).
    """
    # Normalisieren
    if isinstance(skip_mode, int):
        mode_str = {0: "Automatic", 1: "Manual"}.get(skip_mode, "Unknown")
    elif isinstance(skip_mode, str):
        # Strip + Capitalize für mehr Toleranz gegenüber Benutzereingaben
        mode_str = skip_mode.strip().capitalize()
    else:
        mode_str = "Unknown"

    if mode_str == "Automatic":
        xbmc.log("[SmartSkip] Skip Mode: Automatic", xbmc.LOGINFO)
        return True
    elif mode_str == "Manual":
        xbmc.log("[SmartSkip] Skip Mode: Manual", xbmc.LOGINFO)
        return False
    else:
        xbmc.log(f"[SmartSkip] Unbekannter Skip-Modus: {skip_mode}, verwende 'Manual'", xbmc.LOGWARNING)
        return False
