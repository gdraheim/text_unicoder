#! /usr/bin/python3
from __future__ import print_function

__copyright__ = "(C) 2021-2024 Guido U. Draheim, licensed under the APLv2"
__version__ = "1.2.3147"

from typing import List, Dict, Generator, Tuple
from io import StringIO
import sys
import logging

logg = logging.getLogger("UNICODER")

if True:
    norm_base_A = ord('A')
    norm_base_Z = ord('Z')
    norm_base_a = ord('a')
    norm_base_z = ord('z')
    norm_base_0 = ord('0')
    norm_base_9 = ord('9')
    norm_base_sz = 0xDF
    ital_base_A = 0x1D434
    ital_base_Z = 0x1D44D
    ital_base_a = 0x1D44E
    ital_base_z = 0x1D467
    ital_sans_A = 0x1D608
    ital_sans_Z = 0x1D621
    ital_sans_a = 0x1D622
    ital_sans_z = 0x1D63B
    bold_base_A = 0x1D400
    bold_base_Z = 0x1D419
    bold_base_a = 0x1D41A
    bold_base_z = 0x1D433
    bold_base_0 = 0x1D7CE
    bold_base_9 = 0x1D7D7
    bold_ital_base_A = 0x1D468
    bold_ital_base_Z = 0x1D481
    bold_ital_base_a = 0x1D482
    bold_ital_base_z = 0x1D49B
    #
    norm_sans_A = 0x1D5A0
    norm_sans_Z = 0x1D5B9
    norm_sans_a = 0x1D5BA
    norm_sans_z = 0x1D5D3
    norm_sans_0 = 0x1D7E2
    norm_sans_9 = 0x1D7EB
    bold_sans_A = 0x1D5D4
    bold_sans_Z = 0x1D5ED
    bold_sans_a = 0x1D5EE
    bold_sans_z = 0x1D607
    bold_sans_0 = 0x1D7EC
    bold_sans_9 = 0x1D8F5
    ital_sans_A = 0x1D608
    ital_sans_Z = 0x1D621
    ital_sans_a = 0x1D622
    ital_sans_z = 0x1D63B
    bold_ital_sans_A = 0x1D63C
    bold_ital_sans_Z = 0x1D655
    bold_ital_sans_a = 0x1D656
    bold_ital_sans_z = 0x1D66F
    bold_sans_A = 0x1D5D4
    bold_sans_Z = 0x1D5ED
    bold_sans_a = 0x1D5EE
    bold_sans_z = 0x1D607
    #
    norm_fraktur_A = 0x1D504
    norm_fraktur_Y = 0x1D51C
    norm_fraktur_a = 0x1D51E
    norm_fraktur_z = 0x1D537
    bold_fraktur_A = 0x1D56C
    bold_fraktur_Z = 0x1D585
    bold_fraktur_a = 0x1D586
    bold_fraktur_z = 0x1D59F
    # ital_fraktur_A = 0x1D56C
    # ital_fraktur_Z = 0x1D585
    # ital_fraktur_a = 0x1D586
    # ital_fraktur_z = 0x1D59F
    # bold_ital_fraktur_A = n/a
    # bold_ital_fraktur_Z = n/a
    # bold_ital_fraktur_a = n/a
    # bold_ital_fraktur_z = n/a
    #
    norm_script_A = 0x1D49C
    norm_script_Z = 0x1D4B5
    norm_script_a = 0x1D4B6
    norm_script_z = 0x1D4CF
    bold_script_A = 0x1D4D0
    bold_script_Z = 0x1D4E9
    bold_script_a = 0x1D4EA
    bold_script_z = 0x1D503
    #
    norm_double_A = 0x1D538
    norm_double_Y = 0x1D550
    norm_double_a = 0x1D552
    norm_double_z = 0x1D56B
    norm_double_0 = 0x1D7D8
    norm_double_9 = 0x1D7E1
    norm_mono_A = 0x1D670
    norm_mono_Z = 0x1D689
    norm_mono_a = 0x1D68A
    norm_mono_z = 0x1D6A3
    norm_mono_0 = 0x1D7F6
    norm_mono_9 = 0x1D7FF
    norm_parens_A = 0x1F110   # PARENTHESIZED CAPITAL
    norm_parens_O = 0x1F11E   # PARENTHESIZED CAPITAL
    norm_parens_Z = 0x1F129   # PARENTHESIZED CAPITAL
    norm_parens_a = 0x249C    # PARENTHESIZED SMALL
    norm_parens_o = 0x24AA    # PARENTHESIZED SMALL
    norm_parens_z = 0x24B5    # PARENTHESIZED SMALL
    norm_parens_1 = 0x2472    # PARENTHESIZED DIGIT
    norm_parens_9 = 0x247A    # PARENTHESIZED DIGIT
    norm_parens_20 = 0x2485   # PARENTHESIZED DIGIT
    #
    norm_circled_A = 0x24B6  # CIRCLED DIGIT
    norm_circled_O = 0x24C4  # CIRCLED DIGIT
    norm_circled_Z = 0x24CF  # CIRCLED DIGIT
    norm_circled_a = 0x24D0  # CIRCLED DIGIT
    norm_circled_z = 0x24E9  # CIRCLED DIGIT
    norm_circled_0 = 0x24EA  # CIRCLED DIGIT
    norm_circled_1 = 0x245E  # CIRCLED DIGIT
    norm_circled_9 = 0x2466  # CIRCLED DIGIT
    norm_circled_20 = 0x2471  # CIRCLED DIGIT
    norm_circled_sans_1 = 0x2780    # NEGATIVE CIRCLED SANS-SERIF DIGIT (dingbats)
    norm_circled_sans_9 = 0x2788    # NEGATIVE CIRCLED SANS-SERIF DIGIT (dingbats)
    norm_circled_sans_10 = 0x2789   # NEGATIVE CIRCLED SANS-SERIF DIGIT (dingbats)
    #
    norm_button_A = 0x1F150  # NEGATIVE CIRCLED CAPITAL
    norm_button_O = 0x1F15E  # NEGATIVE CIRCLED CAPITAL
    norm_button_Z = 0x1F169  # NEGATIVE CIRCLED CAPITAL
    norm_button_1 = 0x2774   # NEGATIVE CIRCLED DIGIT (dingbats)
    norm_button_9 = 0x277E   # NEGATIVE CIRCLED DIGIT (dingbats)
    norm_button_10 = 0x277F   # NEGATIVE CIRCLED DIGIT (dingbats)
    norm_button_11 = 0x24EB   # NEGATIVE CIRCLED DIGIT
    norm_button_20 = 0x24F4   # NEGATIVE CIRCLED DIGIT
    norm_button_0 = 0x24FF   # NEGATIVE CIRCLED DIGIT
    norm_button_sans_1 = 0x278A   # NEGATIVE CIRCLED SANS-SERIF DIGIT (dingbats)
    norm_button_sans_9 = 0x2792   # NEGATIVE CIRCLED SANS-SERIF DIGIT (dingbats)
    norm_button_sans_10 = 0x2793   # NEGATIVE CIRCLED SANS-SERIF DIGIT (dingbats)
    norm_signum_A = 0x1F170  # NEGATIVE SQUARED CAPITAL
    norm_signum_O = 0x1F17E  # NEGATIVE SQUARED CAPITAL
    norm_signum_Z = 0x1F189  # NEGATIVE SQUARED CAPITAL
    #
    norm_dbutton_1 = 0x24F5   # DOUBLE CIRCLED DIGIT (dingbats)
    norm_dbutton_9 = 0x24FE   # DOUBLE CIRCLED DIGIT (dingbats)
    norm_squared_A = 0x1F130  # SQUARED CAPITAL
    norm_squared_O = 0x1F13E  # SQUARED CAPITAL
    norm_squared_Z = 0x1F149  # SQUARED CAPITAL
    norm_dice_1 = 0x2680
    norm_dice_6 = 0x2685
    norm_regional_A = 0x1F1E6  # REGIONAL INDICATOR 
    norm_regional_Z = 0x1F1FF  # REGIONAL INDICATOR 
    #
    norm_greek_A = 0x391
    norm_greek_O = 0x3A9
    norm_greek_a = 0x3B1
    norm_greek_o = 0x3C9
    norm_greek_nabla = 0x2207
    norm_greek_diffs = 0x2202
    bold_greek_A = 0x1D6A8
    bold_greek_O = 0x1D6C0
    bold_greek_nabla = 0x1D6C1
    bold_greek_a = 0x1D6C2
    bold_greek_o = 0x1D6DA
    bold_greek_diffs = 0x1D6DB
    ital_greek_A = 0x1D6E2
    ital_greek_O = 0x1D6FA
    ital_greek_nabla = 0x1D6FB
    ital_greek_a = 0x1D6FC
    ital_greek_o = 0x1D714
    ital_greek_diffs = 0x1D715
    bold_ital_greek_A = 0x1D71C
    bold_ital_greek_O = 0x1D734
    bold_ital_greek_nabla = 0x1D735
    bold_ital_greek_a = 0x1D736
    bold_ital_greek_o = 0x1D74E
    bold_ital_greek_diffs = 0x1D74F
    #
    norm_frac_1_4 = 0x00BC
    norm_frac_1_2 = 0x00BD
    norm_frac_3_4 = 0x00BE
    norm_frac_1_7 = 0x2150
    norm_frac_1_9 = 0x2151
    norm_frac_1_10 = 0x2152
    norm_frac_1_3 = 0x2153
    norm_frac_2_3 = 0x2154
    norm_frac_1_5 = 0x2155
    norm_frac_2_5 = 0x2156
    norm_frac_3_5 = 0x2157
    norm_frac_4_5 = 0x2158
    norm_frac_1_6 = 0x2159
    norm_frac_5_6 = 0x215A
    norm_frac_1_8 = 0x215B
    norm_frac_3_8 = 0x215C
    norm_frac_5_8 = 0x215D
    norm_frac_7_8 = 0x215E
    norm_frac_1_x = 0x215F
    norm_frac_0_3 = 0x2189
    norm_base_space = 0x20
    norm_nobr_space = 0x00A0
    norm_thin_space = 0x202F
    norm_numm_space = 0x2007
    #
    norm_super_0 = 0x2070
    norm_super_1 = 0x00B9
    norm_super_2 = 0x00B2
    norm_super_3 = 0x00B3
    norm_super_4 = 0x2074
    norm_super_5 = 0x2075
    norm_super_6 = 0x2076
    norm_super_7 = 0x2077
    norm_super_8 = 0x2078
    norm_super_9 = 0x2079
    norm_super_plus = 0x207A
    norm_super_minus = 0x207B
    norm_super_leftparen = 0x207D
    norm_super_rightparen = 0x0207E
    norm_super_equals = 0x207C
    norm_super_n = 0x207F
    norm_sub_0 = 0x2080
    norm_sub_1 = 0x2081
    norm_sub_2 = 0x2082
    norm_sub_3 = 0x2083
    norm_sub_4 = 0x2084
    norm_sub_5 = 0x2085
    norm_sub_6 = 0x2086
    norm_sub_7 = 0x2087
    norm_sub_8 = 0x2088
    norm_sub_9 = 0x2089
    norm_sub_plus = 0x208A
    norm_sub_minus = 0x208B
    norm_sub_equals = 0x208C
    norm_sub_leftparen = 0x208D
    norm_sub_rightparen = 0x0208E
    norm_sub_a =  0x2090
    norm_sub_e =  0x2091
    norm_sub_o =  0x2092
    norm_sub_x =  0x2093
    norm_sub_i =  0x1D62
    norm_sub_r =  0x1D63
    norm_sub_u =  0x1D64
    norm_sub_v =  0x1D65
    #
    norm_turned_a = 0x0250
    norm_turned_b = ord('q')
    norm_turned_c = 0x0254
    norm_turned_d = ord('p')
    norm_turned_e = 0x01DD
    norm_turned_f = 0x025F
    norm_turned_g = 0x1D77 # 0x0183
    norm_turned_h = 0x0265
    norm_turned_i = 0x1D09 # 0x0131
    norm_turned_j = 0x027E
    norm_turned_k = 0x029E
    norm_turned_l = ord('l')
    norm_turned_m = 0x026F
    norm_turned_n = ord('u')
    norm_turned_o = ord('o')
    norm_turned_p = ord('d')
    norm_turned_q = ord('b')
    norm_turned_r = 0x0279
    norm_turned_s = ord('s')
    norm_turned_t = 0x0287
    norm_turned_u = ord('n')
    norm_turned_v = 0x028C
    norm_turned_w = 0x028D
    norm_turned_x = ord('x')
    norm_turned_y = 0x028E
    norm_turned_z = ord('z')
    norm_turned_amp = 0x214B
    norm_turned_dot = 0x02D9
    norm_turned_comma = 0x02BB
    norm_turned_bang = 0x00A1
    norm_turned_question = 0x00BF
    norm_turned_A = 0x2200 # 0x2C6F
    norm_turned_C = 0x0186
    norm_turned_E = 0x018E
    norm_turned_F = 0x2132
    norm_turned_G = 0x2141 # 0x05E4
    norm_turned_J = 0x017F
    norm_turned_M = 0x019C
    norm_turned_L = 0x2142
    norm_turned_R = 0x1D1A
    norm_turned_T = 0xA7B1 # 0x2534
    norm_turned_U = 0x2229
    norm_turned_V = 0x039B
    norm_turned_W = ord('M')
    norm_turned_Y = 0x2144
    norm_turned_1 = 0x21C2
    norm_turned_3 = 0x0190
    norm_turned_6 = ord('9')
    norm_turned_9 = ord('6')
    norm_turned_ue = 0x1E49 # n with under line
    norm_turned_UE = 0x1E4B # n with under hacek
    norm_turned_AE = 0x1E7E # V with ring under
    norm_turned_OE = 0x1ECC # O with dot under
    norm_turned_ae = 0x1D02 # ae turned
    norm_turned_oe = 0x1ECD # o with dot under # 0x1D14 # oe turned
    norm_turned_sz = 0x00FE # thorn # 0x025B # open e # 0x0D93 # open e with retroflex

