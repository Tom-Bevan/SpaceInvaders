"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['main.py']
DATA_FILES = ['../graphics/extra.png', 
'../graphics/green.png', 
'../graphics/player.png',
'../graphics/red.png',
'../graphics/tv.png',
'../graphics/yellow.png',
'../font/Pixeled.ttf',
'../audio/laser.wav',
'../audio/music.wav',
'../audio/explosion.wav']
OPTIONS = {}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
