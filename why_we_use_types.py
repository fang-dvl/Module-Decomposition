def half(value):
    return value / 2

def double(value):
    return value * 2

def second(value):
    return value[1]


print(half(22)) # My prediction was correct. It returned 11
# print(half("hello")) # My prediction was correct. It gave an error since it is a string 
# print(half("22")) #  # I thought maybe Python would see it as a number and return 11


print(double(22)) # My prediction was correct. It returned 44
print(double("hello")) # I expected an error
print(double("22")) # I thought maybe Python would treat it as a number and return 44

# print(second(22)) # # My prediction was correct. It gave an error since it is a number 
# print(second(0x16)) # # My prediction was correct. It gave an error
print(second("hello")) # My prediction was correct. It returned 'e'
print(second("22")) # My prediction was correct. It returned '2'

def double1(number):
    return number * 3

print(double1(10))   
# When you check the function name, it doesn’t fit what we have to expect.
# A better name would be 'triple' or 'multiply_by_three'.
# If you use this func you would expect it to give you double like 20, not 30.
# It might cause a problem for your code.

