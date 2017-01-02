# Main file for game
import charsheet as chars
import freqstrings as strs

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

print strs.dead[1]


print "Welcome to Programmin' Cameryn's World of Adventure!"
character = chars.CharCreate()

print character

print "Thank you,", character[0]
