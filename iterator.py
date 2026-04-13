Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=["hey","you", "are","awesome"]
>>> cls
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    cls
NameError: name 'cls' is not defined
>>> a=["hey","bro","you","are","awesome"]
>>> for i in a:
	print(i)

	
hey
bro
you
are
awesome
>>> dir(a)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> itr=itr(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    itr=itr(a)
NameError: name 'itr' is not defined
>>> itr=iter(a)
>>> itr
<list_iterator object at 0x000001D8D192FD60>
>>> next(itr)
'hey'
>>> next(itr)
'bro'
>>> next(itr)
'you'
>>> next(itr)
'are'
>>> next(itr)
'awesome'
>>> next(itr)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    next(itr)
StopIteration
>>> dir(itr)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__length_hint__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__']
>>> list=[1,2,3,4,5]
>>> for element in list:
	print(element=2)

	
Traceback (most recent call last):
  File "<pyshell#20>", line 2, in <module>
    print(element=2)
TypeError: 'element' is an invalid keyword argument for print()
>>> list=['a','b','c','d','e']
>>> for element in list:
	print(element)

	
a
b
c
d
e
>>> tuple=(1,2,3,4)
>>> for element in tuple :
	print(element*element)

	
1
4
9
16
>>> for line in open("D:\\data\\funny2.txt")
SyntaxError: invalid syntax
>>> for line in open("D:\\data\\funny2.txt"):
	print(line)

	
Teacher: Why are you late,Frank?

Frank: Because of the sign.

Teacher : What sign?

Frank :The one that says "School Ahead, Go Slow".
>>> itr=reversed(a)
>>> next(itr)
'awesome'
>>> next(itr)
'are'
>>> next(itr)
'you'
>>> 
>>> next(itr)
'bro'
>>> next(itr)
'hey'
>>> next(itr)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    next(itr)
StopIteration
>>> dir(a)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> 