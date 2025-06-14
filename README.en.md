<p align="center">
  <img src="icon.png" alt="SmartSkip Icon" width="120" />
</p>

# SmartSkip

**SmartSkip** is a Kodi service add-on for **Kodi Omega** and newer that automatically or manually skips TV and movie segments such as **intros**, **recaps**, **outros**, **previews**, and **credits** – based on EDL files. Segment detection is powered by the fully embedded [`intro-skipper`](https://github.com/intro-skipper/intro-skipper) tool, with no external Python dependencies.

---

## ✨ Features

- 🎮 Automatically or manually skip:
  - Intros
  - Recaps
  - Outros
  - Previews
  - Credits
- 🧠 Fully embedded `intro-skipper` for generating EDLs
- 💕 Skipping dialog with interactive button during playback
- 📁 EDL creation supported during library scans or manually
- 🌐 Language support: English & German
- 🎨 Progress bar, auto-fade, skin-compatible UI
- 🧹 No external Python packages required

---

## 🔧 Installation

> **Requirement:** Kodi **Omega** or newer

1. Clone or download this repository:
   ```bash
   git clone https://github.com/mildman1848/SmartSkip.git
   ```
2. In Kodi:
   - Go to **Add-ons > Install from ZIP file**
   - Select the downloaded folder or ZIP archive

---

## ⚙️ Configuration

- **EDL Mode:**
  - *Basic Detection* (fast, heuristic)
  - *Full intro-skipper* (precise analysis)
- **Button display timeout**
- **Language selection (EN/DE)**

---

## 📁 Project Structure

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
│   │   └── ... (embedded tool)
│   └── skins/default/1080i/
│       └── DialogSmartSkipButton.xml
├── LICENSE.txt
├── CHANGELOG.md
├── README.md
├── README.de.md
└── README.en.md
```

---

## 📜 License

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

## 🤝 Contributing

Pull requests, ideas, and bug reports are very welcome.\
📁 Repository: [https://github.com/mildman1848/SmartSkip](https://github.com/mildman1848/SmartSkip)

> **Note:** Kodi® is a trademark of the XBMC Foundation. This project is not affiliated with the XBMC Foundation or Kodi.
