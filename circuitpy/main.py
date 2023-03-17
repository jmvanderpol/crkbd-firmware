from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.hid import HIDModes
from kmk.handlers.sequences import send_string
import supervisor
from kmk.extensions.peg_oled_Display import Oled,OledDisplayMode,OledReactionType,OledData
from kmk.extensions.peg_rgb_matrix import Rgb_matrix
from kmk.modules.split import Split, SplitSide, SplitType
keyboard = KMKKeyboard()
modtap = ModTap()
layers_ext = Layers()
keyboard.modules.append(layers_ext)
keyboard.modules.append(modtap)
# oled
oled_ext = Oled(OledData(corner_one={0:OledReactionType.LAYER,1:["1 2 3","1 2 3","","","","","",""]},corner_two={0:OledReactionType.LAYER,1:["--Layer--","--Layer--","","","","","",""]},corner_three={0:OledReactionType.LAYER,1:["^","  ^","","","","","",""]},corner_four={0:OledReactionType.LAYER,1:["  Normal","  Raised","","","","","",""]}),toDisplay=OledDisplayMode.TXT,flip= True)
# oled
keyboard.extensions.append(oled_ext)
# ledmap
rgb_ext = Rgb_matrix(ledDisplay=[[255,255,255],[255,0,242],[255,0,242],[255,0,242],[255,0,242],[255,0,242],[255,0,242],[255,0,242],[255,0,242],[255,0,242],[255,0,242],[255,0,242],[255,255,255],[56,0,131],[56,0,131],[56,0,131],[56,0,131],[56,0,131],[56,0,131],[56,0,131],[56,0,131],[56,0,131],[56,0,131],[56,0,131],[255,255,255],[0,212,255],[0,212,255],[0,212,255],[0,212,255],[0,212,255],[0,212,255],[0,212,255],[0,212,255],[0,212,255],[0,212,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,0,242],[255,0,242],[255,0,242],[255,0,242],[255,0,242],[255,0,242],[0,212,255],[0,212,255],[0,212,255],[0,212,255],[0,212,255],[0,212,255]],split=True,rightSide=False,disable_auto_write=True)
# ledmap
keyboard.extensions.append(rgb_ext)
# TODO Comment one of these on each side
#split_side = SplitSide.LEFT
#split_side = SplitSide.RIGHT
split = Split(use_pio=True)
keyboard.modules.append(split)

# keymap
keyboard.keymap = [ [KC.ESCAPE,KC.Q,KC.W,KC.E,KC.R,KC.T,KC.Y,KC.U,KC.I,KC.O,KC.P,KC.BSLASH,KC.TAB,KC.A,KC.S,KC.D,KC.F,KC.G,KC.H,KC.J,KC.K,KC.L,KC.SCOLON,KC.ENTER,KC.LSHIFT,KC.Z,KC.X,KC.C,KC.V,KC.B,KC.N,KC.M,KC.COMMA,KC.DOT,KC.SLASH,KC.MO(1),KC.LCTRL,KC.LGUI,KC.SPACE,KC.BSPC,KC.LBRACKET,KC.RBRACKET,KC.RALT,KC.NO], 
[KC.GRAVE,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,KC.N6,KC.N7,KC.N8,KC.N9,KC.N0,KC.MINUS,KC.TAB,KC.LEFT,KC.UP,KC.DOWN,KC.RIGHT,KC.QUOTE,KC.PGUP,KC.PGDOWN,KC.HOME,KC.END,KC.EQUAL,KC.ENTER,KC.LSHIFT,KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,KC.F6,KC.F7,KC.F8,KC.F9,KC.F10,KC.MO(0),KC.LCTRL,KC.LALT,KC.SPACE,KC.RGUI,KC.LEFT_CURLY_BRACE,KC.RIGHT_CURLY_BRACE,KC.RALT,KC.NO], 
[KC.NO,KC.NO,KC.AT,KC.HASH,KC.NO,KC.NO,KC.KP_7,KC.KP_8,KC.KP_9,KC.KP_MINUS,KC.KP_SLASH,KC.BSPC,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.KP_4,KC.KP_5,KC.KP_6,KC.KP_PLUS,KC.KP_ASTERISK,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.KP_1,KC.KP_2,KC.KP_3,KC.KP_ENTER,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.KP_0,KC.KP_DOT,KC.RALT,KC.NO], 
[KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.RALT,KC.NO], 
[KC.MO(1),KC.MO(2),KC.RGB_TOG,KC.E,KC.R,KC.T,KC.Y,KC.U,KC.I,KC.O,KC.P,KC.BSPC,KC.ENTER,KC.A,KC.S,KC.D,KC.F,KC.G,KC.H,KC.J,KC.K,KC.L,KC.NO,KC.NO,KC.NO,KC.Z,KC.X,KC.C,KC.V,KC.B,KC.N,KC.M,KC.NO,KC.DOT,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.RALT,KC.NO], 
[KC.NO,KC.NO,KC.AT,KC.HASH,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.BSPC,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.PIPE,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.PLUS,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.RALT,KC.NO], 
[KC.NO,KC.NO,KC.AT,KC.HASH,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.BSPC,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.PIPE,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.PLUS,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.RALT,KC.NO], 
[KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.RALT,KC.NO] ] 
# keymap
if __name__ == '__main__': 
    keyboard.go(hid_type=HIDModes.USB)