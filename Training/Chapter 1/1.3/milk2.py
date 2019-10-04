"""
ID: kripaki1
LANG: PYTHON2
TASK: milk2
"""

times = set()

with open('milk2.in','r') as fin:
    N = int(fin.readline())
    for i in range(N):
        s, e = map(int, fin.readline().split())
        times.update(range(s,e))

start, end = min(times), max(times)
l = [int(i in times) for i in range(start,end+1)]
#print times
#print l
s = ''.join(list(map(str, l)))
#print s
milk = len(max(s.split('0')))
idle = len(max(s.split('1')))

with open('milk2.out','w') as fout:
    fout.write(str(milk) + ' ' + str(idle) + '\n')
