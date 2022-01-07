#! /usr/bin/python3
from __future__ import print_function

__copyright__ = "(C) 2021-2022 Guido U. Draheim, licensed under the APLv2"
__version__ = "1.0.1015"

from typing import List, Generator
from io import StringIO
import sys
import logging

logg = logging.getLogger("UNICODER")

def nobrspace(text: str) -> str:
    """replace base space by thin nobreak space """
    base_space = ord(' ')
    base_0 = ord('0')
    base_9 = ord('9')
    nobr_space = 0x00A0
    thin_space = 0x202F
    numm_space = 0x2007
    out = StringIO()
    last_ch = 0
    for c in text:
        ch = ord(c)
        if base_space == ch:
            if base_0 <= last_ch and last_ch <= base_9:
                out.write(chr(numm_space))
            else:
                out.write(chr(nobr_space))
        else:
            out.write(c)
        last_ch = ch
    return out.getvalue()

def thinspace(text: str) -> str:
    """replace base space by thin nobreak space """
    base_space = ord(' ')
    nobr_space = 0x00A0
    thin_space = 0x202F
    numm_space = 0x8199
    out = StringIO()
    for c in text:
        ch = ord(c)
        if base_space == ch or numm_space == ch:
            out.write(chr(thin_space))
        else:
            out.write(c)
    return out.getvalue()

def fractions(text: str) -> str:
    """replace base space by thin nobreak space """
    frac_1_4 = 0x00BC
    frac_1_2 = 0x00BD
    frac_3_4 = 0x00BE
    frac_1_7 = 0x2150
    frac_1_9 = 0x2151
    frac_1_10 = 0x2152
    frac_1_3 = 0x2153
    frac_2_3 = 0x2154
    frac_1_5 = 0x2155
    frac_2_5 = 0x2156
    frac_3_5 = 0x2157
    frac_4_5 = 0x2158
    frac_1_6 = 0x2159
    frac_5_6 = 0x215A
    frac_1_8 = 0x215B
    frac_3_8 = 0x215C
    frac_5_8 = 0x215D
    frac_7_8 = 0x215E
    frac_1_x = 0x215F
    frac_0_3 = 0x2189
    base_space = 0x20
    nobr_space = 0x00A0
    thin_space = 0x202F
    numm_space = 0x8199
    def splitfrac(text: str) -> Generator[str,str, None]:
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
            out.write(chr(frac_1_8))
        elif item == "2/8" or item == "1/4":
            space = ""
            out.write(chr(frac_1_4))
        elif item == "3/8":
            space = ""
            out.write(chr(frac_3_8))
        elif item == "4/8" or item == "2/4" or item == "1/2":
            space = ""
            out.write(chr(frac_1_2))
        elif item == "5/8":
            space = ""
            out.write(chr(frac_5_8))
        elif item == "6/8" or item == "3/4":
            space = ""
            out.write(chr(frac_3_4))
        elif item == "7/8":
            space = ""
            out.write(chr(frac_7_8))
        elif item == "1/5":
            space = ""
            out.write(chr(frac_1_5))
        elif item == "2/5":
            space = ""
            out.write(chr(frac_2_5))
        elif item == "3/5":
            space = ""
            out.write(chr(frac_3_5))
        elif item == "4/5":
            space = ""
            out.write(chr(frac_4_5))
        elif item == "0/6" or item == "0/3":
            space = ""
            out.write(chr(frac_0_3))
        elif item == "1/6":
            space = ""
            out.write(chr(frac_1_6))
        elif item == "2/6" or item == "1/3":
            space = ""
            out.write(chr(frac_1_3))
        elif item == "3/6":
            space = ""
            out.write(chr(frac_1_2))
        elif item == "4/6" or item == "2/3":
            space = ""
            out.write(chr(frac_2_3))
        elif item == "5/6":
            space = ""
            out.write(chr(frac_5_6))
        else:
            if ord(item[-1]) in [base_space, thin_space, nobr_space, numm_space]:
                out.write(space + item[:-1])
                space = item[-1]
            else:
                out.write(space + item)
                space = ""
    return out.getvalue()

