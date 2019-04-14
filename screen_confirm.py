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

import random
from random import shuffle

import g
import utils as u
import logic as ai
#from basic_widgets import *

class confirmExit(ModalView):
	def __init__(self,**kwargs):
		super(confirmExit,self).__init__(**kwargs)
		
		self.size_hint = (None, None)
		self.size = (290*g.scale, 290*g.scale)
		self.border = (0.2,0.4,0.2,0)
		
		self.auto_dismiss = False
		
		self.background_color = (0,0,0,0.2)
		self.background = g.IMG_CONFIRM_BG
		
		textlabel = Label(text = g.xml_root[6][5].text)
		textlabel.font_name = g.FONT_CR
		textlabel.font_size = 26*g.scale
		textlabel.color = g.COLOR_BLUE
		
		self.rl = RelativeLayout()
		self.add_widget(self.rl)
		
		self.rl.add_widget( confirmationButton('yes') )
		self.rl.add_widget( confirmationButton('no') )
		self.rl.add_widget( textlabel )
		
		# If we're in the main screen, add option to return to title
		if g.manager.current_screen.name == 'main_screen':
			self.title_btn = confSmallButton('title',self) #The btn will addd itself to parent
			show_undo = False
			if len(g.moves_history['player_1'])>0:
				show_undo = True
			if g.players == 1 and g.player == 'player_2':
				show_undo = False
			if show_undo:
				pass
			self.undo_btn = confSmallButton('undo',self) #The btn will addd itself to parent
		
		# Create volume button
		self.volume_btn = ToggleButton()
		self.volume_btn.size_hint = (None,None)
		self.volume_btn.size = (130*g.scale, 130*g.scale)
			
		self.volume_btn.border = (0,0,0,0)
		self.volume_btn.background_normal = g.IMG_CONFIRM_VOLUMEBTN_NORMAL
		self.volume_btn.background_down = g.IMG_CONFIRM_VOLUMEBTN_PRESS
		posx = self.size[0]/2 - self.volume_btn.size[0]/2
		posy = self.size[1]/2 - self.volume_btn.size[1]/2 + 235*g.scale
		self.volume_btn.pos = (posx, posy)
		self.volume_btn.bind( on_press = self.confirm_volume )
		
		if g.sound:
			self.volume_btn.state = 'normal'
		else:
			self.volume_btn.state = 'down'
			
		self.rl.add_widget(self.volume_btn)
		

	def confirm_title(self, arg1):
		self.dismiss()
		print 'COUNTING:',g.ad_count
		if g.ad_count > 5:
			g.manager.current = 'splash_screen'
		else:
			g.manager.current = 'title_screen'
		g.modal_screen = False

	def confirm_volume(self, btn):
		if self.volume_btn.state == 'normal':
			#Volume has just been turned on
			#g.sound_controller.play_music()
			g.sound = True
		elif self.volume_btn.state == 'down':
			#Volume has just been turned off
			#g.sound_controller.stop_music()
			g.sound = False

class confirmationButton(Button):
	def __init__(self,name,**kwargs):
		super(confirmationButton,self).__init__(**kwargs)
		
		self.size_hint = (None,None)
		self.size = (289*g.scale, 145*g.scale)
		self.border = (0,0,0,0)
		self.x = 0# g.screen_size[0]/2 - self.size[0]/2
		if name == 'yes':
			self.background_down = g.IMG_CONFIRM_YESBTN_PRESS
			self.background_normal = g.IMG_CONFIRM_YESBTN_NORMAL
			self.y = self.size[1]#0#g.screen_size[1]/2
			self.bind( on_press = self.confirm_yes )
			label_text = g.xml_root[6][0].text
			font_y = 138*g.scale
			font_color = g.COLOR_BROWN
		elif name == 'no':
			self.background_down = g.IMG_CONFIRM_NOBTN_PRESS
			self.background_normal = g.IMG_CONFIRM_NOBTN_NORMAL
			self.y = 0#- self.size[1]#g.screen_size[1]/2 - self.size[1]
			self.bind( on_press = self.confirm_no )
			label_text = g.xml_root[6][1].text
			font_y = 16*g.scale
			font_color = g.COLOR_BLUE
			
		self.label = Label(text = label_text, font_name = g.FONT_CB, font_size = 80*g.scale, color = font_color)
		self.label.texture_update()
		self.label.size = self.label.texture_size
		self.label.pos = (self.size[0]/2-self.label.size[0]/2, self.size[1]/2-self.label.size[1]/2 + font_y )
		self.add_widget(self.label)

	def confirm_yes(self, arg1):
		g.modal_screen = False
		self.parent.parent.dismiss()
		g.app.stop()
	
	def confirm_no(self, arg1):
		g.modal_screen = False
		self.parent.parent.dismiss()

