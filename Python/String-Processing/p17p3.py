#request a string input containing cat and dog
#
#set words to lowercase
#
#if the number of times cat appears equals the number of times dog appears
#   print that cat and dog appear the same number of times
#else
#   print that cat and dog do not appear the same number of times

words = input('Please enter a string with the words cat and dog: ')

words = words.lower()


if words.count('cat') == words.count('dog'):
    print('Dog and cat appear the same number of times!')

else:
    print('The string cat or dog does not appear the same number of times.')