def nobrspace(text: str) -> str:
    """replace base space by thin nobreak space """
    out = StringIO()
    last_ch = 0
    for c in text:
        ch = ord(c)
        if norm_base_space == ch:
            if norm_base_0 <= last_ch and last_ch <= norm_base_9:
                out.write(chr(norm_numm_space))
            else:
                out.write(chr(norm_nobr_space))
        else:
            out.write(c)
        last_ch = ch
    return out.getvalue()

def thinspace(text: str) -> str:
    """replace base space by thin nobreak space """
    out = StringIO()
    for c in text:
        ch = ord(c)
        if norm_base_space == ch or norm_numm_space == ch:
            out.write(chr(norm_thin_space))
        else:
            out.write(c)
    return out.getvalue()

def fractions(text: str) -> str:
    """replace base space by thin nobreak space """
    def splitfrac(text: str) -> Generator[str, str, None]:
        frac = "0123456789/"
        if text[0] in frac:
            isfrac = True
        else:
            isfrac = False
        value = StringIO()
        for c in text:
            if c in frac:
                if isfrac:
                    value.write(c)
                else:
                    yield value.getvalue()
                    value = StringIO()
                    value.write(c)
                    isfrac = True
            else:
                if isfrac:
                    yield value.getvalue()
                    value = StringIO()
                    value.write(c)
                    isfrac = False
                else:
                    value.write(c)
        if value:
            yield value.getvalue()
    out = StringIO()
    space = ""
    for item in splitfrac(text):
        if item == "1/8":
            space = ""
            out.write(chr(norm_frac_1_8))
        elif item == "2/8" or item == "1/4":
            space = ""
            out.write(chr(norm_frac_1_4))
        elif item == "3/8":
            space = ""
            out.write(chr(norm_frac_3_8))
        elif item == "4/8" or item == "2/4" or item == "1/2":
            space = ""
            out.write(chr(norm_frac_1_2))
        elif item == "5/8":
            space = ""
            out.write(chr(norm_frac_5_8))
        elif item == "6/8" or item == "3/4":
            space = ""
            out.write(chr(norm_frac_3_4))
        elif item == "7/8":
            space = ""
            out.write(chr(norm_frac_7_8))
        elif item == "1/5":
            space = ""
            out.write(chr(norm_frac_1_5))
        elif item == "2/5":
            space = ""
            out.write(chr(norm_frac_2_5))
        elif item == "3/5":
            space = ""
            out.write(chr(norm_frac_3_5))
        elif item == "4/5":
            space = ""
            out.write(chr(norm_frac_4_5))
        elif item == "0/6" or item == "0/3":
            space = ""
            out.write(chr(norm_frac_0_3))
        elif item == "1/6":
            space = ""
            out.write(chr(norm_frac_1_6))
        elif item == "2/6" or item == "1/3":
            space = ""
            out.write(chr(norm_frac_1_3))
        elif item == "3/6":
            space = ""
            out.write(chr(norm_frac_1_2))
        elif item == "4/6" or item == "2/3":
            space = ""
            out.write(chr(norm_frac_2_3))
        elif item == "5/6":
            space = ""
            out.write(chr(norm_frac_5_6))
        else:
            if ord(item[-1]) in [norm_base_space, norm_thin_space, norm_nobr_space, norm_numm_space]:
                out.write(space + item[:-1])
                space = item[-1]
            else:
                out.write(space + item)
                space = ""
    return out.getvalue()

