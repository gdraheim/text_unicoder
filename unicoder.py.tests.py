#! /usr/bin/python3
""" testing the unicoder.py functions """

import sys
import unittest
import logging
from fnmatch import fnmatchcase as fnmatch

try:
    from . import unicoder
except:
    import unicoder

logg = logging.getLogger("TEST")



class UnicoderTest(unittest.TestCase):
    def test_001_opt_scan(self):
        opt = unicoder.scan(["-v"])
        self.assertEqual(opt.verbose, 1)
    def test_002_opt_scan(self):
        opt = unicoder.scan(["-vv"])
        self.assertEqual(opt.verbose, 2)
    def test_003_opt_scan(self):
        opt = unicoder.scan(["-v", "-vv"])
        self.assertEqual(opt.verbose, 3)
    def test_110_bold_base(self):
        uni = unicoder.convert("fix", "abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(uni, "abcdefghijklmnopqrstuvwxyz")
    def test_111_bold_base(self):
        uni = unicoder.convert("fat", "abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(uni, "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳")
    def test_112_bold_base(self):
        uni = unicoder.convert("bold", "abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(uni, "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳")
    def test_113_bold_base(self):
        uni = unicoder.convert("fat", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(uni, "𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙")
    def test_114_bold_base(self):
        uni = unicoder.convert("bold", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(uni, "𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙")
    def test_115_bold_base(self):
        uni = unicoder.bold("abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(uni, "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳")
    def test_116_bold_base(self):
        uni = unicoder.bold("abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(uni, "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳")
    def test_117_bold_base(self):
        uni = unicoder.bold("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(uni, "𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙")
    def test_118_bold_base(self):
        uni = unicoder.bold("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(uni, "𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙")
    def test_120_ital_base(self):
        uni = unicoder.convert("fix", "abcdefg-ijklmnopqrstuvwxyz")
        self.assertEqual(uni, "abcdefg-ijklmnopqrstuvwxyz")
    def test_121_ital_base(self):
        uni = unicoder.convert("slant", "abcdefg-ijklmnopqrstuvwxyz")
        self.assertEqual(uni, "𝑎𝑏𝑐𝑑𝑒𝑓𝑔-𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧")
    def test_122_ital_base(self):
        uni = unicoder.convert("ital", "abcdefg-ijklmnopqrstuvwxyz")
        self.assertEqual(uni, "𝑎𝑏𝑐𝑑𝑒𝑓𝑔-𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧")
    def test_123_ital_base(self):
        uni = unicoder.convert("slant", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(uni, "𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍")
    def test_124_ital_base(self):
        uni = unicoder.convert("ital", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(uni, "𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍")
    def test_125_ital_base(self):
        uni = unicoder.ital("abcdefg-ijklmnopqrstuvwxyz")
        self.assertEqual(uni, "𝑎𝑏𝑐𝑑𝑒𝑓𝑔-𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧")
    def test_126_ital_base(self):
        uni = unicoder.ital("abcdefg-ijklmnopqrstuvwxyz")
        self.assertEqual(uni, "𝑎𝑏𝑐𝑑𝑒𝑓𝑔-𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧")
    def test_127_ital_base(self):
        uni = unicoder.ital("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(uni, "𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍")
    def test_128_ital_base(self):
        uni = unicoder.ital("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(uni, "𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍")
    def test_130_bold_ital_base(self):
        uni = unicoder.convert("fix", "abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(uni, "abcdefghijklmnopqrstuvwxyz")
    def test_131_ital_bold_base(self):
        uni = unicoder.convert("fatslant", "abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(uni, "𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛")
    def test_132_ital_bold_base(self):
        uni = unicoder.convert("italbold", "abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(uni, "𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛")
    def test_133_ital_bold_base(self):
        uni = unicoder.convert("fatslant", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(uni, "𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁")
    def test_134_ital_bold_base(self):
        uni = unicoder.convert("italbold", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(uni, "𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁")
    def test_136_ital_bold_base(self):
        uni = unicoder.ital(unicoder.bold("abcdefghijklmnopqrstuvwxyz"))
        self.assertEqual(uni, "𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛")
    def test_137_ital_bold_base(self):
        uni = unicoder.ital(unicoder.bold("abcdefghijklmnopqrstuvwxyz"))
        self.assertEqual(uni, "𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛")
    def test_138_ital_bold_base(self):
        uni = unicoder.ital(unicoder.bold("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        self.assertEqual(uni, "𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁")
    def test_139_ital_bold_base(self):
        uni = unicoder.ital(unicoder.bold("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        self.assertEqual(uni, "𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁")
    def test_140_bold_ital_base(self):
        uni = unicoder.bold(unicoder.ital("abcdefghijklmnopqrstuvwxyz"))
        self.assertEqual(uni, "𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛")
    def test_141_bold_ital_base(self):
        uni = unicoder.bold(unicoder.ital("abcdefghijklmnopqrstuvwxyz"))
        self.assertEqual(uni, "𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛")
    def test_142_bold_ital_base(self):
        uni = unicoder.bold(unicoder.ital("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        self.assertEqual(uni, "𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁")
    def test_143_bold_ital_base(self):
        uni = unicoder.bold(unicoder.ital("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        self.assertEqual(uni, "𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁")
    def test_150_bold_numm(self):
        uni = unicoder.convert("fix", "0123456789")
        self.assertEqual(uni, "0123456789")
    def test_151_bold_numm(self):
        uni = unicoder.convert("fat", "0123456789")
        self.assertEqual(uni, "𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗")
    def test_152_bold_numm(self):
        uni = unicoder.convert("bold", "0123456789")
        self.assertEqual(uni, "𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗")
    def test_155_bold_numm(self):
        uni = unicoder.bold("0123456789")
        self.assertEqual(uni, "𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗")
    def test_156_bold_numm(self):
        uni = unicoder.bold("0123456789")
        self.assertEqual(uni, "𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗")
    def test_160_ital_numm(self):
        uni = unicoder.convert("fix", "0123456789")
        self.assertEqual(uni, "0123456789")
    def test_161_ital_numm(self):
        uni = unicoder.convert("slant", "0123456789")
        self.assertEqual(uni, "0123456789")
    def test_162_ital_numm(self):
        uni = unicoder.convert("ital", "0123456789")
        self.assertEqual(uni, "0123456789")
    def test_170_bold_base_sz(self):
        uni = unicoder.convert("fix", "abcxyzABCXYZ0123456789ß")
        self.assertEqual(uni, "abcxyzABCXYZ0123456789ß")
    def test_171_bold_base_sz(self):
        uni = unicoder.convert("fat", "abcxyzABCXYZ0123456789ß")
        self.assertEqual(uni, "𝐚𝐛𝐜𝐱𝐲𝐳𝐀𝐁𝐂𝐗𝐘𝐙𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𝛃")
    def test_172_bold_base_sz(self):
        uni = unicoder.convert("bold", "abcxyzABCXYZ0123456789ß")
        self.assertEqual(uni, "𝐚𝐛𝐜𝐱𝐲𝐳𝐀𝐁𝐂𝐗𝐘𝐙𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𝛃")
    def test_180_ital_base_sz(self):
        uni = unicoder.convert("fix", "abcxyzABCXYZ0123456789ß")
        self.assertEqual(uni, "abcxyzABCXYZ0123456789ß")
    def test_181_ital_base_sz(self):
        uni = unicoder.convert("slant", "abcxyzABCXYZ0123456789ß")
        self.assertEqual(uni, "𝑎𝑏𝑐𝑥𝑦𝑧𝐴𝐵𝐶𝑋𝑌𝑍0123456789𝛽")
    def test_182_ital_base_sz(self):
        uni = unicoder.convert("ital", "abcxyzABCXYZ0123456789ß")
        self.assertEqual(uni, "𝑎𝑏𝑐𝑥𝑦𝑧𝐴𝐵𝐶𝑋𝑌𝑍0123456789𝛽")
    def test_190_bold_ital_base_sz(self):
        uni = unicoder.convert("fix", "abcxyzABCXYZ0123456789ß")
        self.assertEqual(uni, "abcxyzABCXYZ0123456789ß")
    def test_191_bold_ital_base_sz(self):
        uni = unicoder.convert("fatslant", "abcxyzABCXYZ0123456789ß")
        self.assertEqual(uni, "𝒂𝒃𝒄𝒙𝒚𝒛𝑨𝑩𝑪𝑿𝒀𝒁𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𝜷")
    def test_192_bold_ital_base_sz(self):
        uni = unicoder.convert("italbold", "abcxyzABCXYZ0123456789ß")
        self.assertEqual(uni, "𝒂𝒃𝒄𝒙𝒚𝒛𝑨𝑩𝑪𝑿𝒀𝒁𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𝜷")
    #
    def test_200_norm_double(self):
        uni = unicoder.convert("fix", "abcxyzABCXYZ")
        self.assertEqual(uni, "abcxyzABCXYZ")
    def test_201_norm_double(self):
        uni = unicoder.convert("double", "abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(uni, "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫")
    def test_202_norm_double(self):
        uni = unicoder.convert("wide", "abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(uni, "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫")
    def test_203_norm_double(self):
        uni = unicoder.convert("double", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(uni, "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ")
    def test_204_norm_double(self):
        uni = unicoder.convert("wide", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(uni, "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ")
    def test_205_norm_double(self):
        uni = unicoder.double("abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(uni, "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫")
    def test_206_norm_double(self):
        uni = unicoder.double("abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(uni, "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫")
    def test_207_norm_double(self):
        uni = unicoder.double("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(uni, "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ")
    def test_208_norm_double(self):
        uni = unicoder.double("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(uni, "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ")
    def test_210_bold_double(self):
        uni = unicoder.convert("fix", "abcxyzABXY")
        self.assertEqual(uni, "abcxyzABXY")
    def test_211_bold_double(self):
        uni = unicoder.convert("fatdouble", "abcxyzABXY")
        self.assertEqual(uni, "𝕒𝕓𝕔𝕩𝕪𝕫𝔸𝔹𝕏𝕐")
    def test_212_bold_double(self):
        uni = unicoder.convert("boldwide", "abcxyzABXY")
        self.assertEqual(uni, "𝕒𝕓𝕔𝕩𝕪𝕫𝔸𝔹𝕏𝕐")
    def test_215_bold_double(self):
        uni = unicoder.bold(unicoder.double("abcxyzABXY"))
        self.assertEqual(uni, "𝕒𝕓𝕔𝕩𝕪𝕫𝔸𝔹𝕏𝕐")
    def test_216_bold_double(self):
        uni = unicoder.bold(unicoder.double("abcxyzABXY"))
        self.assertEqual(uni, "𝕒𝕓𝕔𝕩𝕪𝕫𝔸𝔹𝕏𝕐")
    def test_240_numm_double(self):
        uni = unicoder.convert("fix", "0123456789")
        self.assertEqual(uni, "0123456789")
    def test_241_numm_double(self):
        uni = unicoder.convert("double", "0123456789")
        self.assertEqual(uni, "𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡")
    def test_242_numm_double(self):
        uni = unicoder.convert("wide", "0123456789")
        self.assertEqual(uni, "𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡")
    def test_245_numm_double(self):
        uni = unicoder.double("0123456789")
        self.assertEqual(uni, "𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡")
    def test_246_numm_double(self):
        uni = unicoder.double("0123456789")
        self.assertEqual(uni, "𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡")
    #
    def test_300_norm_courier(self):
        uni = unicoder.convert("fix", "abcxyzABCXYZ")
        self.assertEqual(uni, "abcxyzABCXYZ")
    def test_301_norm_courier(self):
        uni = unicoder.convert("courier", "abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(uni, "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣")
    def test_302_norm_courier(self):
        uni = unicoder.convert("mono", "abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(uni, "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣")
    def test_303_norm_courier(self):
        uni = unicoder.convert("courier", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(uni, "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉")
    def test_304_norm_courier(self):
        uni = unicoder.convert("mono", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(uni, "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉")
    def test_305_norm_courier(self):
        uni = unicoder.courier("abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(uni, "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣")
    def test_306_norm_courier(self):
        uni = unicoder.courier("abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(uni, "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣")
    def test_307_norm_courier(self):
        uni = unicoder.courier("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(uni, "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉")
    def test_308_norm_courier(self):
        uni = unicoder.courier("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(uni, "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉")
    def test_340_numm_courier(self):
        uni = unicoder.convert("fix", "0123456789")
        self.assertEqual(uni, "0123456789")
    def test_341_numm_courier(self):
        uni = unicoder.convert("courier", "0123456789")
        self.assertEqual(uni, "𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿")
    def test_342_numm_courier(self):
        uni = unicoder.convert("mono", "0123456789")
        self.assertEqual(uni, "𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿")
    def test_345_numm_courier(self):
        uni = unicoder.courier("0123456789")
        self.assertEqual(uni, "𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿")
    def test_346_numm_courier(self):
        uni = unicoder.courier("0123456789")
        self.assertEqual(uni, "𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿")
    #
    def test_500_norm_frak(self):
        uni = unicoder.convert("fix", "abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(uni, "abcdefghijklmnopqrstuvwxyz")
    def test_501_norm_frak(self):
        uni = unicoder.convert("frak", "abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(uni, "𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷")
    def test_502_norm_frak(self):
        uni = unicoder.convert("black", "abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(uni, "𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷")
    def test_503_norm_frak(self):
        uni = unicoder.convert("frak", "AB-DEFG--JKLMNOPQ-STUVWXY-")
        self.assertEqual(uni, "𝔄𝔅-𝔇𝔈𝔉𝔊--𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔-𝔖𝔗𝔘𝔙𝔚𝔛𝔜-")
    def test_504_norm_frak(self):
        uni = unicoder.convert("black", "AB-DEFG--JKLMNOPQ-STUVWXY-")
        self.assertEqual(uni, "𝔄𝔅-𝔇𝔈𝔉𝔊--𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔-𝔖𝔗𝔘𝔙𝔚𝔛𝔜-")
    def test_505_norm_frak(self):
        uni = unicoder.fraktur("abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(uni, "𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷")
    def test_506_norm_frak(self):
        uni = unicoder.fraktur("abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(uni, "𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷")
    def test_507_norm_frak(self):
        uni = unicoder.fraktur("AB-DEFG--JKLMNOPQ-STUVWXY-")
        self.assertEqual(uni, "𝔄𝔅-𝔇𝔈𝔉𝔊--𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔-𝔖𝔗𝔘𝔙𝔚𝔛𝔜-")
    def test_508_norm_frak(self):
        uni = unicoder.fraktur("AB-DEFG--JKLMNOPQ-STUVWXY-")
        self.assertEqual(uni, "𝔄𝔅-𝔇𝔈𝔉𝔊--𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔-𝔖𝔗𝔘𝔙𝔚𝔛𝔜-")
    def test_510_bold_frak(self):
        uni = unicoder.convert("fix", "abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(uni, "abcdefghijklmnopqrstuvwxyz")
    def test_511_bold_frak(self):
        uni = unicoder.convert("boldfrak", "abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(uni, "𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟")
    def test_512_bold_frak(self):
        uni = unicoder.convert("boldblack", "abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(uni, "𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟")
    def test_513_bold_frak(self):
        uni = unicoder.convert("fatfrak", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(uni, "𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅")
    def test_514_bold_frak(self):
        uni = unicoder.convert("boldblack", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(uni, "𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅")
    def test_515_bold_frak(self):
        uni = unicoder.bold(unicoder.fraktur("abcdefghijklmnopqrstuvwxyz"))
        self.assertEqual(uni, "𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟")
    def test_516_bold_frak(self):
        uni = unicoder.bold(unicoder.fraktur("abcdefghijklmnopqrstuvwxyz"))
        self.assertEqual(uni, "𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟")
    def test_517_bold_frak(self):
        uni = unicoder.bold(unicoder.fraktur("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        self.assertEqual(uni, "𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅")
    def test_518_bold_frak(self):
        uni = unicoder.bold(unicoder.fraktur("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        self.assertEqual(uni, "𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅")

    def test_800_norm_value(self):
        txt = "15 km/h more"
        uni = unicoder.convert("fix", txt)
        self.assertEqual(uni, "15 km/h more")
        self.assertEqual(uni, txt)
    def test_801_thin_value(self):
        txt = "15 km/h more"
        uni = unicoder.convert("thin", txt)
        self.assertEqual(uni, "15 km/h more")
        self.assertNotEqual(uni, txt)
    def test_802_nobr_value(self):
        txt = "15 km/h more"
        uni = unicoder.convert("nobr", txt)
        self.assertEqual(uni, "15 km/h more")
        self.assertNotEqual(uni, txt)
        self.assertEqual(uni[2], ' ')
        self.assertEqual(uni[7], ' ')
        self.assertNotEqual(uni[2], uni[7])
    def test_803_thin_nobr_value(self):
        txt = "15 km/h more"
        thin = unicoder.convert("thin", txt)
        nobr = unicoder.convert("nobr", txt)
        self.assertEqual(thin, "15 km/h more")
        self.assertEqual(nobr, "15 km/h more")
        self.assertNotEqual(thin, nobr)
    def test_900_norm_1_8(self):
        txt = "15 1/8 km/h more"
        uni = unicoder.convert("fix", txt)
        self.assertEqual(uni, "15 1/8 km/h more")
        self.assertEqual(uni, txt)
    def test_901_norm_1_8(self):
        txt = "15 1/8 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15⅛ km/h more")
        self.assertNotEqual(uni, txt)
    def test_902_norm_2_8(self):
        txt = "15 2/8 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15¼ km/h more")
        self.assertNotEqual(uni, txt)
    def test_903_norm_3_8(self):
        txt = "15 3/8 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15⅜ km/h more")
        self.assertNotEqual(uni, txt)
    def test_904_norm_4_8(self):
        txt = "15 4/8 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15½ km/h more")
        self.assertNotEqual(uni, txt)
    def test_905_norm_5_8(self):
        txt = "15 5/8 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15⅝ km/h more")
        self.assertNotEqual(uni, txt)
    def test_906_norm_6_8(self):
        txt = "15 6/8 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15¾ km/h more")
        self.assertNotEqual(uni, txt)
    def test_907_norm_7_8(self):
        txt = "15 7/8 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15⅞ km/h more")
        self.assertNotEqual(uni, txt)
    def test_911_norm_1_4(self):
        txt = "15 1/4 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15¼ km/h more")
        self.assertNotEqual(uni, txt)
    def test_912_norm_2_4(self):
        txt = "15 2/4 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15½ km/h more")
        self.assertNotEqual(uni, txt)
    def test_913_norm_3_4(self):
        txt = "15 3/4 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15¾ km/h more")
        self.assertNotEqual(uni, txt)
    def test_914_norm_1_4(self):
        txt = "15 1/2 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15½ km/h more")
        self.assertNotEqual(uni, txt)
    def test_920_norm_0_6(self):
        txt = "15 0/6 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15↉ km/h more")
        self.assertNotEqual(uni, txt)
    def test_921_norm_1_6(self):
        txt = "15 1/6 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15⅙ km/h more")
        self.assertNotEqual(uni, txt)
    def test_922_norm_2_6(self):
        txt = "15 2/6 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15⅓ km/h more")
        self.assertNotEqual(uni, txt)
    def test_923_norm_3_6(self):
        txt = "15 3/6 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15½ km/h more")
        self.assertNotEqual(uni, txt)
    def test_924_norm_4_6(self):
        txt = "15 4/6 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15⅔ km/h more")
        self.assertNotEqual(uni, txt)
    def test_925_norm_5_6(self):
        txt = "15 5/6 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15⅚ km/h more")
        self.assertNotEqual(uni, txt)
    def test_930_norm_0_3(self):
        txt = "15 0/3 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15↉ km/h more")
        self.assertNotEqual(uni, txt)
    def test_931_norm_1_3(self):
        txt = "15 1/3 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15⅓ km/h more")
        self.assertNotEqual(uni, txt)
    def test_932_norm_2_3(self):
        txt = "15 2/3 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15⅔ km/h more")
        self.assertNotEqual(uni, txt)
    def test_941_norm_1_5(self):
        txt = "15 1/5 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15⅕ km/h more")
        self.assertNotEqual(uni, txt)
    def test_942_norm_2_5(self):
        txt = "15 2/5 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15⅖ km/h more")
        self.assertNotEqual(uni, txt)
    def test_943_norm_3_5(self):
        txt = "15 3/5 km/h more"
        uni = unicoder.convert("fract", txt)
        self.assertEqual(uni, "15⅗ km/h more")
        self.assertNotEqual(uni, txt)
    def test_944_norm_4_5(self):
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