def sans(text: str) -> str:
    base_A = ord('A')
    base_Z = ord('Z')
    base_a = ord('a')
    base_z = ord('z')
    base_0 = ord('0')
    base_9 = ord('9')
    sans_A = 0x1D5A0
    sans_Z = 0x1D5B9
    sans_a = 0x1D5BA
    sans_z = 0x1D5D3
    sans_0 = 0x1D7E2
    sans_9 = 0x1D7EB
    out = StringIO()
    for c in text:
        ch = ord(c)
        if base_A <= ch and ch <= base_Z:
            out.write(chr(sans_A+(ch-base_A)))
        elif base_a <= ch and ch <= base_z:
            out.write(chr(sans_a+(ch-base_a)))
        elif base_0 <= ch and ch <= base_9:
            out.write(chr(sans_0+(ch-base_0)))
        else:
            out.write(c)
    return out.getvalue()

greek_upper = {
   "A": (0x391,), # Alpha
   "B": (0x392,), # Beta
   "G": (0x393,), # Gamma
   "D": (0x394,), # Delta
   "E": (0x395,), # Epsilon
   "Z": (0x396,), # Zeta
   "H": (0x397,), # Eta
   "TH": (0x398,), # Theta
   "I": (0x399,), # Iota
   "K": (0x39A,), # Kappa
   "L": (0x39B,), # Lambda
   "M": (0x39C,), # My
   "N": (0x39D,), # Ny
   "X": (0x39E,), # Xi
   "o": (0x39F,), # Omikron
   "P": (0x3A0,), # Pi
   "R": (0x3A1,), # Rho
                    # Schluss-Sigma
   "S": (0x3A3,), # Sigma
   "T": (0x3A4,), # Tau
   "Y": (0x3A5,), # Ypsilon
   "F": (0x3A6,), # Phi
   "PH": (0x3A6,), # Phi
   "C": (0x3A7,), # Chi
   "CH": (0x3A7,), # Chi
   "CK": (0x39A,), # Kappa
   "W": (0x3A8,), # Psi
   "U": (0x3A9,), # Omega
   "OO": (0x3A9,), # Omega
   #
   "J": (0x399,), # Iota
   "Q": (0x39A,), # Kappa
   "QU": (0x39A,), # Kappa
   "V": (0x2207,), # Nabla Operatur
}

greek_lower = {
   "a": (0x3B1,), # Alpha
   "b": (0x3B2,), # Beta
   "g": (0x3B3,), # Gamma
   "d": (0x3B4,), # Delta
   "e": (0x3B5,), # Epsilon
   "z": (0x3B6,), # Zeta
   "h": (0x3B7,), # Eta
   "th": (0x3B8,), # Theta
   "i": (0x3B9,), # Iota
   "k": (0x3BA,), # Kappa
   "l": (0x3BB,), # Lambda
   "m": (0x3BC,), # My
   "n": (0x3BD,), # Ny
   "x": (0x3BE,), # Xi
   "o": (0x3BF,), # Omikron
   "p": (0x3C0,), # Pi
   "r": (0x3C1,), # Rho
   "s": (0x3C3,), # Sigma
   "t": (0x3C4,), # Tau
   "y": (0x3C5,), # Ypsilon
   "f": (0x3C6,), # Phi
   "ph": (0x3C6,), # Phi
   "c": (0x3C7,), # Chi
   "ch": (0x3C7,), # Chi
   "ck": (0x3BA,), # Kappa
   "w": (0x3C8,), # Psi
   "u": (0x3C9,), # Omega
   "oo": (0x3C9,), # Omega
   #
   "j": (0x3B9,), # Iota
   "q": (0x3BA,), # Kappa
   "qu": (0x3BA,), # Kappa
   "v": (0x2202,), # Differential
}

def greek(text: str) -> str: # gothic, blackletter
    base_A = ord('A')
    base_Z = ord('Z')
    base_a = ord('a')
    base_z = ord('z')
    greek_A = 0x391
    greek_O = 0x3A9
    greek_a = 0x3B1
    greek_o = 0x3C9
    greek_nabla = 0x8711
    greek_diffs = 0x2202
    out = StringIO()
    skip = False
    for i, c in enumerate(text):
        if skip:
            skip = False
            continue
        ch = ord(c)
        if base_A <= ch and ch <= base_Z:
            if i+1 < len(text):
               c2 = text[i+1]
            else:
               c2 = " "
            if c+c2 in greek_upper:
               for n in greek_upper[c+c2]:
                   out.write(chr(n))
               skip = True
            elif c in greek_upper:
               for n in greek_upper[c]:
                   out.write(chr(n))
            else:
               logg.error("did not find greek for '%s'", c)
        elif base_a <= ch and ch <= base_z:
            if i+1 < len(text):
               c2 = text[i+1]
            else:
               c2 = " "
            if c+c2 in greek_lower:
               for n in greek_lower[c+c2]:
                   out.write(chr(n))
               skip = True
            elif c in greek_lower:
               for n in greek_lower[c]:
                   out.write(chr(n))
            else:
               logg.error("did not find greek for '%s'", c)
        else:
            out.write(c)
    return out.getvalue()

