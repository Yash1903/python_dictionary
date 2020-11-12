import json
from difflib import get_close_matches
data = json.load(open("info.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys()))>0:
        print("did you means %s instead" %get_close_matches(word , data.keys())[0])
        dicide = input("press y for yes or n for no")
        if dicide == "y":
            return data[get_close_matches(word , data.keys())[0]]
        elif dicide =="n":
            return ("enter word is not in dictionary")
        else:
            return("you have entered wrong input please enter just y or n")
    else:
        print("enter word is not in dictionary")

word = input("enter the word you want to search")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)