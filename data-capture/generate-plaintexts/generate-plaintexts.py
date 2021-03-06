#!/usr/bin/env python

import random

with open('./orig-plaintexts.txt', 'r') as f:
    plaintext_bytes = []
    for line in [l.strip() for l in f.readlines()]:
        plaintext_bytes.append([int(s, 16) for s in line.split(" ")])

size_of_line = len(plaintext_bytes[0])

# size_of_line = 16
# plaintext_bytes = []

char_codes = range(0,256)

extra_plaintexts_count = 300
for i in range(extra_plaintexts_count):
        plaintext_bytes.append([char_codes[random.randint(0,len(char_codes)-1)] for s in range(size_of_line)])

num_lines = len(plaintext_bytes)
assert size_of_line  == 16
assert num_lines > 0 and num_lines < 1000

data_str = '\n'.join([str(arr)[1:-1] for arr in plaintext_bytes])

with open('plaintexts.txt', 'w') as f:
    f.write(data_str)


