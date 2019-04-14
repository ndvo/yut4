import kivy
kivy.require('1.8.0')

from kivy.uix.screenmanager import *
from kivy.uix.modalview import ModalView
from kivy.uix.relativelayout import RelativeLayout
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.stencilview import StencilView
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import *
from kivy.graphics import *
from kivy.uix.togglebutton import ToggleButton
from kivy.animation import Animation

from kivy.core.audio import SoundLoader

from jnius import autoclass
from jnius import cast

import random
from random import shuffle
from functools import partial

import g
import utils as u
import ocanim as oa
#from basic_widgets import *

			

class titleScreen(Screen):
	"""As the name suggests, this is the title screen."""
	
	def __init__(self,name,**kwargs):
		"""The __init__ function runs at the beginning of the application and not every time the screen is presented. This means only static elements can be created here, alongside with declaring variables and stubs."""
		super(titleScreen,self).__init__(**kwargs)

		# All screens must have a name so we can access it
		self.name = name
		
		# Every temporary widget, must be placed in a list, so they can be removed on the on_leave function. The buttons are not actually added to it (they are directly handled by the on_called and on_leave function. So the temporary list is just a reference for a possible future addition.
		self.temporary_widgets = []


		with self.canvas:
			# lets draw a semi-transparent red square
			Color(1,1,1,1, mode='rgba')
			Rectangle(pos=(0,0), size=g.screen_size)

		# Loading component images
		back_image = u.mImage(source = g.IMG_BACKGROUND, size = (433,769), rpos = (0,0))
		main_image = u.mImage(source = g.IMG_TITLE_SCENE, size = (433,769), rpos = (0,0))
		
		self.add_widget(back_image)
		self.add_widget(main_image)

		
		version_count_string =  u.get_string('title', 'teste')+ ' ' + g.current_version_human + ' ' + g.current_resolution_human
		self.version_count = Label( text = version_count_string, font_name = g.FONT_CB, font_size = 18*g.scale, color = g.COLOR_WHITE, pos = (0,-115*g.scale) )
		self.add_widget(self.version_count)
		
		self.buttons = []
			
	def remove_image(self, image_to_remove, arg1=None ):
		self.remove_widget( image_to_remove )
	
	def on_pre_enter(self):
		btn_play = titleButton(btn_id = 'play', appearance = 1,  rpos = (0,68))
		btn_learn = titleButton(btn_id = 'learn', appearance = 2, rpos = (0,-2))	
		btn_more = titleButton(btn_id = 'more', appearance = 1,  rpos = (0,-72))
		
		self.create_buttons_2( btn_play, btn_learn, btn_more )
		
	def create_buttons_2(self, btn1, btn2, btn3):
		self.buttons = [btn1,btn2,btn3]
		Clock.schedule_once( partial ( self.create_buttons_2_extra, btn1 ), 0.5 )
		Clock.schedule_once( partial ( self.create_buttons_2_extra, btn2 ), 0.6 )
		Clock.schedule_once( partial ( self.create_buttons_2_extra, btn3 ), 0.7 )
		
	def create_buttons_2_extra(self, btn, arg1 = None):
		self.add_widget(btn)
		oa.pop( widget = btn, loops = 1 )

	def create_buttons(self, btn1, btn2, btn3, arg1 = None, arg2 = None, arg3 = None):
		if len(self.buttons) == 0:
			self.buttons.append(btn1)
			self.add_widget(btn1)
			#Clock.schedule_once( partial(self.create_buttons, btn1, btn2, btn3), 1.0 )
			oa.pop( widget = btn1, end_func = partial( self.create_buttons, btn1, btn2, btn3), loops = 1 )
		elif len(self.buttons) == 1:
			self.buttons.append(btn2)
			self.add_widget(btn2)
			oa.pop( widget = btn2, end_func = partial( self.create_buttons, btn1, btn2, btn3), loops = 1 )
			#Clock.schedule_once( partial(self.create_buttons, btn1, btn2, btn3), 1.0 )
		elif len(self.buttons) == 2:
			self.buttons.append(btn3)
			self.add_widget(btn3)
			oa.pop( widget = btn3, loops = 1 )
			#oa.pop( widget = btn3, end_func = partial( self.create_buttons, self, btn1, btn2, btn3), loops = 1 )

	def on_enter(self):
		g.sound_controller.music_type = 'title'
		g.ad_count += 1
		
	def on_pre_leave(self):
		self.purge_btns()
		g.sound_controller.play_sound(g.SOUND_SHEET)

	def on_leave(self):
		"""This functions will delete widgets inside the temporary_widgets_list and erase the buttons inside the button box. This function will run automatically when the screen is changed - calling it is not required."""
		# Removing temporary widgets
		for widget in self.temporary_widgets:
			self.remove_widget(widget)
		if g.manager.current_screen.name == 'main_screen':
			g.sound_controller.stop_music()
	
	def on_called(self):
		"""This function does two important things. First it checks if the player deservers the 'profile' milestone, giving or taking it depending on the completeness of the player's profile. It then creates the buttons that are available to the player."""
		pass
	
	def purge_btns(self):
		for btn in self.buttons:
			self.remove_widget(btn)
		self.buttons = []


