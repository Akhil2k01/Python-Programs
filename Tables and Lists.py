import copy

def printTable(l):
    for i in range(n):
        for j in range(m):
            print(l[j][i],end=" ")
        print()

l = []
n = int(input("Enter number of items in the inner list : "))
m = int(input("Enter the number of inner list : "))

for i in range(m):
    l1 = []
    print("Enter the",i+1,"row elements")
    for j in range(n):
        l1.append(input())
    l.append(l1)
printTable(l)
