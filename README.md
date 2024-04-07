[![Style Check](https://github.com/gdraheim/text-unicoder/actions/workflows/stylecheck.yml/badge.svg?event=push)](https://github.com/gdraheim/text-unicoder/actions/workflows/stylecheck.yml)
[![Type Check](https://github.com/gdraheim/text-unicoder/actions/workflows/typecheck.yml/badge.svg?event=push)](https://github.com/gdraheim/text-unicoder/actions/workflows/typecheck.yml)
[![Unit Tests](https://github.com/gdraheim/text-unicoder/actions/workflows/unittests.yml/badge.svg?event=push)](https://github.com/gdraheim/text-unicoder/actions/workflows/unittests.yml)
[![Code Coverage](https://img.shields.io/badge/311%20test-100%25%20coverage-brightgreen)](https://github.com/gdraheim/text-unicoder/blob/master/unicoder.py.tests.py)
[![PyPI version](https://badge.fury.io/py/text-unicoder.svg)](https://pypi.org/project/text-unicoder/)

This script allows to convert ascii to unicode specials 
including bold italic greek fraktur script.


Examples:

    unicoder.py bold foobar
    unicoder.py ital foobar
    unicoder.py boldital foobar
    unicoder.py double foobar
    unicoder.py mono foobar
    unicoder.py sans foobar
    unicoder.py greek foobar
    unicoder.py greek FOOBAR
    unicoder.py fraktur foobar
    unicoder.py boldfraktur foobar
    unicoder.py fract 15 1/4
    unicoder.py 15 1/4 km/h
    unicoder.py value 15 1/4 km/h
    unicoder.py thin 15 1/4 km/h
    unicoder.py nobr 15 1/4 km/h
    unicoder.py power 15^3
    unicoder.py index x_1
    unicoder.py math X_1^3 +1/4
    unicoder.py back answer
    unicoder.py down answer
    unicoder.py flip answer

This script helps to bold or slanted text to various social media platforms.
The nobr thin fract parts are particularly useful for Wikipedia.
The flip text (or turn text) allows to provide a pun on a question.

### RESULT

Just for amusement, this is the result when running the commands shown above. 
Note that the bold and italic text snippets do not rely on \<i\> \<b\> \<font\> hints
or some similar style markup, instead they use different codepoints from the 
[Mathematical Alphanumeric Symbols](https://en.wikipedia.org/wiki/Mathematical_Alphanumeric_Symbols)
unicode blocks. Likewise fraktur and greek and double stroke characters are used 
often in the field of mathematics. The sans and mono are rarely used however.

    𝐟𝐨𝐨𝐛𝐚𝐫
    𝑓𝑜𝑜𝑏𝑎𝑟
    𝒇𝒐𝒐𝒃𝒂𝒓
    𝕗𝕠𝕠𝕓𝕒𝕣
    𝚏𝚘𝚘𝚋𝚊𝚛
    foobar
    φωβαρ
    ΦΩΒΑΡ
    𝔣𝔬𝔬𝔟𝔞𝔯
    𝖋𝖔𝖔𝖇𝖆𝖗
    15¼
    15¼ km/h
    15¼ km/h
    15 1/4 km/h
    15 1/4 km/h
    15³
    x₁
    Ξ₁³ +¼
    rewsna
    ɐusʍǝɹ
    ɹǝʍsuɐ

### TESTSUITE

Yes, there is a testsuite with more than a hundred unittests for the functions.
The module can also be imported as helper to other scripts.

For developers, please run "make tests" for the testsuite. Please do also
run "make type" for mypy typehints checks and "make pep" for pep8 style checks.



