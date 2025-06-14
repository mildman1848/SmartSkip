<p align="center">
  <img src="icon.png" alt="SmartSkip Icon" width="120" />
</p>

# README.de.md

# SmartSkip

**SmartSkip** ist ein Kodi-Dienst-Addon für **Kodi Omega** und höher, das automatisch oder manuell Serien- und Filmsegmente wie **Intros**, **Recaps**, **Outros**, **Vorschauen** und **Credits** überspringt – basierend auf EDL-Dateien. Die Segmenterkennung erfolgt durch das vollständig integrierte Tool [`intro-skipper`](https://github.com/intro-skipper/intro-skipper), ohne externe Python-Abhängigkeiten.

---

## ✨ Features

- 🎮 Automatisches oder manuelles Überspringen von:
  - Intros
  - Recaps
  - Outros
  - Vorschauen
  - Credits
- 🧠 Vollständig eingebetteter `intro-skipper` für EDL-Erzeugung
- 💕 Dialog mit Überspringen-Button während der Wiedergabe
- 📁 Unterstützung für EDL-Erstellung bei Bibliotheks-Scan oder manuell
- 🌐 Sprachunterstützung: Englisch & Deutsch
- 🎨 Fortschrittsanzeige, automatische Ausblendung, Skin-kompatibles UI
- 🧹 Keine extern installierten Python-Pakete notwendig

---

## 🔧 Installation

> **Voraussetzung:** Kodi **Omega** oder neuer

1. Repository klonen oder als ZIP herunterladen:
   ```bash
   git clone https://github.com/mildman1848/SmartSkip.git
   ```
2. In Kodi:
   - Gehe zu **Addons > Aus ZIP-Datei installieren**
   - Wähle das heruntergeladene Verzeichnis oder ZIP-Archiv

---

## ⚙️ Konfiguration

- **EDL Mode:**
  - *Basic Detection* (schnell, heuristisch)
  - *Full intro-skipper* (präzise Analyse)
- **Button-Anzeigezeit (Timeout)**
- **Sprachwahl (EN/DE)**

---

## 📁 Projektstruktur

```
SmartSkip/
├── addon.xml
├── default.py
├── lib/
│   ├── edl_handler.py
│   ├── gui/
│   │   └── dialog_smartskip_button.py
│   ├── player_monitor.py
│   ├── settings_handler.py
│   └── video.py
├── resources/
│   ├── language/
│   │   ├── resource.language.en_gb/
│   │   │   └── strings.po
│   │   └── resource.language.de_de/
│   │       └── strings.po
│   ├── lib/intro_skipper/
│   │   └── ... (eingebettetes Tool)
│   └── skins/default/1080i/
│       └── DialogSmartSkipButton.xml
├── LICENSE.txt
├── CHANGELOG.md
├── README.md
├── README.de.md
└── README.en.md
```

---

## 📜 Lizenz

```
SmartSkip - Kodi Smart Skipping Service

Copyright (C) 2025 mildman1848

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

See https://www.gnu.org/licenses/gpl-3.0.html for details.
```

---

## 🤝 Mitwirken

Pull Requests, Ideen und Bugmeldungen sind herzlich willkommen.📁 Repository: [https://github.com/mildman1848/SmartSkip](https://github.com/mildman1848/SmartSkip)

> **Hinweis:** Kodi® ist eine Marke der XBMC Foundation. Dieses Projekt steht in keiner offiziellen Verbindung zur XBMC Foundation oder Kodi.