
def displayInventory(inventory):
    d = 0
    for i,j in inventory.items():
           print(j,i)
           d += int(j)
    print("Total number of items ",d)
    
def addToInventory(inventory,dragonLoot):
    count = 1
    for i in range(len(dragonLoot)):
        for j in range(1,len(dragonLoot)):
            if i<j and dragonLoot[i] == dragonLoot[j]:
                count += 1
                dragonLoot.pop(j)
                j -= 1
        if dragonLoot[i] in inventory.keys():
            inventory[dragonLoot[i]] = inventory[dragonLoot[i]]+count
        else:
            inventory.setdefault(dragonLoot[i],count)
        count = 1
    displayInventory(inventory)


inventory={}
n = int(input("Enter the number of elements "))
for i in range(n):
    key = input("Enter the invetory element : ")
    print("Enter the count of",key,": ",end="")
    value = int(input())
    inventory[key] = value
displayInventory(inventory)
dragonLoot = []
n = int(input("Enter the number of items to be added "))
for i in range(n):
    a = input("Enter the item to be added ")
    dragonLoot += [a]
addToInventory(inventory,dragonLoot)
