#def print_max():
#   """Function that prints out the largest of two numbers 
#   uses the function max to find the largest"""
#
#   define function max a,b 
#       """Function that returns the largest of two numbers and
#       uses the function max to find the largest"""
#           if a > b:
#               return a
#           else
#               return b
#   request number_1 input float 'Enter a number'
#   request number_2 input float 'Enter a number'
#   set variable biggest = max(number_1,number_2)
#
#   print The largest of', number_1,'and', number_2,'is', max(number1, number2)
#
#   return
#call print max()
#

def print_max():
    """Function that prints out the largest of two numbers uses the function max to find the largest"""
    
    def max(a, b):
        """Function that returns the largest of its two arguments"""
        if a > b:
            return a
        else:
            return b

    number1 = float(input('Enter a number: '))
    number2 = float(input('Enter a number: '))
    print('The largest of', number1, 'and', number2,'is', max(number1, number2))

    return
   
print_max()