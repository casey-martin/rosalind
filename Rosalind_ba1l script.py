# -*- coding: utf-8 -*-
"""
Created on Tue May 03 11:26:12 2016

@author: martincg
"""

def patternToNumber(dna):
    crumb = dict(zip('ACGT', '0123'))
    return int("".join(crumb[i] for i in dna), 4)


def numberToPattern(number, dnaLen):
    
    def baseConvert(number):
        convertString = "01234"
        if number < 4:
            return convertString[number]
        else:
            return  baseConvert(number//4) + convertString[number%4]
    
    numBase4 = baseConvert(number)
    crumb = dict(zip('0123', 'ACGT'))
    pattern = "".join(crumb[i] for i in numBase4)
   
   if len(numBase4) < dnaLen:
        return ((dnaLen - len(numBase4)) * 'A') + pattern
    else:
        return pattern



 
numberToPattern(900, 5)