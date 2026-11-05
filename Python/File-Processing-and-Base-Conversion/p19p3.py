# request a string containing the filename
# open the file in read mode
# read the contents of the file
# close the file
#
# set the count of left round brackets to 0
# set the count of right round brackets to 0
# set the count of left triangle brackets to 0
# set the count of right triangle brackets to 0
# set the count of left square brackets to 0
# set the count of right square brackets to 0
# set the count of left curly brackets to 0
# set the count of right curly brackets to 0
#
# go through each character in the file
#     if the character is '('
#         increase the count of left round brackets by 1
#     if the character is ')'
#         increase the count of right round brackets by 1
#     if the character is '<'
#         increase the count of left triangle brackets by 1
#     if the character is '>'
#         increase the count of right triangle brackets by 1
#     if the character is '['
#         increase the count of left square brackets by 1
#     if the character is ']'
#         increase the count of right square brackets by 1
#     if the character is '{'
#         increase the count of left curly brackets by 1
#     if the character is '}'
#         increase the count of right curly brackets by 1
#
# print the total number of left and right round brackets
# if the counts are equal
#     print that the counts are equal
# else
#     print that the counts are not equal
#
# print the total number of left and right triangle brackets
# if the counts are equal
#     print that the counts are equal
# else
#     print that the counts are not equal
#
# print the total number of left and right square brackets
# if the counts are equal
#     print that the counts are equal
# else
#     print that the counts are not equal
#
# print the total number of left and right curly brackets
# if the counts are equal
#     print that the counts are equal
# else
#     print that the counts are not equal
#
# if the counts of all four pairs of brackets are equal
#     print that all the brackets in the file are balanced
# else
#     print that the brackets in the file are not balanced

filename = 'websourcegit.html'

filehandle = open(filename,'r')
websrc = filehandle.read()
filehandle.close()

leftbrack = 0
rightbrack = 0
lefttri = 0
righttri = 0
listleft = 0
listright = 0
squigleft = 0
squigright = 0


for i in websrc:
    if i == '(':
        leftbrack+=1
    if i == ')':
        rightbrack+=1
    if i == '<':
        lefttri+=1
    if i == '>':
        righttri+=1
    if i == '[':
        listleft+=1
    if i == ']':
        listright+=1
    if i == '{':
        squigleft+=1
    if i == '}':
        squigright+=1



print('Total number of left brackets is',leftbrack,'and the total number of right brackets is',rightbrack)
if leftbrack == rightbrack:
     print('There are an equal amount of right and left brackets.')
else:
    print('There are not an equal amount of right and left brackets.')
print()
print('Total number of left triangles is',lefttri,'and the total number of right triangles is',righttri)
if lefttri == righttri:
     print('There are an equal amount of right and left triangles brackets.')
else:
    print('There are not an equal amount of right and left triangles brackets.')
print()
print('Total number of left list brackets is',listleft,'and the total number of right list brackets is',listright)
if listleft == listright:
     print('There are an equal amount of right and left list brackets.')
else:
    print('There are not an equal amount of right and left list brackets.')
print()
print('Total number of left squigley brackets is',squigleft,'and the total number of right squigley brackets is',squigright)
if squigleft == squigright:
     print('There are an equal amount of right and left squigley brackets.')
else:
    print('There are not an equal amount of right and left squigley brackets.')
print()
if leftbrack == rightbrack and lefttri == righttri and listleft == listright and squigleft == squigright:
    print('All the brackets in this source are balanced.')
else:
    print('The brackets in this source are not balanced.')

