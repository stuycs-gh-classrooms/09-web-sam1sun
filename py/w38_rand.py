#!/usr/bin/python
print('Content-type: text/html\n')


from random import random
r=random()
print('''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>SSUNKO Index</title>
  </head>
  <body>
      <p>a random number for you:''', r,'''</p>
  </body>
</html>''')