norm_super_numbers: Dict[str, int] = {
    "0": norm_super_0,
    "1": norm_super_1,
    "2": norm_super_2,
    "3": norm_super_3,
    "4": norm_super_4,
    "5": norm_super_5,
    "6": norm_super_6,
    "7": norm_super_7,
    "8": norm_super_8,
    "9": norm_super_9,
    "+": norm_super_plus,
    "-": norm_super_minus,
}

norm_super_before: Dict[str, int] = {
    "=": norm_super_equals,
    "(": norm_super_leftparen,
}
norm_super_after: Dict[str, int] = {
    ")": norm_super_rightparen,
    "n": norm_super_n,
}

def superscript(text: str) -> str:
    out = StringIO()
    for x, c in enumerate(text):
        if c in norm_super_numbers:
            out.write(chr(norm_super_numbers[c]))
        elif c in norm_super_after and x > 0 and text[x-1] in norm_super_numbers:
            out.write(chr(norm_super_after[c]))
        elif c in norm_super_before and x+1 < len(text) and text[x+1] in norm_super_numbers:
            out.write(chr(norm_super_before[c]))
        else:
            out.write(c)
    return out.getvalue()

norm_power_signs = "^"
def power(text: str) -> str:
    out = StringIO()
    power = False
    for x, c in enumerate(text):
        if c in norm_power_signs and x+1 < len(text) and (text[x+1] in norm_super_numbers or text[x+1] in norm_super_before):
            power = True
            continue # drop the power sign
        if power:
            if c in norm_super_numbers:
                out.write(chr(norm_super_numbers[c]))
            elif c in norm_super_before:
                out.write(chr(norm_super_before[c]))
            elif c in norm_super_after:
                out.write(chr(norm_super_after[c]))
            else:
                power = False
                out.write(c)
        else:
            out.write(c)
    return out.getvalue()

norm_sub_numbers: Dict[str, int] = {
    "0": norm_sub_0,
    "1": norm_sub_1,
    "2": norm_sub_2,
    "3": norm_sub_3,
    "4": norm_sub_4,
    "5": norm_sub_5,
    "6": norm_sub_6,
    "7": norm_sub_7,
    "8": norm_sub_8,
    "9": norm_sub_9,
    "+": norm_sub_plus,
    "-": norm_sub_minus,
}

norm_sub_before: Dict[str, int] = {
    "=": norm_sub_equals,
    "(": norm_sub_leftparen,
}
norm_sub_after: Dict[str, int] = {
    ")": norm_sub_rightparen,
    "a": norm_sub_a,
    "e": norm_sub_e,
    "i": norm_sub_i,
    "o": norm_sub_o,
    "u": norm_sub_u,
    "v": norm_sub_v,
    "x": norm_sub_x,
    "r": norm_sub_r,
}

