Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = ('Paramet')
>>> print(name)
Paramet
>>> type(name)
<class 'str'>
>>> name.lower()
'paramet'
>>> name.upper()
'PARAMET'
>>> friend = 'Maruay'
>>> print('สวัสดีมารวยสบายดีไหมง)
...       
SyntaxError: incomplete input
>>> print('สวัสดีมารวยสบายดีไหม')
...       
สวัสดีมารวยสบายดีไหม
>>> print('สวัสดี'+friend+'สบายดีไหม')
...       
สวัสดีMaruayสบายดีไหม
>>> money = 100
...       
>>> print(friend + 'ยืมเงิน' + money)
...       
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(friend + 'ยืมเงิน' + money)
TypeError: can only concatenate str (not "int") to str
>>> type(money)
...       
<class 'int'>
>>> print('{} ยืมเงิน {} บาท'.format(friend,money))
...       
Maruay ยืมเงิน 100 บาท
>>> print(f'{friend} ยืมเงิน {money} บาท')
...       
Maruay ยืมเงิน 100 บาท
