s='XCIVIX'
d={'I': 1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
d2={'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
N=0
for key in d2:
    if key in s and len(s)>0:
        N=N+d2[key]
        s=s.replace(key,'')

if len(s)>0:
    for l in list(s):
        N+=d[l]
print(N)