def subscript(text: str) -> str:
    out = StringIO()
    for x, c in enumerate(text):
        if c in norm_sub_numbers:
            out.write(chr(norm_sub_numbers[c]))
        elif c in norm_sub_after and x > 0 and text[x-1] in norm_sub_numbers:
            out.write(chr(norm_sub_after[c]))
        elif c in norm_sub_before and x+1 < len(text) and text[x+1] in norm_sub_numbers:
            out.write(chr(norm_sub_before[c]))
        else:
            out.write(c)
    return out.getvalue()

norm_indexed_signs = "_"
def indexed(text: str) -> str:
    out = StringIO()
    indexed = False
    for x, c in enumerate(text):
        if c in norm_indexed_signs and x+1 < len(text) and (text[x+1] in norm_sub_numbers or text[x+1] in norm_sub_before):
            indexed = True
            continue # drop the indexed sign
        if indexed:
            if c in norm_sub_numbers:
                out.write(chr(norm_sub_numbers[c]))
            elif c in norm_sub_before:
                out.write(chr(norm_sub_before[c]))
            elif c in norm_sub_after:
                out.write(chr(norm_sub_after[c]))
            else:
                indexed = False
                out.write(c)
        else:
            out.write(c)
    return out.getvalue()



norm_greek_upper: Dict[str, Tuple[int, ...]] = {
    "A": (0x391,),  # Alpha
    "B": (0x392,),  # Beta
    "G": (0x393,),  # Gamma
    "D": (0x394,),  # Delta
    "E": (0x395,),  # Epsilon
    "Z": (0x396,),  # Zeta
    "H": (0x397,),  # Eta
    "TH": (0x398,),  # Theta
    "I": (0x399,),  # Iota
    "K": (0x39A,),  # Kappa
    "L": (0x39B,),  # Lambda
    "M": (0x39C,),  # My
    "N": (0x39D,),  # Ny
    "X": (0x39E,),  # Xi
    "O": (0x39F,),  # Omikron
    "P": (0x3A0,),  # Pi
    "R": (0x3A1,),  # Rho
    # Schluss-Sigma
    "S": (0x3A3,),  # Sigma
    "T": (0x3A4,),  # Tau
    "Y": (0x3A5,),  # Ypsilon
    "F": (0x3A6,),  # Phi
    "PH": (0x3A6,),  # Phi
    "C": (0x3A7,),  # Chi
    "CH": (0x3A7,),  # Chi
    "CK": (0x39A,),  # Kappa
    "W": (0x3A8,),  # Psi
    "U": (0x3A9,),  # Omega
    "OO": (0x3A9,),  # Omega
    #
    "J": (0x399,),  # Iota
    "Q": (0x39A,),  # Kappa
    "QU": (0x39A,),  # Kappa
    "V": (norm_greek_nabla,),  # Nabla Operator
}

norm_greek_lower: Dict[str, Tuple[int, ...]] = {
    "a": (0x3B1,),  # Alpha
    "b": (0x3B2,),  # Beta
    "g": (0x3B3,),  # Gamma
    "d": (0x3B4,),  # Delta
    "e": (0x3B5,),  # Epsilon
    "z": (0x3B6,),  # Zeta
    "h": (0x3B7,),  # Eta
    "th": (0x3B8,),  # Theta
    "i": (0x3B9,),  # Iota
    "k": (0x3BA,),  # Kappa
    "l": (0x3BB,),  # Lambda
    "m": (0x3BC,),  # My
    "n": (0x3BD,),  # Ny
    "x": (0x3BE,),  # Xi
    "o": (0x3BF,),  # Omikron
    "p": (0x3C0,),  # Pi
    "r": (0x3C1,),  # Rho
    "s": (0x3C3,),  # Sigma
    "t": (0x3C4,),  # Tau
    "y": (0x3C5,),  # Ypsilon
    "f": (0x3C6,),  # Phi
    "ph": (0x3C6,),  # Phi
    "c": (0x3C7,),  # Chi
    "ch": (0x3C7,),  # Chi
    "ck": (0x3BA,),  # Kappa
    "w": (0x3C8,),  # Psi
    "u": (0x3C9,),  # Omega
    "oo": (0x3C9,),  # Omega
    #
    "j": (0x3B9,),  # Iota
    "q": (0x3BA,),  # Kappa
    "qu": (0x3BA,),  # Kappa
    "v": (norm_greek_diffs,),  # Differential
}

def greek(text: str) -> str:
    def as_norm(text: str) -> str:
        return text
    def as_ital(text: str) -> str:
        return ital(text)
    def as_bold(text: str) -> str:
        return bold(text)
    def as_bold_ital(text: str) -> str:
        return bold(ital(text))
    out = StringIO()
    skip = False
    for i, c in enumerate(text):
        if skip:
            skip = False
            continue
        # orig_c = c
        ch = ord(c)
        as_style = as_norm
        if ital_base_A <= ch and ch <= ital_base_Z:
            ch = norm_base_A + (ch - ital_base_A)
            c = chr(ch)
            as_style = as_ital
        if ch in ital_base_lower:
            ch = ital_base_lower[ch]
            c = chr(ch)
            as_style = as_ital
        if ital_base_a <= ch and ch <= ital_base_z:
            ch = norm_base_a + (ch - ital_base_a)
            c = chr(ch)
            as_style = as_ital
        if bold_base_A <= ch and ch <= bold_base_Z:
            ch = norm_base_A + (ch - bold_base_A)
            c = chr(ch)
            as_style = as_bold
        if bold_base_a <= ch and ch <= bold_base_z:
            ch = norm_base_a + (ch - bold_base_a)
            c = chr(ch)
            as_style = as_bold
        if bold_ital_base_A <= ch and ch <= bold_ital_base_Z:
            ch = norm_base_A + (ch - bold_ital_base_A)
            c = chr(ch)
            as_style = as_bold_ital
        if bold_ital_base_a <= ch and ch <= bold_ital_base_z:
            ch = norm_base_a + (ch - bold_ital_base_a)
            c = chr(ch)
            as_style = as_bold_ital
        if i + 1 < len(text):
            d = text[i + 1]
        else:
            d = " "
        # orig_d = d
        dh = ord(d)
        if ital_base_A <= dh and dh <= ital_base_Z:
            d = chr(norm_base_A + (dh - ital_base_A))
        if dh in ital_base_lower:
            d = chr(ital_base_lower[dh])
        if ital_base_a <= dh and dh <= ital_base_z:
            d = chr(norm_base_a + (dh - ital_base_a))
        if bold_base_A <= dh and dh <= bold_base_Z:
            d = chr(norm_base_A + (dh - bold_base_A))
        if bold_base_a <= dh and dh <= bold_base_z:
            d = chr(norm_base_a + (dh - bold_base_a))
        if bold_ital_base_A <= dh and dh <= bold_ital_base_Z:
            d = chr(norm_base_A + (dh - bold_ital_base_A))
        if bold_ital_base_a <= dh and dh <= bold_ital_base_z:
            d = chr(norm_base_a + (dh - bold_ital_base_a))
        #
        # logg.info("'%s' => '%s' (%x) & '%s' => '%s'", orig_c, c, ch, orig_d, d)
        #
        if norm_base_A <= ch and ch <= norm_base_Z:
            if c + d in norm_greek_upper:
                for n in norm_greek_upper[c + d]:
                    out.write(as_style(chr(n)))
                skip = True
            elif c in norm_greek_upper:
                for n in norm_greek_upper[c]:
                    out.write(as_style(chr(n)))
            else:
                logg.error("did not find greek for '%s'", c)
                out.write(c)
        elif norm_base_a <= ch and ch <= norm_base_z:
            if c + d in norm_greek_lower:
                for n in norm_greek_lower[c + d]:
                    out.write(as_style(chr(n)))
                skip = True
            elif c in norm_greek_lower:
                for n in norm_greek_lower[c]:
                    out.write(as_style(chr(n)))
            else:
                logg.error("did not find greek for '%s'", c)
                out.write(c)
        else:
            out.write(c)
    return out.getvalue()

