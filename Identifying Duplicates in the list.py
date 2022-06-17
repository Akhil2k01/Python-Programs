import sys,copy

def has_duplicate(l):
    dup = 0
    for ele in l:
        if l.count(ele) > 1:
            dup = 1
    if dup == 1:
        return True
    else:
        return False

def delete_duplicates(l):
    for ele in l:
        if l.count(ele) > 1:
            l.remove(ele)
    return l

def is_sorted(l):
    l1 = copy.copy(l)
    l1.sort()
    for i in range(len(l)):
        if l1[i] != l[i]:
            return False
    return True

l = []
n = int(input("Enter total number of elements : "))
print("Enter the list values ")
for i in range(n):
    l.append(int(input()))
print(l)
print("1.Check for duplicates")
print("2.Delete duplicates")
print("3.Check whether the list is sorted in ascending order")
print("Press any other key to Exit")
ch = input("Enter your choice : ")
if ch == "1":
    if has_duplicate(l):
        print("Duplicates found in the list")
    else:
        print("Duplicate free list")
elif ch == "2":
    print("Duplicates free list ",delete_duplicates(l))
elif ch == "3":
    if is_sorted(l):
        print("List is in ascending order")
    else:
        print("List is not in ascending order")
else:
    sys.exit()

