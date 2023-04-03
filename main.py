import json
from difflib import get_close_matches

data = json.load(open('dictionary_compact.json'))

user_search = input('The word you want to search : ').lower()



def translate(words):
    print(words)
    if words in data:
        return data[words] 
        # searching word and return meaning
    else:       
        sugget_words = get_close_matches(words, data.keys())
        # word suggetions
        
        if len(sugget_words) > 0 :
            second_search = input(f"Oops! no word match, do you mean this {sugget_words} :\n").lower()
            #reading suggested word input
                        
            if second_search in sugget_words and second_search != words:
                return data[second_search]
                #second in the suggested list that means word meaning available
            elif second_search == words:
                return "no matching found, try again"
                #same word try to search again
            else:        
                return translate(second_search)
                #Recursion -- second searched word new and not in the suggested list
        
        else:        
            return "no matching found, try again"
            #word not in the file

print(translate(user_search))
