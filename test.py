flag=0
a=list("11")
b=list("1")
re=""
while flag or len(a)>0 or len(b)>0:
    nums_1= int(a.pop()) if len(a)>0 else 0
    nums_2= int(b.pop()) if len(b)>0 else 0
    sum_item =flag + nums_1 + nums_2
    item=sum_item % 2
    re=re+str(item)
    flag=sum_item//2
print(re[::-1])