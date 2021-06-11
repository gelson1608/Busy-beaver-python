# -*- coding: utf-8 -*-
"""
Test script for running a Turing machine unary adder

Created on Fri Mar 29 21:57:42 2019

@author: shakes
"""
from turing_machine import TuringMachine
from itertools import islice

#create the Turing machine
multiplier = TuringMachine(
    {
        #Write your transition rules here as entries to a Python dictionary
        #For example, the key will be a pair (state, character)
        #The value will be the triple (next state, character to write, move head L or R)
        #such as ('q0', '1'): ('q1', '0', 'R'), which says if current state is q0 and 1 encountered
        #then transition to state q1, write a 0 and move head right.

        ('q0', '0'): ('By0', 'X', 'R'),
        ('By0', '1'): ('By0', 'X', 'R'),
        ('By0', ''): ('End', '', 'R'),
        ('q0', '1'): ('FindDelimiter0', '1', 'R'),

        ('FindDelimiter0', '1'): ('FindDelimiter0', '1', 'R'),
        ('FindDelimiter0', '0'): ('FindRightmost', '0', 'R'),

        ('FindRightmost', '1'): ('FindRightmost', '1', 'R'),
        ('FindRightmost', ''): ('Find0', '=', 'L'),

        ('Find0', '1'): ('Find0', '1', 'L'),
        ('Find0', '0'): ('MarkRightSide', '0', 'R'),

        ('MarkRightSide', 'X'): ('MarkRightSide', 'X', 'R'),
        ('MarkRightSide', '1'): ('Loop', 'X', 'L'),
        ('MarkRightSide', '='): ('End', '', 'L'),

        ('FindNext1Left', 'X'): ('FindNext1Left', 'X', 'L'),
        ('FindNext1Left', '1'): ('Multiply', 'X', 'R'),
        ('FindNext1Left', ''): ('ResetX', '', 'R'),

        ('ResetX', 'X'): ('ResetX', '1', 'R'),
        ('ResetX', '0'): ('MarkRightSide', '0', 'R'),

        ('Multiply', '1'): ('Multiply', '1', 'R'),
        ('Multiply', '0'): ('Multiply', '0', 'R'),
        ('Multiply', 'X'): ('Multiply', 'X', 'R'),
        ('Multiply', '='): ('Multiply', '=', 'R'),
        ('Multiply', ''): ('Loop', '1', 'L'),

        ('Loop', 'X'): ('Loop', 'X', 'L'),
        ('Loop', '1'): ('Loop', '1', 'L'),
        ('Loop', '='): ('Loop', '=', 'L'),
        ('Loop', '0'): ('FindNext1Left', '0', 'L'),

        ('End', '1'): ('End', '', 'L'),
        ('End', '0'): ('End', '', 'L'),
        ('End', 'X'): ('End', '', 'L'),
        ('End', ''): ('qa', '', 'R'),

    }
)

w = '111011111'
multiplier.debug(w, step_limit=1500)
print("-------------------------------------")
listS = list(islice(multiplier.run(w), 1500))

if listS[len(listS)-1][0] == 'Accept':
    count = 0
    list1 = listS[len(listS)-1][1]['right_hand_side']
    for i in list1:
        if i == '1':
            count = count + 1
    print("Result: {}".format(count))
else:
    print("String rejected")
