a = float(input("Pecentage of days attended: "))
if a >= 85:
    print ("You are eligible to take the examination")
else:
    b = (bool(input("You are ineligible to take the examination. Do you have a medical reason for you absent days? (True or False): ")))
    if b == True:
        print("You are eligible to take the examination")
    else:
        print ("You are ineligible to take the examination")