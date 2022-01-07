
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

This script helps to bold or slanted text to various social media platforms.
The nobr thin fract parts are particularly useful for Wikipedia.

### RESULT

Just for amusement, this is the result when running the commands shown above. 
Note that the bold and italic text snippets do not rely on \<i\> \<b\> \<font\> hints
or some similar style markup, instead they use unicode codepoints from the 
math extensions. Likewise fraktur and greek and double stroke characters are used 
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
