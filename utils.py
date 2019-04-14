from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from kivy.clock import Clock

import random
from functools import partial

import g


def set_scale():
	xfactor = Window.size[0]/360.0
	yfactor = Window.size[1]/640.0
	
	smaller_factor = xfactor
	if yfactor < xfactor:
		smaller_factor = yfactor
		
	g.scale = smaller_factor
	g.scale_x = xfactor
	g.scale_y = yfactor
	
	if g.scale <= 1.0:
		g.base_path = './res/drawable/'
	elif g.scale <= 1.5:
		g.base_path = './res/drawable-hdpi/'
	elif g.scale <= 2.0:
		g.base_path = './res/drawable-xhdpi/'
	elif g.scale <= 3.0:
		g.base_path = './res/drawable-xxhdpi/'
	else:
		g.base_path = './res/drawable-xxxhdpi/'
	
	recreate_image_paths()
	
	return g.scale

def rpos_to_pos(widget, rpos = (0,0)):
	rx = g.screen_size[0]/2-widget.size[0]/2+rpos[0]*g.scale
	ry = g.screen_size[1]/2-widget.size[1]/2+rpos[1]*g.scale
	return (rx,ry)

def recreate_image_paths():
	"""This will create the image paths according to resolution. If there are no resolution options available, set g.force_resolution to True."""
	
	if g.force_resolution:
		base_path = g.default_image_path
	else:
		base_path = g.base_path
	
	g.IMG_BACKGROUND = base_path+'background.png'

	g.IMG_SPLASH_SCENE = base_path+'splash_bg.png'
	g.IMG_SPLASH_BUTTON_NORMAL = base_path+'splash_btn_normal.png'
	g.IMG_SPLASH_BUTTON_PRESSED = base_path+'splash_btn_pressed.png'
	
	g.IMG_SPLASH_BACK = base_path+'background_image.png'
	g.IMG_SPLASH_BIGBTN_NORMAL = base_path+'startbtn-normal.png'
	g.IMG_SPLASH_BIGBTN_PRESS = base_path+'startbtn-press.png'

	g.IMG_TITLE_SCENE = base_path+'title_scene.png'
	g.IMG_TITLE_BTN1_NORMAL = base_path+'title_btn1_normal.png'
	g.IMG_TITLE_BTN1_PRESS = base_path+'title_btn1_pressed.png'
	g.IMG_TITLE_BTN2_NORMAL = base_path+'title_btn2_normal.png'
	g.IMG_TITLE_BTN2_PRESS = base_path+'title_btn2_pressed.png'
	g.IMG_TITLE_BTN3_NORMAL = base_path+'title_btn3_normal.png'
	g.IMG_TITLE_BTN3_PRESS = base_path+'title_btn3_pressed.png'

	g.IMG_MORE_SCENE = base_path+'more_scene.png'
	g.IMG_MORE_BTN_CHESS_NORMAL = base_path+'more_btn_chess_normal.png'
	g.IMG_MORE_BTN_CHESS_PRESS = base_path+'more_btn_chess_pressed.png'
	g.IMG_MORE_BTN_OCA_NORMAL = base_path+'more_btn_oca_normal.png'
	g.IMG_MORE_BTN_OCA_PRESS = base_path+'more_btn_oca_pressed.png'
	g.IMG_MORE_BTN_BACK_NORMAL = base_path+'more_btn_back_normal.png'
	g.IMG_MORE_BTN_BACK_PRESS = base_path+'more_btn_back_pressed.png'

	g.IMG_TUTORIAL_BTN_BACK_NORMAL = base_path+'tutorial_btn_back_normal.png'
	g.IMG_TUTORIAL_BTN_BACK_PRESS = base_path+'tutorial_btn_back_pressed.png'
	g.IMG_TUTORIAL_BTN_FORWARD_NORMAL = base_path+'tutorial_btn_forward_normal.png'
	g.IMG_TUTORIAL_BTN_FORWARD_PRESS = base_path+'tutorial_btn_forward_pressed.png'
	g.IMG_TUTORIAL_FRAME_1 = base_path+'tutorial_frame1.png'
	g.IMG_TUTORIAL_TAPIR_ALLY = base_path+'tutorial_tapir_ally.png'
	g.IMG_TUTORIAL_TAPIR_FOE = base_path+'tutorial_tapir_opponent.png'
	g.IMG_TUTORIAL_RACCOON = base_path+'tutorial_raccoon.png'
	g.IMG_TUTORIAL_RACCOON_ARROWS3 = base_path+'tutorial_raccoon_arrows3.png'
	g.IMG_TUTORIAL_FOX = base_path+'tutorial_fox.png'
	g.IMG_TUTORIAL_RACCOON_ARROWS4 = base_path+'tutorial_raccoon_arrows4.png'
	g.IMG_TUTORIAL_CARP_FOE = base_path+'tutorial_carp_opponent.png'
	g.IMG_TUTORIAL_RACCOON_ARROWS5 = base_path+'tutorial_raccoon_arrows5.png'
	g.IMG_TUTORIAL_CARP_ALLY = base_path+'tutorial_carp_ally.png'
	g.IMG_TUTORIAL_FARM_ALLY = base_path+'tutorial_farm_ally.png'
	g.IMG_TUTORIAL_PROMOTION_ZONE = base_path+'tutorial_promotion_zone.png'
	g.IMG_TUTORIAL_PROMOTION_X = base_path+'tutorial_promotion_X.png'
	g.IMG_TUTORIAL_KOI = base_path+'tutorial_koi.png'
	g.IMG_TUTORIAL_FARM_FOE = base_path+'tutorial_farm_opponent.png'

	g.IMG_PIECE_CARP = base_path+'piece_carp.png'
	g.IMG_PIECE_RACCOON = base_path+'piece_raccoon.png'
	g.IMG_PIECE_FOX = base_path+'piece_fox.png'
	g.IMG_PIECE_TAPIR = base_path+'piece_tapir.png'
	g.IMG_PIECE_KOI = base_path+'piece_koi.png'
	g.IMG_PIECE_TANUKI = base_path+'piece_tanuki.png'
	g.IMG_PIECE_KITSUNE = base_path+'piece_kitsune.png'
	g.IMG_PIECE_BAKU = base_path+'piece_baku.png'
	g.IMG_PIECE_CRANE = base_path+'piece_crane.png'
	g.IMG_PIECE_PHEASANT = base_path+'piece_pheasant.png'


	g.IMG_MAIN_BOARD = base_path+'main_board.png'
	g.IMG_MAIN_ENDBTN_2PWIN = base_path+'end_p2_win.png'
	g.IMG_MAIN_ENDBTN_1PLOSE = base_path+'end_p1_lose.png'
	g.IMG_MAIN_ENDBTN_1PWIN = base_path+'end_p1_win.png'
	g.IMG_MAIN_DOUBLE = base_path+'main_x2.png'
	g.IMG_MAIN_SLIDER_BG = base_path+'main_slider_background.png'
	g.IMG_MAIN_SLIDER_BTN = base_path+'main_slider_button.png'

	g.IMG_CONFIRM_BG = base_path+'confirm_bg.png'
	g.IMG_CONFIRM_TITLEBTN_NORMAL = base_path+'confirm_btn_title_normal.png'
	g.IMG_CONFIRM_TITLEBTN_PRESS = base_path+'confirm_btn_title_pressed.png'
	g.IMG_CONFIRM_VOLUMEBTN_NORMAL = base_path+'confirm_btn_volume_normal.png'
	g.IMG_CONFIRM_VOLUMEBTN_PRESS = base_path+'confirm_btn_volume_pressed.png'
	g.IMG_CONFIRM_YESBTN_NORMAL = base_path+'confirm_btn_yes_normal.png'
	g.IMG_CONFIRM_YESBTN_PRESS = base_path+'confirm_btn_yes_pressed.png'
	g.IMG_CONFIRM_NOBTN_NORMAL = base_path+'confirm_btn_no_normal.png'
	g.IMG_CONFIRM_NOBTN_PRESS = base_path+'confirm_btn_no_pressed.png'
	g.IMG_CONFIRM_UNDOBTN_NORMAL = base_path+'confirm_btn_undo_normal.png'
	g.IMG_CONFIRM_UNDOBTN_PRESS = base_path+'confirm_btn_undo_pressed.png'

