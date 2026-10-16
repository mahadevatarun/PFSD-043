Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #int
>>> int(9)
9
>>> int(7.8)
7
>>> # the reson for only 7 is the point will not be convert
>>> int("hi)
...     
SyntaxError: unterminated string literal (detected at line 1)
>>> # it is str it cant to be convert
...     
>>> int(6+8j)
...     
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int(6+8j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> # it is complex it cant to be convert
...     
>>> float(5)
...     
5.0
# it is int so it convert in to float by add a .0
    
float(9.0)
    
9.0
# it is float
    
float("hi)
      
SyntaxError: unterminated string literal (detected at line 1)
# it is str it will not converted
      
float(6+9j)
      
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    float(6+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
#it is complex so it will not converted
      
float("HI")
      
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    float("HI")
ValueError: could not convert string to float: 'HI'

#
      
str(9)
      
'9'
# in str int is converted into str by number""
      
str(9.0)
      
'9.0'
#in str float is converted into str by symbol""
      
str("hi")
      
'hi'
# it str so it will convert into str
      
str("7+8j")
      
'7+8j'
"it is complex so it converted into str"
      
'it is complex so it converted into str'



complex(4)
      
(4+0j)
complex(5.0)
      
(5+0j)
complex("hi")
      
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    complex("hi")
ValueError: complex() arg is a malformed string
complex(5+7J)
      
(5+7j)
int(ture)
      
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    int(ture)
NameError: name 'ture' is not defined. Did you mean: 'tuple'?
int(True)
      
1
int(false)
      
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    int(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
int(Flase)
      
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    int(Flase)
NameError: name 'Flase' is not defined. Did you mean: 'False'?
int(False)
      
0
float(True)
      
1.0
float(Flase)
      
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    float(Flase)
NameError: name 'Flase' is not defined. Did you mean: 'False'?
float(False)
      
0.0
str(True)
      
'True'
str(False)
      
'False'
complex(True)
      
(1+0j)
complex(Fasle)
      
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    complex(Fasle)
NameError: name 'Fasle' is not defined. Did you mean: 'False'?
complex(False)
      
0j
