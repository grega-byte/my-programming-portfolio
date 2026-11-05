#create variable pass_input and ask the user to input their password
#create variable password and set the password
#if pass_input is equal to password
#    print that they have successfully logged in
#else
#    ask the user to enter the password again
#    if pass_input is equal to password
#        print that they have successfully logged in
#    else
#        ask the user to enter the password again
#        if pass_input is equal to password
#            print that they have successfully logged in
#        else
#            ask the user to enter the password again
#            if pass_input is equal to password
#                print that they have successfully logged in
#            else
#                print that they have been denied access

pass_input = input('Please enter password: ')

password = 'banana'

if pass_input == password:
    print('You have successfully logged in. ')
else:
    pass_input = input('Incorrect. Please enter password again: ')
    if pass_input == password:
        print('You have successfully logged in. ')
    else:
        pass_input = input('Incorrect. Please enter password again: ')
        if pass_input == password:
                print('You have successfully logged in. ')
        else:
                pass_input = input('Incorrect. Please enter password again: ')
                if pass_input == password:
                        print('You have successfully logged in. ')
                else:
                    print('You have been denied access.')