rune_upper = {
   "A": (0x391,), # Alpha
   "B": (0x392,), # Beta
   "G": (0x393,), # Gamma
   "D": (0x394,), # Delta
   "E": (0x395,), # Epsilon
   "Z": (0x396,), # Zeta
   "H": (0x397,), # Eta
   "TH": (0x398,), # Theta
   "I": (0x399,), # Iota
   "K": (0x39A,), # Kappa
   "L": (0x39B,), # Lambda
   "M": (0x39C,), # My
   "N": (0x39D,), # Ny
   "X": (0x39E,), # Xi
   "o": (0x39F,), # Omikron
   "P": (0x3A0,), # Pi
   "R": (0x3A1,), # Rho
                    # Schluss-Sigma
   "S": (0x3A3,), # Sigma
   "T": (0x3A4,), # Tau
   "Y": (0x3A5,), # Ypsilon
   "F": (0x3A6,), # Phi
   "PH": (0x3A6,), # Phi
   "C": (0x3A7,), # Chi
   "CH": (0x3A7,), # Chi
   "CK": (0x39A,), # Kappa
   "W": (0x3A8,), # Psi
   "U": (0x3A9,), # Omega
   "OO": (0x3A9,), # Omega
   #
   "J": (0x399,), # Iota
   "Q": (0x39A,), # Kappa
   "QU": (0x39A,), # Kappa
   "V": (0x2207,), # Nabla Operatur
}

rune_lower = {
   "a": (0x3B1,), # Alpha
   "b": (0x3B2,), # Beta
   "g": (0x3B3,), # Gamma
   "d": (0x3B4,), # Delta
   "e": (0x3B5,), # Epsilon
   "z": (0x3B6,), # Zeta
   "h": (0x3B7,), # Eta
   "th": (0x3B8,), # Theta
   "i": (0x3B9,), # Iota
   "k": (0x3BA,), # Kappa
   "l": (0x3BB,), # Lambda
   "m": (0x3BC,), # My
   "n": (0x3BD,), # Ny
   "x": (0x3BE,), # Xi
   "o": (0x3BF,), # Omikron
   "p": (0x3C0,), # Pi
   "r": (0x3C1,), # Rho
   "s": (0x3C3,), # Sigma
   "t": (0x3C4,), # Tau
   "y": (0x3C5,), # Ypsilon
   "f": (0x3C6,), # Phi
   "ph": (0x3C6,), # Phi
   "c": (0x3C7,), # Chi
   "ch": (0x3C7,), # Chi
   "ck": (0x3BA,), # Kappa
   "w": (0x3C8,), # Psi
   "u": (0x3C9,), # Omega
   "oo": (0x3C9,), # Omega
   #
   "j": (0x3B9,), # Iota
   "q": (0x3BA,), # Kappa
   "qu": (0x3BA,), # Kappa
   "v": (0x2202,), # Differential
}

def rune(text: str) -> str: # gothic, blackletter
    base_A = ord('A')
    base_Z = ord('Z')
    base_a = ord('a')
    base_z = ord('z')
    rune_A = 0x391
    rune_O = 0x3A9
    rune_a = 0x3B1
    rune_o = 0x3C9
    rune_nabla = 0x8711
    rune_diffs = 0x2202
    out = StringIO()
    skip = False
    for i, c in enumerate(text):
        if skip:
            skip = False
            continue
        ch = ord(c)
        if base_A <= ch and ch <= base_Z:
            if i+1 < len(text):
               c2 = text[i+1]
            else:
               c2 = " "
            if c+c2 in rune_upper:
               for n in rune_upper[c+c2]:
                   out.write(chr(n))
               skip = True
            elif c in rune_upper:
               for n in rune_upper[c]:
                   out.write(chr(n))
            else:
               logg.error("did not find greek for '%s'", c)
        elif base_a <= ch and ch <= base_z:
            if i+1 < len(text):
               c2 = text[i+1]
            else:
               c2 = " "
            if c+c2 in rune_lower:
               for n in rune_lower[c+c2]:
                   out.write(chr(n))
               skip = True
            elif c in rune_lower:
               for n in rune_lower[c]:
                   out.write(chr(n))
            else:
               logg.error("did not find greek for '%s'", c)
        else:
            out.write(c)
    return out.getvalue()

