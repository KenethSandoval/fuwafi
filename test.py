import re

def stringMatcher():
    patron = re.compile("^[()]+\d+")
    s = input("Patron: ")
    match = patron.match(s)

    if match:
        print("Si")
    else:
       print("no")

stringMatcher()
