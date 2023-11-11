x=int(input("Enter the number of elements : "))
y=list(map(int,input("Enter the elements : ").split()))
z=sorted(y)
for i in range(-1000,1000):
    if i>0 and i not in z:
        print(i)
        break