def get_string(screen, string):
	print screen, string
	assert g.xml_root  and screen and string 
	return g.xml_root.find("./"+screen+"/string/[@name='"+string+"']").text


# Widgets

class mImage(Image):
	""" A costumization of kivy's Image widget, better prepared to deal with different screen sizes."""

	def __init__(self, size = (100,100), rpos = None, anchor = [], **kwargs):
		super(mImage,self).__init__(**kwargs)
		
		# So the image can be rendered larger then their intended resolution
		self.allow_stretch = True
		
		# It auto-corrects its size to fit the current screen size
		self.size_hint = (None,None)
		self.size = [ size[0]*g.scale, size[1]*g.scale ]
		
		# Positions are almost always given as relative coordinates, so we have to consider them.
		if rpos != None:
			self.apply_relative_position(rpos)
			
		# Images must sometimes be anchored to the sides of the screen.
		
		if 'left' in anchor:
			self.pos[0] = 0
		elif 'right' in anchor:
			self.pos[0] = g.screen_size[0] - self.size[0]
		if 'bottom' in anchor:
			self.pos[1] = 0
		elif 'top' in anchor:
			self.pos[1] = g.screen_size[1] - self.size[1]
	
	def apply_relative_position(self, rpos):
		"""This function will center the image on a given rpos."""
		x_pos = g.screen_size[0]/2 - self.size[0]/2 + rpos[0]*g.scale
		y_pos = g.screen_size[1]/2 - self.size[1]/2 + rpos[1]*g.scale
		self.pos = [x_pos, y_pos]

