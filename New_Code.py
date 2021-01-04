Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = "muaaz"
>>> name
'muaaz'
>>> name[]1
SyntaxError: invalid syntax
>>> name[1]
'u'
>>> name[-1]
'z'
>>> name[0]
'm'
>>> name[1*2]
'a'
>>> name[1*(-1)]
'z'
>>> name[-1 + 1]
'm'
>>> s = 'muaaz'
>>> a
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> s
'muaaz'
>>> 
>>> 
>>> 


>>> (s + 'ity')[1]
'u'
>>> word = "assume"
>>> word
'assume'
>>> word[3]
'u'
>>> word[4:6]
'me'
>>> word[1:3]
'ss'
>>> word[2:5]
'sum'
>>> word[:]
'assume'
>>> word[;]
SyntaxError: invalid syntax
>>> word[4:]
'me'
>>> word[4:10]
'me'
>>> word[4:(-10)]
''
>>> word[1;]
SyntaxError: invalid syntax
>>> word[1:]
'ssume'
>>> word[0:]
'assume'
>>> word[0:0]
''
>>> s = "audacity"
>>> s
'audacity'
>>> s[0:]
'audacity'
>>> s[1:7]
'udacit'
>>> print("U" + s[2:7])
Udacit
>>> print("U" + s[2:8])
Udacity
>>> s
'audacity'
>>> s[:]
'audacity'
>>> s+s[0:-1+1]
'audacity'
>>> s[0:]
'audacity'
>>> s[:-1]
'audacit'
>>> s[-1]
'y'
>>> s[:3] + s[3:]
'audacity'
>>> s='a'
>>> s
'a'
>>> s[:3] + s[3:]
'a'
>>> [-1]
[-1]
>>> s[-1]
'a'
>>> 