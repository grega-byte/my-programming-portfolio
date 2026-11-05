#create variable pass_input and ask the user to input their password
#create variable password and set the password
#if pass_input is equal to password
#    print that they have successfully logged in
#elif pass_input is not equal to password
#    print that the password is wrong
#    ask the user to enter the password three times
#    create variable pass_input2 and ask the user to input their password
#    create variable pass_input3 and ask the user to input their password
#    create variable pass_input4 and ask the user to input their password
#    if pass_input2 is equal to password and pass_input3 is equal to password and pass_input4 is equal to password
#        print that they have successfully logged in
#    else
#        print that they have been denied access

pass_input = input('Please enter your password: ')

password = 'chocolate123'

if pass_input == password:
    print('You have successfully logged in. ')
    
elif pass_input != password:
    print('Sorry, the password is wrong. Please enter the password three times for verification.')
    pass_input2 = input('Please enter your password: ')
    pass_input3 = input('Please enter your password: ')
    pass_input4 = input('Please enter your password: ')
    if pass_input2 == password and pass_input3 == password and pass_input4 == password:
        print('You have successfully logged in.')
    else:
         print('You have been denied access.')

   