def fraktur(text: str) -> str: # gothic, blackletter
    base_A = ord('A')
    base_Z = ord('Z')
    base_a = ord('a')
    base_z = ord('z')
    base_0 = ord('0')
    base_9 = ord('9')
    fraktur_A = 0x1D504
    fraktur_a = 0x1D51E
    fat_base_0 = 0x1D7CE
    fat_base_9 = 0x1D7D7
    out = StringIO()
    for c in text:
        ch = ord(c)
        if base_A <= ch and ch <= base_Z:
            out.write(chr(fraktur_A+(ch-base_A)))
        elif base_a <= ch and ch <= base_z:
            out.write(chr(fraktur_a+(ch-base_a)))
        # elif base_0 <= ch and ch <= base_9:
        #     out.write(chr(fat_base_0+(ch-base_0)))
        else:
            out.write(c)
    return out.getvalue()

def rounded(text: str) -> str: # real cursive
    base_A = ord('A')
    base_Z = ord('Z')
    base_a = ord('a')
    base_z = ord('z')
    rounded_A = 0x1D49C
    rounded_Z = 0x1D4B5
    rounded_a = 0x1D4B6
    rounded_z = 0x1D4CF
    out = StringIO()
    for c in text:
        ch = ord(c)
        if base_A <= ch and ch <= base_Z:
            out.write(chr(rounded_A+(ch-base_A)))
        elif base_a <= ch and ch <= base_z:
            out.write(chr(rounded_a+(ch-base_a)))
        else:
            out.write(c)
    return out.getvalue()

def double(text: str) -> str: # gothic, blackletter
    base_A = ord('A')
    base_Z = ord('Z')
    base_a = ord('a')
    base_z = ord('z')
    base_0 = ord('0')
    base_9 = ord('9')
    double_A = 0x1D538
    double_a = 0x1D552
    double_0 = 0x1D7D8
    double_9 = 0x1D7E1
    double_C = 0x2102 # Complex Numbers
    double_H = 0x210D # Hamilton Numbers
    double_N = 0x2115 # Natural Numbers
    double_P = 0x2119
    double_Q = 0x211A # Rational Numbers
    double_R = 0x211D # Real Numbers
    double_Z = 0x2124 # Integer Numbers
    double_map = { 'C' : double_C, 'H': double_H, 'N': double_N, 
        'P': double_P, 'Q': double_Q, 'R': double_R, 'Z': double_Z }
    out = StringIO()
    for c in text:
        ch = ord(c)
        if c in double_map:
            out.write(chr(double_map[c]))
        elif base_A <= ch and ch <= base_Z:
            out.write(chr(double_A+(ch-base_A)))
        elif base_a <= ch and ch <= base_z:
            out.write(chr(double_a+(ch-base_a)))
        elif base_0 <= ch and ch <= base_9:
            out.write(chr(double_0+(ch-base_0)))
        else:
            out.write(c)
    return out.getvalue()

def courier(text: str) -> str: # gothic, blackletter
    base_A = ord('A')
    base_Z = ord('Z')
    base_a = ord('a')
    base_z = ord('z')
    base_0 = ord('0')
    base_9 = ord('9')
    cour_A = 0x1D670
    cour_Z = 0x1D689
    cour_a = 0x1D68A
    cour_z = 0x1D6A3
    cour_0 = 0x1D7F6
    cour_9 = 0x1D7FF
    out = StringIO()
    for c in text:
        ch = ord(c)
        if base_A <= ch and ch <= base_Z:
            out.write(chr(cour_A+(ch-base_A)))
        elif base_a <= ch and ch <= base_z:
            out.write(chr(cour_a+(ch-base_a)))
        elif base_0 <= ch and ch <= base_9:
            out.write(chr(cour_0+(ch-base_0)))
        else:
            out.write(c)
    return out.getvalue()

def uppercasedouble(text: str) -> str: # gothic, blackletter
    base_A = ord('A')
    base_Z = ord('Z')
    base_a = ord('a')
    base_z = ord('z')
    double_A = 0x1D538
    double_a = 0x1D552
    out = StringIO()
    for c in text:
        ch = ord(c)
        if base_A <= ch and ch <= base_Z:
            out.write(chr(double_A+(ch-base_A)))
        else:
            out.write(c)
    return out.getvalue()

