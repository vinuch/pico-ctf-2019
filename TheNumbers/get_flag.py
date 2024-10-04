#!/usr/bin/env python

import re


text = "16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14}"

result = re.split(r'[{}]', text)

result = [x for x in result if x]

letters1 = ''.join([chr(int(num) + 96) for num in result[0].split()])
letters2 = ''.join([chr(int(num) + 96) for num in result[1].split()])

print("%s{%s}" % (letters1, letters2))