norm_rune_lower: Dict[str, Tuple[int, ...]] = {
    "f": (0x16A0,),  # Fehu
    "u": (0x16A2,),  # Uruz
    "th": (0x16A6,),  # Thurs
    "a": (0x16A8,),  # ansuz
    "r": (0x16B1,),  # raido
    "k": (0x16B3,),  # kaunan
    "g": (0x16B7,),  # gebo
    "w": (0x16D5,),  # wunja # 0x1F7 0x1BF
    "h": (0x16BA,),  # hagalaz
    "n": (0x16BE,),  # naudiz
    "i": (0x16C1,),  # isaz
    "j": (0x16E1,),  # jera
    "y": (0x16C7,),  # ihwaz
    "p": (0x16C8,),  # perth
    "z": (0x16C9,),  # algiz
    "s": (0x16CB,),  # sowilo
    "t": (0x16CF,),  # tiwaz
    "b": (0x16D2,),  # berkan
    "e": (0x16D6,),  # ehwaz
    "m": (0x16D7,),  # mannaz
    "l": (0x16DA,),  # laguz
    "ng": (0x16DC,),  # ingwaz
    "o": (0x16DF,),  # othila
    "d": (0x16DE,),  # dagaz
    #
    "c": (0x16B3,),  # kaunan
    "q": (0x16B3,),  # kaunan
    "qu": (0x16B3,),  # kaunan
    "u": (0x16B9,),  # wunja
    "v": (0x16B9,),  # wunja
    "x": (0x16B3, 0x16CB),  # kaunan, sowilo
}

def rune(text: str) -> str:  # gothic, blackletter
    rune_a = 0x16A0
    rune_o = 0x16F8
    out = StringIO()
    skip = False
    for i, c in enumerate(text):
        if skip:
            skip = False
            continue
        ch = ord(c)
        if norm_base_A <= ch and ch <= norm_base_Z:
            ch = norm_base_a + (ch - norm_base_A)
            c = chr(ch)
        if i + 1 < len(text):
            d = text[i + 1]
        else:
            d = " "
        dh = ord(d)
        if norm_base_A <= dh and dh <= norm_base_Z:
            dh = norm_base_a + (dh - norm_base_A)
            d = chr(dh)
        if norm_base_a <= ch and ch <= norm_base_z:
            if c + d in norm_rune_lower:
                for n in norm_rune_lower[c + d]:
                    out.write(chr(n))
                skip = True
            elif c in norm_rune_lower:
                for n in norm_rune_lower[c]:
                    out.write(chr(n))
            else:
                logg.error("did not find rune for '%s'", c)
                out.write(c)
        else:
            out.write(c)
    return out.getvalue()

norm_fraktur__C = 0x212D  # Complex Numbers
norm_fraktur__H = 0x210C  # Hamilton Numbers
norm_fraktur__I = 0x2111
norm_fraktur__R = 0x211C  # Real Numbers
norm_fraktur__Z = 0x2128  # Integer Numbers
norm_fraktur_encode: Dict[str, int] = {
    'C': norm_fraktur__C,
    'H': norm_fraktur__H,
    'I': norm_fraktur__I,
    'R': norm_fraktur__R,
    'Z': norm_fraktur__Z}
norm_fraktur_upper: Dict[int, int] = {
    norm_fraktur__C: ord('C'),
    norm_fraktur__H: ord('H'),
    norm_fraktur__I: ord('I'),
    norm_fraktur__R: ord('R'),
    norm_fraktur__Z: ord('Z')}

def fraktur(text: str) -> str:  # gothic, blackletter
    out = StringIO()
    for c in text:
        ch = ord(c)
        if c in norm_fraktur_encode:
            out.write(chr(norm_fraktur_encode[c]))
        elif norm_base_A <= ch and ch <= norm_base_Z:
            out.write(chr(norm_fraktur_A + (ch - norm_base_A)))
        elif norm_base_a <= ch and ch <= norm_base_z:
            out.write(chr(norm_fraktur_a + (ch - norm_base_a)))
        # elif norm_base_0 <= ch and ch <= norm_base_9:
        #     out.write(chr(bold_base_0+(ch-norm_base_0)))
        else:
            out.write(c)
    return out.getvalue()

norm_turned_encode: Dict[str, int] = {
    'a': norm_turned_a,
    'b': norm_turned_b,
    'c': norm_turned_c,
    'd': norm_turned_d,
    'e': norm_turned_e,
    'f': norm_turned_f,
    'g': norm_turned_g,
    'h': norm_turned_h,
    'i': norm_turned_i,
    'j': norm_turned_j,
    'k': norm_turned_k,
    'l': norm_turned_l,
    'm': norm_turned_m,
    'n': norm_turned_n,
    'p': norm_turned_p,
    'q': norm_turned_q,
    'r': norm_turned_r,
    't': norm_turned_t,
    'u': norm_turned_u,
    'v': norm_turned_v,
    'w': norm_turned_w,
    'y': norm_turned_y,
    '&': norm_turned_amp,
    ',': norm_turned_comma,
    '.': norm_turned_dot,
    '!': norm_turned_bang,
    '?': norm_turned_question,
    'A': norm_turned_A,
    'C': norm_turned_C,
    'E': norm_turned_E,
    'F': norm_turned_F,
    'G': norm_turned_G,
    'J': norm_turned_J,
    'L': norm_turned_L,
    'M': norm_turned_M,
    'P': ord('d'),
    'R': norm_turned_R,
    'T': norm_turned_T,
    'U': norm_turned_U,
    'V': norm_turned_V,
    'W': norm_turned_W,
    'Y': norm_turned_Y,
    chr(0xE4): norm_turned_ae,
    chr(0xF6): norm_turned_oe,
    chr(0xFC): norm_turned_ue,
    chr(0xC4): norm_turned_AE,
    chr(0xD6): norm_turned_OE,
    chr(0xDC): norm_turned_UE,
    chr(0xDF): norm_turned_sz,
    }

