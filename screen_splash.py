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
import kivy.utils
#import xml.etree.ElementTree as ET

import g
import utils as u
import ocanim as oa

class splashScreen(Screen):
	def __init__(self,name,**kwargs):
		super(splashScreen,self).__init__(**kwargs)

		self.name = name

		back_image = u.mImage(source = g.IMG_BACKGROUND, size = (433,769), rpos = (0,0))
		main_image = u.mImage(source = g.IMG_SPLASH_SCENE, size = (433,769), rpos = (0,0))
		
		self.add_widget(back_image)
		self.add_widget(main_image)
		
		#self.label1 = Label( text = g.xml_root[0][0].text, font_name = g.FONT_CR, font_size = 26*g.scale, color = g.COLOR_BROWN, pos = (0,83*g.scale) )
		#self.label2 = Label( text = g.xml_root[0][1].text, font_name = g.FONT_CR, font_size = 26*g.scale, color = g.COLOR_BROWN, pos = (0,54*g.scale) )
		#self.label3 = Label( text = g.xml_root[0][2].text, font_name = g.FONT_CR, font_size = 26*g.scale, color = g.COLOR_BROWN, pos = (0,25*g.scale) )
		#self.add_widget( self.label1 )
		#self.add_widget( self.label2 )
		#self.add_widget( self.label3 )
		
	def create_btn(self, elapsed_time = 0.0):
		self.bigbtn = splashButton()
		self.add_widget(self.bigbtn)
		oa.move_to( self.bigbtn, target_pos = self.bigbtn.end_pos )
		oa.move_to( self.bigbtn.btn_text, target_pos = self.bigbtn.btn_text.end_pos )
		
	def on_pre_enter(self):
		# This will cache ads. We only run this once, early in the game.
		pass
#		if g.do_cache_ads:
#			g.do_cache_ads = False
#			if kivy.utils.platform == 'android':
#				g.is_android = True
#			
#				g.Ads = autoclass('com.purplebrain.adbuddiz.sdk.AdBuddiz')
#				g.Ads.setPublisherKey( g.adbuddiz_code )
#				
#				python_activity = autoclass( 'org.renpy.android.PythonActivity' )
#				current_activity = cast( 'android.app.Activity', python_activity.mActivity )
#				
#				g.Ads.cacheAds( current_activity )
#						
#			else:
#				g.is_android = False
#				print 'Not android: we do not cache ads.'

	def on_enter(self):
		Clock.schedule_once(self.create_btn, g.splash_time)
		
		#self.label1.text = str(kivy.utils.platform)
		#self.label2.text = str(g.ad_count)
		#self.label3.text = g.fix_string
		
		if g.ad_count > 0:
			g.ad_count = 0
			
			if g.is_android:
				#self.label3.text = "SHOW AD NOW"
				python_activity = autoclass( 'org.renpy.android.PythonActivity' )
				current_activity = cast( 'android.app.Activity', python_activity.mActivity )
				g.Ads.showAd( current_activity )
			else:
				print "Skip ad: not android"

	def on_pre_leave(self):
		g.sound_controller = u.SoundController()
		g.sound_controller.play_sound(g.SOUND_SHEET)
	
	def on_leave(self):
		self.remove_widget( self.bigbtn )

	def switch_to_title_screen(self,time_elapsed):
		g.manager.current = g.screens['title'].name


class splashButton(Button):
	def __init__(self,**kwargs):
		super(splashButton,self).__init__(**kwargs)

		self.size_hint = (None,None)
		self.size = (288*g.scale, 144*g.scale)
		self.border = (0,0,0,0)

		self.background_normal = g.IMG_SPLASH_BUTTON_NORMAL
		self.background_down = g.IMG_SPLASH_BUTTON_PRESSED

		self.pos = ( g.screen_size[0]/2-self.size[0]/2, -144*g.scale ) 
		self.end_pos = ( g.screen_size[0]/2-self.size[0]/2, 0 ) 
		self.bind(on_press = self.tap_screen)
		
		self.btn_text = Label(
			text = u.get_string("splash","first"),
			font_name = g.FONT_CB,
			font_size = 32*g.scale,
			color = g.COLOR_BROWN
			)

		self.btn_text.texture_update()
		self.btn_text.size = self.btn_text.texture_size[:]
		self.btn_text.pos = ( g.screen_size[0]/2 - self.btn_text.size[0]/2, 25*g.scale - self.pos[1] )
		self.btn_text.end_pos = ( g.screen_size[0]/2 - self.btn_text.size[0]/2, 25*g.scale )
		self.add_widget( self.btn_text )

	def tap_screen(self, arg1 = None):
		g.manager.current = g.screens['title'].name
