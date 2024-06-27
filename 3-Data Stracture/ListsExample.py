
# Example 1. Manage A To Do List
## Create a To Do List to keep track of tasks

to_do_list = ["study","clean the house","gym"]

## Adding to task
to_do_list.append("Practice coding")
to_do_list.append("Drawing")

## Remove a completed task
to_do_list.remove("study")

## Checking if a task is in the list
if "gym" in to_do_list:
    print("Don't forget to go to gym")

print("To Do List remaining")
for task in to_do_list:
    print(f"-{task}")
#End....

## Example 2. Organizing students grades
grades = [80,95,76,89,90]

# Adding a new grade
grades.append(96)

# Calculating the average grade
averageGrade = sum(grades)/len(grades)
print(f"Average Grade: {averageGrade:.2f}")

#Finding the highest and lowest grades
highestGrade = max(grades)
lowestGrade = min(grades)
print(f"Highest Grade: {highestGrade}")
print(f"Lowest Grade: {lowestGrade}")
#End...

# Example 3. Managing An Inventory
inventory = ["apple","banana","mango","grapes"]
#Adding a new item
inventory.append("cherry")

#Removing an item that is out of stock
inventory.remove("mango")

# Checking if an item is in stock
item = "apple"
if item in inventory:
    print(f"{item} are in stock")
else:
    print(f"{item} are out of stock")

print("Inventory List: ")
for item in inventory:
    print(f" -{item}")

#End...

# Collecting user feedback

feedback = ["Great service!","could be better","very satisfied","excellent experience"]

#Adding new feedback
feedback.append("Not satisfied")

#Counting specific feedback
positiveFeedbackCount = sum(1 for comment in feedback if "great" in comment.lower() or "excellent" in comment.lower())

#Print all feedback
print("User Feedback:")
for comment in feedback:
    print(f" -{comment}")

print("Positive Feedback: ",positiveFeedbackCount)






















