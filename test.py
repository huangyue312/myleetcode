def countAndSay( n: int) -> str:
        l=['0','1','11']
        #if n<=2: return l[n]
        for i in range(3,n+1):
            reads=''
            j=1
            s=1
            while j < len(l[i-1]):
                
                if l[i-1][j-1]==l[i-1][j]:
                    s+=1
                    j=j+1
                else:
                    t=str(s)+l[i-1][j-1]
                    reads=reads+t
                    j=j+1
                    s=1
                if j== len(l[i-1]):
                    t=str(s)+l[i-1][j-1]
                    reads=reads+t
                    #break
            l.append(reads)
        print (l)
countAndSay(4)
