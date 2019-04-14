import kivy
kivy.require('1.8.0')

from kivy.uix.screenmanager import *
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.stencilview import StencilView
from kivy.clock import Clock

from functools import partial

import g
import utils as u
import ocanim as oa

class tutorialScreen(Screen):
	def __init__(self,name,**kwargs):
		super(tutorialScreen,self).__init__(**kwargs)
		
		self.name = name
		
		self.frame = 1
		
		back_image = u.mImage(source = g.IMG_BACKGROUND, size = (433,769), rpos = (0,0))
		self.add_widget(back_image)
		
		self.create_img_frames()
		
		self.btn_back = tutorialButton(direction = 'back')
		self.btn_forward = tutorialButton(direction = 'forward')
		
		self.add_widget( self.btn_back )
		self.add_widget( self.btn_forward )
		
		self.title = tutorialTitle()
		self.add_widget(self.title)
		self.label = tutorialText()
		self.add_widget(self.label)
	
	def create_img_frames(self):
		
		#FRAME1
		self.img_f1 = u.mImage(source = g.IMG_TUTORIAL_FRAME_1, size = (270,236), rpos = (0,94))
		self.img_f1.opacity = 0.0
		self.add_widget(self.img_f1)
		
		#FRAME 2
		self.img_tapir_ally = u.mImage(source = g.IMG_TUTORIAL_TAPIR_ALLY, size = (136,136))
		self.img_tapir_ally.pos_initial = u.rpos_to_pos( self.img_tapir_ally, (0,-g.screen_size[1]/2-68) )
		self.img_tapir_ally.pos_final = u.rpos_to_pos( self.img_tapir_ally, (0,40) )
		self.img_tapir_ally.pos = self.img_tapir_ally.pos_initial[:]
		
		self.img_tapir_foe = u.mImage(source = g.IMG_TUTORIAL_TAPIR_FOE, size = (136,136))
		self.img_tapir_foe.pos_initial = u.rpos_to_pos( self.img_tapir_ally, (0,g.screen_size[1]/2+68) )
		self.img_tapir_foe.pos_final = u.rpos_to_pos( self.img_tapir_ally, (0,180) )
		self.img_tapir_foe.pos = self.img_tapir_foe.pos_initial[:]
		
		self.add_widget(self.img_tapir_ally)
		self.add_widget(self.img_tapir_foe)
		
		#FRAME 3
		self.img_raccoon = u.mImage(source = g.IMG_TUTORIAL_RACCOON, size = (136,136))
		self.img_raccoon.p0 = u.rpos_to_pos( self.img_raccoon, (0,-g.screen_size[1]/2-68) )
		self.img_raccoon.p1 = u.rpos_to_pos( self.img_raccoon, (0,110) )
		self.img_raccoon.p2 = u.rpos_to_pos( self.img_raccoon, (62,38) )
		self.img_raccoon.pos = self.img_raccoon.p0[:]
		self.add_widget(self.img_raccoon)
		
		self.img_raccoon_a3 = u.mImage(source = g.IMG_TUTORIAL_RACCOON_ARROWS3, size = (214,214))
		self.img_raccoon_a3.pos = u.rpos_to_pos( self.img_raccoon_a3, (0,110) )
		self.img_raccoon_a3.opacity = 0.0
		self.add_widget(self.img_raccoon_a3)
		
		#FRAME4
		self.img_fox = u.mImage(source = g.IMG_TUTORIAL_FOX, size = (136,136))
		self.img_fox.p0 = u.rpos_to_pos( self.img_fox, (-80,-g.screen_size[1]/2-68) )
		self.img_fox.p1 = u.rpos_to_pos( self.img_fox, (-80,180) )
		self.img_fox.pos = self.img_fox.p0[:]
		self.add_widget(self.img_fox)
		
		self.img_raccoon_a4 = u.mImage(source = g.IMG_TUTORIAL_RACCOON_ARROWS4, size = (336,334))
		self.img_raccoon_a4.pos = u.rpos_to_pos( self.img_raccoon_a3, (-60,40) )
		self.img_raccoon_a4.opacity = 0.0
		self.add_widget(self.img_raccoon_a4)
		
		#FRAME5
		self.img_carp_foe = u.mImage(source = g.IMG_TUTORIAL_CARP_FOE, size = (136,136))
		self.img_carp_foe.p0 = u.rpos_to_pos( self.img_carp_foe, (-80,g.screen_size[1]/2+68) )
		self.img_carp_foe.p1 = u.rpos_to_pos( self.img_carp_foe, (-80,180) )
		self.img_carp_foe.p2 = u.rpos_to_pos( self.img_carp_foe, (-80,-g.screen_size[1]/2-68) )
		self.img_carp_foe.p3 = u.rpos_to_pos( self.img_carp_foe, (0,g.screen_size[1]/2+68) )
		self.img_carp_foe.p4 = u.rpos_to_pos( self.img_carp_foe, (0,180) )
		self.img_carp_foe.pos = self.img_carp_foe.p0[:]
		#The carp is added further along so it can be on top of further widgets
		#self.add_widget(self.img_carp_foe)

		self.img_raccoon_a5 = u.mImage(source = g.IMG_TUTORIAL_RACCOON_ARROWS5, size = (31,31))
		self.img_raccoon_a5.pos = u.rpos_to_pos( self.img_raccoon_a5, (-20,120) )
		self.img_raccoon_a5.opacity = 0.0
		#This arrow is added further along so it can be on top of further widgets
		#self.add_widget(self.img_raccoon_a5)
		
		#FRAME6
		self.img_farm_ally = u.mImage(source = g.IMG_TUTORIAL_FARM_ALLY, size = (433,614)) #550
		#self.img_farm_ally.p0 = u.rpos_to_pos( self.img_farm_ally, (0,-g.screen_size[1]/2-275) )#-275
		self.img_farm_ally.p0 = ( g.screen_size[0]/2 - self.img_farm_ally.size[0]/2, -self.img_farm_ally.size[1])
		self.img_farm_ally.p1 = u.rpos_to_pos( self.img_farm_ally, (0,-126) )#-86,-132
		self.img_farm_ally.pos = self.img_farm_ally.p0[:]
		self.add_widget(self.img_farm_ally)

		self.img_carp_ally = u.mImage(source = g.IMG_TUTORIAL_CARP_ALLY, size = (136,136))
		self.img_carp_ally.p0 = u.rpos_to_pos( self.img_carp_ally, (0,-g.screen_size[1]/2-68) )
		self.img_carp_ally.p1 = u.rpos_to_pos( self.img_carp_ally, (0,15) )
		self.img_carp_ally.p2 = u.rpos_to_pos( self.img_carp_ally, (0,40) )
		self.img_carp_ally.p3 = u.rpos_to_pos( self.img_carp_ally, (0,130) )
		self.img_carp_ally.p4 = u.rpos_to_pos( self.img_carp_ally, (0,g.screen_size[1]/2+68) )
		self.img_carp_ally.pos = self.img_carp_ally.p0[:]
		self.img_carp_ally.keep_ratio = False
		#The carp is added further along so it can be on top of further widgets
		#self.add_widget(self.img_carp_ally)
		
		#FRAME7
		self.img_zone = u.mImage(source = g.IMG_TUTORIAL_PROMOTION_ZONE, size = (410,137))
		self.img_zone.p0 = u.rpos_to_pos( self.img_zone, (0,g.screen_size[1]/2+68) )
		self.img_zone.p1 = u.rpos_to_pos( self.img_zone, (0,180) )
		self.img_zone.p2 = u.rpos_to_pos( self.img_zone, (0,130) )
		self.img_zone.pos = self.img_zone.p0[:]
		self.add_widget(self.img_zone)
		
		self.img_zoneX = u.mImage(source = g.IMG_TUTORIAL_PROMOTION_X, size = (338,66))
		self.img_zoneX.pos = u.rpos_to_pos( self.img_zoneX, (0,180) )
		self.img_zoneX.opacity = 0.0
		self.add_widget(self.img_zoneX)
		
		#FRAME10
		self.img_farm_foe = u.mImage(source = g.IMG_TUTORIAL_FARM_FOE, size = (433,614)) #550
		#self.img_farm_foe.p0 = u.rpos_to_pos( self.img_farm_foe, (0,g.screen_size[1]/2+307) )#-275
		self.img_farm_foe.p0 = (g.screen_size[0]/2-self.img_farm_foe.size[0]/2, g.screen_size[1])
		self.img_farm_foe.p1 = u.rpos_to_pos( self.img_farm_foe, (0,300) )#-86,-132
		self.img_farm_foe.pos = self.img_farm_foe.p0[:]
		self.add_widget(self.img_farm_foe)
		
		

		self.add_widget(self.img_carp_foe)
		self.add_widget(self.img_carp_ally)
		self.add_widget(self.img_raccoon_a5)
		
		# If halt_frame is True, then something is being written.
		# We finish it already button don't change frames.
		self.halt_frame = False
		self.writing = False
	
	def on_pre_enter(self):
		self.title.text = ''
		self.label.text = ''
		self.title.opacity = 1.0
		self.label.opacity = 1.0
		self.frame = 1
		# Sometimes we have promblem with the carps.
		# As a paleative, let's reset their position when we enter.
		self.img_carp_ally.pos = self.img_carp_ally.p0
		self.img_carp_foe.pos = self.img_carp_foe.p0
	
	def on_enter(self):
		oa.move_to( self.btn_back, self.btn_back.pos_final )
		oa.move_to( self.btn_forward, self.btn_forward.pos_final )
		self.title.rewrite(g.xml_root[3][0].text, self.write_text_body)
		oa.fade_in(self.img_f1)
	
	def on_pre_leave(self):
		oa.move_to( self.btn_back, self.btn_back.pos_initial )
		oa.move_to( self.btn_forward, self.btn_forward.pos_initial )

		g.sound_controller.play_sound(g.SOUND_SHEET)
	
	def on_leave(self):
		pass
	
	def get_title_ref(self):
		xlist = [0,2,4,6,8,10,12,14,16,18]
		return xlist[self.frame-1]
	
	def write_text_body(self):
		self.label.rewrite(g.xml_root[3][self.get_title_ref()+1].text)

	def force_write(self):
		x = self.get_title_ref()
		self.title.text = g.xml_root[3][x].text
		self.label.text = g.xml_root[3][x+1].text
		
	def previous_frame(self):
		if self.frame == 1:
			oa.fade_out(self.title)
			oa.fade_out(self.label)
			oa.fade_out(self.img_f1)
			#---
			
		elif self.frame == 2:
			oa.move_to(self.img_tapir_ally, self.img_tapir_ally.pos_initial)
			oa.move_to(self.img_tapir_foe, self.img_tapir_foe.pos_initial)
			self.label.clear()
			#---
			self.title.rewrite(g.xml_root[3][0].text, self.write_text_body)
			oa.fade_in(self.img_f1)
		elif self.frame == 3:
			self.label.clear()
			oa.move_to(self.img_raccoon, self.img_raccoon.p0)
			oa.fade_out( self.img_raccoon_a3 )
			#---
			self.title.rewrite(g.xml_root[3][2].text, self.write_text_body)
			oa.move_to(self.img_tapir_ally, self.img_tapir_ally.pos_final)
			oa.move_to(self.img_tapir_foe, self.img_tapir_foe.pos_final)
		elif self.frame == 4:
			self.label.clear()
			oa.move_to(self.img_raccoon, self.img_raccoon.p1)
			oa.move_to(self.img_fox, self.img_fox.p0)
			oa.fade_out( self.img_raccoon_a4 )
			#---
			self.title.rewrite(g.xml_root[3][4].text, self.write_text_body)
			oa.fade_in( self.img_raccoon_a3 )
		elif self.frame == 5:
			self.label.clear()
			self.img_carp_foe.pos = self.img_carp_foe.p1 #<---
			oa.move_to(self.img_carp_foe, self.img_carp_foe.p0)
			oa.fade_out( self.img_raccoon_a5 )
			#---
			self.title.rewrite(g.xml_root[3][6].text, self.write_text_body)
			oa.move_to(self.img_raccoon, self.img_raccoon.p2)
			oa.move_to(self.img_fox, self.img_fox.p1)
			oa.fade_in( self.img_raccoon_a4 )
		elif self.frame == 6:
			self.label.clear()
			self.img_carp_ally.pos = self.img_carp_ally.p1 #<---
			oa.move_to(self.img_carp_ally, self.img_carp_ally.p0)
			oa.move_to(self.img_farm_ally, self.img_farm_ally.p0)
			#---
			self.img_carp_foe.pos = self.img_carp_foe.p2 #<---
			self.title.rewrite(g.xml_root[3][8].text, self.write_text_body)
			oa.move_to(self.img_carp_foe, self.img_carp_foe.p1)
			oa.move_to(self.img_raccoon, self.img_raccoon.p2)
			oa.fade_in( self.img_raccoon_a5 )
		elif self.frame == 7:
			self.label.clear()
			self.img_carp_ally.pos = self.img_carp_ally.p2 #<---
			oa.move_to(self.img_carp_ally, self.img_carp_ally.p1)
			#---
			self.title.rewrite(g.xml_root[3][10].text, self.write_text_body)
			oa.move_to(self.img_farm_ally, self.img_farm_ally.p1)
		elif self.frame == 8:
			self.label.clear()
			oa.move_to(self.img_zone, self.img_zone.p0)
			oa.fade_out(self.img_zoneX)
			#---
			self.title.rewrite(g.xml_root[3][12].text, self.write_text_body)
		elif self.frame == 9:
			self.label.clear()
			self.img_carp_ally.pos = self.img_carp_ally.p3 #<---
			oa.move_to(self.img_zone, self.img_zone.p1)
			oa.move_to(self.img_carp_ally, self.img_carp_ally.p2, self.demote_carp)
			#---
			self.title.rewrite(g.xml_root[3][14].text, self.write_text_body)
			oa.fade_in(self.img_zoneX)
		elif self.frame == 10:
			self.label.clear()
			self.img_carp_foe.pos = self.img_carp_foe.p4 #<---
			oa.move_to(self.img_carp_foe, self.img_carp_foe.p3, self.phase_carp_back)
			oa.move_to(self.img_farm_foe, self.img_farm_foe.p0)
			#---
			self.img_carp_ally.pos = self.img_carp_ally.p4 #<---
			self.title.rewrite(g.xml_root[3][16].text, self.write_text_body)
			oa.move_to(self.img_zone, self.img_zone.p2)
			oa.move_to(self.img_carp_ally, self.img_carp_ally.p3)

	def phase_carp_back(self, arg1=None, arg2=None):
		self.img_carp_foe.pos = self.img_carp_foe.p2

	def next_frame(self):
		
		if self.frame == 1:
			self.label.clear()
			oa.fade_out(self.img_f1)
			#---
			self.title.rewrite(g.xml_root[3][2].text, self.write_text_body)
			oa.move_to(self.img_tapir_ally, self.img_tapir_ally.pos_final)
			oa.move_to(self.img_tapir_foe, self.img_tapir_foe.pos_final)
			
		elif self.frame == 2:
			oa.move_to(self.img_tapir_ally, self.img_tapir_ally.pos_initial)
			oa.move_to(self.img_tapir_foe, self.img_tapir_foe.pos_initial)
			self.label.clear()
			#---
			self.title.rewrite(g.xml_root[3][4].text, self.write_text_body)
			oa.move_to(self.img_raccoon, self.img_raccoon.p1)
			oa.fade_in( self.img_raccoon_a3 )
			
		elif self.frame == 3:
			self.label.clear()
			oa.fade_out( self.img_raccoon_a3 )
			#---
			self.title.rewrite(g.xml_root[3][6].text, self.write_text_body)
			oa.move_to(self.img_raccoon, self.img_raccoon.p2)
			oa.move_to(self.img_fox, self.img_fox.p1)
			oa.fade_in( self.img_raccoon_a4 )
		elif self.frame == 4:
			self.label.clear()
			oa.fade_out( self.img_raccoon_a4 )
			oa.move_to(self.img_fox, self.img_fox.p0)
			#---
			self.img_carp_foe.pos = self.img_carp_ally.p0 #<---
			self.title.rewrite(g.xml_root[3][8].text, self.write_text_body)
			oa.move_to(self.img_carp_foe, self.img_carp_foe.p1)
			oa.fade_in( self.img_raccoon_a5 )
		elif self.frame == 5:
			self.label.clear()
			oa.move_to(self.img_carp_foe, self.img_carp_foe.p2)
			oa.move_to(self.img_raccoon, self.img_raccoon.p0)
			oa.fade_out( self.img_raccoon_a5 )
			#---
			self.img_carp_ally.pos = self.img_carp_ally.p0 #<---
			self.title.rewrite(g.xml_root[3][10].text, self.write_text_body)
			oa.move_to(self.img_carp_ally, self.img_carp_ally.p1)
			oa.move_to(self.img_farm_ally, self.img_farm_ally.p1)
		elif self.frame == 6:
			self.label.clear()
			oa.move_to(self.img_farm_ally, self.img_farm_ally.p0)
			#---
			self.img_carp_ally.pos = self.img_carp_ally.p1 #<---
			self.title.rewrite(g.xml_root[3][12].text, self.write_text_body)
			oa.move_to(self.img_carp_ally, self.img_carp_ally.p2)
		elif self.frame == 7:
			self.label.clear()
			#---
			self.title.rewrite(g.xml_root[3][14].text, self.write_text_body)
			oa.move_to(self.img_zone, self.img_zone.p1)
			oa.fade_in(self.img_zoneX)
		elif self.frame == 8:
			self.label.clear()
			oa.fade_out(self.img_zoneX)
			#---
			self.img_carp_ally.pos = self.img_carp_ally.p2 #<---
			self.title.rewrite(g.xml_root[3][16].text, self.write_text_body)
			oa.move_to(self.img_zone, self.img_zone.p2)
			oa.move_to(self.img_carp_ally, self.img_carp_ally.p3,self.promote_carp)
		elif self.frame == 9:
			self.label.clear()
			oa.move_to(self.img_zone, self.img_zone.p0)
			oa.move_to(self.img_carp_ally, self.img_carp_ally.p4)
			#---
			self.title.rewrite(g.xml_root[3][18].text, self.write_text_body)
			self.img_carp_foe.pos = self.img_carp_foe.p3
			oa.move_to(self.img_carp_foe, self.img_carp_foe.p4)
			oa.move_to(self.img_farm_foe, self.img_farm_foe.p1)
		if self.frame == 10:
			oa.fade_out(self.title)
			oa.fade_out(self.label)
			self.img_carp_foe.pos = self.img_carp_foe.p4 #<---
			oa.move_to(self.img_carp_foe, self.img_carp_foe.p0)
			oa.move_to(self.img_farm_foe, self.img_farm_foe.p0)
			self.demote_carp()
			#---
	
	def promote_carp(self, arg1=None, arg2=None):
		oa.flip( self.img_carp_ally, None, None, None, 2, 'horizontal', self.carp_to_koi, True)
		
	def carp_to_koi(self):
		self.img_carp_ally.source=g.IMG_TUTORIAL_KOI
		self.img_carp_ally.reload()

	def demote_carp(self, arg1=None, arg2=None):
		oa.flip( self.img_carp_ally, None, None, None, 2, 'horizontal', self.koi_to_carp, True)
		
	def koi_to_carp(self):
		self.img_carp_ally.source=g.IMG_TUTORIAL_CARP_ALLY
		self.img_carp_ally.reload()
		