class titleButton(Button):
	"""These are the buttons presented in the title screen. Their appearance and behavior are defined by the btn_id parameter."""
	
	def __init__(self,btn_id,appearance = 1, rpos = None, **kwargs):
		"""Based on the btn_id, let's prepare the button's appearance and behavior."""
		super(titleButton,self).__init__(**kwargs)
		self.name = btn_id
		self.text = u.get_string("title",btn_id)
		self.border = (0,0,0,0)
		self.background_normal = getattr(g,'IMG_TITLE_BTN'+str(appearance)+'_NORMAL')
		self.background_down = getattr(g,'IMG_TITLE_BTN'+str(appearance)+'_PRESS')
		# Set button behaviors
		self.bind(on_release = getattr(self,'click_'+btn_id))
		self.font_name = g.FONT_CR
		self.color = g.COLOR_BROWN
		self.size_hint = (None,None)
		self.size = [280*g.scale,60*g.scale]
		self.font_size = 28*g.scale
		if rpos != None:
			self.apply_relative_position(rpos)

	def apply_relative_position(self, rpos):
		"""This function will center the image on a given rpos."""
		x_pos = g.screen_size[0]/2 - self.size[0]/2 + rpos[0]*g.scale
		y_pos = g.screen_size[1]/2 - self.size[1]/2 + rpos[1]*g.scale
		self.pos = [x_pos, y_pos]
		
	def click_play(self, btn_object = None):
		""" When clicking the play button."""
		title_screen = self.parent
		g.sound_controller.play_sound(g.SOUND_BUTTON)
		for button in title_screen.buttons:
			title_screen.remove_widget(button)
		title_screen.purge_btns()
		btn_solo = titleButton(btn_id = 'solo', appearance = 2,  rpos = (0,68))
		btn_two = titleButton(btn_id = 'two', appearance = 1,  rpos = (0,-2))
		btn_back = titleButton(btn_id = 'back', appearance = 3,  rpos = (0,-72))
		title_screen.buttons = [ btn_solo, btn_two, btn_back ]
		title_screen.add_widget(btn_solo)
		title_screen.add_widget(btn_two)
		title_screen.add_widget(btn_back)
		
	def click_learn(self, btn_object = None):
		""" When clicking the play button."""
		g.sound_controller.play_sound(g.SOUND_BUTTON)
		g.manager.current = 'tutorial'
		
	def click_more(self, btn_object = None):
		""" When clicking the play button."""
		g.sound_controller.play_sound(g.SOUND_BUTTON)
		g.manager.current = 'more'

	def click_solo(self, btn_object = None):
		""" When clicking the play button."""
		g.sound_controller.play_sound(g.SOUND_BUTTON)
		g.players = 1
		g.manager.current = g.screens['main'].name
		
	def click_two(self, btn_object = None):
		""" When clicking the play button."""
		g.sound_controller.play_sound(g.SOUND_BUTTON)
		g.players = 2
		g.manager.current = g.screens['main'].name
		
	def click_back(self, btn_object = None):
		""" When clicking the play button."""
		title_screen = self.parent
		g.sound_controller.play_sound(g.SOUND_BUTTON)
		for button in title_screen.buttons:
			title_screen.remove_widget(button)
		title_screen.purge_btns()
		btn_play = titleButton(btn_id = 'play', appearance = 1,  rpos = (0,68))
		btn_learn = titleButton(btn_id = 'learn', appearance = 2,  rpos = (0,-2))
		btn_more = titleButton(btn_id = 'more', appearance = 1,  rpos = (0,-72))
		title_screen.buttons = [ btn_play, btn_learn, btn_more ]
		title_screen.add_widget(btn_play)
		title_screen.add_widget(btn_learn)
		title_screen.add_widget(btn_more)
