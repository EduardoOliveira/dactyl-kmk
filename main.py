print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.consts import UnicodeMode
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide
from kmk.modules.holdtap import HoldTap
from kmk.modules.tapdance import TapDance
from kmk.modules.oneshot import OneShot

from kmk.handlers.sequences import simple_key_sequence
from kmk.extensions.media_keys import MediaKeys


keyboard = KMKKeyboard()
layers = Layers()
keyboard.modules.append(layers)
split = Split( 
    split_flip=True, 
    split_side=SplitSide.LEFT,
    data_pin=board.GP17,  # The primary data pin to talk to the secondary device with
    data_pin2=board.GP16,  # Second uart pin to allow 2 way communication
    )
keyboard.modules.append(split)
oneshot = OneShot()
# oneshot.tap_time = 1500
keyboard.modules.append(oneshot)
keyboard.extensions.append(MediaKeys())

holdtap = HoldTap()
holdtap.tap_time = 1
keyboard.modules.append(holdtap)


#homerow mods
LCTL_A = KC.HT(KC.A, KC.LCTRL)
LSFT_S = KC.HT(KC.S, KC.LSFT)
LALT_D = KC.HT(KC.D, KC.LALT)
LGUI_F = KC.HT(KC.F, KC.LGUI)


LCTL_L = KC.HT(KC.L, KC.LCTRL)
LSFT_K = KC.HT(KC.K, KC.LSFT)
LALT_J = KC.HT(KC.J, KC.LALT)
LGUI_H = KC.HT(KC.H, KC.LGUI)
#homerow mods

tapdance = TapDance()
tapdance.tap_time = 750
keyboard.modules.append(tapdance)

LAYERTD = KC.TD(

)

keyboard.debug_enabled = True
keyboard.col_pins = (board.GP14,board.GP13,board.GP12,board.GP11,board.GP10,board.GP9,)
keyboard.row_pins = (board.GP26,board.GP22,board.GP21,board.GP20,board.GP19,board.GP18,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.unicode_mode = UnicodeMode.WINC



CC = simple_key_sequence(
        (
                KC.LALT(no_release=True),
                KC.MACRO_SLEEP_MS(30),
                KC.KP_1,
                KC.KP_3,
                KC.KP_5,
                KC.MACRO_SLEEP_MS(30),
                KC.LALT(no_press=True),
        )
)

CL = simple_key_sequence(
        (
                KC.LGUI(no_release=True),
                KC.MACRO_SLEEP_MS(30),
                KC.SPACE,
                KC.MACRO_SLEEP_MS(30),
                KC.LGUI(no_press=True),
        )
)


OSLCTL = KC.OS(KC.LCTRL,tap_time=750)
OSLSFT = KC.OS(KC.LSFT,tap_time=750)
OSLALT = KC.OS(KC.LALT,tap_time=750)
OSLGUI = KC.OS(KC.LGUI,tap_time=750)

_ = KC.NO
xx = KC.TRNS

keyboard.keymap = [
    [
        KC.ESCAPE,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,            KC.N6,KC.N7,KC.N8,KC.N9,KC.N0,KC.BSLS,
        KC.GRAVE,KC.Q,KC.W,KC.E,KC.R,KC.T,                  KC.Y,KC.U,KC.I,KC.O,KC.P,KC.EQL,
        KC.TAB,LCTL_A,LSFT_S,LALT_D,LGUI_F,KC.G,            LGUI_H,LALT_J,LSFT_K,LCTL_L,KC.SCLN,KC.QUOTE,
        KC.LSFT,KC.Z,KC.X,KC.C,KC.V,KC.B,                   KC.N,KC.M,KC.COMM,KC.DOT,KC.SLSH,KC.MINS,
        _,_,  KC.LGUI,KC.LCTL,KC.MO(1),_,                   _,KC.MO(2),KC.LBRC,KC.RBRC,_,_,
        _,_,  KC.LSFT,KC.ENTER,KC.SPACE,KC.BSPC,                  KC.ENTER,KC.BSPC,KC.D,KC.C,_,_,
    ],
    [
        KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,                      KC.F6,KC.F7,KC.F8,KC.F9,KC.F10,KC.F11,KC.F12,
        xx,xx,KC.MPRV,KC.MPLY,KC.MNXT,KC.VOLU,              KC.HOME,KC.END,xx,xx,xx,xx,
        xx,OSLCTL,OSLSFT,OSLALT,OSLGUI,KC.VOLD,             KC.LEFT,KC.DOWN,KC.UP,KC.RIGHT,xx,xx,
        xx,xx,xx,xx,xx,KC.MUTE,                             KC.LCTL(KC.LSFT(KC.LEFT)),KC.LCTL(KC.LSFT(KC.RIGHT)),KC.LALT(KC.LEFT),KC.LALT(KC.RIGHT),xx,xx,
        _,_,xx,xx,KC.MO(1), _,                              _,KC.MO(2),xx,xx,_,_,
        _,_,  xx,xx,xx,xx,                                 xx,KC.DELETE,xx,xx, _,_,
    ],
    [
        xx,xx,xx,xx,xx,xx,                                  xx,xx,xx,xx,xx,xx,
        xx,xx,xx,xx,xx,xx,                                  KC.PIPE,KC.BSLS,KC.RBRC,KC.RCBR,xx,xx,
        xx,xx,xx,xx,xx,xx,                                  xx,xx,xx,xx,xx,xx, 
        xx,xx,xx,CC,xx,xx,                                  xx,xx,xx,xx,xx,xx,
        _,_,xx,xx,KC.MO(1),_,                               _,KC.MO(2),xx,xx,_,_,
        _,_,  xx,xx,CL,xx,                                  xx,xx,xx,xx, _,_,
    ]
    
]

if __name__ == '__main__':
    keyboard.go()