Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> basket={"orange","apple","mango","apple","orange"]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> basket={"orange","apple","mango","apple","orange"}
>>> type(basket)
<class 'set'>
>>> basket
{'mango', 'orange', 'apple'}
>>> a=set()
>>> a.add(1)
>>> b.add()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    b.add()
NameError: name 'b' is not defined
>>> a.add(2)
>>> a.add(2)
>>> a
{1, 2}
>>> a{}
SyntaxError: invalid syntax
>>> a{}
SyntaxError: invalid syntax
>>> a={}
>>> type(a)
<class 'dict'>
>>> a={'something'}
>>> type(a)
<class 'set'>
>>> basket[0]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    basket[0]
TypeError: 'set' object is not subscriptable
>>> numbers = [1,2,3,4,2,3,4]
>>> unique_numbers=set(numbers)
>>> unique_numbers
{1, 2, 3, 4}
>>> unique_numbers.add(5)
>>> unique_number
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    unique_number
NameError: name 'unique_number' is not defined
>>> unique_numbers
{1, 2, 3, 4, 5}
>>> fs=frozenset(numbers)
>>> fs
frozenset({1, 2, 3, 4})
>>> fs.add(5)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    fs.add(5)
AttributeError: 'frozenset' object has no attribute 'add'
>>> 
>>> 


>>> 

>>> 

>>> 