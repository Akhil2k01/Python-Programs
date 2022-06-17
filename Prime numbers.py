n = int(input('Enter a number : '))
prime = True
if n > 2 :
    for i in range(2,n):
        if n%i == 0:
            prime = False
            break
if prime:
    print(str(n) + ' is a prime number')
else:
    print(str(n) + ' is not a prime number')
