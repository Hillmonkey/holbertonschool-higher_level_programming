#!/usr/bin/python3
import hidden_4

dud = dir(hidden_4)
for s in dud:
    if s[:2] != '__':
        print(s)
