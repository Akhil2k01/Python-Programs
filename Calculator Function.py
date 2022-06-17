def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

while True :
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    print("Enter Your Choice : ")
    ch = int(input())

    if ch == 5 :
        break

    elif ch>5 or ch<1 :
        print("Invalid Choice\n")
        continue

    print("Enter two numbers ")
    n1 = float(input())
    n2 = float(input())

    if ch == 1:
        print(str(n1)+" + "+str(n2)+" = "+str(add(n1,n2))+"\n")
    elif ch == 2 :
        print(str(n1)+" - "+str(n2)+" = "+str(sub(n1,n2))+"\n")
    elif ch == 3 :
        print(str(n1)+" * "+str(n2)+" = "+str(mul(n1,n2))+"\n")
    elif ch == 4 :
        if n2 == 0 :
            print("Divide by Zero is not possible\n")
            continue
        else :
            print(str(n1)+" / "+str(n2)+" = "+str(div(n1,n2))+"\n")
print("Thank You")
