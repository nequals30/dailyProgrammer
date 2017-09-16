# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 17:11:59 2017

Given a dollar amount between 0.00 and 999,999.00, create a program that will
 provide a worded representation of a dollar amount on a check.
 
https://www.reddit.com/r/dailyprogrammer/comments/6yep7x/20170906_challenge_330_intermediate_check_writer/

@author: nEquals30
"""
numIn = 919616.12

def num2word(strIn):
    # Dictionary of digit names
    ones = {1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
    teens = {10:"Ten",11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen"}
    tens = {1:"Ten",2:"Twenty",3:"Thirty",4:"Forty",5:"Fifty",6:"Sixty",7:"Seventy",8:"Eighty",9:"Ninety"}

    strIn = strIn.zfill(3)
    if strIn == '000':
        return('Zero ')
        
    strOut = ''
    # Hundreds
    if strIn[0]!='0':
        strOut = strOut + ones[int(strIn[0])] + ' Hundred '
    # Tens and Teens
    if strIn[1]!='0':
        if strIn[1] == '1':
            strOut = strOut + teens[int(strIn[1:])] + ' '
        else:
            strOut = strOut + tens[int(strIn[1])] + ' '
    # Singles
    if not (strIn[1]=='1' or strIn[2]=='0'):
        strOut = strOut + ones[int(strIn[2])] + ' '

    return(strOut)

# n is the number of digits to left of period
strIn = '%.2f' % numIn
n = len(strIn)-3

# Figure out strings for hundreds, thousands and cents
cents = strIn[len(strIn)-2:]
hundreds = strIn[(n-min(n,3)):(n)]
if n>3:
    thousands = strIn[(n-min(n,6)):(n-3)]

strOut = ''
if n>3:
    strOut = strOut + num2word(thousands) + 'Thousand, '
strOut = strOut + num2word(hundreds) + "Dollars and " + num2word(cents) + "Cents"
print(strOut)