#!/usr/bin/python
print('Content-type: text/html\n')


from random import random
r=random()
print('''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>SSUNKO Index</title>
  </head>''')
print('a random number for you:', r)