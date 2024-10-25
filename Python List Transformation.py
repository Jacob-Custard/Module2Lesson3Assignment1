#Task 1: You've been given a list of grades from an exam. You need to process and analyze these grades. Given the lis of grades:
#grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
#Sort the grades in descending order and print the sorted list.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]              #created a list called "grades" from the list of grades we were given
grades.sort()                                                  #this function sorts the list into numerical or alphabetical order
print(f"{grades}")                                             #this will print our newly sorted list

#Task 2: Calculate the average grade and print it
average_grade = sum(grades) / len(grades)                      #creating a new variable "average_grade". Since the average is the total sum of the numbers divided by how many numbers there were, i used the sum function divided by the len function to find the average. This way even if the list changes at some point the average will still be correctley calculated.
print("The average grade score was", average_grade)            #this will print the average value of the grades


