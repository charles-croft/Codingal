num = float(input("Choose a number:"))

if num>50:
    print("Number is greater than 50")
    if num%2==0:
        print("And it is also even")
    else:
        print("And it is also odd")
else:
    print("Number is less than 50")