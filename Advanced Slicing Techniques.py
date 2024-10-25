#Task 1: You have a list of daily temperatures for one month, and you'd like to extract specific data from it. Given the list:
#temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 105, 106]
#Extract the temperatures for the second week (7 days) of the month (index to 14).

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 105, 106]          #created a list called [temperatures] using the provided data
second_week_temps = temperatures[7:14]                                                                                 #created a new list called [second_week_temps] and added the 7th through 14th index from our temperatures list to the new list through the slicing method
print(second_week_temps)                                                                                               #print statement to print out our new list

#Task 2: Extract all the temperatures above 100.
big_temps = [temperatures.pop(-1), temperatures.pop(-1)]                                                               #created a new list [big_temps] to hold our 100+ temps. Since i knew the largest temps were at the end of the list and that there were only 2, i just used to pop method at the -1 index to remove them, and store them in the new list
print(big_temps)                                                                                                       #print statement for [big_temps]
print(temperatures)                                                                                                    #print statement for the original lsit without the 100+ temps


