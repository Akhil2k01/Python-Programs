print("Basic Arithmetic Calculator")

while True:
    print("1.ADD 2 numbers")
    print("2.SUBTRACT 2 numbers")
    print("3.MULTIPLY 2 numbers")
    print("4.DIVISION 2 numbers")
    print("5.Exit")
    
    ch = input("Enter your choice : ")
    if ch<'1' or ch>'5':
        print("Invalid choice")
        continue
    elif ch == '5':
        break

    print("Enter 2 numbers : ")
    n1 = input()
    n2 = input()

    if ch == '1':
        res = str(float(n1)+float(n2))
        print(n1+" + "+n2+" = "+res+"\n")
    elif ch == '2':
        res = str(float(n1)-float(n2))
        print(n1+" - "+n2+" = "+res+"\n")
    elif ch == '3':
        res = str(float(n1)*float(n2))
        print(n1+" * "+n2+" = "+res+"\n")
    elif ch == '4':
        res = str(float(n1)/float(n2))
        print(n1+" / "+n2+" = "+res+"\n")

print("Thank You")
