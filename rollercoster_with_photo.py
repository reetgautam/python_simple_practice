print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoster!")
  age =int (input("what is your age?"))
  if age <=12:
    bill = 5
    print("Child tickets are $5");
  elif age <=18:
    bill = 7
    print("Youth tickets are $7");
  else:
    bill = 12
    print("Adult tickets are $12");
    
    wants_photo = input("Do you want to have a photo taken? Type Y for Yes and N for No.")
    if wants_photo =="Y":
      bill += 3

    print(f"your final bill is ${bill}")


else:
  print("sorry,you can't ride the rollercoster!")