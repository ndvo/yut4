# This will hold information about the screens during runtime. This stub is just a reminder of that.
board = [0]*10
status = 0
turn = 0
screens = {}

app = None
is_android = False

# Connection to database (stub)
conn = None

# Ads variables
ad_count = 0
ad_count_limit = 5
adbuddiz_code = 'TEST_PUBLISHER_KEY'
do_cache_ads = True

# The size of the screen, specially useful if running on Android.
# If True, will use images from 'default_image_path' below
force_resolution = False
# Path used if force_resolution == True
default_image_path = './res/drawable/'
# Stub. According to the detected screen size, it will choose the appropriate path.
base_path = './res/drawable/'
# Some images will change with version, so we keep track of it.
current_version = '1-0-2'
current_version_human = '1.0.2'
current_resolution_human = 'regular'

#The screen_size when running from the PC.
screen_size = (360,640) #normal
#screen_size = (360+180,640+320) #x1.5
#screen_size = (720,1280) #x2
#screen_size = (1080,1920) #x3
#screen_size = (1440,2560) #x4

#screen_size = (600, 1028) # 7 inch
#screen_size = (1120, 1792) # 10 inch
#screen_size = (1920, 1080) # tv

ssx = 0
ssy = 0
screen_size = ( screen_size[0]+ssx, screen_size[1]+ssy )

# Very Important! How big is the screen compared with the default (360x640).
# Images and fonts are scaled according to it all over the program.
scale = 1.0

# How long it takes for the button to apper in the splashscreen
splash_time = 2.0

# If the game has ended
end_game = False
force_end_game = False

piece_size = 85


# To see if there is a modal screen open
modal_screen = False
# Sound stuff
# If sound is on or off
sound = True
# A stub for the unique instance of sound controller class
sound_controller = None
# Just to communicate when the king is dead
game_over = False

# This will hold all game strings
xml_path = './res/values/strings.xml'
#xml_path = './res/values-pt/strings.xml'
xml_root = None

# GAME CONSTANTS - standards.
COLOR_BLACK = (0,0,0,1)
COLOR_BLACK_ALPHA_50 = (0,0,0,0.5)
COLOR_BLACK_ALPHA_40 = (0,0,0,0.4)
COLOR_BLUE = (0.43,0.57,0.71,1)
#COLOR_BROWN = (0.56,0.64,0.35,1.0)
#COLOR_BROWN_LIGHT = (0.22,0.46,0.03,1.0)
#COLOR_BROWN_LIGHT_ALPHA_50 = (0.22,0.46,0.03,0.5)
#COLOR_BROWN_DARK = (0.24,0.31,0.16,1.0)
#COLOR_BROWN = (0.58, 0.52, 0.45, 1.0)
COLOR_GOLDEN = (0.8,0.8, 0.1,1)
COLOR_GRAY_DARK = (0.4,0.4,0.4,1.0)
COLOR_PURPLE = (0.56,0.29,0.65,1.0)
COLOR_TRANSPARENT = (1,1,1,0)
COLOR_WHITE = (1,1,1,1)
COLOR_WHITE_ALPHA_50 = (1,1,1,.50)
COLOR_WHITE_ALPHA_25 = (1,1,1,.25)
COLOR_BLUE = (0.61, 0.61, 0.7, 1)

COLOR_BROWN = (0.816, 0.703, 0.598, 1.)
COLOR_BROWN_LIGHT = (0.916, 0.803, 0.698, 1.)
COLOR_BROWN_60 = (0.816, 0.703, 0.598, .6)

COLOR_BROWN_DARK = (0.816, 0.703, 0.8, 1.)
COLOR_BLUE_DARK = (0.43,0.57,0.91,1)

FONT_CB = './res/fonts/Comfortaa-Bold.ttf'
FONT_CR = './res/fonts/Comfortaa-Regular.ttf'
FONT_IN = './res/fonts/intuitive.ttf'
MUSIC_THEME = 'res/sounds/pdsound_applause.mp3'
MUSIC_0 = 'res/sounds/pdsound_applause.mp3'
MUSIC_1 = 'res/sounds/pdsound_applause.mp3'
MUSIC_2 = 'res/sounds/pdsound_applause.mp3'
MUSIC_3 = 'res/sounds/pdsound_applause.mp3'
MUSIC_4 = 'res/sounds/pdsound_applause.mp3'
SOUND_SHEET = 'res/sounds/pdsound_applause.mp3'
SOUND_BUTTON = 'res/sounds/pdsound_applause.mp3'