def bold(text: str) -> str:
    logg.debug("apply fat to ascii/black letters")
    base_A = ord('A')
    base_Z = ord('Z')
    base_a = ord('a')
    base_z = ord('z')
    base_0 = ord('0')
    base_9 = ord('9')
    base_sz = 0xDF
    fat_base_A = 0x1D400
    fat_base_Z = 0x1D419
    fat_base_a = 0x1D41A
    fat_base_z = 0x1D433
    fat_base_0 = 0x1D7CE
    fat_base_9 = 0x1D7D7
    sla_base_A = 0x1D434
    sla_base_Z = 0x1D44D
    sla_base_a = 0x1D44E
    sla_base_z = 0x1D467
    fat_sla_base_A = 0x1D468
    fat_sla_base_Z = 0x1D481
    fat_sla_base_a = 0x1D482
    fat_sla_base_z = 0x1D49B
    sans_A = 0x1D5A0
    sans_Z = 0x1D5B9
    sans_a = 0x1D5BA
    sans_z = 0x1D5D3
    sans_0 = 0x1D7E2
    sans_9 = 0x1D7EB
    fat_sans_A = 0x1D5D4
    fat_sans_Z = 0x1D5ED
    fat_sans_a = 0x1D5EE
    fat_sans_z = 0x1D607
    fat_sans_0 = 0x1D7EC
    fat_sans_9 = 0x1D8F5
    sla_sans_A = 0x1D608
    sla_sans_Z = 0x1D621
    sla_sans_a = 0x1D622
    sla_sans_z = 0x1D63B
    fat_sla_sans_A = 0x1D63E
    fat_sla_sans_Z = 0x1D655
    fat_sla_sans_a = 0x1D656
    fat_sla_sans_z = 0x1D66F
    #
    fraktur_A = 0x1D504
    fraktur_Z = 0x1D51D
    fraktur_a = 0x1D51E
    fraktur_z = 0x1D537
    fat_fraktur_A = 0x1D56C
    fat_fraktur_Z = 0x1D585
    fat_fraktur_a = 0x1D586
    fat_fraktur_z = 0x1D59F
    rounded_A = 0x1D49C
    rounded_Z = 0x1D4B5
    rounded_a = 0x1D4B6
    rounded_z = 0x1D4CF
    fat_rounded_A = 0x1D4D0
    fat_rounded_Z = 0x1D4E9
    fat_rounded_a = 0x1D4EA
    fat_rounded_z = 0x1D503
    greek_A = 0x391
    greek_O = 0x3A9
    greek_a = 0x3B1
    greek_o = 0x3C9
    greek_nabla = 0x8711
    greek_diffs = 0x2202
    fat_greek_A = 0x1D6A8
    fat_greek_O = 0x1D6C0
    fat_greek_nabla = 0x1D6C1
    fat_greek_a = 0x1D6C2
    fat_greek_o = 0x1D6DA
    fat_greek_diffs = 0x1D6DB
    sla_greek_A = 0x1D6E2
    sla_greek_O = 0x1D6FA
    sla_greek_nabla = 0x1D6FB
    sla_greek_a = 0x1D6FC
    sla_greek_o = 0x1D714
    sla_greek_diffs = 0x1D715
    fat_sla_greek_A = 0x1D71C
    fat_sla_greek_O = 0x1D734
    fat_sla_greek_nabla = 0x1D735
    fat_sla_greek_a = 0x1D736
    fat_sla_greek_o = 0x1D74E
    fat_sla_greek_diffs = 0x1D74F
    out = StringIO()
    for c in text:
        ch = ord(c)
        if base_A <= ch and ch <= base_Z:
            out.write(chr(fat_base_A+(ch-base_A)))
        elif base_a <= ch and ch <= base_z:
            out.write(chr(fat_base_a+(ch-base_a)))
        elif base_0 <= ch and ch <= base_9:
            out.write(chr(fat_base_0+(ch-base_0)))
        elif base_sz == ch:
            out.write(chr(fat_greek_a+1))
        elif sla_base_A <= ch and ch <= sla_base_Z:
            out.write(chr(fat_sla_base_A+(ch-sla_base_A)))
        elif sla_base_a <= ch and ch <= sla_base_z:
            out.write(chr(fat_sla_base_a+(ch-sla_base_a)))
        elif sans_A <= ch and ch <= sans_Z:
            out.write(chr(fat_sans_A+(ch-sans_A)))
        elif sans_a <= ch and ch <= sans_z:
            out.write(chr(fat_sans_a+(ch-sans_a)))
        elif sans_0 <= ch and ch <= sans_9:
            out.write(chr(fat_sans_0+(ch-sans_0)))
        elif sla_sans_A <= ch and ch <= sla_sans_Z:
            out.write(chr(fat_sla_sans_A+(ch-sla_sans_A)))
        elif sla_sans_a <= ch and ch <= sla_sans_z:
            out.write(chr(fat_sla_sans_a+(ch-sla_sans_a)))
        elif fraktur_A <= ch and ch <= fraktur_Z:
            out.write(chr(fat_fraktur_A+(ch-fraktur_A)))
        elif fraktur_a <= ch and ch <= fraktur_z:
            out.write(chr(fat_fraktur_a+(ch-fraktur_a)))
        elif rounded_A <= ch and ch <= rounded_Z:
            out.write(chr(fat_rounded_A+(ch-rounded_A)))
        elif rounded_a <= ch and ch <= rounded_z:
            out.write(chr(fat_rounded_a+(ch-rounded_a)))
        elif greek_A <= ch and ch <= greek_O:
            out.write(chr(fat_greek_A+(ch-greek_A)))
        elif greek_a <= ch and ch <= greek_o:
            out.write(chr(fat_greek_a+(ch-greek_a)))
        elif greek_nabla == ch:
            out.write(chr(fat_greek_nabla))
        elif greek_diffs == ch:
            out.write(chr(fat_greek_diffs))
        elif sla_greek_A <= ch and ch <= sla_greek_O+1:
            out.write(chr(fat_sla_greek_A+(ch-sla_greek_A)))
        elif sla_greek_a <= ch and ch <= sla_greek_o+1:
            out.write(chr(fat_sla_greek_a+(ch-sla_greek_a)))
        else:
            out.write(c)
    return out.getvalue()

