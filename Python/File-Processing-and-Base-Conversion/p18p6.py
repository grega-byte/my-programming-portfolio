# import os
#
# set filename to 'websourcegit.html'
#
# if the file does not exist
#     print that the file does not exist
# else
#     open the web source file in read mode
#     read the contents of the file into websrc
#     close the file
#
#     set leftbrack to 0
#     set rightbrack to 0
#     set newline to 0
#     set let_e to 0
#     set punct1 to 0
#     set punct2 to 0
#
#     go through each character in websrc
#         if the character is '<'
#             increase leftbrack by 1
#         if the character is '>'
#             increase rightbrack by 1
#         if the character is a newline
#             increase newline by 1
#         if the character is 'e'
#             increase let_e by 1
#
#     set punct1 to the number of times '<!--' appears in websrc
#     set punct2 to the number of times '-->' appears in websrc
#
#     open 'results.txt' in write mode
#
#     write a heading to the results file
#     write the number of left brackets to the results file
#     write the number of right brackets to the results file
#     write the number of newlines to the results file
#     write the number of lowercase 'e' characters to the results file
#     write the number of '<!--' occurrences to the results file
#     write the number of '-->' occurrences to the results file
#
#     close the results file
#
#     open 'results.txt' in read mode
#     go through each line in the results file
#         print the line without its final newline character
#     close the results file
#
#     print 'Finished!'

import os 

filename = 'websourcegit.html'

if not os.path.isfile(filename):
     print('File'+ ' ' + filename + ' ' +'does not exist')
else:
     filehandle = open(filename,'r')
     websrc = filehandle.read()
     filehandle.close()
     


     leftbrack = 0
     rightbrack = 0
     newline = 0
     let_e = 0
     punct1 = 0
     punct2 = 0

     for i in websrc:
         if i == '<':
             leftbrack+=1
         if i == '>':
                 rightbrack+=1
         if i == '\n':
             newline+=1
         if i == 'e':
             let_e+=1
     punct1 = websrc.count('<!--')
     punct2 = websrc.count('-->')

     filehandle = open('results.txt','w')
            

     filehandle.write('Here is a list of occurences found in this web source:'+ '\n')
     filehandle.write('There are' + ' ' +  str(leftbrack) + ' ' +  'left brackets in this web source.'+'\n')
     filehandle.write('There are' + ' ' +  str(rightbrack) + ' ' +  'right brackets in this web source.'+'\n')
     filehandle.write('There are' + ' ' +  str(newline) + ' ' +  'new lines in this web source.'+'\n')
     filehandle.write('There are' + ' ' +  str(let_e) + ' ' +  'letters "e" in this web source.'+'\n')
     filehandle.write('There are' + ' ' + str(punct1) + ' ' + 'web punctuations <!-- in this web source.'+'\n')
     filehandle.write('There are' + ' ' + str(punct2) + ' ' + 'web punctuations --> in this web source.'+'\n')


     filehandle.close()

     filehandle = open('results.txt','r')
     for line in filehandle:
         print(line[:-1])
     filehandle.close()

     print('Finished!')