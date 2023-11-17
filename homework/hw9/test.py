row=5
col=3
Size=8
c=col
for i in range(row-1,-1,-1):
    c-=1
    if c<0: break
    print(f'{i,c}')

print("for 2")

c=col
for r in range(row-1,-1,-1):
    c+=1
    if c>=Size: break
    print(f'{r,c}')