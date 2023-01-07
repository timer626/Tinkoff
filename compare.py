import re
import sys
def levenstein(str_1, str_2):
    n, m = len(str_1), len(str_2)
    if n > m:
        str_1, str_2 = str_2, str_1
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if str_1[j - 1] != str_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return (current_row[n])/(n+m)

def DoString(s):
    s1=''
    s=re.split('[ \n]',s)
    for i in range(0,len(s)):
        s1=s1+s[i]
    return s1
def readInput(f):
    b=[[0,0],[0,0],[0,0]]
    for i in range(0,3):
        a=re.split('[ \n]',f.readline())
        b[i][0]=a[0]
        b[i][1]=a[1]
    return b
def ReadOneFile(s):
    f=open(s)
    a=f.read()
    return a
def ReadAllFiles(с):
    a=[[0,0],[0,0],[0,0]]
    for i in range(0,3):
        for j in range(0,2):
            a[i][j]=ReadOneFile(c[i][j])
    return a
def DoStringAll(d):
    a=[[0,0],[0,0],[0,0]]
    for i in range(0,3):
        for j in range(0,2):
            a[i][j]=DoString(d[i][j])
    return a
def CountLeven(k):
    a=[0,0,0]
    a[0]=(levenstein(k[0][0],k[0][1]))
    a[1]=(levenstein(k[1][0],k[1][1]))
    a[2]=(levenstein(k[2][0],k[2][1]))
    return a
def printres(file,q):
    f=open(file,'w')
    for i in range(0,3):
        f.write(str(q[i])+' ')
f=open(sys.argv[1])
c=readInput(f)
d=ReadAllFiles(c)
f.close()
k=DoStringAll(d)
q=CountLeven(k)
printres(sys.argv[2],q)

