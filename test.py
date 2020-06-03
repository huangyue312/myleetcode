nums=[]
s=1
for i in range(0,len(nums)-1):
    if nums[i]!=nums[i+1]:
        nums[s]=nums[i+1]
        s+=1
print s