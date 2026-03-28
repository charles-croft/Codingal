num_elements = int(input("How many elements in your tuple: "))
temp_list = []

for i in range(num_elements):
    element = input(f"Enter element {i+1}: ")
    temp_list.append(element)

my_tuple = tuple(temp_list)

my_list = list(my_tuple)
print("List:", my_list)