class tutorialButton(Button):
	def __init__(self, direction = 'back', **kwargs):
		super(tutorialButton,self).__init__(**kwargs)
		
		self.border = (0,0,0,0)
		self.size_hint = (None, None)
		self.size = (130*g.scale, 130*g.scale)

		if direction == 'back':
			self.background_normal = g.IMG_TUTORIAL_BTN_BACK_NORMAL
			self.background_down = g.IMG_TUTORIAL_BTN_BACK_PRESS
			self.bind(on_press = self.go_back)
			self.pos_final = (0,0)
			self.pos_initial = (-130*g.scale,-130*g.scale)
			self.pos = self.pos_initial[:]
		else:
			self.background_normal = g.IMG_TUTORIAL_BTN_FORWARD_NORMAL
			self.background_down = g.IMG_TUTORIAL_BTN_FORWARD_PRESS
			self.bind(on_press = self.go_forward)
			self.pos_final = (g.screen_size[0]-self.size[0],0)
			self.pos_initial = (g.screen_size[0],-130*g.scale)
			self.pos = self.pos_initial[:]
	
	def interrupt_writing(self):
		pass
	
	def force_fix_carp_size(self):
		self.parent.img_carp_ally.size = (136*g.scale,136*g.scale)
			
	def go_back(self, arg1):
		if self.parent.writing == True:
			self.parent.halt_frame = True
			self.parent.writing = False
			self.force_fix_carp_size()
		else:
			self.parent.previous_frame()
			if self.parent.frame == 1:
				if g.ad_count > 5:
					g.manager.current = 'splash_screen'
				else:
					g.manager.current = g.screens['title'].name
			else:
				self.parent.frame-=1
			
	def go_forward(self, arg1):
		if self.parent.writing == True:
			self.parent.halt_frame = True
			self.parent.writing = False
			self.force_fix_carp_size()
		else:
			self.parent.next_frame()
			if self.parent.frame == 10:
				if g.ad_count > 5:
					g.manager.current = 'splash_screen'
				else:
					g.manager.current = g.screens['title'].name
			else:
				self.parent.frame+=1

