import kivy
kivy.require('1.8.0')
from kivy.animation import Animation

from functools import partial
import random

import g

#All animations suppose the widgets use absolute positioning. This means the origin point must be adapted during animation.
#The animations can be timed to three circumstances: 1st, to a set number of loops, 2nd, to a set time, and, finally, it can be in an infinite loop (which can be broken). The end function will be called 1 fewer times than the loop count.
#If both time and count caps are enabled, the animation will end as soon as any of them ends. If None of them are set, then the loop is infinite.



def dispel(widget, now = False, arg1 = None, arg2 = None):
	"""It will stop all current animations (not only oa animations, so be careful) on a widget, and return it to its original attributes."""
	Animation.cancel_all(widget)
	
	if now:
		if hasattr( widget, 'oa_original_size' ):
			widget.size = widget.oa_original_size
		if hasattr( widget, 'oa_original_pos' ):
			widget.pos = widget.oa_original_pos
	else:
		anim = Animation(duration = 0.1)
		if hasattr( widget, 'oa_original_size' ):
			anim &= Animation( size = widget.oa_original_size )
		if hasattr( widget, 'oa_original_pos' ):
			anim &= Animation( pos = widget.oa_original_pos )
		anim.start(widget)
	

def jiggle(widget, end_func = None, loop_func = None, duration = None, loops = None, keep_bottom = False, first_call = True, arg1 = None, arg2 = None ):
	"""The widget will get a little bigger, then a little smaller, then return to its original size."""
	
	current_duration = duration
	current_loops = loops
	current_keep_bottom = keep_bottom
	
	if first_call:
		widget.oa_original_size = widget.size[:]
		widget.oa_original_pos = widget.pos[:]
	
	#Let's see if we go another loop or if we end the animation now.
	end_anim = False
	sx = 0.8
	
	# If time is up, end animation
	if duration != None:
		if duration < 0.0:
			end_anim = True
		else:
			current_duration = current_duration - 0.4*sx
			
	# If count is up, end animation
	if loops != None:
		if loops <= 1:
			end_anim = True
		else:
			current_loops -= 1

	# If it is in a loop, it acts as a recursive function. It will play the loop_func, but it won't play end_func.
	if end_anim == False:
		if loop_func != None and first_call == False:
			loop_func()
	
		big_size = ( widget.size[0]*1.03, widget.size[1]*1.03 )
		big_x = widget.pos[0] - (big_size[0]-widget.oa_original_size[0])/2
		if keep_bottom:
			big_y = widget.y
		else:
			big_y = widget.pos[1] - (big_size[1]-widget.oa_original_size[1])/2
		big_pos = (big_x,big_y)
	
		small_size = ( widget.oa_original_size[0]*0.97, widget.oa_original_size[1]*0.97 )
		small_x = widget.oa_original_pos[0] - (small_size[0]-widget.oa_original_size[0])/2
		small_y = widget.oa_original_pos[1] - (small_size[1]-widget.oa_original_size[1])/2
		small_pos = (small_x,small_y)

		anim_jiggle = Animation( size = big_size, pos = big_pos, duration = 0.1*sx, t = 'out_cubic' )
		anim_jiggle += Animation( size = small_size, pos = small_pos, duration = .2*sx, t = 'in_out_cubic' )
		anim_jiggle += Animation( size = widget.oa_original_size, pos = widget.oa_original_pos, duration = .1*sx, t = 'in_cubic' )

		anim_jiggle.bind( on_complete = partial( jiggle, widget, end_func, loop_func, current_duration, current_loops, current_keep_bottom, False ) )

		anim_jiggle.start(widget)
	# If it is not on a loop
	else:
		#If it is time to end, play end_func
		if end_func != None:
			end_func()
	
