import kivy
kivy.require('1.8.0')


from kivy.uix.screenmanager import *
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.clock import Clock
from kivy.animation import *
from kivy.uix.stencilview import StencilView

from jnius import autoclass
from jnius import cast

import g
import utils as u

import webbrowser


#if g.is_android:
import kivy.utils
if kivy.utils.platform == 'android':
	from kivy.utils import platform
	from kivy.logger import Logger
	from kivy.ext import load
	from jnius import autoclass, cast

class moreScreen(Screen):
	def __init__(self,name,**kwargs):
		super(moreScreen,self).__init__(**kwargs)

		self.name = name

		back_image = u.mImage(source = g.IMG_BACKGROUND, size = (433,769), rpos = (0,0))
		main_image = u.mImage(source = g.IMG_MORE_SCENE, size = (433,769), rpos = (0,0))

		self.add_widget(back_image)
		self.add_widget(main_image)
		
		chessbtn = moreButton(btn_name = 'chess')
		ocabtn = moreButton(btn_name = 'oca')
		backbtn = moreButton(btn_name = 'back')
		
		self.add_widget(chessbtn)
		self.add_widget(ocabtn)
		self.add_widget(backbtn)

		#self.label1 = Label( text = g.xml_root[2][0].text, font_name = g.FONT_CR, font_size = 26*g.scale, color = g.COLOR_BLACK, pos = (0,230*g.scale) )
		#self.label2 = Label( text = g.xml_root[2][1].text, font_name = g.FONT_CR, font_size = 26*g.scale, color = g.COLOR_BLACK, pos = (0,200*g.scale) )
		#self.add_widget( self.label1 )
		#self.add_widget( self.label2 )
	
	def on_pre_leave(self):
		g.sound_controller.play_sound(g.SOUND_SHEET)

class moreButton(Button):
	def __init__(self, btn_name = None, **kwargs):
		super(moreButton,self).__init__(**kwargs)
		
		self.border = (0,0,0,0)
		self.size_hint = (None, None)
		self.size = (130*g.scale, 130*g.scale)

		if btn_name == 'chess':
			self.bind(on_press = self.click_chess)
			y_mod = 100*g.scale
			self.background_normal = g.IMG_MORE_BTN_CHESS_NORMAL
			self.background_down = g.IMG_MORE_BTN_CHESS_PRESS
		elif btn_name == 'oca':
			self.bind(on_press = self.click_oca)
			y_mod = -40*g.scale
			self.background_normal = g.IMG_MORE_BTN_OCA_NORMAL
			self.background_down = g.IMG_MORE_BTN_OCA_PRESS
		elif btn_name == 'back':
			self.bind(on_press = self.click_back)
			y_mod = -200*g.scale
			self.background_normal = g.IMG_MORE_BTN_BACK_NORMAL
			self.background_down = g.IMG_MORE_BTN_BACK_PRESS
		
		self.x = g.screen_size[0]/2 - self.size[0]/2
		self.y = g.screen_size[1]/2 - self.size[1]/2 + y_mod

	def click_chess(self, arg1):
		webbrowser.open( 'https://play.google.com/store/apps/details?id=com.ocastudios.chess4&hl=en' )

	def click_oca(self, arg1):
		webbrowser.open( 'http://www.ocastudios.com' )
		
	def click_back(self, arg1):
		#g.manager.current = 'title_screen'
		if g.ad_count >= g.ad_count_limit:
			g.manager.current = 'splash_screen'
		else:
			g.manager.current = 'title_screen'
		
