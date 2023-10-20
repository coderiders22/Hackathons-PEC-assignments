
#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Sid:         22106028
#
# Question: Use lambda expressions and the filter() function to filter out words
#            from a list that don't start with the letter 's'.For example: seq =
#            ['soup','dog','salad','cat','great']
# Question no. : 8
# Assignment:   2
# Created :   14-09-23
#-------------------------------------------------------------------------------


seq = ['soup', 'dog', 'salad', 'cat', 'great']

filtered_words = list(filter(lambda word: word.startswith('s'), seq))

print(filtered_words)
