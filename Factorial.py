def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)

print("Enter a number ")
n = int(input())

print(str(n)+"! = "+str(fact(n)))

