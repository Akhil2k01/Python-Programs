import sys

def hotel_cost(nights):
    cost = 140*nights
    return cost

def plane_ride_cost(city):
    if city == "Charlotte":
        cost = 183
        return cost
    elif city == "Tampa":
        cost = 220
        return cost
    elif city == "Pittsburgh":
        cost = 222
        return cost
    elif city == "Los Angeles":
        cost = 475
        return cost
    else :
        return -1

def rental_car_cost(days):
    cost = 40*days
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost

def trip_cost(city,days):
    total_cost = hotel_cost(days)+plane_ride_cost(city)+rental_car_cost(days)
    return total_cost


print("Available Cities 'Charlotte', 'Tampa', 'Pittsburgh', 'Los Angeles'")
city = input("Enter the CITY you are TRAVELLING to : ")
if plane_ride_cost(city) == -1:
    print("Entered CITY is NOT FOUND") 
    sys.exit()
days = int(input("Enter the TOTAL DAYS you are TRAVELLING : "))
disc = "0"
total = str(40*days)
if days >= 7:
    disc = "50"
elif days >= 3:
    disc = "20"
total_cost = str(trip_cost(city,days))

print("\nCITY = ",city,"\nDAYS OF TRAVELLING =",days)
print("\nTRAVELLING (PLANE) EXPENSES = $"+str(plane_ride_cost(city)))
print("STAYING (HOTEL) EXPENSES = $"+str(hotel_cost(days)))
print("STAYING (RENTING A CAR) EXPENSES (TOTAl = $"+total,"-$"+disc+" DISCOUNTED) FINAL TOTAL = $"+str(rental_car_cost(days)))
print("TOTAL TRIP COST = $"+total_cost)



    
