import pyglet

def load_sound_library():
	# Special code for Windows so we grab the proper avbin from our directory.
	# Otherwise hope the correct package is installed.
	import os
	if os.name == "nt":

		import sys
		is64bit = sys.maxsize > 2**32

		import site
		packages = site.getsitepackages()

		if is64bit:
			path = packages[0] + "/lib/site-packages/arcade/Win64/avbin"
		else:
			path = packages[0] + "/lib/site-packages/arcade/Win32/avbin"
	else:
		path = "avbin"

	pyglet.lib.load_library(path)
	pyglet.have_avbin=True

load_sound_library()

def load_sound(filename):
	"""
	Load a sound and get it ready to play.

	>>> import arcade
	>>> my_sound = arcade.load_sound("examples/sounds/laser1.ogg")
	>>> arcade.play_sound(my_sound)
	"""
	source = pyglet.media.load(filename, streaming=False)
	return source

def play_sound(sound):
	"""
	Play a previously loaded sound.
	"""
	sound.play()
