from functools import *
from itertools import *

#finds all the partitions of a number
def partitions(n):
    if n == 0:
        return [[]]
    else:
        return [([(m + 1)] + p)
                for m in range(n)
                for p in partitions (n - (m + 1))
                if p == [] or (m + 1) <= (p[0])]

#Finds all partitions of a number n, of a given length l
def lengPartitions(n,l):
    filter(lambda x: len(x) == l, partitions(n))

#Given a number, this finds the next number using those digits
#It can be used to find permutations or combinations and probably a bunch
#of other things.
def nextPerm(arr):
    status = False
    k = len(arr) - 2
    new = []
    mid = [arr[k+1]]
    while(k >= 0):
        mid.append(arr[k])
        if(arr[k+1] > arr[k]):
            status = True
            while(len(new) < k):
                new.append(arr[len(new)])
            check = arr[k]
            a = 0
            x = arr[k+1]
            mid.sort()
            c = k + 1
            while(a < len(mid)):
                if(mid[a] > check and mid[a] <= x):
                    x = mid[a]
                    c = a
                a = a + 1
            new.append(x)
            b = 0
            while(b < len(mid)):
                if(b != c):
                    new.append(mid[b])
                b = b + 1
            break
        k = k - 1
    return(status, new)


def combPerm(arr,n):
    m = len(arr)-n
    binary = []
    while(len(binary) <= m - 1):
        binary.append(0)
    while(len(binary) <= m + n - 1):
        binary.append(1)
    print(len(binary))
    combs = [binary]
    status = True
    while(status == True):
        status, new = nextPerm(combs[len(combs)-1])
        if(status == True):
            combs.append(new)
    for i in range(len(combs)):
        print(combs[i])
    a = 0
    combPerms = []
    while(a < len(combs)):
        b = 0
        ones = []
        zeros = []
        while(b < len(combs[a])):
            if(combs[a][b] == 1):
                ones.append(b + 1)
            else:
                zeros.append(b + 1)
            b = b + 1
        perms = [ones]
        status = True
        while(status == True):
            status, new = nextPerm(perms[len(perms)-1])
            if(status == True):
                perms.append(new)
        c = 0
        while(c < len(perms)):
            d = len(zeros) - 1
            while(d >= 0):
                perms[c].insert(0,zeros[d])
                d = d - 1
            combPerms.append(perms[c])
            c = c + 1
        a = a + 1
    combPermArr = []
    e = 0
    while(e < len(combPerms)):
        arr2 = []
        f = 0
        while(f < len(combPerms[e])):
            arr2.append(arr[combPerms[e][f]-1])
            f = f + 1
        combPermArr.append(arr2)
        e = e + 1
    return(combPermArr)


#############################################################
#PROPERTIES

def properties(arr, r):
    status = False
    n = 1
    while(n <= len(arr) - 1):
        nPerms = combPerm(arr, n)
        nProps = lengPartitions(len(arr)-1, n)
        a = 0
        while(a < len(nProps)):
            b = 0
            while(b < len(arr)-n):
                nProps[a].insert(0,0)
                b = b + 1
            a = a + 1
        a = 0
        while(a < len(nProps)):
            b = 0
            while(b < len(nPerms)):
                c = 0
                count = 0
                while(c < len(nPerms[b])):
                    d = 0
                    while(d < len(nPerms[b][c])):
                        if(nPerms[b][c][d] > nProps[a][c]):
                            count = count + 1
                        d = d + 1
                    c = c + 1
                if(count < r):
                    status = True
                b = b + 1
            a = a + 1
        n = n + 1
    return(status)

# sums up all the naturals to r-1 (rC2).
def choose2(r):
    return (n*(n-1))/2

def prop04(arr,r):
    return reduce(lambda x,y: x+y,                             # sum up list.
                  map(lambda l: choose2(l),                    # apply choose2 to each.
                      reduce(lambda l1,l2: l1 + l2, arr, [])), # concatenate lists.
                  0) < choose2(r)                              # check constraint.

#This finds all the cases for r colors
def getCases(r):
    parts1 = partitions(r-2)
    parts2 = partitions(r)
    a = 0
    perms = []
    while(a < len(parts1)):
        while(len(parts1[a]) < len(parts2)):
            parts1[a].append(0)
        parts1[a].sort()
        perms.append(parts1[a])
        status = True
        while(status == True):
            status, new = nextPerm(perms[len(perms)-1])
            if(status == True):
                perms.append(new)
        a = a + 1
    a = 0
    cases = []
    while(a < len(perms)):
        b = 0
        new = []
        while(b < len(parts2)):
            c = 0
            while(c < perms[a][b]):
                new.append(parts2[b])
                c = c + 1
            b = b + 1
        a = a + 1
        cases.append(new)
    cases.sort(reverse = True)
    return(cases)

def main():
    r = int(input('r: '))
    cases = getCases(r)
    a = 0
    count = 0
    while(a < len(cases)):
        status = False
        stat1 = properties(cases[a],r)
        if(stat1 == True):
            status = True
        stat2 = prop04(cases[a],r)
        if(stat2 == True):
            status = True
        if(status == False):
            print(cases[a])
            count = count + 1
        a = a + 1
    print(count)

main()
