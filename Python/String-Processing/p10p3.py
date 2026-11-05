#request input word or nothing to exit 
#
#while word != ''
#   set a,e,i,o,u = [0,0,0,0,0]
#   for ch in word
#       if ch == 'a'
#       a+=1
#       if ch == 'e'
#           e+=1
#       if ch == 'i'
#           i+=1
#       if ch == 'o'
#           o+=1
#       if ch == 'u'
#           u+=1
#   print a+e+i+o+u
#   request input word or nothing to exit
#


word = input('Enter a word(or enter nothing to exit): ')


while word != '':
    a,e,i,o,u = [0,0,0,0,0]
    for ch in word:
        if ch == 'a':
            a+=1
        if ch == 'e':
            e+=1
        if ch == 'i':
            i+=1
        if ch == 'o':
            o+=1
        if ch == 'u':
            u+=1
    print(a+e+i+o+u)
    word = input('Enter a word(or enter nothing to exit): ')
