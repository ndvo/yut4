import kivy
kivy.require('1.8.0')

from kivy.uix.screenmanager import *
from kivy.uix.modalview import ModalView
from kivy.uix.relativelayout import RelativeLayout
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.stencilview import StencilView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.animation import *
from kivy.graphics import *

from functools import partial
import random
from random import shuffle
from math import sqrt

import g
import utils as u
import ocanim as oa
import pieces

class mainScreen(Screen):
	"""As the name suggests, this is the title screen."""
	
	def __init__(self, name, **kwargs):
		"""The __init__ function runs at the beginning of the
		application and not every time the screen is presented. This
		means only static elements can be created here, alongside with
		declaring variables and stubs."""
		super(mainScreen,self).__init__(**kwargs)
		
		# All screens must have a name so we can access it
		self.name = name
		
		with self.canvas:
			Color(1,1,1)
			Rectangle( pos= (0,0), size = g.screen_size )
		
		# Every temporary widget, must be placed in a list, so they can
		# be removed on the on_leave function. The buttons are not
		# actually added to it (they are directly handled by the
		# on_called and on_leave function. So the temporary list is
		# just a reference for a possible future addition.
		self.temporary_widgets = []
		self.add_widget(Image(source='res/drawable/board.png'))
		self.add_widget(Label(text="vaca", font_size='40sp', color=(0,0,0,1)))
		self.add_widget(pieces.Piece(board=self,player=0))

		
	def on_pre_leave(self):
		pass
		
	def on_leave(self):
		"""This functions will delete widgets inside the
		temporary_widgets_list and erase the buttons inside the button
		box. This function will run automatically when the screen is
		changed - calling it is not required."""
		
		# Removing temporary widgets
		for widget in self.temporary_widgets:
			self.remove_widget(widget)

	def on_pre_enter(self):
		"""This function will create the objects that can't be recycled
		between the games, such as the pieces. These elements will be
		placed in a temporary list, so they are erased when we leave
		this screen."""
		pass
			
	def on_enter(self):
		pass

	def set_arrows(self, piece):
		pass


