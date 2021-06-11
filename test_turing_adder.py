# -*- coding: utf-8 -*-
"""
Test script for running a Turing machine unary adder

Created on Fri Mar 29 21:57:42 2019

@author: shakes
"""
from turing_machine import TuringMachine
from itertools import islice

#create the Turing machine
adder = TuringMachine(
    {
        #Write your transition rules here as entries to a Python dictionary
        #For example, the key will be a pair (state, character)
        #The value will be the triple (next state, character to write, move head L or R)
        #such as ('q0', '1'): ('q1', '0', 'R'), which says if current state is q0 and 1 encountered
        #then transition to state q1, write a 0 and move head right.

        ('q0', '1'): ('FindDelimiter0', '1', 'R'),
        ('q0', '0'): ('NoAdd', '0', 'R'),
        ('NoAdd', '1'): ('FindRightmost', '1', 'R'),
        ('NoAdd', ''): ('End', '', 'R'),

        ('FindDelimiter0', '1'): ('FindDelimiter0', '1', 'R'),
        ('FindDelimiter0', '') : ('End', '', 'R'),
        ('FindDelimiter0', '0'): ('FindRightmost', '0', 'R'),

        ('FindRightmost', '1'): ('FindRightmost', '1', 'R'),
        ('FindRightmost', ''): ('Check1', '', 'L'),

        ('Check1', '1'): ('Find0', '', 'L'),
        ('Find0', '1'): ('Find0', '1', 'L'),
        ('Find0', '0'): ('End', '1', 'R'),
        ('End', '1'): ('End', '1', 'R'),
        ('End', ''): ('qa', '', 'R')

    }
)
adder.debug('110111')
print("-------------------------------------")
listS = list(islice(adder.run('110111'), 100))

if listS[len(listS)-1][0] == 'Accept':
    count = 0
    list1 = listS[len(listS)-1][1]['left_hand_side']
    for i in list1:
        if i == '1':
            count = count + 1
    print("Result: {}".format(count))
else:
    print("String rejected")
