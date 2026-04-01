def half(value):
    return value / 2 

def double(value):
    return value * 2 

def second(value):
    return value[1]

print(double(22))
print(double("hello"))
print(double("22")) 

# In Python when we multiply a string by a number, it repeats the string that many times(in our case it is 2 times). 
# I expected print(double("22")) returns 44 (I compare with JavaScript).