def turned(text: str) -> str:  # characters flipped upside down
    out = StringIO()
    for c in text:
        ch = ord(c)
        if c in norm_turned_encode:
            out.write(chr(norm_turned_encode[c]))
        else:
            out.write(c)
    return out.getvalue()

def backlines(text: str) -> str:  # lines right-left inversed
    out = StringIO()
    line = StringIO()
    for c in text:
        if c in '\r\n\f':
            out.write(line.getvalue()[::-1])
            out.write(c)
            line = StringIO()
        else:
            line.write(c)
    out.write(line.getvalue()[::-1])
    return out.getvalue()

def turnlines(text: str) -> str:
    return turned(backlines(text))

norm_script__B = 0x212C
norm_script__E = 0x2130
norm_script__F = 0x2131
norm_script__H = 0x210B
norm_script__I = 0x2110
norm_script__L = 0x2112
norm_script__M = 0x2133
norm_script__R = 0x211B
norm_script__e = 0x212F
norm_script__g = 0x210A
norm_script__o = 0x2134
norm_script_encode: Dict[str, int] = {
    'B': norm_script__B,
    'E': norm_script__E,
    'F': norm_script__F,
    'H': norm_script__H,
    'I': norm_script__I,
    'L': norm_script__L,
    'M': norm_script__M,
    'R': norm_script__R,
    'e': norm_script__e,
    'g': norm_script__g,
    'o': norm_script__o}
norm_script_upper: Dict[int, int] = {
    norm_script__B: ord('B'),
    norm_script__E: ord('E'),
    norm_script__F: ord('F'),
    norm_script__H: ord('H'),
    norm_script__I: ord('I'),
    norm_script__L: ord('L'),
    norm_script__M: ord('M'),
    norm_script__R: ord('R')}
norm_script_lower: Dict[int, int] = {
    norm_script__e: ord('e'),
    norm_script__g: ord('g'),
    norm_script__o: ord('o')}

def script(text: str) -> str:  # real cursive
    out = StringIO()
    for c in text:
        ch = ord(c)
        if c in norm_script_encode:
            out.write(chr(norm_script_encode[c]))
        elif norm_base_A <= ch and ch <= norm_base_Z:
            out.write(chr(norm_script_A + (ch - norm_base_A)))
        elif norm_base_a <= ch and ch <= norm_base_z:
            out.write(chr(norm_script_a + (ch - norm_base_a)))
        elif bold_base_A <= ch and ch <= bold_base_Z:
            out.write(chr(bold_script_A + (ch - bold_base_A)))
        elif bold_base_a <= ch and ch <= bold_base_z:
            out.write(chr(bold_script_a + (ch - bold_base_a)))
        else:
            out.write(c)
    return out.getvalue()

norm_double__C = 0x2102  # Complex Numbers
norm_double__H = 0x210D  # Hamilton Numbers
norm_double__N = 0x2115  # Natural Numbers
norm_double__P = 0x2119
norm_double__Q = 0x211A  # Rational Numbers
norm_double__R = 0x211D  # Real Numbers
norm_double__Z = 0x2124  # Integer Numbers
norm_double_encode: Dict[str, int] = {
    'C': norm_double__C,
    'H': norm_double__H,
    'N': norm_double__N,
    'P': norm_double__P,
    'Q': norm_double__Q,
    'R': norm_double__R,
    'Z': norm_double__Z}
norm_double_upper: Dict[int, int] = {
    norm_double__C: ord('C'),
    norm_double__H: ord('H'),
    norm_double__N: ord('N'),
    norm_double__P: ord('P'),
    norm_double__Q: ord('Q'),
    norm_double__R: ord('R'),
    norm_double__Z: ord('Z')}

def doubled(text: str) -> str:  # gothic, blackletter
    out = StringIO()
    for c in text:
        ch = ord(c)
        if c in norm_double_encode:
            out.write(chr(norm_double_encode[c]))
        elif norm_base_A <= ch and ch <= norm_base_Z:
            out.write(chr(norm_double_A + (ch - norm_base_A)))
        elif norm_base_a <= ch and ch <= norm_base_z:
            out.write(chr(norm_double_a + (ch - norm_base_a)))
        elif norm_base_0 <= ch and ch <= norm_base_9:
            out.write(chr(norm_double_0 + (ch - norm_base_0)))
        else:
            out.write(c)
    return out.getvalue()

def button(text: str) -> str:  # squred
    # only ABO for bloodgroup are common, digit 0 is different than 9
    out = StringIO()
    for c in text:
        ch = ord(c)
        if norm_base_A <= ch and ch <= norm_base_Z:
            out.write(chr(norm_signum_A + (ch - norm_base_A)))
        elif norm_base_a <= ch and ch <= norm_base_z:
            out.write(chr(norm_button_A + (ch - norm_base_a)))
        elif norm_base_0+1 <= ch and ch <= norm_base_9:
            out.write(chr(norm_button_1 + (ch - norm_base_0+1)))
        elif norm_base_0 == ch and ch:
            out.write(chr(norm_button_0))
        else:
            out.write(c)
    return out.getvalue()

def circled(text: str) -> str:  # squred
    # most fonts have that inconsistent - found M to be blue
    out = StringIO()
    for c in text:
        ch = ord(c)
        if norm_base_A <= ch and ch <= norm_base_Z:
            out.write(chr(norm_circled_A + (ch - norm_base_A)))
        elif norm_base_a <= ch and ch <= norm_base_z:
            out.write(chr(norm_circled_a + (ch - norm_base_a)))
        elif norm_base_0+1 <= ch and ch <= norm_base_9:
            out.write(chr(norm_circled_1 + (ch - norm_base_0+1)))
        elif norm_base_0 == ch and ch:
            out.write(chr(norm_circled_0))
        else:
            out.write(c)
    return out.getvalue()

def parens(text: str) -> str:  # squred
    # most fonts have that incomplete - only lowercase and digts are common
    out = StringIO()
    for c in text:
        ch = ord(c)
        if norm_base_A <= ch and ch <= norm_base_Z:
            out.write(chr(norm_parens_A + (ch - norm_base_A)))
        elif norm_base_a <= ch and ch <= norm_base_z:
            out.write(chr(norm_parens_a + (ch - norm_base_a)))
        elif norm_base_0+1 <= ch and ch <= norm_base_9:
            out.write(chr(norm_parens_1 + (ch - norm_base_0+1)))
        elif norm_base_0 == ch and ch:
            out.write(chr(norm_parens_o))
        else:
            out.write(c)
    return out.getvalue()

