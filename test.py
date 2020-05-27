x=-121
flag = -1 if x<0  else 1
re=int(str(x*flag)[::-1])*flag
print(True if re==x else False)