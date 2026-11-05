#set variable b = 0
#set variable a = 1
#
#prompt input enter non negative integer
#print 0 end 
#
#set count = 1
#while count < limit
##  b,a = b+ a,b
#   print , b, sep "", end ""
#   count +=1
#print new line
#print finished



b = 0
a = 1

limit = int(input('Enter a non-negative integer: '))
print(0,end = "")

count = 1
while count < limit:
    b,a = b + a,b
    print(',',b, sep = "", end = "")
    count+=1
print()
print('Finished!')