def courier(text: str) -> str:  # gothic, blackletter
    out = StringIO()
    for c in text:
        ch = ord(c)
        if norm_base_A <= ch and ch <= norm_base_Z:
            out.write(chr(norm_mono_A + (ch - norm_base_A)))
        elif norm_base_a <= ch and ch <= norm_base_z:
            out.write(chr(norm_mono_a + (ch - norm_base_a)))
        elif norm_base_0 <= ch and ch <= norm_base_9:
            out.write(chr(norm_mono_0 + (ch - norm_base_0)))
        else:
            out.write(c)
    return out.getvalue()

def initial(text: str) -> str:
    out = StringIO()
    newline = True
    for c in text:
        ch = ord(c)
        if newline and norm_base_A <= ch and ch <= norm_base_Z:
            out.write(doubled(c))
            newline = False
        else:
            if c in "\r\n":
                newline = True
            out.write(c)
    return out.getvalue()

def sans(text: str) -> str:
    out = StringIO()
    for c in text:
        ch = ord(c)
        if norm_base_A <= ch and ch <= norm_base_Z:
            out.write(chr(norm_sans_A + (ch - norm_base_A)))
        elif norm_base_a <= ch and ch <= norm_base_z:
            out.write(chr(norm_sans_a + (ch - norm_base_a)))
        elif norm_base_0 <= ch and ch <= norm_base_9:
            out.write(chr(norm_sans_0 + (ch - norm_base_0)))
        elif bold_base_A <= ch and ch <= bold_base_Z:
            out.write(chr(bold_sans_A + (ch - bold_base_A)))
        elif bold_base_a <= ch and ch <= bold_base_z:
            out.write(chr(bold_sans_a + (ch - bold_base_a)))
        elif bold_base_0 <= ch and ch <= bold_base_9:
            out.write(chr(bold_sans_0 + (ch - bold_base_0)))
        elif ch in ital_base_lower:
            out.write(chr(ital_sans_a + (ital_base_lower[ch] - norm_base_a)))
        elif ital_base_A <= ch and ch <= ital_base_Z:
            out.write(chr(ital_sans_A + (ch - ital_base_A)))
        elif ital_base_a <= ch and ch <= ital_base_z:
            out.write(chr(ital_sans_a + (ch - ital_base_a)))
        elif bold_ital_base_A <= ch and ch <= bold_ital_base_Z:
            out.write(chr(bold_ital_sans_A + (ch - bold_ital_base_A)))
        elif bold_ital_base_a <= ch and ch <= bold_ital_base_z:
            out.write(chr(bold_ital_sans_a + (ch - bold_ital_base_a)))
        else:
            out.write(c)
    return out.getvalue()

ital_base__h = 0x210E  # Planck constant
ital_base_encode: Dict[str, int] = {
    'h': ital_base__h}
ital_base_lower: Dict[int, int] = {
    ital_base__h: ord('h')}

def ital(text: str) -> str:
    logg.debug("apply slant to ascii/black letters")
    out = StringIO()
    for c in text:
        ch = ord(c)
        if c in ital_base_encode:
            out.write(chr(ital_base_encode[c]))
        elif norm_base_A <= ch and ch <= norm_base_Z:
            out.write(chr(ital_base_A + (ch - norm_base_A)))
        elif norm_base_a <= ch and ch <= norm_base_z:
            out.write(chr(ital_base_a + (ch - norm_base_a)))
        elif norm_base_sz == ch:
            out.write(chr(ital_greek_a + 1))  # beta
        elif bold_base_A <= ch and ch <= bold_base_Z:
            out.write(chr(bold_ital_base_A + (ch - bold_base_A)))
        elif bold_base_a <= ch and ch <= bold_base_z:
            out.write(chr(bold_ital_base_a + (ch - bold_base_a)))
        elif norm_sans_A <= ch and ch <= norm_sans_Z:
            out.write(chr(ital_sans_A + (ch - norm_sans_A)))
        elif norm_sans_a <= ch and ch <= norm_sans_z:
            out.write(chr(ital_sans_a + (ch - norm_sans_a)))
        elif bold_sans_A <= ch and ch <= bold_sans_Z:
            out.write(chr(bold_ital_sans_A + (ch - bold_sans_A)))
        elif bold_sans_a <= ch and ch <= bold_sans_z:
            out.write(chr(bold_ital_sans_a + (ch - bold_sans_a)))
        elif norm_greek_nabla == ch:
            out.write(chr(ital_greek_nabla))
        elif norm_greek_diffs == ch:
            out.write(chr(ital_greek_diffs))
        elif norm_greek_A <= ch and ch <= norm_greek_O:
            out.write(chr(ital_greek_A + (ch - norm_greek_A)))
        elif norm_greek_a <= ch and ch <= norm_greek_o:
            out.write(chr(ital_greek_a + (ch - norm_greek_a)))
        elif bold_greek_A <= ch and ch <= bold_greek_O + 1:
            out.write(chr(bold_ital_greek_A + (ch - bold_greek_A)))
        elif bold_greek_a <= ch and ch <= bold_greek_o + 1:
            out.write(chr(bold_ital_greek_a + (ch - bold_greek_a)))
        else:
            out.write(c)
    return out.getvalue()