class tutorialTitle(Label):
	def __init__(self, **kwargs):
		super(tutorialTitle,self).__init__(**kwargs)
		self.text = ''
		self.font_name = g.FONT_CB
		self.font_size = 30*g.scale
		self.color = g.COLOR_BROWN
		self.texture_update()
		self.size = self.texture_size
		pos_y = g.screen_size[1]/2 - self.size[1]/2-35*g.scale
		self.pos = ( 0, pos_y )
	
	def rewrite(self, text, end_func = None):
		self.text = ''
		self.write(text, end_func)
	
	def write(self, text, end_func = None, arg1 = None):
		if self.parent.halt_frame == True:
			self.parent.force_write()
			self.parent.halt_frame = False
		else:
			self.text += text[0]
			text = text[1:]
			if len(text)>0:
				self.parent.writing = True
				Clock.schedule_once( partial( self.write, text, end_func ), 0.06 )
			else:
				self.parent.writing = False
				if end_func != None:
					end_func()

class tutorialText(Label):
	def __init__(self, **kwargs):
		super(tutorialText,self).__init__(**kwargs)
		self.text = ''
		self.font_name = g.FONT_IN
		self.font_size = 28*g.scale
		self.color = g.COLOR_BROWN
		self.texture_update()
		self.size = self.texture_size
		#self.pos = ( 0, -123*g.scale )
		#self.text_size = (300*g.scale, 300*g.scale)
		self.pos = ( 0, -133*g.scale )
		self.text_size = (320*g.scale, 300*g.scale)
		self.halign = 'center'
		self.valign = 'middle'
		self.line_height = 1.1
	
	def rewrite(self, text, end_func = None):
		self.text = ''
		self.write(text, end_func)
	
	def write(self, text, end_func = None, arg1 = None):
		if self.parent.halt_frame == True:
			self.parent.force_write()
			self.parent.halt_frame = False
		else:
			self.text += text[0]
			text = text[1:]
			if len(text)>0:
				self.parent.writing = True
				Clock.schedule_once( partial( self.write, text, end_func ), 0.03 )
			else:
				self.parent.writing = False
				if end_func != None:
					end_func()
					
	def clear(self):
		self.text = ''
