print("Welcome to the pizza dilivery!")
size = input("What size pizza do you want? s , n , l:")
pepperoni = input("do you want to add pepperoni on your pizza? y or n:")
extra_cheese = input("do you want to add extra cheee? y or n:")

bill = 0
if size =="s":
    bill +=15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25
else:
    print("you typed wrong input!")

if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill +=3

if extra_cheese == "y":
    if size == "s":
        bill +=1
    else:
        bill +=2

print(f"your final bill is : ${bill}.")            