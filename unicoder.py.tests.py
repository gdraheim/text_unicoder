#! /usr/bin/python3
""" testing the unicoder.py functions """

import sys, os
import unittest
import logging
from fnmatch import fnmatchcase as fnmatch

import unicoder

logg = logging.getLogger("TEST")

base_abcdefghijklmnopqrstuvwxyz = ":abcdefghijklmnopqrstuvwxyz"
base_ABCDEFGHIJKLMNOPQRSTUVWXYZ = ":ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mono_abcdefghijklmnopqrstuvwxyz = ":𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣"
mono_ABCDEFGHIJKLMNOPQRSTUVWXYZ = ":𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉"
sans_abcdefghijklmnopqrstuvwxyz = ":𝖺𝖻𝖼𝖽𝖾𝖿𝗀𝗁𝗂𝗃𝗄𝗅𝗆𝗇𝗈𝗉𝗊𝗋𝗌𝗍𝗎𝗏𝗐𝗑𝗒𝗓"
sans_ABCDEFGHIJKLMNOPQRSTUVWXYZ = ":𝖠𝖡𝖢𝖣𝖤𝖥𝖦𝖧𝖨𝖩𝖪𝖫𝖬𝖭𝖮𝖯𝖰𝖱𝖲𝖳𝖴𝖵𝖶𝖷𝖸𝖹"
base_0123456789 = ":0123456789"
mono_0123456789 = ":𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿"
sans_0123456789 = ":𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫"

bold_sans_abcdefghijklmnopqrstuvwxyz = ":𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇"
bold_sans_ABCDEFGHIJKLMNOPQRSTUVWXYZ = ":𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭"
bold_sans_0123456789 = ":𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"
ital_sans_abcdefghijklmnopqrstuvwxyz = ":𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻"
ital_sans_ABCDEFGHIJKLMNOPQRSTUVWXYZ = ":𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡"
ital_sans_0123456789 = ":𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫" # aka sans
bold_ital_sans_abcdefghijklmnopqrstuvwxyz = ":𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯"
bold_ital_sans_ABCDEFGHIJKLMNOPQRSTUVWXYZ = ":𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕"
bold_ital_sans_0123456789 = ":𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵" # aka bold_sans

