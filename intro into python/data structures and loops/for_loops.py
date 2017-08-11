"""Write a function, `tag_count`, that takes as its argument a list
of strings. It should return a count of how many of those strings
are XML tags. You can tell if a string is an XML tag if it begins
with a left angle bracket "<" and end with a right angle bracket ">".
"""
#TODO: Define the tag_count function
def tag_count(count):
    counter = 0
    for c in count:
        if c[0] == "<" and c[-1] == ">":
            counter += 1
    return counter

# Test for the tag_count function:
list1 = ['<greeting>', 'Hello World!', '</greeting>']
count = tag_count(list1)
print("Expected result: 2, Actual result: {}".format(count))