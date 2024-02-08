my_list = ["first" , "second" , "third", "fourth"] * 3
my_list.append("five")
print(my_list[:3])
print(my_list[1:3])
print(my_list)
for index, item in enumerate(my_list):
    print(f"{index + 1}: {item}")
