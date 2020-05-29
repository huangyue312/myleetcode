def isValid(s):
    d={'(':')','{':'}','[':']'}
    ls=list(s)
    #result=bool(1)
    while len(ls)>0:
        if len(ls)>0 and d[ls[0]]==ls[1]:
            result=1
            ls=ls[2:]
        elif len(ls)>0 and d[ls[0]]==ls[-1]:
            result=1
            ls.pop[-1].pop(0)
        else:
            result=0
            break
s="(]"
print(isValid(s))