def tremble(widget, end_func = None, loop_func = None, duration = None, loops = None, first_call = True, arg1 = None, arg2 = None ):
	"""The widget will rapidly move to random near positions, imitating a tremble effect. It will return to its original position afterwards."""

	current_duration = duration
	current_loops = loops
	sx = 1.0
	
	if first_call:
		widget.oa_original_pos = widget.pos[:]
	
	#Let's see if we go another loop or if we end the animation now.
	end_anim = False

	# If time is up, end animation
	if duration != None:
		if duration < 0.0:
			end_anim = True
		else:
			current_duration = current_duration - 0.1*sx
			
	# If count is up, end animation
	if loops != None:
		if loops <= 1:
			end_anim = True
		else:
			current_loops -= 1


	# If it is in a loop, it acts as a recursive function. It will play the loop_func, but it won't play end_func.
	if end_anim == False:
		if loop_func != None and first_call == False:
			loop_func()

		new_x =  widget.oa_original_pos[0] + (random.randint(-10,10)*random.random() )*g.scale
		new_y =  widget.oa_original_pos[1] + (random.randint(-10,10)*random.random() )*g.scale
		new_pos = (new_x,new_y)
	
		anim = Animation( pos = new_pos, duration = 0.05*sx, t = 'in_quint' )
		anim += Animation( pos = widget.oa_original_pos, duration = 0.05*sx, t = 'in_quint' )
		anim.bind( on_complete = partial( tremble, widget, end_func, loop_func, current_duration, current_loops, False ) )
		anim.start(widget)

	else:
		#If it is time to end, return to orginal position and play end_func
		if end_func != None:
			end_func()
	
	
	
def flip(widget, end_func = None, loop_func = None, duration = None, loops = None, orientation = 'horizontal', half_func = None, first_call = True, arg1 = None, arg2 = None, arg3 = None ):
	"""The widget will have a dimension reduced to zero, then run loop func, then have the dimension size restore. This is made to creat the illusion of it spinning."""

	current_duration = duration
	current_loops = loops
	current_orientation = orientation
	sx = 3.0
	
	if first_call:
		widget.oa_original_pos = widget.pos[:]
		widget.oa_original_size = widget.size[:]
	
	#Let's see if we go another loop or if we end the animation now.
	end_anim = False

	# If time is up, end animation
	if duration != None:
		if duration < 0.0:
			end_anim = True
		else:
			current_duration = current_duration - 0.1*sx
			
	# If count is up, end animation
	if loops != None:
		if loops <= 1:
			end_anim = True
		else:
			current_loops -= 1

	# If it is in a loop, it acts as a semi-recursive function, calling the flop function. It will play the loop_func, but it won't play end_func.
	if end_anim == False:
		if loop_func != None and first_call==False:
			loop_func()

		if orientation == 'horizontal':
			new_x = widget.oa_original_pos[0] + widget.oa_original_size[0]/2
			new_pos = (new_x, widget.oa_original_pos[1])
			anim = Animation( pos = new_pos, size = (0,widget.oa_original_size[1]), duration = 0.1*sx, t = 'in_quad' )
		elif orientation == 'vertical':
			new_y = widget.oa_original_pos[1] + widget.oa_original_size[1]/2
			new_pos = (widget.oa_original_pos[0], new_y)
			anim = Animation( pos = new_pos, size = (widget.oa_original_size[0],0), duration = 0.1*sx, t = 'in_quad' )

		#anim = Animation( pos = new_pos, size = (0,widget.oa_original_size[1]), duration = 0.1*sx, t = 'in_quad' )
		anim.bind( on_complete = partial( flop, widget, end_func, loop_func, current_duration, current_loops, current_orientation, half_func ) )
		anim.start(widget)

	else:
		#If it is time to end, return to orginal position and play end_func
		if end_func != None:
			end_func()
			
def flop(widget, end_func = None, loop_func = None, duration = None, loops = None, orientation = 'horizontal', half_func = None, arg1 = None, arg2 = None, arg3 = None ):
	
	
	"""The exact opposite of the flip function, this will increase instead of decrease the widget's size."""

	current_duration = duration
	current_loops = loops
	current_orientation = orientation
	sx = 3.0
	
	#Let's see if we go another loop or if we end the animation now.
	end_anim = False

	# If time is up, end animation
	if duration != None:
		if duration < 0.0:
			end_anim = True
		else:
			current_duration = current_duration - 0.1*sx
			
	# If count is up, end animation
	if loops != None:
		if loops <= 1:
			end_anim = True
		else:
			current_loops -= 1

	if orientation == 'horizontal':
		new_x = widget.oa_original_pos[0] + widget.oa_original_size[0]/2
		new_pos = (new_x, widget.oa_original_pos[1])
	elif orientation == 'vertical':
		new_y = widget.oa_original_pos[1] + widget.oa_original_size[1]/2
		new_pos = (widget.oa_original_pos[0], new_y)


	anim = Animation( pos = widget.oa_original_pos, size = widget.oa_original_size, duration = 0.1*sx, t = 'in_quad' )
	anim.bind( on_complete = partial( flip, widget, end_func, loop_func, current_duration, current_loops, current_orientation, half_func, False ) )
	anim.start(widget)


	if half_func != None:
		#print '@3', half_func
		half_func()
	# If it is in a loop, it acts as a recursive function. It will play the loop_func, but it won't play end_func.
	#print '@1', half_func
	if end_anim == False:
		pass
		#print '@2', half_func
		#if half_func != None:
		#	print '@3', half_func
		#	half_func()
	else:
		#If it is time to end, return to original position and play end_func
		if end_func != None:
			end_func()	
	
	
