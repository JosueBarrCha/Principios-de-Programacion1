#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year).
age=int(input("Please enter your current age: "))
year=2023
hundred=(year-age)+100
print(f"Your current age is {age}. In {hundred}, you will turn 100 years old!")
