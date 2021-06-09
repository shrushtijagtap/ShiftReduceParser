# ShiftReduceParser
A simple implementation of Shift Reduce Parser in Python, along with a DASH application which demonstrates its working.

Input:
Grammar and String.

Eg.
Grammar:
E->E+E|E-E
E->id

String: 
id + id - id : Accepted
id + id :Accepted

id+id : Rejected
id + id * id : Rejected


Note: The input string should have spaces after every terminal/non terminal. Every entity needs to be space separated
      The grammar should not contain any spaces
      Only '->' symbol can be used, not '=' and '|' should be used for multiple derivations of a single non terminal
     
