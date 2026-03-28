a = int(input("Number of working days: "))
b = int(input("Number of absent days: "))
c = ((a-b)/a) * 100
if c >= 75 < 100:
  print ("You are eligible")
elif c < 75 >= 0:
  print ("You are not eligible")
else:
  print ("Invalid input")