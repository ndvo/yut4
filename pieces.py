import g
import kivy
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image


class Piece(Scatter):
	imgsrc = ["piece_fox.png","piece_fox.png"]
	def __init__(self, **kwargs):
		super(Piece, self).__init__(**kwargs)
		self.board = kwargs['board']
		self.image = Image(
			source='res/drawable/'+self.imgsrc[kwargs['player']],
			size_hint=(None,None),
			size=(50,50)
			)
		self.add_widget(self.image)
		self.size_hint = (None,None)
		self.size = (50,50)
		self.x = 300
		self.y = 200
		try:
			self.player = player
		except:
			self.player = None
		self.active = False

	def on_touch_move(self, touch):
		super(Piece,self).on_touch_move(touch)
		digest = False
		if self.collide_point(touch.x, touch.y):
			self.board.set_arrows(self)
		return digest

	def on_touch_down(self, touch):
		super(Piece,self).on_touch_down(touch)
		digest = False
		digest=False
		if self.collide_point(touch.x, touch.y):
			self.active = True
			digest = True
		return digest

	def on_touch_up(self, touch):
		super(Piece,self).on_touch_up(touch)
		digest = False
		if self.collide_point(touch.x, touch.y):
			#TODO: self.present_movement_options()
			pass
		self.active = False
		return digest



class Stick(Scatter):
	imgsrc = ['title_btn3_pressed.png']
	def __init__(self, **kwargs):
		super(Piece, self).__init__(**kwargs)
		self.board = kwargs['board']
		self.add_widget(Image(source= 'res/drawable/'+self.imgsrc[0]))
		self.size_hint = (None,None)
		self.size = (200,50)
		self.x = 300
		self.y = 50
		self.do_rotation = False
		self.do_scale = False
		try:
			self.player = player
		except:
			self.player = None
		self.active = False

	def on_touch_move(self, touch):
		super(Piece,self).on_touch_move(touch)
		digest = False
		self.collide_point(touch.x, touch.y)
		return digest

	def on_touch_down(self, touch):
		super(Piece,self).on_touch_down(touch)
		digest = False
		digest=False
		if self.collide_point(touch.x, touch.y):
			self.active = True
			digest = True
		return digest

	def on_touch_up(self, touch):
		super(Piece,self).on_touch_up(touch)
		digest = False
		if self.collide_point(touch.x, touch.y):
			#TODO: self.present_movement_options()
			pass
		self.active = False
		return digest