def jump(widget, end_func = None, loop_func = None, duration = None, loops = None, first_call = True, arg1 = None, arg2 = None ):
	"""The widget will get a little bigger, then a little smaller, then return to its original size."""
	
	current_duration = duration
	current_loops = loops
	
	if first_call:
		widget.oa_original_size = widget.size[:]
		widget.oa_original_pos = widget.pos[:]
	
	#Let's see if we go another loop or if we end the animation now.
	end_anim = False
	sx = 1.2
	
	# If time is up, end animation
	if duration != None:
		if duration < 0.0:
			end_anim = True
		else:
			current_duration = current_duration - 0.4*sx
			
	# If count is up, end animation
	if loops != None:
		if loops <= 0:
			end_anim = True
		else:
			current_loops -= 1

	# If it is in a loop, it acts as a recursive function. It will play the loop_func, but it won't play end_func.
	if end_anim == False:
		#if loop_func != None and first_call == False:
		#	loop_func()
			
			
		down_size = ( widget.oa_original_size[0]*1.15, widget.oa_original_size[1]*0.65 )
		down_x = widget.oa_original_pos[0] - ( down_size[0] - widget.oa_original_size[0] )/2
		down_pos = (down_x, widget.oa_original_pos[1])
		
		#up_size = ( widget.size[0]*0.8, widget.size[1]*1.1 )
		#up_x = widget.oa_original_pos[0] + ( widget.size[0] - widget.size[0]*0.8 )/2
		#up_y = widget.oa_original_pos[1]*1.05
		#up_pos = (up_x, up_y)
		
		anim_jump = Animation( size = down_size, pos = down_pos, duration = 0.1*sx)
		#anim_jump += Animation( size = up_size, pos = up_pos, duration = 0.2*sx)
		#anim_jump += Animation( size = widget.oa_original_size, pos = widget.oa_original_pos, duration = .1*sx)

		#anim_jump.bind( on_complete = partial( jump, widget, end_func, loop_func, current_duration, current_loops, False ) )
		anim_jump.bind( on_complete = partial( jump_back, widget, end_func, loop_func, current_duration, current_loops, first_call ) )

		anim_jump.start(widget)
	# If it is not on a loop
	else:
		#If it is time to end, play end_func
		if end_func != None:
			anim = Animation( size = widget.oa_original_size, pos = widget.oa_original_pos, duration = 0.1)
			anim.start(widget)
			end_func()

def jump_back(widget, end_func = None, loop_func = None, duration = None, loops = None, first_call = True, arg1 = None, arg2 = None ):
	current_duration = duration
	current_loops = loops
	sx = 1.2

	if loop_func != None and first_call == False:
		loop_func()

	up_size = ( widget.oa_original_size[0]*0.80, widget.oa_original_size[1]*1.02 )
	up_x = widget.oa_original_pos[0] + ( widget.oa_original_size[0] - up_size[0] )/2
	up_y = widget.oa_original_pos[1]+20*g.scale
	up_pos = (up_x, up_y)

	anim_jump = Animation( size = up_size, pos = up_pos, duration = 0.2*sx)
	#anim_jump += Animation( size = widget.oa_original_size, pos = widget.oa_original_pos, duration = .1*sx)
	
	anim_jump.bind( on_complete = partial( jump, widget, end_func, loop_func, current_duration, current_loops, False ) )
	anim_jump.start(widget)


