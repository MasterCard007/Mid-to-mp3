# MIDI to MP3 Converter

This Python script converts all `.mid` files in the current directory to `.mp3` format using `timidity` and `ffmpeg`. The converted `.mp3` files are saved in a new folder called `MP3`.

## Requirements

- Python 3.11
- `timidity`
- `ffmpeg`

## Download a SoundFont file (`.sf2`)**:
    - Ensure you download a SoundFont file that suits your needs.
    - Place the downloaded `.sf2` file in the same directory as the script.# Installation

## Installation

First, ensure you have `timidity` and `ffmpeg` installed. You can install them using Homebrew:

```bash
brew install timidity
brew install ffmpeg
```

## Usage

Place the script in the same directory as your `.mid` files and run the script:

```bash
python mid_to_mp3.py
```

The script will convert all `.mid` files in the directory to `.mp3` and save them in the `MP3` folder.

## License

This project is licensed under the MIT License.
