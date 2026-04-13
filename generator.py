Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def remote_control_next():
	yield "cnn"
	yield "espn"

	
>>> itr=remote_control_next()
>>> itr
<generator object remote_control_next at 0x00000298E3532B30>
>>> next(itr)
'cnn'
>>> next(itr)
'espn'
>>> next(itr)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    next(itr)
StopIteration
>>> for c in remote_control_next():
	print(c)

	
cnn
espn
>>> 