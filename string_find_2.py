Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> motto = "we can do programming, yes i can, yes you can."
>>> motto.find('can')
3
>>> motto.find(',')
21
>>> motto.find('yes')
23
>>> motto.find('p')
10
>>> motto.find('yes',26)
34
>>> motto.find('yes',44)
-1
>>> 
KeyboardInterrupt
>>>  motto.find('we')
 
SyntaxError: unexpected indent
>>> motto.find('yes',44)
-1
>>>  motto.find('we')
 
SyntaxError: unexpected indent
>>> motto.find('we')
0
>>> motto.find('e',)
1
>>> motto.find('e',3)
24
>>> motto.find('e',2)
24
>>> motto.find('e',1)
1
>>> motto.find('e',44)
-1
>>> motto.find('e',100)
-1
>>> motto.find('.')
45
>>> s = 'muaaz'
>>> t = 'mu'
>>> i = '4'
>>> s[i:].find(t)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s[i:].find(t)
TypeError: slice indices must be integers or None or have an __index__ method
>>> s.find(t,i):
	
SyntaxError: invalid syntax
>>> i = 4
>>> s.find(t,i):
	
SyntaxError: invalid syntax
>>> s.find(t,i)
-1
>>> s.find(t\)
       
SyntaxError: unexpected character after line continuation character
>>> s.find(t)
0
>>> 