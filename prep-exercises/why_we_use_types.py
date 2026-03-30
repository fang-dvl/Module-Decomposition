def half(value):
    return value / 2 

def double(value):
    return value * 2 

def second(value):
    return value[1]

# Prediction: double("22") will return "2222" because * operator repeats strings
print(double("22"))

# Testing other cases
print(half(22))
# print(half("hello"))  # This will error
# print(half("22"))  # This will error

print(double(22))
print(double("hello"))

# print(second(22))  # This will error
print(second("hello"))
print(second("22"))

def double_bug(number):
    return number * 2

print(double_bug(10))  # Returns 20 (correctly doubles the number)