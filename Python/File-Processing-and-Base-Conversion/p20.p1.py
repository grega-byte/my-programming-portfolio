import os

userfile = input('Enter a file: ')

if userfile == '':
        userfile = 'lines.txt'

if not os.path.isfile(userfile):
    print('The file', userfile, 'does not exist.')
else:
    
    
    
    
    userword = input('Please enter a word to search: ')
    while userword != '':
        originalword = userword
        check = False
        while check == False:
            myfile = open(userfile,'r')
            
            for line in myfile:
                if userword in line:
                    print(line, end='')
                    check = True
            myfile.close()
            if check:
                print('The search string', originalword,
                      'or a prefix of it was found.')
                break
            else:
                if len(userword) > 5:
                    userword = userword[:-1]
                else:
                    break
        if check == False:
            print('Neither the search string', originalword,
                  'nor any of its prefixes of it was found.')
        userword = input('Please enter a word to search: ')   
    print('Finished')


