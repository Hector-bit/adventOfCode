import fileinput
import re

L = list([l.strip() for l in fileinput.input()])
R = {}
C = {}

def match_list(line, st, ed, rules):
    key = (st, ed, tuple(rules))

    if st==ed and not rules:
        return True
    if st==ed:
        return False
    if not rules:
        return False
    
    ret = False
    for i in range(st+1, ed+1):
        if i==ed and len(rules)>1:
            continue
        if match(line,st,i,rules[0]) and match_list(line,i,ed,rules[1:]):
            return True
    return False