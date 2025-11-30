n=int(input("Enter a number to find square root : "))
for i in range(1,n):
    if(n==i*i):
        print(f"{n} is square of {i} ")
        break
else:
    print(f"{n} has no perfect squares")