def ital(text: str) -> str:
    logg.debug("apply slant to ascii/black letters")
    base_A = ord('A')
    base_Z = ord('Z')
    base_a = ord('a')
    base_z = ord('z')
    base_0 = ord('0')
    base_9 = ord('9')
    base_sz = 0xDF
    sla_base_A = 0x1D434
    sla_base_Z = 0x1D44D
    sla_base_a = 0x1D44E
    sla_base_z = 0x1D467
    sans_A = 0x1D5A0
    sans_Z = 0x1D5B9
    sans_a = 0x1D5BA
    sans_z = 0x1D5D3
    sla_sans_A = 0x1D608
    sla_sans_Z = 0x1D621
    sla_sans_a = 0x1D622
    sla_sans_z = 0x1D63B
    fat_base_A = 0x1D400
    fat_base_Z = 0x1D419
    fat_base_a = 0x1D41A
    fat_base_z = 0x1D433
    fat_sla_base_A = 0x1D468
    fat_sla_base_Z = 0x1D481
    fat_sla_base_a = 0x1D482
    fat_sla_base_z = 0x1D49B
    fat_sans_A = 0x1D5D4
    fat_sans_Z = 0x1D5ED
    fat_sans_a = 0x1D5EE
    fat_sans_z = 0x1D607
    fat_sla_sans_A = 0x1D63E
    fat_sla_sans_Z = 0x1D655
    fat_sla_sans_a = 0x1D656
    fat_sla_sans_z = 0x1D66F
    #
    fraktur_A = 0x1D504
    fraktur_Z = 0x1D51D
    fraktur_a = 0x1D51E
    fraktur_z = 0x1D537
    sla_fraktur_A = 0x1D56C
    sla_fraktur_Z = 0x1D585
    sla_fraktur_a = 0x1D586
    sla_fraktur_z = 0x1D59F
    fat_fraktur_A = 0x1D56C
    fat_fraktur_Z = 0x1D585
    fat_fraktur_a = 0x1D586
    fat_fraktur_z = 0x1D59F
    # fat_sla_fraktur_A = n/a
    # fat_sla_fraktur_Z = n/a
    # fat_sla_fraktur_a = n/a
    # fat_sla_fraktur_z = n/a
    greek_A = 0x391
    greek_O = 0x3A9
    greek_a = 0x3B1
    greek_o = 0x3C9
    greek_nabla = 0x8711
    greek_diffs = 0x2202
    sla_greek_A = 0x1D6E2
    sla_greek_O = 0x1D6FA
    sla_greek_nabla = 0x1D6FB
    sla_greek_a = 0x1D6FC
    sla_greek_o = 0x1D714
    sla_greek_diffs = 0x1D715
    fat_greek_A = 0x1D6A8
    fat_greek_O = 0x1D6C0
    fat_greek_nabla = 0x1D6C1
    fat_greek_a = 0x1D6C2
    fat_greek_o = 0x1D6DA
    fat_greek_diffs = 0x1D6DB
    fat_sla_greek_A = 0x1D71C
    fat_sla_greek_O = 0x1D734
    fat_sla_greek_nabla = 0x1D735
    fat_sla_greek_a = 0x1D736
    fat_sla_greek_o = 0x1D74E
    fat_sla_greek_diffs = 0x1D74F
    out = StringIO()
    for c in text:
        ch = ord(c)
        if base_A <= ch and ch <= base_Z:
            out.write(chr(sla_base_A+(ch-base_A)))
        elif base_a <= ch and ch <= base_z:
            out.write(chr(sla_base_a+(ch-base_a)))
        elif base_sz == ch:
            out.write(chr(sla_greek_a+1))
        elif fat_base_A <= ch and ch <= fat_base_Z:
            out.write(chr(fat_sla_base_A+(ch-fat_base_A)))
        elif fat_base_a <= ch and ch <= fat_base_z:
            out.write(chr(fat_sla_base_a+(ch-fat_base_a)))
        elif sans_A <= ch and ch <= sans_Z:
            out.write(chr(sla_sans_A+(ch-sans_A)))
        elif sans_a <= ch and ch <= sans_z:
            out.write(chr(sla_sans_a+(ch-sans_a)))
        elif fat_sans_A <= ch and ch <= fat_sans_Z:
            out.write(chr(fat_sla_sans_A+(ch-fat_sans_A)))
        elif fat_sans_a <= ch and ch <= fat_sans_z:
            out.write(chr(fat_sla_sans_a+(ch-fat_sans_a)))
        elif fraktur_A <= ch and ch <= fraktur_Z:
            out.write(chr(sla_fraktur_A+(ch-fraktur_A)))
        elif fraktur_a <= ch and ch <= fraktur_z:
            out.write(chr(sla_fraktur_a+(ch-fraktur_a)))
        elif greek_A <= ch and ch <= greek_O:
            out.write(chr(sla_greek_A+(ch-greek_A)))
        elif greek_a <= ch and ch <= greek_o:
            out.write(chr(sla_greek_a+(ch-greek_a)))
        elif greek_nabla == ch:
            out.write(chr(sla_greek_nabla))
        elif greek_diffs == ch:
            out.write(chr(sla_greek_diffs))
        elif fat_greek_A <= ch and ch <= fat_greek_O+1:
            out.write(chr(fat_sla_greek_A+(ch-fat_greek_A)))
        elif fat_greek_a <= ch and ch <= fat_greek_o+1:
            out.write(chr(fat_sla_greek_a+(ch-fat_greek_a)))
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
    if "frac" in cmd or "value" in cmd:
        text = fractions(text)
    if "doub" in cmd or "wide" in cmd:
        text = double(text)
    if "caps" in cmd or "init" in cmd:
        text = uppercasedouble(text)
    if "greek" in cmd or "math" in cmd:
        text = greek(text)
    if "black" in cmd or "frak" in cmd:
        text = fraktur(text)
    if "ital" in cmd or "name" in cmd or "slant" in cmd:
        text = ital(text)
    if "round" in cmd or "scripted" in cmd or "writ" in cmd:
        text = rounded(text)
    if "cour" in cmd or "type" in cmd or "mono" in cmd:
        text = courier(text)
    if "fat" in cmd or "bold" in cmd:
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
     *caps* *init*    uppercase chars to double stroke
     *nobr* *word*    using base nobr spaces
     *thin* *value*   using thin nobr spaces
    """
    
if __name__ == "__main__":
    __opt = scan(sys.argv[1:])
    logging.basicConfig(level=max(0, logging.WARNING - __opt.verbose * 10))
    if __opt.helpinfo:
        print(helpinfo())
    else:
        print(convert(__opt.cmd, __opt.text))
