import random
var_X = random.randint(0,1)
if var_X == 0:
    print("head".capitalize())
else:
    print("tail".capitalize())
    
# TASK 2
var_list = []

for i in range(0,5):
    var_list.append(random.randint(1,30))
print(var_list, "Final list")

# TASK 3

string_list = ["Manuk", "Sargis", "Hask", "Artyom"]

sorted_list = sorted(string_list)
print(sorted_list)
res = sorted_list[1:-1]
print(res)