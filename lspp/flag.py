# -*- coding: UTF-8 -*-
#!/usr/bin/python3
# This is flag judge module

import os

def judge_flag(flag):
    with open('flag', 'r') as file:
        text = file.readlines()
    text = [line.strip("\n") for line in text]
    #print(text)
    for i in range(len(text)):
        if flag == text[i]:
            return True
    return False

if __name__ == '__main__':
    #if judge_flag('first') == True:
    #    print('yes')
    #elif judge_flag('first') == False:
    #    print('no')
    
    print('ok')
