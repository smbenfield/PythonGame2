# Main file for game
name = None
pronouns = None
age = None

swing_exists = True

from sys import *

#Frequently used strings
prompt = ">>"
error = "Please try again."
dead = ["You have died. Thank you for playing.", "That was stupid, now you're dead."]
deadend = "You have reached a dead end, please return to whence you came."

# Character Management


print "Welcome to Programmin' Cameryn's World of Adventure!"
print "What is your name?"
name = raw_input(prompt)

print "Thank you, %s.", name