def pop(widget, end_func = None, loop_func = None, duration = None, loops = None, keep_bottom = False, first_call = True, arg1 = None, arg2 = None ):
	"""This function assumes the widget has opacity 0 It will shrink it and then make it bigger and opaque in one pop. If there are loops, each loop will shrink it and pop it again."""
	
	current_duration = duration
	current_loops = loops
	current_keep_bottom = keep_bottom
	
	if first_call:
		widget.oa_original_size = widget.size[:]
		widget.oa_original_pos = widget.pos[:]
	
	#Let's see if we go another loop or if we end the animation now.
	end_anim = False
	sx = 2
	
	# If time is up, end animation
	if duration != None:
		if duration < 0.0:
			end_anim = True
		else:
			current_duration = current_duration - 0.4*sx
			
	# If count is up, end animation
	if loops != None:
		if loops <= 1:
			end_anim = True
		else:
			current_loops -= 1

	widget.size = (0,0)
	micro_pos = (widget.oa_original_pos[0]+widget.oa_original_size[0]/2, widget.oa_original_pos[1]+widget.oa_original_size[1]/2)
	widget.pos = micro_pos[:]
	widget.opacity = 1.0

	if loop_func != None and first_call == False:
		loop_func()
	
	bigger_size = ( widget.oa_original_size[0]*1.2, widget.oa_original_size[1]*1.2 )
	bigger_x = widget.oa_original_pos[0] - (bigger_size[0]-widget.oa_original_size[0])/2
	if keep_bottom:
		bigger_y = widget.y
	else:
		bigger_y = widget.oa_original_pos[1] - (bigger_size[1]-widget.oa_original_size[1])/2
	bigger_pos = (bigger_x,bigger_y)
	
	#anim_pop = Animation( size = widget.oa_original_size, pos = widget.oa_original_pos, duration = .3*sx )
	#anim_opacity = Animation( opacity = 1.0, duration = .3*sx )
	
	if end_anim == False:
		bigger_size = ( widget.oa_original_size[0]*1.1, widget.oa_original_size[1]*1.1 )
		bigger_x = widget.oa_original_pos[0] - (bigger_size[0]-widget.oa_original_size[0])/2
		if keep_bottom:
			bigger_y = widget.y
		else:
			bigger_y = widget.oa_original_pos[1] - (bigger_size[1]-widget.oa_original_size[1])/2
		bigger_pos = (bigger_x,bigger_y)

		anim_pop = Animation( size = bigger_size, pos = bigger_pos, duration = 0.3*sx )
		anim_pop &= Animation( opacity = 0.0, duration = .2*sx, t='in_quad' )
		anim_pop.bind( on_complete = partial( pop, widget, end_func, loop_func, current_duration, current_loops, current_keep_bottom, False ) )
			
			
	else:
		anim_pop = Animation( size = widget.oa_original_size, pos = widget.oa_original_pos, duration = .3*sx )
		if end_func != None:
			anim_pop.bind( on_complete = end_func )
			
	anim_pop.start(widget)
	#anim_opacity.start(widget)


def move_to (widget, target_pos = (0,0), end_func = None, arg1 = None, arg2 = None ):
	anim = Animation( pos=target_pos, duration = 0.3)#, t = 'out_back' )
	anim.start(widget)
	if end_func != None:
		anim.bind( on_complete = end_func )

def move_to_fast (widget, target_pos = (0,0), end_func = None, arg1 = None, arg2 = None ):
	anim = Animation( pos=target_pos, duration = 0.05)#, t = 'out_back' )
	anim.start(widget)
	if end_func != None:
		anim.bind( on_complete = end_func )

def fade_in(widget, end_func = None, arg1 = None, arg2 = None ):
	anim = Animation( opacity = 1.0, duration = 0.3)#, t = 'out_back' )
	anim.start(widget)
	if end_func != None:
		anim.bind( on_complete = end_func )

def fade_out(widget, end_func = None, arg1 = None, arg2 = None ):
	anim = Animation( opacity = 0.0, duration = 0.3)#, t = 'out_back' )
	anim.start(widget)
	if end_func != None:
		anim.bind( on_complete = end_func )
	
	
	
	
	
	
	
	
	
	
	
	