# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
import datetime
name = input ("Enter your name : ")
age = int(input("Enter your age : "))
now = datetime.datetime.now()
year_you_turn_100 = (now.year) + (100-age)
print(name.title() , "you will turn 100 in " , str(year_you_turn_100))
