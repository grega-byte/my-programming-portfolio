#create variable name and ask the user to input their name
#if name is Greg
#    print that it is a cool name
#elif name is Mickey Mouse or name is Spongebob Squarepants
#    print that you are not sure that is their name
#else
#    print that they have a nice name

name = (input('What is your name? '))

if name == 'Greg':
    print('That is a cool name!')
elif name == 'Mickey Mouse' or name == 'Spongebob Squarepants':
    print('I am not sure that is your name.')
else:
    print('You have a nice name.')