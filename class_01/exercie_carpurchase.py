#Given the purchase year of a car, write a program to:
#Calcualte the number of months since the purchase.
#How about number of days?
#Print the results

purchase_year = 2012
current_year = 2021    # We should be using the "Date" function here normally.

year_difference = (current_year - purchase_year)

number_months = year_difference * 12
number_days = year_difference * 365

print(number_months)
print(number_days)

print("Number of months since purchase " + str(number_months))
print("Number of days since purchase ") + str(number_days)