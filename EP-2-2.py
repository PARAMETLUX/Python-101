Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from datetime
SyntaxError: incomplete input
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2023, 2, 12, 15, 15, 16, 464299)
>>> datetime.now().strftime('%Y%m%d %H:%M:%S)
...                         
SyntaxError: incomplete input
>>> datetime.now().strftime('%Y%m%d %H:%M:%S')
...                         
'20230212 15:16:55'
>>> import random
>>> random.randint(1,7)
6
