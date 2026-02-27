# KeySounds

KeySounds is a lightweight Python app that plays keyboard sound effects while you type.

## Features

- Plays random click sounds for regular keys
- Uses dedicated sounds for Space, Enter, and Backspace
- Uses low-latency pygame mixer settings for responsive playback

## Requirements

- Python 3.10+
- Windows

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

The app starts listening to keyboard input in the background. Press Ctrl + C in the terminal to stop it.

## Audio Files

Keep these files in the same folder as main.py:

- click1.wav
- click2.wav
- click3.wav
- space.wav
- enter.wav
- delete.wav

## Build EXE (Optional)

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

The output will be created in the dist folder.

## Contributing

Contributions are welcome. Feel free to open an issue or submit a pull request.

## License

This project is for personal and educational use. Add a LICENSE file if you plan to share it publicly.
