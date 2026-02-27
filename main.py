import os
import random
import sys

import pygame
from pynput import keyboard

pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=512)


def get_current_dir():
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


def load_sounds(base_dir):
    generic_clicks = []
    special_keys = {}

    for index in range(1, 4):
        path = os.path.join(base_dir, f"click{index}.wav")
        if os.path.exists(path):
            generic_clicks.append(pygame.mixer.Sound(path))

    files = {
        "space": "space.wav",
        "enter": "enter.wav",
        "backspace": "delete.wav",
    }
    for key_name, file_name in files.items():
        path = os.path.join(base_dir, file_name)
        if os.path.exists(path):
            special_keys[key_name] = pygame.mixer.Sound(path)

    return generic_clicks, special_keys


def create_handlers(generic_clicks, special_keys):
    pressed_keys = set()

    def on_press(key):
        if key in pressed_keys:
            return
        pressed_keys.add(key)

        sound = None
        if key == keyboard.Key.space and "space" in special_keys:
            sound = special_keys["space"]
        elif key == keyboard.Key.enter and "enter" in special_keys:
            sound = special_keys["enter"]
        elif key == keyboard.Key.backspace and "backspace" in special_keys:
            sound = special_keys["backspace"]
        elif generic_clicks:
            sound = random.choice(generic_clicks)

        if sound is not None:
            try:
                sound.set_volume(random.uniform(0.6, 1.0))
                sound.stop()
                sound.play()
            except pygame.error:
                pass

    def on_release(key):
        if key in pressed_keys:
            pressed_keys.remove(key)

    return on_press, on_release


def main():
    pygame.mixer.init()
    pygame.mixer.set_num_channels(32)

    base_dir = get_current_dir()
    generic_clicks, special_keys = load_sounds(base_dir)

    if not generic_clicks and not special_keys:
        print("Warning: No sound files were found. The app will continue listening.")

    on_press, on_release = create_handlers(generic_clicks, special_keys)
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":
    main()