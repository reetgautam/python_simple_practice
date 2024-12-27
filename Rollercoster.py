print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoster!")
  age =int (input("what is your age?"))
  if age <=12:
    print("plese pay $5");
  elif age <=18:
    print("plese pay $7");
  else:
    print("plese pay $12");

else:
  print("sorry,you can't ride the rollercoster!")