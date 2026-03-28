num_str = input("Enter a number: ")
power = len(num_str)
original = int(num_str)

temp = original
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** power
    temp //= 10

# Print True or False
print(total == original)