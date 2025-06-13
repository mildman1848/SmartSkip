# -*- coding: utf-8 -*-
def detect_heuristic_segments(duration):
    segments = []
    # Beispiel: Letzte 30 Sekunden = Credits
    if duration > 60:
        segments.append((duration - 30, duration))
    return segments