class SoundController():
	"""This class manages sound. You need one instance of it on the game."""
	def __init__(self):
		self.music_info_title = [g.MUSIC_THEME]
		self.music_info_game = [g.MUSIC_0]#, g.MUSIC_2, g.MUSIC_3, g.MUSIC_4, g.MUSIC_5, g.MUSIC_6]

		self.music_data_title = [ g.MUSIC_THEME ]
		self.music_data_game = [ g.MUSIC_1 ]
		
		self.music_type = 'title'
		self.current_music = 0
	
	def stop_music(self):
		if self.current_music:
			self.current_music.stop()
			self.current_music.unload()
		self.current_info = None
	
	def play_music(self, btn = None, music_type = 'title'):
		
		if g.sound == True and self.music_type == music_type:
			
			if music_type == 'title':
				self.current_info = random.choice(self.music_data_title)
				#self.current_info = random.choice( self.music_info_title )
			else:
				self.current_info = random.choice(self.music_data_game)
				#self.current_info = random.choice( self.music_info_game )
				
			#print 'music path is', self.current_info
			self.current_music = SoundLoader.load( self.current_info[0] )

			self.current_music.bind (on_stop = self.on_music_stop )
			
			
			if self.current_music:
				self.current_music.volume = 0.25
				
				Clock.schedule_once ( self.play_music, self.current_info[1] + 3.0 )
				self.current_music.play()
	
	def play_music_weak(self, btn = None, music_typei = 'title'):
		# If it is a weak call, it won't interrupt an ongoing music.
		stop = False
		
		if self.current_music:
			if self.current_music.state == 'play':
				stop = True
		
		if stop == False:
			self.play_music(music_type = music_typei)
	
	def on_music_stop(self, btn = None):
		pass
	
	def play_sound(self, sound_to_play, arg1 = None):
		"""This will play a one shot sound."""
		if g.sound:
			#sound = SoundLoader.load( sound_to_play[0] )
			#if sound_to_play == g.SOUND_SHEET:
			#	sound.volume = 0.8
			#sound.play()
			
			unload_time = 10.0
			#Clock.schedule_once( partial(self.unload_sound,sound), 10.0)
	
	def unload_sound(self,sound_to_unload,time_elapsed):
		sound_to_unload.unload()
		
	
	
	
	
	
	
	
	
