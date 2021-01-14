Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> einstein = "Two thing are infinite: the universe and human stupidity"
>>> einstein.find("the")
24
>>> einstein = "Two things are infinite: the universe and human stupidity"
>>> einstein.find("the")
25
>>> einstein.find("muaaz")
-1
>>> einstein.find(":")
23
>>> einstein.find("t")
4
>>> einstein.find("23 :")
-1
>>> einstein.find("T")
0
>>> einstein[23 :]
': the universe and human stupidity'
>>> einstein.find("stupidity")
48
>>> einstein[48 :]
'stupidity'
>>> einstein[-10]
' '
>>> einstein[10]
' '
>>> "test".find('t')
0
>>> test[2:]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    test[2:]
NameError: name 'test' is not defined
>>> test = "test"
>>> test[2:]
'st'
>>> test.find('s')
2
>>> test.find
<built-in method find of str object at 0x000001A34325CE70>

(
>>> test.find(2)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    test.find(2)
TypeError: must be str, not int
>>> test.find('2')
-1
>>> test.find('t','e','s','t')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    test.find('t','e','s','t')
TypeError: find() takes at most 3 arguments (4 given)
>>> test.find('t')
0
>>> test = "Test"
>>> test.find(t)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    test.find(t)
NameError: name 't' is not defined
>>> test.find("t")
3
>>> test.find('te')
-1
>>> test.find('test')
-1
>>> "test".find('test')
0
>>> test.find('Test')
0
>>> 