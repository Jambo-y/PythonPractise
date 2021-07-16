# String formatting

str1 = "Red"
str2 = "Blue"
str3 = "Green"



print("First we have {} then we have {} and finally {}".format(str1, str2, str3))


# We want this -> colours = str1 + str2
colours = "{}{}".format(str1, str2)
print(colours)

my_float = 1.56
print("The value is {}".format(my_float))

my_float2 = 1.00
print("The value is {}".format(my_float2))  # The result will be 1.0

