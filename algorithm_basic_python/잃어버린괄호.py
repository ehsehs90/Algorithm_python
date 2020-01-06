import sys
import re

expretion =sys.stdin.readline().split('-')
print(expretion)
partial_sum=[]

for t in expretion:
    temp = list(map(int, t.split('+')))
    partial_sum.append(sum(temp))
print(partial_sum)
total= partial_sum[0]
for psum in partial_sum[1:]:
    total -= psum

print(total)
