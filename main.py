import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.config import Config
from kivy.base import EventLoop

from kivy.core.window import Window
from kivy.metrics import Metrics
import xml.etree.ElementTree as ET

from jnius import autoclass
from jnius import cast
import kivy.utils

import kivy.uix.screenmanager as screenmanager
import g
import utils
import screen_main 
import screen_title
import screen_splash
import screen_tutorial
import screen_more


Window.clearcolor = (1, 1, 1, 1)

if kivy.utils.platform == 'android':
	from kivy.utils import platform
	from kivy.logger import Logger
	from kivy.ext import load
	from jnius import autoclass, cast

class gameApp(App):
	"""This is the main class. It sets basic parameters when initializing, then calls the main layout."""

	def build(self):
		"""Setting initial parameters and calls for creation of main layout."""

		# Prepare to parse strings from xml
		g.xml_str_tree = ET.parse(g.xml_path)
		g.xml_root = g.xml_str_tree.getroot()

		self.cache_ads()

		self.generate_screens()
		
		# This will allow us to intercept the ESC/BACK key
		EventLoop.window.bind(on_keyboard=self.hook_keyboard)
		
		g.app = thisApp
		
		return g.manager
	
	def cache_ads(self):
		if g.do_cache_ads:
			g.do_cache_ads = False
			if str(kivy.utils.platform) == 'android':
				g.is_android = True
				g.fix_string = "Ads were cached."
			
				g.Ads = autoclass('com.purplebrain.adbuddiz.sdk.AdBuddiz')
				g.Ads.setPublisherKey( g.adbuddiz_code )
				
				python_activity = autoclass( 'org.renpy.android.PythonActivity' )
				current_activity = cast( 'android.app.Activity', python_activity.mActivity )
				
				g.Ads.cacheAds( current_activity )
						
			else:
				g.is_android = False
				print 'Not android: we do not cache ads.'
	
	def open_settings(self):
		pass
	
	def hook_keyboard(self, window, key, *largs):   
		"""This function intercepts the keyboard. We use it to add confirmation popups."""
		
		if key == 27:
			# Prevent two modal screens from opening on top of each other
			if g.modal_screen:
				pass
			else:
				g.modal_screen = True
				popup = confirmExit()
				popup.open()
				
		return True

	def on_pause(self):
		return True

	def on_resume(self):
		pass
	
	def on_stop(self):
		pass

	def generate_screens(self):
		"""Screens are generated here, in the start of the program. Initializing them will run __init__ as usual, then added to g.screen. As it happens, some things cannot be made in advance, because they depend on user input during the program (e.g. adding option buttons). These are handled in the function 'pre_enter', present in every screen."""

		g.manager = screenmanager.ScreenManager(transition = screenmanager.SwapTransition())

		g.screens['splash'] = screen_splash.splashScreen(name = 'splash_screen')
		g.screens['main'] = screen_main.mainScreen(name = 'main_screen')
		g.screens['title'] = screen_title.titleScreen(name = 'title_screen')
		g.screens['tutorial'] = screen_tutorial.tutorialScreen(name = 'tutorial')
		g.screens['more'] = screen_more.moreScreen(name = 'more')

		g.manager.add_widget(g.screens['splash'])
		g.manager.add_widget(g.screens['main'])
		g.manager.add_widget(g.screens['title'])
		g.manager.add_widget(g.screens['tutorial'])
		g.manager.add_widget(g.screens['more'])

thisApp = None

if __name__ == '__main__':
	
	if kivy.utils.platform == 'android':
		g.screen_size = Window.size

	elif kivy.utils.platform == 'linux':
		Config.set('graphics','width',g.screen_size[0])
		Config.set('graphics','height',g.screen_size[1])
		Config.set('graphics','resizable',0)
		Config.write()
		
	utils.set_scale()
	thisApp = gameApp()
	thisApp.run()

