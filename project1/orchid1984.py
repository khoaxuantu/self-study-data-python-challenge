#'A time in month' doesn't really make sense here... 
# You can change the output to: print(f"{month} month is equal to {year} year"). The same goes with converting weight.
# Overall, nice work but consider the output but it may not be accurate for all cases. If you need more accurate month lengths, you would need a more detailed conversion considering the specific month and year (for leap years).
# Lastly, this project requires you to convert between a pair, here you have 7 conversions so it will be counted as 3 pairs = 1 bonus points 

# Input a time in month.
month = int(input("Input time in month: "))

# Convert the time in month to year.
year = month / 12

# Convert the time in month to week.
week = month * 4.348

# Convert the time in month to day.
day = month * 30.437

# Print the calculated time in years, weeks, days.
print("The time in years is %.2f years." % year)
print(f"{month} month is equal to {year} year")
print("The time in weeks is %.2f weeks." % week)
print("The time in days is %.2f days." % day)


# Input a weight in pound.
pound = int(input("Input weight in pound: "))

# Convert the weight in pound to ounce.
ounce = pound  * 16

# Convert the weight in pound to kg.
kg = pound * 0.453

# Convert the weight in pound to gram.
gram = pound * 453.592

# Print the calculated weight in ounces, kgs, grams.
print("The weight in ounces is %i ounces." % ounce)
print("The weight in kgs is %.2f kgs." % kg)
print("The weight in grams is %.2f grams." % gram)