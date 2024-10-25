#Task 1: You have two lists of student names. One list contains the names of sudents who have submitted their assignments,
#and the other list contains the names of students who attended the last class. Given the two lists:
#submitted = ["Alice", "Bob", "Charlie", "David"]
#attended = ["Charlie", "Eve", "Alice", "Frank"]
#Find out if Alice submitted their assignment and attended class.

submitted = ["Alice", "Bob", "Charlie", "David"]                                                      #creating a list called [submitted] using the names provided
attended = ["Charlie", "Eve", "Alice", "Frank"]                                                       #creating a list called [attended] using the names provided
if "Alice" in submitted and "Alice" in attended:                                                      #wrote an if statement using the "in" and "and" modifiers to check and see if "Alice" was present in both lists
    print("Alice both attended yesterdays class and turned in her assignment.")                       #print statement telling the user "Alice" was found in both lists
else:                                                                                                 #only looking for one set of condtions so added an else statement to account for the conditions not being met
    print("Alice either forgot to turn in her assignment or was not present in yesterdys class.")     #print statement telling the user the conditions were not met

