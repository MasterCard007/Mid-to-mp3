from setuptools import setup, find_packages

setup(
    name='midi_to_mp3_converter',
    version='1.0.0',
    description='A script to convert MIDI files to MP3 format using timidity and ffmpeg.',
    author='MasterCard007',
    author_email='',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'mid_to_mp3=mid_to_mp3:main',
        ],
    },
)
