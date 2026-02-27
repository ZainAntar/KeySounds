# 🎹 KeySounds

KeySounds is a lightweight Python app that plays keyboard sound effects while you type.

## ✨ Features

- 🔊 Random click sounds for regular keys
- ⌨️ Dedicated sounds for `Space`, `Enter`, and `Backspace`
- ⚡ Low-latency `pygame.mixer` setup for responsive playback

## 🖥️ Requirements

- Python 3.10+
- Windows

## 🚀 Quick Start

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

The app starts listening to keyboard input in the background.
Press `Ctrl + C` in the terminal to stop it.

## 🎵 Audio Files

Keep these files in the same folder as `main.py`:

- `click1.wav`
- `click2.wav`
- `click3.wav`
- `space.wav`
- `enter.wav`
- `delete.wav`

## 📦 Build EXE (Optional)

```bash
pip install pyinstaller
pyinstaller --noconfirm --windowed --onefile \
  --add-data "click1.wav;." \
  --add-data "click2.wav;." \
  --add-data "click3.wav;." \
  --add-data "space.wav;." \
  --add-data "enter.wav;." \
  --add-data "delete.wav;." \
  main.py
```

The output is generated in the `dist` folder.

## 🤝 Contributing

Contributions are welcome. Feel free to open an issue or submit a pull request.

## 📄 License

This project is currently for personal and educational use.
If you plan to publish it publicly, add a `LICENSE` file (for example: MIT).

## 📫 Contatct
antar.zain1@gmail.com
