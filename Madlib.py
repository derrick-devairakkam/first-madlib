# Welcome to my Madlib, one of my first personal projects.

print(f"Welcome to my first Madlib")

silly_word1 = input("Enter a silly word. ")
last_name = input("What is your last name? ")
sickness = input("Input an illness. ")
noun = input("Enter a noun (plural). ")
adjective1 = input("Please type an adjective. ")
adjective2 = input("Enter another adjective. ")
silly_word2 = input("Another silly word. ")
place = input("Enter a place. ")
number = input("Enter a number. ")
adjective3 = input("Enter another adjective. ")
madlib = (f"Dear School Nurse: {silly_word1} {last_name} will not be attending school today. \
He/she has come down with a case of {sickness} and has horrible {noun} and a/an {adjective1} fever. \
We have made an appointment with the {adjective2} Dr. {silly_word2}, who studied for many years in {place} and has {number} degrees in \
pediatrics. He will send you all the information you need. Thank you! Sincerely Mrs. {adjective3}.")

print(madlib)
