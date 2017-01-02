def CharCreate():
    n = raw_input("Please enter your character's name:")
    a = raw_input("How old is your character?")
    g = raw_input("Is your character a (m)ale, (f)emale, or (o)ther gender?")
    h = int(10)
    i = list()
    charsheet = [n, a, g, h, i]
    return charsheet

items = ['book', 'doll', 'paper', 'picture', 'rock']
