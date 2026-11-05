#int input total number of toppings (n)
#int input standard total toppings (k)
#
#set variable n = 1
#set variable k = 1
#
#total_minus_standard = total_topping-standard_topping
#variable n_minus_k = 1
#
#for i in range 1,total_topping+1
#   n*=i
#print(n)
#for i in range 1,Standard_topping+1 
#    k*=i
#print(k)
#for i in range 1,total_minus_standard+1 
#    n_minus_k*=i
#print n_minus_k
#
#print Total combinations n/(k*n_minus_k)

total_topping = int(input('Total toppings available: ')) #n
Standard_topping = int(input('Standard pizza topping total: ')) #k

n = 1
k = 1

total_minus_standard = total_topping-Standard_topping
n_minus_k = 1

for i in range(1,total_topping+1):
    n*=i
#print(n)
for i in range(1,Standard_topping+1):
    k*=i
#print(k)
for i in range(1,total_minus_standard+1):
    n_minus_k*=i
#print(n_minus_k)


print('Total combinations:', n/(k*n_minus_k))