class UnicoderTest(unittest.TestCase):
    def test_001_opt_scan(self) -> None:
        opt = unicoder.scan(["-v"])
        self.assertEqual(opt.verbose, 1)
    def test_002_opt_scan(self) -> None:
        opt = unicoder.scan(["-vv"])
        self.assertEqual(opt.verbose, 2)
    def test_003_opt_scan(self) -> None:
        opt = unicoder.scan(["-v", "-vv"])
        self.assertEqual(opt.verbose, 3)
    def test_110_bold_base(self) -> None:
        uni = unicoder.convert("fix", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, base_abcdefghijklmnopqrstuvwxyz)
    def test_111_bold_base(self) -> None:
        uni = unicoder.convert("fat", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳")
    def test_112_bold_base(self) -> None:
        uni = unicoder.convert("bold", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳")
    def test_113_bold_base(self) -> None:
        uni = unicoder.convert("fat", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙")
    def test_114_bold_base(self) -> None:
        uni = unicoder.convert("bold", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙")
    def test_115_bold_base(self) -> None:
        uni = unicoder.bold(base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳")
    def test_116_bold_base(self) -> None:
        uni = unicoder.bold(base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳")
    def test_117_bold_base(self) -> None:
        uni = unicoder.bold(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙")
    def test_118_bold_base(self) -> None:
        uni = unicoder.bold(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙")
    def test_120_ital_base(self) -> None:
        uni = unicoder.convert("fix", ":abcdefg-ijklmnopqrstuvwxyz")
        self.assertEqual(uni, ":abcdefg-ijklmnopqrstuvwxyz")
        uni = unicoder.convert("fix", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":abcdefghijklmnopqrstuvwxyz")
    def test_121_ital_base(self) -> None:
        uni = unicoder.convert("slant", ":abcdefg-ijklmnopqrstuvwxyz")
        self.assertEqual(uni, ":𝑎𝑏𝑐𝑑𝑒𝑓𝑔-𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧")
        uni = unicoder.convert("slant", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧")
    def test_122_ital_base(self) -> None:
        uni = unicoder.convert("ital", ":abcdefg-ijklmnopqrstuvwxyz")
        self.assertEqual(uni, ":𝑎𝑏𝑐𝑑𝑒𝑓𝑔-𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧")
        uni = unicoder.convert("ital", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧")
    def test_123_ital_base(self) -> None:
        uni = unicoder.convert("slant", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍")
    def test_124_ital_base(self) -> None:
        uni = unicoder.convert("ital", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍")
    def test_125_ital_base(self) -> None:
        uni = unicoder.ital(":abcdefg-ijklmnopqrstuvwxyz")
        self.assertEqual(uni, ":𝑎𝑏𝑐𝑑𝑒𝑓𝑔-𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧")
        uni = unicoder.ital(base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧")
    def test_126_ital_base(self) -> None:
        uni = unicoder.ital(":abcdefg-ijklmnopqrstuvwxyz")
        self.assertEqual(uni, ":𝑎𝑏𝑐𝑑𝑒𝑓𝑔-𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧")
        uni = unicoder.ital(base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧")
    def test_127_ital_base(self) -> None:
        uni = unicoder.ital(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍")
    def test_128_ital_base(self) -> None:
        uni = unicoder.ital(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍")
    def test_130_bold_ital_base(self) -> None:
        uni = unicoder.convert("fix", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, base_abcdefghijklmnopqrstuvwxyz)
    def test_131_ital_bold_base(self) -> None:
        uni = unicoder.convert("fatslant", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛")
    def test_132_ital_bold_base(self) -> None:
        uni = unicoder.convert("italbold", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛")
    def test_133_ital_bold_base(self) -> None:
        uni = unicoder.convert("fatslant", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁")
    def test_134_ital_bold_base(self) -> None:
        uni = unicoder.convert("italbold", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁")
    def test_136_ital_bold_base(self) -> None:
        uni = unicoder.ital(unicoder.bold(base_abcdefghijklmnopqrstuvwxyz))
        self.assertEqual(uni, ":𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛")
    def test_137_ital_bold_base(self) -> None:
        uni = unicoder.ital(unicoder.bold(base_abcdefghijklmnopqrstuvwxyz))
        self.assertEqual(uni, ":𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛")
    def test_138_ital_bold_base(self) -> None:
        uni = unicoder.ital(unicoder.bold(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ))
        self.assertEqual(uni, ":𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁")
    def test_139_ital_bold_base(self) -> None:
        uni = unicoder.ital(unicoder.bold(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ))
        self.assertEqual(uni, ":𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁")
    def test_140_bold_ital_base(self) -> None:
        uni = unicoder.bold(unicoder.ital(base_abcdefghijklmnopqrstuvwxyz))
        self.assertEqual(uni, ":𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛")
    def test_141_bold_ital_base(self) -> None:
        uni = unicoder.bold(unicoder.ital(base_abcdefghijklmnopqrstuvwxyz))
        self.assertEqual(uni, ":𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛")
    def test_142_bold_ital_base(self) -> None:
        uni = unicoder.bold(unicoder.ital(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ))
        self.assertEqual(uni, ":𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁")
    def test_143_bold_ital_base(self) -> None:
        uni = unicoder.bold(unicoder.ital(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ))
        self.assertEqual(uni, ":𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁")
    def test_150_bold_numm(self) -> None:
        uni = unicoder.convert("fix", base_0123456789)
        self.assertEqual(uni, base_0123456789)
    def test_151_bold_numm(self) -> None:
        uni = unicoder.convert("fat", base_0123456789)
        self.assertEqual(uni, ":𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗")
    def test_152_bold_numm(self) -> None:
        uni = unicoder.convert("bold", base_0123456789)
        self.assertEqual(uni, ":𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗")
    def test_155_bold_numm(self) -> None:
        uni = unicoder.bold(base_0123456789)
        self.assertEqual(uni, ":𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗")
    def test_156_bold_numm(self) -> None:
        uni = unicoder.bold(base_0123456789)
        self.assertEqual(uni, ":𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗")
    def test_160_ital_numm(self) -> None:
        uni = unicoder.convert("fix", base_0123456789)
        self.assertEqual(uni, base_0123456789)
    def test_161_ital_numm(self) -> None:
        uni = unicoder.convert("slant", base_0123456789)
        self.assertEqual(uni, base_0123456789)
    def test_162_ital_numm(self) -> None:
        uni = unicoder.convert("ital", base_0123456789)
        self.assertEqual(uni, base_0123456789)
    def test_170_bold_base_sz(self) -> None:
        uni = unicoder.convert("fix", ":abcxyzABCXYZ0123456789ß")
        self.assertEqual(uni, ":abcxyzABCXYZ0123456789ß")
    def test_171_bold_base_sz(self) -> None:
        uni = unicoder.convert("fat", ":abcxyzABCXYZ0123456789ß")
        self.assertEqual(uni, ":𝐚𝐛𝐜𝐱𝐲𝐳𝐀𝐁𝐂𝐗𝐘𝐙𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𝛃")
    def test_172_bold_base_sz(self) -> None:
        uni = unicoder.convert("bold", ":abcxyzABCXYZ0123456789ß")
        self.assertEqual(uni, ":𝐚𝐛𝐜𝐱𝐲𝐳𝐀𝐁𝐂𝐗𝐘𝐙𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𝛃")
    def test_180_ital_base_sz(self) -> None:
        uni = unicoder.convert("fix", ":abcxyzABCXYZ0123456789ß")
        self.assertEqual(uni, ":abcxyzABCXYZ0123456789ß")
    def test_181_ital_base_sz(self) -> None:
        uni = unicoder.convert("slant", ":abcxyzABCXYZ0123456789ß")
        self.assertEqual(uni, ":𝑎𝑏𝑐𝑥𝑦𝑧𝐴𝐵𝐶𝑋𝑌𝑍0123456789𝛽")
    def test_182_ital_base_sz(self) -> None:
        uni = unicoder.convert("ital", ":abcxyzABCXYZ0123456789ß")
        self.assertEqual(uni, ":𝑎𝑏𝑐𝑥𝑦𝑧𝐴𝐵𝐶𝑋𝑌𝑍0123456789𝛽")
    def test_190_bold_ital_base_sz(self) -> None:
        uni = unicoder.convert("fix", ":abcxyzABCXYZ0123456789ß")
        self.assertEqual(uni, ":abcxyzABCXYZ0123456789ß")
    def test_191_bold_ital_base_sz(self) -> None:
        uni = unicoder.convert("fatslant", ":abcxyzABCXYZ0123456789ß")
        self.assertEqual(uni, ":𝒂𝒃𝒄𝒙𝒚𝒛𝑨𝑩𝑪𝑿𝒀𝒁𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𝜷")
    def test_192_bold_ital_base_sz(self) -> None:
        uni = unicoder.convert("italbold", ":abcxyzABCXYZ0123456789ß")
        self.assertEqual(uni, ":𝒂𝒃𝒄𝒙𝒚𝒛𝑨𝑩𝑪𝑿𝒀𝒁𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𝜷")
    #
    def test_200_norm_double(self) -> None:
        uni = unicoder.convert("fix", ":abcxyzABCXYZ")
        self.assertEqual(uni, ":abcxyzABCXYZ")
    def test_201_norm_double(self) -> None:
        uni = unicoder.convert("double", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫")
    def test_202_norm_double(self) -> None:
        uni = unicoder.convert("wide", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫")
    def test_203_norm_double(self) -> None:
        uni = unicoder.convert("double", ":AB-DEFG-IJKLM-O---STUVWXY-")
        self.assertEqual(uni, ":𝔸𝔹-𝔻𝔼𝔽𝔾-𝕀𝕁𝕂𝕃𝕄-𝕆---𝕊𝕋𝕌𝕍𝕎𝕏𝕐-")
        uni = unicoder.convert("double", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ")
    def test_204_norm_double(self) -> None:
        uni = unicoder.convert("wide", ":AB-DEFG-IJKLM-O---STUVWXY-")
        self.assertEqual(uni, ":𝔸𝔹-𝔻𝔼𝔽𝔾-𝕀𝕁𝕂𝕃𝕄-𝕆---𝕊𝕋𝕌𝕍𝕎𝕏𝕐-")
        uni = unicoder.convert("wide", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ")
    def test_205_norm_double(self) -> None:
        uni = unicoder.double(base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫")
    def test_206_norm_double(self) -> None:
        uni = unicoder.double(base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫")
    def test_207_norm_double(self) -> None:
        uni = unicoder.double(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ")
    def test_208_norm_double(self) -> None:
        uni = unicoder.double(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ")
    def test_210_bold_double(self) -> None:
        uni = unicoder.convert("fix", ":abcxyzABXY")
        self.assertEqual(uni, ":abcxyzABXY")
    def test_211_bold_double(self) -> None:
        uni = unicoder.convert("fatdouble", ":abcxyzABXY")
        self.assertEqual(uni, ":𝕒𝕓𝕔𝕩𝕪𝕫𝔸𝔹𝕏𝕐")
    def test_212_bold_double(self) -> None:
        uni = unicoder.convert("boldwide", ":abcxyzABXY")
        self.assertEqual(uni, ":𝕒𝕓𝕔𝕩𝕪𝕫𝔸𝔹𝕏𝕐")
    def test_215_bold_double(self) -> None:
        uni = unicoder.bold(unicoder.double(":abcxyzABXY"))
        self.assertEqual(uni, ":𝕒𝕓𝕔𝕩𝕪𝕫𝔸𝔹𝕏𝕐")
    def test_216_bold_double(self) -> None:
        uni = unicoder.bold(unicoder.double(":abcxyzABXY"))
        self.assertEqual(uni, ":𝕒𝕓𝕔𝕩𝕪𝕫𝔸𝔹𝕏𝕐")
    def test_240_numm_double(self) -> None:
        uni = unicoder.convert("fix", base_0123456789)
        self.assertEqual(uni, base_0123456789)
    def test_241_numm_double(self) -> None:
        uni = unicoder.convert("double", base_0123456789)
        self.assertEqual(uni, ":𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡")
    def test_242_numm_double(self) -> None:
        uni = unicoder.convert("wide", base_0123456789)
        self.assertEqual(uni, ":𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡")
    def test_245_numm_double(self) -> None:
        uni = unicoder.double(base_0123456789)
        self.assertEqual(uni, ":𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡")
    def test_246_numm_double(self) -> None:
        uni = unicoder.double(base_0123456789)
        self.assertEqual(uni, ":𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡")
    #
    def test_250_norm_script(self) -> None:
        uni = unicoder.convert("fix", ":abcxyzABCXYZ")
        self.assertEqual(uni, ":abcxyzABCXYZ")
    def test_251_norm_script(self) -> None:
        uni = unicoder.convert("script", ":abcd-f-hijklmn-pqrstuvwxyz")
        self.assertEqual(uni, ":𝒶𝒷𝒸𝒹-𝒻-𝒽𝒾𝒿𝓀𝓁𝓂𝓃-𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏")
        uni = unicoder.convert("script", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏")
    def test_252_norm_script(self) -> None:
        uni = unicoder.convert("round", ":abcd-f-hijklmn-pqrstuvwxyz")
        self.assertEqual(uni, ":𝒶𝒷𝒸𝒹-𝒻-𝒽𝒾𝒿𝓀𝓁𝓂𝓃-𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏")
        uni = unicoder.convert("round", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏")
    def test_253_norm_script(self) -> None:
        uni = unicoder.convert("script", ":A-CD--G--JK--NOPQ-STUVWXYZ")
        self.assertEqual(uni, ":𝒜-𝒞𝒟--𝒢--𝒥𝒦--𝒩𝒪𝒫𝒬-𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵")
        uni = unicoder.convert("script", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵")
    def test_254_norm_script(self) -> None:
        uni = unicoder.convert("round", ":A-CD--G--JK--NOPQ-STUVWXYZ")
        self.assertEqual(uni, ":𝒜-𝒞𝒟--𝒢--𝒥𝒦--𝒩𝒪𝒫𝒬-𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵")
        uni = unicoder.convert("round", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵")
    def test_255_norm_script(self) -> None:
        uni = unicoder.script(":abcd-f-hijklmn-pqrstuvwxyz")
        self.assertEqual(uni, ":𝒶𝒷𝒸𝒹-𝒻-𝒽𝒾𝒿𝓀𝓁𝓂𝓃-𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏")
        uni = unicoder.script(base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏")
    def test_256_norm_script(self) -> None:
        uni = unicoder.script(":abcd-f-hijklmn-pqrstuvwxyz")
        self.assertEqual(uni, ":𝒶𝒷𝒸𝒹-𝒻-𝒽𝒾𝒿𝓀𝓁𝓂𝓃-𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏")
        uni = unicoder.script(base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏")
    def test_257_norm_script(self) -> None:
        uni = unicoder.script(":A-CD--G--JK--NOPQ-STUVWXYZ")
        self.assertEqual(uni, ":𝒜-𝒞𝒟--𝒢--𝒥𝒦--𝒩𝒪𝒫𝒬-𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵")
        uni = unicoder.script(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵")
    def test_258_norm_script(self) -> None:
        uni = unicoder.script(":A-CD--G--JK--NOPQ-STUVWXYZ")
        self.assertEqual(uni, ":𝒜-𝒞𝒟--𝒢--𝒥𝒦--𝒩𝒪𝒫𝒬-𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵")
        uni = unicoder.script(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵")
    def test_260_bold_script(self) -> None:
        uni = unicoder.convert("fix", ":abcxyzABXY")
        self.assertEqual(uni, ":abcxyzABXY")
    def test_261_bold_script(self) -> None:
        uni = unicoder.convert("fatscript", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃")
    def test_262_bold_script(self) -> None:
        uni = unicoder.convert("boldround", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃")
    def test_263_bold_script(self) -> None:
        uni = unicoder.convert("fatscript", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩")
    def test_264_bold_script(self) -> None:
        uni = unicoder.convert("boldround", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩")
    def test_272_bold_script(self) -> None:
        uni = unicoder.bold(unicoder.script(base_abcdefghijklmnopqrstuvwxyz))
        self.assertEqual(uni, ":𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃")
    def test_273_bold_script(self) -> None:
        uni = unicoder.bold(unicoder.script(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ))
        self.assertEqual(uni, ":𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩")
    def test_277_bold_script(self) -> None:
        uni = unicoder.script(unicoder.bold(base_abcdefghijklmnopqrstuvwxyz))
        self.assertEqual(uni, ":𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃")
    def test_278_bold_script(self) -> None:
        uni = unicoder.script(unicoder.bold(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ))
        self.assertEqual(uni, ":𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩")
    def test_290_numm_script(self) -> None:
        uni = unicoder.convert("fix", base_0123456789)
        self.assertEqual(uni, base_0123456789)
    def test_291_numm_script(self) -> None:
        uni = unicoder.convert("script", base_0123456789)
        self.assertEqual(uni, base_0123456789)
    def test_292_numm_script(self) -> None:
        uni = unicoder.convert("round", base_0123456789)
        self.assertEqual(uni, base_0123456789)
    def test_295_numm_script(self) -> None:
        uni = unicoder.script(base_0123456789)
        self.assertEqual(uni, base_0123456789)
    def test_296_numm_script(self) -> None:
        uni = unicoder.script(base_0123456789)
        self.assertEqual(uni, base_0123456789)
    #
    def test_300_norm_courier(self) -> None:
        uni = unicoder.convert("fix", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, base_abcdefghijklmnopqrstuvwxyz)
        self.assertNotEqual(base_abcdefghijklmnopqrstuvwxyz,
                            sans_abcdefghijklmnopqrstuvwxyz)
        self.assertNotEqual(mono_abcdefghijklmnopqrstuvwxyz,
                            sans_abcdefghijklmnopqrstuvwxyz)
    def test_301_norm_courier(self) -> None:
        uni = unicoder.convert("courier", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, mono_abcdefghijklmnopqrstuvwxyz)
    def test_302_norm_courier(self) -> None:
        uni = unicoder.convert("mono", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, mono_abcdefghijklmnopqrstuvwxyz)
    def test_303_norm_courier(self) -> None:
        uni = unicoder.convert("courier", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, mono_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
    def test_304_norm_courier(self) -> None:
        uni = unicoder.convert("mono", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, mono_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
    def test_305_norm_courier(self) -> None:
        uni = unicoder.courier(base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, mono_abcdefghijklmnopqrstuvwxyz)
    def test_306_norm_courier(self) -> None:
        uni = unicoder.courier(base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, mono_abcdefghijklmnopqrstuvwxyz)
    def test_307_norm_courier(self) -> None:
        uni = unicoder.courier(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, mono_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
    def test_308_norm_courier(self) -> None:
        uni = unicoder.courier(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, mono_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
    def test_340_numm_courier(self) -> None:
        uni = unicoder.convert("fix", base_0123456789)
        self.assertEqual(uni, base_0123456789)
    def test_341_numm_courier(self) -> None:
        uni = unicoder.convert("courier", base_0123456789)
        self.assertEqual(uni, mono_0123456789)
    def test_342_numm_courier(self) -> None:
        uni = unicoder.convert("mono", base_0123456789)
        self.assertEqual(uni, mono_0123456789)
    def test_345_numm_courier(self) -> None:
        uni = unicoder.courier(base_0123456789)
        self.assertEqual(uni, mono_0123456789)
    def test_346_numm_courier(self) -> None:
        uni = unicoder.courier(base_0123456789)
        self.assertEqual(uni, mono_0123456789)
    #
    def test_400_norm_sans(self) -> None:
        uni = unicoder.convert("fix", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, base_abcdefghijklmnopqrstuvwxyz)
        self.assertNotEqual(base_abcdefghijklmnopqrstuvwxyz,
                            sans_abcdefghijklmnopqrstuvwxyz)
        self.assertNotEqual(mono_abcdefghijklmnopqrstuvwxyz,
                            sans_abcdefghijklmnopqrstuvwxyz)
    def test_401_norm_sans(self) -> None:
        uni = unicoder.convert("sans", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, sans_abcdefghijklmnopqrstuvwxyz)
    def test_402_norm_sans(self) -> None:
        uni = unicoder.convert("vect", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, sans_abcdefghijklmnopqrstuvwxyz)
    def test_403_norm_sans(self) -> None:
        uni = unicoder.convert("sans", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, sans_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
    def test_404_norm_sans(self) -> None:
        uni = unicoder.convert("vect", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, sans_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
    def test_405_norm_sans(self) -> None:
        uni = unicoder.sans(base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, sans_abcdefghijklmnopqrstuvwxyz)
    def test_406_norm_sans(self) -> None:
        uni = unicoder.sans(base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, sans_abcdefghijklmnopqrstuvwxyz)
    def test_407_norm_sans(self) -> None:
        uni = unicoder.sans(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, sans_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
    def test_408_norm_sans(self) -> None:
        uni = unicoder.sans(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, sans_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
    def test_410_numm_sans(self) -> None:
        uni = unicoder.convert("fix", base_0123456789)
        self.assertEqual(uni, base_0123456789)
    def test_411_numm_sans(self) -> None:
        uni = unicoder.convert("sans", base_0123456789)
        self.assertEqual(uni, sans_0123456789)
    def test_412_numm_sans(self) -> None:
        uni = unicoder.convert("vect", base_0123456789)
        self.assertEqual(uni, sans_0123456789)
    def test_415_numm_sans(self) -> None:
        uni = unicoder.sans(base_0123456789)
        self.assertEqual(uni, sans_0123456789)
    def test_416_numm_sans(self) -> None:
        uni = unicoder.sans(base_0123456789)
        self.assertEqual(uni, sans_0123456789)
    def test_421_bold_sans(self) -> None:
        uni = unicoder.convert("boldsans", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, bold_sans_abcdefghijklmnopqrstuvwxyz)
    def test_422_bold_sans(self) -> None:
        uni = unicoder.convert("fatvect", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, bold_sans_abcdefghijklmnopqrstuvwxyz)
    def test_423_bold_sans(self) -> None:
        uni = unicoder.convert("boldsans", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, bold_sans_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
    def test_424_bold_sans(self) -> None:
        uni = unicoder.convert("fatvect", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, bold_sans_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
    def test_425_bold_sans(self) -> None:
        uni = unicoder.bold(unicoder.sans(base_abcdefghijklmnopqrstuvwxyz))
        self.assertEqual(uni, bold_sans_abcdefghijklmnopqrstuvwxyz)
    def test_426_bold_sans(self) -> None:
        uni = unicoder.sans(unicoder.bold(base_abcdefghijklmnopqrstuvwxyz))
        self.assertEqual(uni, bold_sans_abcdefghijklmnopqrstuvwxyz)
    def test_427_bold_sans(self) -> None:
        uni = unicoder.bold(unicoder.sans(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ))
        self.assertEqual(uni, bold_sans_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
    def test_428_bold_sans(self) -> None:
        uni = unicoder.sans(unicoder.bold(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ))
        self.assertEqual(uni, bold_sans_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
    def test_430_numm_bold_sans(self) -> None:
        uni = unicoder.convert("fix", base_0123456789)
        self.assertEqual(uni, base_0123456789)
    def test_431_numm_bold_sans(self) -> None:
        uni = unicoder.convert("boldsans", base_0123456789)
        self.assertEqual(uni, bold_sans_0123456789)
    def test_432_numm_bold_sans(self) -> None:
        uni = unicoder.convert("fatvect", base_0123456789)
        self.assertEqual(uni, bold_sans_0123456789)
    def test_435_numm_bold_sans(self) -> None:
        uni = unicoder.bold(unicoder.sans(base_0123456789))
        self.assertEqual(uni, bold_sans_0123456789)
    def test_436_numm_bold_sans(self) -> None:
        uni = unicoder.sans(unicoder.bold(base_0123456789))
        self.assertEqual(uni, bold_sans_0123456789)
    def test_441_ital_sans(self) -> None:
        uni = unicoder.convert("italsans", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ital_sans_abcdefghijklmnopqrstuvwxyz)
    def test_442_ital_sans(self) -> None:
        uni = unicoder.convert("slantvect", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ital_sans_abcdefghijklmnopqrstuvwxyz)
    def test_443_ital_sans(self) -> None:
        uni = unicoder.convert("italsans", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ital_sans_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
    def test_444_ital_sans(self) -> None:
        uni = unicoder.convert("slantvect", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ital_sans_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
    def test_445_ital_sans(self) -> None:
        uni = unicoder.ital(unicoder.sans(base_abcdefghijklmnopqrstuvwxyz))
        self.assertEqual(uni, ital_sans_abcdefghijklmnopqrstuvwxyz)
    def test_446_ital_sans(self) -> None:
        uni = unicoder.sans(unicoder.ital(base_abcdefghijklmnopqrstuvwxyz))
        self.assertEqual(uni, ital_sans_abcdefghijklmnopqrstuvwxyz)
    def test_447_ital_sans(self) -> None:
        uni = unicoder.ital(unicoder.sans(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ))
        self.assertEqual(uni, ital_sans_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
    def test_448_ital_sans(self) -> None:
        uni = unicoder.sans(unicoder.ital(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ))
        self.assertEqual(uni, ital_sans_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
    def test_450_numm_ital_sans(self) -> None:
        uni = unicoder.convert("fix", base_0123456789)
        self.assertEqual(uni, base_0123456789)
    def test_451_numm_ital_sans(self) -> None:
        uni = unicoder.convert("italsans", base_0123456789)
        self.assertEqual(uni, ital_sans_0123456789)
    def test_452_numm_ital_sans(self) -> None:
        uni = unicoder.convert("slantvect", base_0123456789)
        self.assertEqual(uni, ital_sans_0123456789)
    def test_455_numm_ital_sans(self) -> None:
        uni = unicoder.ital(unicoder.sans(base_0123456789))
        self.assertEqual(uni, ital_sans_0123456789)
    def test_456_numm_ital_sans(self) -> None:
        uni = unicoder.sans(unicoder.ital(base_0123456789))
        self.assertEqual(uni, ital_sans_0123456789)
    def test_459_numm_ital_sans(self) -> None:
        self.assertEqual(ital_sans_0123456789, sans_0123456789)
    def test_461_bold_ital_sans(self) -> None:
        uni = unicoder.convert("bolditalsans", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, bold_ital_sans_abcdefghijklmnopqrstuvwxyz)
    def test_462_bold_ital_sans(self) -> None:
        uni = unicoder.convert("fatslantvect", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, bold_ital_sans_abcdefghijklmnopqrstuvwxyz)
    def test_463_bold_ital_sans(self) -> None:
        uni = unicoder.convert("bolditalsans", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, bold_ital_sans_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
    def test_464_bold_ital_sans(self) -> None:
        uni = unicoder.convert("fatslantvect", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, bold_ital_sans_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
    def test_465_bold_ital_sans(self) -> None:
        uni = unicoder.bold(unicoder.ital(
            unicoder.sans(base_abcdefghijklmnopqrstuvwxyz)))
        self.assertEqual(uni, bold_ital_sans_abcdefghijklmnopqrstuvwxyz)
    def test_466_bold_ital_sans(self) -> None:
        uni = unicoder.sans(
            unicoder.bold(unicoder.ital(base_abcdefghijklmnopqrstuvwxyz)))
        self.assertEqual(uni, bold_ital_sans_abcdefghijklmnopqrstuvwxyz)
    def test_467_bold_ital_sans(self) -> None:
        uni = unicoder.bold(unicoder.ital(
            unicoder.sans(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)))
        self.assertEqual(uni, bold_ital_sans_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
    def test_468_bold_ital_sans(self) -> None:
        uni = unicoder.ital(unicoder.bold(
            unicoder.sans(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)))
        self.assertEqual(uni, bold_ital_sans_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
    def test_469_bold_ital_sans(self) -> None:
        uni = unicoder.sans(
            unicoder.bold(unicoder.ital(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)))
        self.assertEqual(uni, bold_ital_sans_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
    def test_470_numm_bold_ital_sans(self) -> None:
        uni = unicoder.convert("fix", base_0123456789)
        self.assertEqual(uni, base_0123456789)
    def test_471_numm_bold_ital_sans(self) -> None:
        uni = unicoder.convert("bolditalsans", base_0123456789)
        self.assertEqual(uni, bold_ital_sans_0123456789)
    def test_472_numm_bold_ital_sans(self) -> None:
        uni = unicoder.convert("fatslantvect", base_0123456789)
        self.assertEqual(uni, bold_ital_sans_0123456789)
    def test_475_numm_bold_ital_sans(self) -> None:
        uni = unicoder.bold(unicoder.ital(unicoder.sans(base_0123456789)))
        self.assertEqual(uni, bold_ital_sans_0123456789)
    def test_476_numm_bold_ital_sans(self) -> None:
        uni = unicoder.sans(unicoder.bold(unicoder.ital(base_0123456789)))
        self.assertEqual(uni, bold_ital_sans_0123456789)
    def test_479_numm_bold_ital_sans(self) -> None:
        self.assertEqual(bold_ital_sans_0123456789, bold_sans_0123456789)
    #
    def test_500_norm_frak(self) -> None:
        uni = unicoder.convert("fix", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, base_abcdefghijklmnopqrstuvwxyz)
    def test_501_norm_frak(self) -> None:
        uni = unicoder.convert("frak", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷")
    def test_502_norm_frak(self) -> None:
        uni = unicoder.convert("black", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷")
    def test_503_norm_frak(self) -> None:
        uni = unicoder.convert("frak", ":AB-DEFG--JKLMNOPQ-STUVWXY-")
        self.assertEqual(uni, ":𝔄𝔅-𝔇𝔈𝔉𝔊--𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔-𝔖𝔗𝔘𝔙𝔚𝔛𝔜-")
        uni = unicoder.convert("frak", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ")
    def test_504_norm_frak(self) -> None:
        uni = unicoder.convert("black", ":AB-DEFG--JKLMNOPQ-STUVWXY-")
        self.assertEqual(uni, ":𝔄𝔅-𝔇𝔈𝔉𝔊--𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔-𝔖𝔗𝔘𝔙𝔚𝔛𝔜-")
        uni = unicoder.convert("black", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ")
    def test_505_norm_frak(self) -> None:
        uni = unicoder.fraktur(base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷")
    def test_506_norm_frak(self) -> None:
        uni = unicoder.fraktur(base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷")
    def test_507_norm_frak(self) -> None:
        uni = unicoder.fraktur(":AB-DEFG--JKLMNOPQ-STUVWXY-")
        self.assertEqual(uni, ":𝔄𝔅-𝔇𝔈𝔉𝔊--𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔-𝔖𝔗𝔘𝔙𝔚𝔛𝔜-")
    def test_508_norm_frak(self) -> None:
        uni = unicoder.fraktur(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ")
    def test_510_bold_frak(self) -> None:
        uni = unicoder.convert("fix", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, base_abcdefghijklmnopqrstuvwxyz)
    def test_511_bold_frak(self) -> None:
        uni = unicoder.convert("boldfrak", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟")
    def test_512_bold_frak(self) -> None:
        uni = unicoder.convert("boldblack", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟")
    def test_513_bold_frak(self) -> None:
        uni = unicoder.convert("fatfrak", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅")
    def test_514_bold_frak(self) -> None:
        uni = unicoder.convert("boldblack", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅")
    def test_515_bold_frak(self) -> None:
        uni = unicoder.bold(unicoder.fraktur(base_abcdefghijklmnopqrstuvwxyz))
        self.assertEqual(uni, ":𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟")
    def test_516_bold_frak(self) -> None:
        uni = unicoder.bold(unicoder.fraktur(base_abcdefghijklmnopqrstuvwxyz))
        self.assertEqual(uni, ":𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟")
    def test_517_bold_frak(self) -> None:
        uni = unicoder.bold(unicoder.fraktur(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ))
        self.assertEqual(uni, ":𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅")
    def test_518_bold_frak(self) -> None:
        uni = unicoder.bold(unicoder.fraktur(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ))
        self.assertEqual(uni, ":𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅")
    #
    def test_600_norm_greek(self) -> None:
        uni = unicoder.convert("fix", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, base_abcdefghijklmnopqrstuvwxyz)
    def test_601_norm_greek(self) -> None:
        uni = unicoder.convert("greek", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":αβχδεφγηιικλμνοπκρστω∂ψξυζ")
    def test_602_norm_greek(self) -> None:
        uni = unicoder.convert("math", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":αβχδεφγηιικλμνοπκρστω∂ψξυζ")
    def test_603_norm_greek(self) -> None:
        uni = unicoder.convert("greek", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":ΑΒΧΔΕΦΓΗΙΙΚΛΜΝΟΠΚΡΣΤΩ∇ΨΞΥΖ")
    def test_604_norm_greek(self) -> None:
        uni = unicoder.convert("math", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":ΑΒΧΔΕΦΓΗΙΙΚΛΜΝΟΠΚΡΣΤΩ∇ΨΞΥΖ")
    def test_605_norm_greek(self) -> None:
        uni = unicoder.greek(base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":αβχδεφγηιικλμνοπκρστω∂ψξυζ")
    def test_606_norm_greek(self) -> None:
        uni = unicoder.greek(base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":αβχδεφγηιικλμνοπκρστω∂ψξυζ")
    def test_607_norm_greek(self) -> None:
        uni = unicoder.greek(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":ΑΒΧΔΕΦΓΗΙΙΚΛΜΝΟΠΚΡΣΤΩ∇ΨΞΥΖ")
    def test_608_norm_greek(self) -> None:
        uni = unicoder.greek(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":ΑΒΧΔΕΦΓΗΙΙΚΛΜΝΟΠΚΡΣΤΩ∇ΨΞΥΖ")
    def test_621_bold_greek(self) -> None:
        uni = unicoder.convert("boldgreek", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝛂𝛃𝛘𝛅𝛆𝛗𝛄𝛈𝛊𝛊𝛋𝛌𝛍𝛎𝛐𝛑𝛋𝛒𝛔𝛕𝛚𝛛𝛙𝛏𝛖𝛇")
    def test_622_bold_greek(self) -> None:
        uni = unicoder.convert("fatmath", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝛂𝛃𝛘𝛅𝛆𝛗𝛄𝛈𝛊𝛊𝛋𝛌𝛍𝛎𝛐𝛑𝛋𝛒𝛔𝛕𝛚𝛛𝛙𝛏𝛖𝛇")
    def test_623_bold_greek(self) -> None:
        uni = unicoder.convert("boldgreek", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝚨𝚩𝚾𝚫𝚬𝚽𝚪𝚮𝚰𝚰𝚱𝚲𝚳𝚴𝚶𝚷𝚱𝚸𝚺𝚻𝛀∇𝚿𝚵𝚼𝚭")
    def test_624_bold_greek(self) -> None:
        uni = unicoder.convert("fatmath", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝚨𝚩𝚾𝚫𝚬𝚽𝚪𝚮𝚰𝚰𝚱𝚲𝚳𝚴𝚶𝚷𝚱𝚸𝚺𝚻𝛀∇𝚿𝚵𝚼𝚭")
    def test_625_bold_greek(self) -> None:
        uni = unicoder.bold(unicoder.greek(base_abcdefghijklmnopqrstuvwxyz))
        self.assertEqual(uni, ":𝛂𝛃𝛘𝛅𝛆𝛗𝛄𝛈𝛊𝛊𝛋𝛌𝛍𝛎𝛐𝛑𝛋𝛒𝛔𝛕𝛚𝛛𝛙𝛏𝛖𝛇")
    def test_626_bold_greek(self) -> None:
        uni = unicoder.greek(unicoder.bold(base_abcdefghijklmnopqrstuvwxyz))
        self.assertEqual(uni, ":𝛂𝛃𝛘𝛅𝛆𝛗𝛄𝛈𝛊𝛊𝛋𝛌𝛍𝛎𝛐𝛑𝛋𝛒𝛔𝛕𝛚𝛛𝛙𝛏𝛖𝛇")
    def test_627_bold_greek(self) -> None:
        uni = unicoder.bold(unicoder.greek(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ))
        self.assertEqual(uni, ":𝚨𝚩𝚾𝚫𝚬𝚽𝚪𝚮𝚰𝚰𝚱𝚲𝚳𝚴𝚶𝚷𝚱𝚸𝚺𝚻𝛀∇𝚿𝚵𝚼𝚭")
    def test_628_bold_greek(self) -> None:
        uni = unicoder.greek(unicoder.bold(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ))
        self.assertEqual(uni, ":𝚨𝚩𝚾𝚫𝚬𝚽𝚪𝚮𝚰𝚰𝚱𝚲𝚳𝚴𝚶𝚷𝚱𝚸𝚺𝚻𝛀∇𝚿𝚵𝚼𝚭")
    def test_641_ital_greek(self) -> None:
        uni = unicoder.convert("italgreek", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝛼𝛽𝜒𝛿𝜀𝜑𝛾𝜂𝜄𝜄𝜅𝜆𝜇𝜈𝜊𝜋𝜅𝜌𝜎𝜏𝜔𝜕𝜓𝜉𝜐𝜁")
    def test_642_ital_greek(self) -> None:
        uni = unicoder.convert("slantmath", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝛼𝛽𝜒𝛿𝜀𝜑𝛾𝜂𝜄𝜄𝜅𝜆𝜇𝜈𝜊𝜋𝜅𝜌𝜎𝜏𝜔𝜕𝜓𝜉𝜐𝜁")
    def test_643_ital_greek(self) -> None:
        uni = unicoder.convert("italgreek", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝛢𝛣𝛸𝛥𝛦𝛷𝛤𝛨𝛪𝛪𝛫𝛬𝛭𝛮𝛰𝛱𝛫𝛲𝛴𝛵𝛺∇𝛹𝛯𝛶𝛧")
    def test_644_ital_greek(self) -> None:
        uni = unicoder.convert("slantmath", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝛢𝛣𝛸𝛥𝛦𝛷𝛤𝛨𝛪𝛪𝛫𝛬𝛭𝛮𝛰𝛱𝛫𝛲𝛴𝛵𝛺∇𝛹𝛯𝛶𝛧")
    def test_645_ital_greek(self) -> None:
        uni = unicoder.ital(unicoder.greek(base_abcdefghijklmnopqrstuvwxyz))
        self.assertEqual(uni, ":𝛼𝛽𝜒𝛿𝜀𝜑𝛾𝜂𝜄𝜄𝜅𝜆𝜇𝜈𝜊𝜋𝜅𝜌𝜎𝜏𝜔𝜕𝜓𝜉𝜐𝜁")
    def test_646_ital_greek(self) -> None:
        uni = unicoder.greek(unicoder.ital(base_abcdefghijklmnopqrstuvwxyz))
        self.assertEqual(uni, ":𝛼𝛽𝜒𝛿𝜀𝜑𝛾𝜂𝜄𝜄𝜅𝜆𝜇𝜈𝜊𝜋𝜅𝜌𝜎𝜏𝜔𝜕𝜓𝜉𝜐𝜁")
    def test_647_ital_greek(self) -> None:
        uni = unicoder.ital(unicoder.greek(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ))
        self.assertEqual(uni, ":𝛢𝛣𝛸𝛥𝛦𝛷𝛤𝛨𝛪𝛪𝛫𝛬𝛭𝛮𝛰𝛱𝛫𝛲𝛴𝛵𝛺∇𝛹𝛯𝛶𝛧")
    def test_648_ital_greek(self) -> None:
        uni = unicoder.greek(unicoder.ital(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ))
        self.assertEqual(uni, ":𝛢𝛣𝛸𝛥𝛦𝛷𝛤𝛨𝛪𝛪𝛫𝛬𝛭𝛮𝛰𝛱𝛫𝛲𝛴𝛵𝛺∇𝛹𝛯𝛶𝛧")
    def test_661_bold_ital_greek(self) -> None:
        uni = unicoder.convert("bolditalgreek", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝜶𝜷𝝌𝜹𝜺𝝋𝜸𝜼𝜾𝜾𝜿𝝀𝝁𝝂𝝄𝝅𝜿𝝆𝝈𝝉𝝎𝝏𝝍𝝃𝝊𝜻")
    def test_662_bold_ital_greek(self) -> None:
        uni = unicoder.convert("fatslantmath", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":𝜶𝜷𝝌𝜹𝜺𝝋𝜸𝜼𝜾𝜾𝜿𝝀𝝁𝝂𝝄𝝅𝜿𝝆𝝈𝝉𝝎𝝏𝝍𝝃𝝊𝜻")
    def test_663_bold_ital_greek(self) -> None:
        uni = unicoder.convert("bolditalgreek", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝜜𝜝𝜲𝜟𝜠𝜱𝜞𝜢𝜤𝜤𝜥𝜦𝜧𝜨𝜪𝜫𝜥𝜬𝜮𝜯𝜴∇𝜳𝜩𝜰𝜡")
    def test_664_bold_ital_greek(self) -> None:
        uni = unicoder.convert("fatslantmath", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":𝜜𝜝𝜲𝜟𝜠𝜱𝜞𝜢𝜤𝜤𝜥𝜦𝜧𝜨𝜪𝜫𝜥𝜬𝜮𝜯𝜴∇𝜳𝜩𝜰𝜡")
    def test_665_bold_ital_greek(self) -> None:
        uni = unicoder.bold(unicoder.ital(
            unicoder.greek(base_abcdefghijklmnopqrstuvwxyz)))
        self.assertEqual(uni, ":𝜶𝜷𝝌𝜹𝜺𝝋𝜸𝜼𝜾𝜾𝜿𝝀𝝁𝝂𝝄𝝅𝜿𝝆𝝈𝝉𝝎𝝏𝝍𝝃𝝊𝜻")
    def test_666_bold_ital_greek(self) -> None:
        uni = unicoder.greek(
            unicoder.bold(unicoder.ital(base_abcdefghijklmnopqrstuvwxyz)))
        self.assertEqual(uni, ":𝜶𝜷𝝌𝜹𝜺𝝋𝜸𝜼𝜾𝜾𝜿𝝀𝝁𝝂𝝄𝝅𝜿𝝆𝝈𝝉𝝎𝝏𝝍𝝃𝝊𝜻")
    def test_667_bold_ital_greek(self) -> None:
        uni = unicoder.bold(unicoder.ital(
            unicoder.greek(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)))
        self.assertEqual(uni, ":𝜜𝜝𝜲𝜟𝜠𝜱𝜞𝜢𝜤𝜤𝜥𝜦𝜧𝜨𝜪𝜫𝜥𝜬𝜮𝜯𝜴∇𝜳𝜩𝜰𝜡")
    def test_668_bold_ital_greek(self) -> None:
        uni = unicoder.ital(unicoder.bold(
            unicoder.greek(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)))
        self.assertEqual(uni, ":𝜜𝜝𝜲𝜟𝜠𝜱𝜞𝜢𝜤𝜤𝜥𝜦𝜧𝜨𝜪𝜫𝜥𝜬𝜮𝜯𝜴∇𝜳𝜩𝜰𝜡")
    def test_669_bold_ital_greek(self) -> None:
        uni = unicoder.greek(
            unicoder.bold(unicoder.ital(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)))
        self.assertEqual(uni, ":𝜜𝜝𝜲𝜟𝜠𝜱𝜞𝜢𝜤𝜤𝜥𝜦𝜧𝜨𝜪𝜫𝜥𝜬𝜮𝜯𝜴∇𝜳𝜩𝜰𝜡")
    #
    def test_700_norm_rune(self) -> None:
        uni = unicoder.convert("fix", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, base_abcdefghijklmnopqrstuvwxyz)
    def test_701_norm_rune(self) -> None:
        uni = unicoder.convert("rune", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":ᚨᛒᚳᛞᛖᚠᚷᚺᛁᛡᚳᛚᛗᚾᛟᛈᚳᚱᛋᛏᚹᚹᛕᚳᛋᛇᛉ")
    def test_702_norm_rune(self) -> None:
        uni = unicoder.convert("futark", base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":ᚨᛒᚳᛞᛖᚠᚷᚺᛁᛡᚳᛚᛗᚾᛟᛈᚳᚱᛋᛏᚹᚹᛕᚳᛋᛇᛉ")
    def test_703_norm_rune(self) -> None:
        uni = unicoder.convert("rune", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":ᚨᛒᚳᛞᛖᚠᚷᚺᛁᛡᚳᛚᛗᚾᛟᛈᚳᚱᛋᛏᚹᚹᛕᚳᛋᛇᛉ")
    def test_704_norm_rune(self) -> None:
        uni = unicoder.convert("futark", base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":ᚨᛒᚳᛞᛖᚠᚷᚺᛁᛡᚳᛚᛗᚾᛟᛈᚳᚱᛋᛏᚹᚹᛕᚳᛋᛇᛉ")
    def test_705_norm_rune(self) -> None:
        uni = unicoder.rune(base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":ᚨᛒᚳᛞᛖᚠᚷᚺᛁᛡᚳᛚᛗᚾᛟᛈᚳᚱᛋᛏᚹᚹᛕᚳᛋᛇᛉ")
    def test_706_norm_rune(self) -> None:
        uni = unicoder.rune(base_abcdefghijklmnopqrstuvwxyz)
        self.assertEqual(uni, ":ᚨᛒᚳᛞᛖᚠᚷᚺᛁᛡᚳᛚᛗᚾᛟᛈᚳᚱᛋᛏᚹᚹᛕᚳᛋᛇᛉ")
    def test_707_norm_rune(self) -> None:
        uni = unicoder.rune(base_ABCDEFGHIJKLMNOPQRSTUVWXYZ)
        self.assertEqual(uni, ":ᚨᛒᚳᛞᛖᚠᚷᚺᛁᛡᚳᛚᛗᚾᛟᛈᚳᚱᛋᛏᚹᚹᛕᚳᛋᛇᛉ")
    #
    def test_800_norm_value(self) -> None:
        txt = "15 km/h more"
        uni = unicoder.convert("fix", txt)
        self.assertEqual(uni, "15 km/h more")
        self.assertEqual(uni, txt)
    def test_801_thin_value(self) -> None:
        txt = "15 km/h more"
        uni = unicoder.convert("thin", txt)
        self.assertEqual(uni, "15 km/h more")
        self.assertNotEqual(uni, txt)
    def test_802_nobr_value(self) -> None:
        txt = "15 km/h more"
        uni = unicoder.convert("nobr", txt)
        self.assertEqual(uni, "15 km/h more")
        self.assertNotEqual(uni, txt)
        self.assertEqual(uni[2], ' ')
        self.assertEqual(uni[7], ' ')
        self.assertNotEqual(uni[2], uni[7])
    def test_803_thin_nobr_value(self) -> None:
        txt = "15 km/h more"
        thin = unicoder.convert("thin", txt)
        nobr = unicoder.convert("nobr", txt)
        self.assertEqual(thin, "15 km/h more")
        self.assertEqual(nobr, "15 km/h more")
        self.assertNotEqual(thin, nobr)
    def test_900_norm_1_8(self) -> None:
        txt = "15 1/8 km/h more"
        uni = unicoder.convert("fix", txt)
        self.assertEqual(uni, "15 1/8 km/h more")
        self.assertEqual(uni, txt)
    def test_901_norm_1_8(self) -> None:
        txt = "15 1/8 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15⅛ km/h more")
        self.assertNotEqual(uni, txt)
    def test_902_norm_2_8(self) -> None:
        txt = "15 2/8 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15¼ km/h more")
        self.assertNotEqual(uni, txt)
    def test_903_norm_3_8(self) -> None:
        txt = "15 3/8 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15⅜ km/h more")
        self.assertNotEqual(uni, txt)
    def test_904_norm_4_8(self) -> None:
        txt = "15 4/8 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15½ km/h more")
        self.assertNotEqual(uni, txt)
    def test_905_norm_5_8(self) -> None:
        txt = "15 5/8 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15⅝ km/h more")
        self.assertNotEqual(uni, txt)
    def test_906_norm_6_8(self) -> None:
        txt = "15 6/8 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15¾ km/h more")
        self.assertNotEqual(uni, txt)
    def test_907_norm_7_8(self) -> None:
        txt = "15 7/8 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15⅞ km/h more")
        self.assertNotEqual(uni, txt)
    def test_911_norm_1_4(self) -> None:
        txt = "15 1/4 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15¼ km/h more")
        self.assertNotEqual(uni, txt)
    def test_912_norm_2_4(self) -> None:
        txt = "15 2/4 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15½ km/h more")
        self.assertNotEqual(uni, txt)
    def test_913_norm_3_4(self) -> None:
        txt = "15 3/4 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15¾ km/h more")
        self.assertNotEqual(uni, txt)
    def test_914_norm_1_4(self) -> None:
        txt = "15 1/2 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15½ km/h more")
        self.assertNotEqual(uni, txt)
    def test_920_norm_0_6(self) -> None:
        txt = "15 0/6 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15↉ km/h more")
        self.assertNotEqual(uni, txt)
    def test_921_norm_1_6(self) -> None:
        txt = "15 1/6 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15⅙ km/h more")
        self.assertNotEqual(uni, txt)
    def test_922_norm_2_6(self) -> None:
        txt = "15 2/6 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15⅓ km/h more")
        self.assertNotEqual(uni, txt)
    def test_923_norm_3_6(self) -> None:
        txt = "15 3/6 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15½ km/h more")
        self.assertNotEqual(uni, txt)
    def test_924_norm_4_6(self) -> None:
        txt = "15 4/6 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15⅔ km/h more")
        self.assertNotEqual(uni, txt)
    def test_925_norm_5_6(self) -> None:
        txt = "15 5/6 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15⅚ km/h more")
        self.assertNotEqual(uni, txt)
    def test_930_norm_0_3(self) -> None:
        txt = "15 0/3 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15↉ km/h more")
        self.assertNotEqual(uni, txt)
    def test_931_norm_1_3(self) -> None:
        txt = "15 1/3 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15⅓ km/h more")
        self.assertNotEqual(uni, txt)
    def test_932_norm_2_3(self) -> None:
        txt = "15 2/3 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15⅔ km/h more")
        self.assertNotEqual(uni, txt)
    def test_941_norm_1_5(self) -> None:
        txt = "15 1/5 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15⅕ km/h more")
        self.assertNotEqual(uni, txt)
    def test_942_norm_2_5(self) -> None:
        txt = "15 2/5 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15⅖ km/h more")
        self.assertNotEqual(uni, txt)
    def test_943_norm_3_5(self) -> None:
        txt = "15 3/5 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15⅗ km/h more")
        self.assertNotEqual(uni, txt)
    def test_944_norm_4_5(self) -> None:
        txt = "15 4/5 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15⅘ km/h more")
        self.assertNotEqual(uni, txt)


if __name__ == "__main__":
    from optparse import OptionParser
    _o = OptionParser("%prog [options] test*",
                      epilog=__doc__.strip().split("\n")[0])
    _o.add_option("-v", "--verbose", action="count", default=0,
                  help="increase logging level [%default]")
    _o.add_option("--xmlresults", metavar="FILE", default=None,
                  help="capture results as a junit xml file [%default]")
    _o.add_option("-l", "--logfile", metavar="FILE", default="",
                  help="additionally save the output log to a file [%default]")
    opt, args = _o.parse_args()
    logging.basicConfig(level=logging.WARNING - opt.verbose * 5)
    #
    logfile = None
    if opt.logfile:
        if os.path.exists(opt.logfile):
            os.remove(opt.logfile)
        logfile = logging.FileHandler(opt.logfile)
        logfile.setFormatter(logging.Formatter("%(levelname)s:%(relativeCreated)d:%(message)s"))
        logging.getLogger().addHandler(logfile)
        logg.info("log diverted to %s", opt.logfile)
    xmlresults = None
    if opt.xmlresults:
        if os.path.exists(opt.xmlresults):
            os.remove(opt.xmlresults)
        xmlresults = open(opt.xmlresults, "w")
        logg.info("xml results into %s", opt.xmlresults)
    # unittest.main()
    suite = unittest.TestSuite()
    if not args: args = ["test_*"]
    for arg in args:
        for classname in sorted(globals()):
            if not classname.endswith("Test"):
                continue
            testclass = globals()[classname]
            for method in sorted(dir(testclass)):
                if "*" not in arg: arg += "*"
                if arg.startswith("_"): arg = arg[1:]
                if fnmatch(method, arg):
                    suite.addTest(testclass(method))
    # select runner
    if not logfile:
        if xmlresults:
            import xmlrunner  # type: ignore
            Runner = xmlrunner.XMLTestRunner
            result = Runner(xmlresults).run(suite)
        else:
            Runner = unittest.TextTestRunner
            result = Runner(verbosity=opt.verbose).run(suite)
    else:
        Runner = unittest.TextTestRunner
        if xmlresults:
            import xmlrunner
            Runner = xmlrunner.XMLTestRunner
        result = Runner(logfile.stream, verbosity=opt.verbose).run(suite)  # type: ignore
    if not result.wasSuccessful():
        sys.exit(1)
