height=[0,1,0,2,1,0,1,3,2,1,2,1]
stack=[]
a=0
if len(height)<3: return 0
for i in range(0,len(height)):
    if len(stack)>0 and height[i]>height[stack[-1]]:
        top=stack.pop()
        if len(stack)==0: break
        h=min(height[i],height[stack[-1]])-height[top]
        s=i-stack[-1]-1
        a=a+(h*s)
    stack.append(i)
print(a)