def bold(text: str) -> str:
    logg.debug("apply fat to ascii/black letters")
    out = StringIO()
    for c in text:
        ch = ord(c)
        if norm_base_A <= ch and ch <= norm_base_Z:
            out.write(chr(bold_base_A + (ch - norm_base_A)))
        elif norm_base_a <= ch and ch <= norm_base_z:
            out.write(chr(bold_base_a + (ch - norm_base_a)))
        elif norm_base_0 <= ch and ch <= norm_base_9:
            out.write(chr(bold_base_0 + (ch - norm_base_0)))
        elif norm_base_sz == ch:
            out.write(chr(bold_greek_a + 1))
        elif ch in ital_base_lower:
            out.write(chr(bold_ital_base_a + (ital_base_lower[ch] - norm_base_a)))
        elif ital_base_A <= ch and ch <= ital_base_Z:
            out.write(chr(bold_ital_base_A + (ch - ital_base_A)))
        elif ital_base_a <= ch and ch <= ital_base_z:
            out.write(chr(bold_ital_base_a + (ch - ital_base_a)))
        elif norm_sans_A <= ch and ch <= norm_sans_Z:
            out.write(chr(bold_sans_A + (ch - norm_sans_A)))
        elif norm_sans_a <= ch and ch <= norm_sans_z:
            out.write(chr(bold_sans_a + (ch - norm_sans_a)))
        elif norm_sans_0 <= ch and ch <= norm_sans_9:
            out.write(chr(bold_sans_0 + (ch - norm_sans_0)))
        elif ital_sans_A <= ch and ch <= ital_sans_Z:
            out.write(chr(bold_ital_sans_A + (ch - ital_sans_A)))
        elif ital_sans_a <= ch and ch <= ital_sans_z:
            out.write(chr(bold_ital_sans_a + (ch - ital_sans_a)))
        elif ch in norm_fraktur_upper:
            out.write(chr(bold_fraktur_A + (norm_fraktur_upper[ch] - norm_base_A)))
        elif norm_fraktur_A <= ch and ch <= norm_fraktur_Y:
            out.write(chr(bold_fraktur_A + (ch - norm_fraktur_A)))
        elif norm_fraktur_a <= ch and ch <= norm_fraktur_z:
            out.write(chr(bold_fraktur_a + (ch - norm_fraktur_a)))
        elif ch in norm_script_upper:
            out.write(chr(bold_script_A + (norm_script_upper[ch] - norm_base_A)))
        elif ch in norm_script_lower:
            out.write(chr(bold_script_a + (norm_script_lower[ch] - norm_base_a)))
        elif norm_script_A <= ch and ch <= norm_script_Z:
            out.write(chr(bold_script_A + (ch - norm_script_A)))
        elif norm_script_a <= ch and ch <= norm_script_z:
            out.write(chr(bold_script_a + (ch - norm_script_a)))
        elif norm_greek_nabla == ch:
            out.write(chr(bold_greek_nabla))
        elif norm_greek_diffs == ch:
            out.write(chr(bold_greek_diffs))
        elif norm_greek_A <= ch and ch <= norm_greek_O:
            out.write(chr(bold_greek_A + (ch - norm_greek_A)))
        elif norm_greek_a <= ch and ch <= norm_greek_o:
            out.write(chr(bold_greek_a + (ch - norm_greek_a)))
        elif ital_greek_A <= ch and ch <= ital_greek_O + 1:
            out.write(chr(bold_ital_greek_A + (ch - ital_greek_A)))
        elif ital_greek_a <= ch and ch <= ital_greek_o + 1:
            out.write(chr(bold_ital_greek_a + (ch - ital_greek_a)))
        else:
            out.write(c)
    return out.getvalue()


class Scanned:
    text: str = ""
    cmd: str = ""
    verbose: int = 0
    helpinfo: int = 0

def scan(args: List[str]) -> Scanned:
    opt = Scanned()
    stopped = False
    for arg in args:
        if arg.startswith("-") and not stopped:
            if arg.startswith("--"):
                if arg.startswith("--verbose"):
                    opt.verbose += 1
                elif arg.startswith("--help"):
                    opt.helpinfo += 1
                else:
                    print("unknown option {arg} (ignored)".format(**locals()), file=sys.stderr)
            else:
                accept = "hv"
                opt.verbose += arg.count("v")
                opt.helpinfo += arg.count("h")
                for a in arg[1:]:
                    if a not in accept:
                        print("unknown option -{a} (ignored)".format(**locals()), file=sys.stderr)
        else:
            if not opt.cmd:
                opt.cmd = arg
                stopped = True
            elif not opt.text:
                opt.text = arg
            else:
                opt.text += " " + arg
    return opt

def convert(cmd: str, text: str) -> str:
    if cmd and cmd[0] in "0123456789":
        text = cmd + " " + text
        cmd = "value"
    logg.debug("cmd = '%s'", cmd)
    if "nobr" in cmd or "word" in cmd:
        text = nobrspace(text)
    if "thin" in cmd or "value" in cmd:
        text = thinspace(text)
    if "button" in cmd or "button" in cmd:
        text = button(text)
    if "circ" in cmd or "circled" in cmd:
        text = circled(text)
    if "parens" in cmd or "parent" in cmd:
        text = parens(text)
    if "frac" in cmd or "value" in cmd:
        text = fractions(text)
    if "subi" in cmd or "below" in cmd:
        text = subscript(text)
    if "super" in cmd or "above" in cmd:
        text = superscript(text)
    if "power" in cmd or "dim" in cmd:
        text = power(text)
    if "index" in cmd or "idx" in cmd:
        text = indexed(text)
    if "math" in cmd:
        text = indexed(power(fractions(nobrspace(text))))
    if "doub" in cmd or "wide" in cmd:
        text = doubled(text)
    if "caps" in cmd or "init" in cmd:
        text = initial(text)
    if "turned" in cmd or "down" in cmd:
        text = turned(text)
    if "flip" in cmd or "ambi" in cmd or "turnlines" in cmd:
        text = turnlines(text) # turned(backlines(text))
    if "back" in cmd or "swap" in cmd:
        text = backlines(text)
    if "turn" in cmd and "turned" not in cmd and "turnlines" not in cmd:
        logg.warning("use 'flip' to turnlines")
        text = turned(backlines(text))
    if "rune" in cmd or "futark" in cmd:
        text = rune(text)
    if "greek" in cmd or "math" in cmd:
        text = greek(text)
    if "black" in cmd or "frak" in cmd:
        text = fraktur(text)
    if "round" in cmd or "script" in cmd or "writ" in cmd:
        text = script(text)
    if "cour" in cmd or "type" in cmd or "mono" in cmd:
        text = courier(text)
    if "sans" in cmd or "vect" in cmd:
        text = sans(text)
    # and the variants in ital and bold
    if "ital" in cmd or "name" in cmd or "slant" in cmd:
        text = ital(text)
    if "bold" in cmd or "fat" in cmd:
        text = bold(text)
    return text

def helpinfo() -> str:
    return """unicoder [-options] command [text..]
    -h / --help       this help info
    -v / --verbose    increase logging level
    command contains:
     *fat*  *bold*    convert to math fat symbols
     *ital* *name*    convert to math slanted symbols
     *round* *script* convert to math writing symbols
     *greek* *math*   convert to math greek
     *frak* *black*   convert to math fraktur 
     *doub* *wide*    convert to math double stroke
     *cour* *type*    convert to math courier monospace
     *rune* *futark*  transliterate to runic script
     *caps* *init*    initial uppercase char to double stroke
     *nobr* *word*    using base nobr spaces
     *thin* *value*   using thin nobr spaces
     *fract* *vect*   convert fractional values
     *subi* *below*   convert numbers to subscript (and +/-)
     *super* *above*  convert numbers to superscript (and +/-)
     *power* *dim*    convert numbers after ^ to superscript
     *index* *idx*    convert numbers after _ to subscript
     *math*           nobr+frac+power+index
     *turned* *down*  turn each character (upside-down)
     *swap* *back*    reverse each line
     *flip* *ambi*    turned (upside-down and reversed)
    some combinations provide different codepoints:
      italboldbase
      italgreek
      boldgreek
      italboldgreek
      italsans
      boldsans
      italboldsans
      boldfrak
    """

if __name__ == "__main__":  # pragma: no cover
    __opt = scan(sys.argv[1:])
    logging.basicConfig(level=max(0, logging.WARNING - __opt.verbose * 10))
    if __opt.helpinfo:
        print(helpinfo())
    else:
        print(convert(__opt.cmd, __opt.text))