class confSmallButton(Button):
	def __init__(self,name,btn_parent,**kwargs):
		super(confSmallButton,self).__init__(**kwargs)


		self.size_hint = (None,None)
		self.size = (130*g.scale, 130*g.scale)
			
		self.border = (0,0,0,0)
		

		#textlabel.font_name = g.FONT_CR
		#textlabel.font_size = 26*g.scale
		#textlabel.color = g.COLOR_BLUE

		if name == 'title':
			#posx = btn_parent.size[0]/2 - self.size[0]/2
			#posy = btn_parent.size[1]/2 - self.size[1]/2 - 235*g.scale
			#self.pos = (posx, posy)

			self.background_normal = g.IMG_CONFIRM_TITLEBTN_NORMAL
			self.background_down = g.IMG_CONFIRM_TITLEBTN_PRESS

			posx = btn_parent.size[0]/2 - self.size[0]/2 + g.screen_size[0]/3.7
			posy = btn_parent.size[1]/2 - self.size[1]/2 - 235*g.scale + 18*g.scale
			self.pos = (posx, posy)

			self.label1 = Label(text = g.xml_root[6][3].text, color = g.COLOR_BLUE, font_size = 26*g.scale, font_name = g.FONT_CR)
			self.label2 = Label(text = g.xml_root[6][4].text, color = g.COLOR_BLUE, font_size = 26*g.scale, font_name = g.FONT_CR)
			self.label1.pos = (self.pos[0]+self.size[0]/2-self.label1.size[0]/2, self.pos[1]+self.size[1]/2-self.label1.size[1]/2 - 4*g.scale)
			self.label2.pos = (self.pos[0]+self.size[0]/2-self.label1.size[0]/2, self.pos[1]+self.size[1]/2-self.label1.size[1]/2 - 28*g.scale)
			self.add_widget(self.label1)
			self.add_widget(self.label2)
			self.bind( on_press = self.confirm_title )
		
		if name == 'undo':
			
			self.background_normal = g.IMG_CONFIRM_UNDOBTN_NORMAL
			self.background_down = g.IMG_CONFIRM_UNDOBTN_PRESS

			posx = btn_parent.size[0]/2 - self.size[0]/2 - g.screen_size[0]/3.7
			posy = btn_parent.size[1]/2 - self.size[1]/2 - 235*g.scale + 18*g.scale
			self.pos = (posx, posy)

			self.label1 = Label(text = g.xml_root[6][2].text, color = g.COLOR_BLUE, font_size = 26*g.scale, font_name = g.FONT_CR)
			self.label1.pos = (self.pos[0]+self.size[0]/2-self.label1.size[0]/2, self.pos[1]+self.size[1]/2-self.label1.size[1]/2 )#- 16*g.scale)
			self.add_widget(self.label1)
			self.bind( on_press = self.undo_move )
			
		btn_parent.rl.add_widget(self)

	def confirm_title(self, arg1 = None):
		self.parent.parent.dismiss()
		if g.ad_count >=5:
			g.manager.current = 'splash_screen'
		else:
			g.manager.current = 'title_screen'
		g.modal_screen = False
	
	def undo_move(self, arg1 = None):
		ai.undo()
		g.modal_screen = False
		self.parent.parent.dismiss()
