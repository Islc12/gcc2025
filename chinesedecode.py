#!/usr/bin/env python3

# The input string to decode
word = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽'

flag = ""

for i in range(0, len(word)):
    flag += chr(ord(word[i]) >> 8)
    flag += chr(ord(word[i]) - (ord(flag[len(flag)-1]) << 8))

print(flag)
