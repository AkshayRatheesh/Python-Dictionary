import json
from difflib import get_close_matches

data = json.load(open('dictionary_compact.json'))

user_search = input('The word you want to search : ').lower()



def translate(words):
    if words in data:
        return data[user_search] # searching word and return meaning
    else:       
        sugget_words = get_close_matches(user_search, data.keys()) # word suggetions
        
        if len(sugget_words) > 0 :
            #error fixing
            user_searchs = input(f"Oops! no word match, do you mean this {sugget_words} : ").lower()
            return translate(user_searchs)
            #error fixing
        else:        
            return "no matching found, try again"

print(translate(user_search))

