"""
ID: kripaki1
LANG: PYTHON2
TASK: ride
"""
with open('ride.in', 'r') as fin:
    comet = fin.readline().strip()
    group = fin.readline().strip()

def value(name):
    val = 1
    for char in name:
        val *= ord(char) - ord('A') + 1
    return val

def judge(comet, group):
    return 'STAY' if value(comet) % 47 != value(group) % 47 else 'GO'

with open('ride.out', 'w') as fout:
    fout.write(judge(comet, group) + '\n')
