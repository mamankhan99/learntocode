Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> string = "iusedtoplaypubgmobile"
>>> string.find('i')
0
>>> string.find('i',1)
18
>>> string.find('',0)
0
>>> string.find('e',0)
3
>>> string.find('e',3)
3
>>> string.find('e',-5)
20
>>> string.find('i',-1100)
0
>>> string = "IusedToPlayPubgMobile"
>>> string
'IusedToPlayPubgMobile'
>>> str = "muaaz"
>>> str
'muaaz'
>>> string
'IusedToPlayPubgMobile'
>>> str = (str + 'kareem')
>>> str
'muaazkareem'
>>> str = (str + ' ' + 'kareem')
>>> str
'muaazkareem kareem'
>>> str = (str + ' kareem')
>>> str
'muaazkareem kareem kareem'
>>> str = (str + 'kareem')
>>> str
'muaazkareem kareem kareemkareem'
>>> str = (str+'kareem')
>>> str
'muaazkareem kareem kareemkareemkareem'
>>> str = (  str  + '   kareem    ')
>>> str
'muaazkareem kareem kareemkareemkareem   kareem    '
>>> string.find('IusedToPlayPubgMobile',5)
-1
>>> string.find('IusedToPlayPubgMobile',0)
0
>>> string.find('IusedToPlayPubgMobile')
0
>>> string.find('IusedToPlayPubgMobile':)
SyntaxError: invalid syntax
>>> s = 'muaaz'
>>> t = 'm'uaaz
SyntaxError: invalid syntax
>>> s = 'hello'
>>> t = 'muaaz'
>>> i = 4
>>> s[u:]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    s[u:]
NameError: name 'u' is not defined
>>> s[i:]
'o'
>>> t[m:]
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    t[m:]
NameError: name 'm' is not defined
>>> s[t:i]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    s[t:i]
TypeError: slice indices must be integers or None or have an __index__ method
>>> 