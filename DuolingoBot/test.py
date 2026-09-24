import time
import json

from itertools import permutations
solution = "NoahSimonCheese"
def combinations(words):
    length = 5
    if len(words) < length:
        length = len(words)
    result = words.copy()
    while length > 1:
        for perm in permutations(words, length):
            result.append(" ".join(perm))
        length -= 1
    return result

def lookup_word(search):
    with open("DuolingoBot/words.json","r") as vocab_file:
        vocab = json.load(vocab_file)
    if search.lower().strip() in vocab:
        search = vocab[search.lower().strip()]
    return search


def wort_erkennen(words,search):
    search = lookup_word(search)

    words = combinations(words)

    possibilities = {}

    search = search.lower()

    for i in range(0,len(words)):
        matches = 0

        for number, char in enumerate(search.lower()):
            if char in words[i][number - 2 if number - 2 >= 0 else number - 1 if number - 1 >= 0 else number:number + 2 if number + 2 <= len(words[i]) else number + 1 if number + 1 <= len(words[i]) else number if number <= len(words[i]) else len(words[i]) - 1]:
                matches += 1


        possibilities.setdefault(words[i], matches / max(len(words[i]), len(search)))

    highest_poss = max(possibilities,key=possibilities.get)
    return highest_poss

def check_answer(search_list, answers):
    global solution
    while answers != [] or search_list != []:
        if not solution.startswith(answers[0]):
            print("Wrong answer.")
            print("Correct answer was: " + search_list[0])
            with open("DuolingoBot/words.json","r") as words:
                vocab = json.load(words)
                vocab.update({search_list[0].lower().strip(): search_list[0].lower().strip()})

            with open("DuolingoBot/words.json","w") as words:
                json.dump(vocab, words)
            search_list.pop(0)
            answers.pop(0)
        else:
            print("Correct answer!")
            solution = solution[len(answers[0]):]
            with open("DuolingoBot/words.json","r") as words:
                vocab = json.load(words)
                vocab.update({search_list[0].lower().strip(): answers[0].lower().strip()})

            with open("DuolingoBot/words.json","w") as words:
                json.dump(vocab, words)
            search_list.pop(0)
            answers.pop(0)        

start = input("Press Enter to start the bot.")
while True:
    search_list = []
    question_key_list = []
    question_key = ""
    answers = []
    search = ""
    print("-----------------------------------------------------------------")
    
    page_text = ["complete","Noah Simon Cheese","Simon","Noah","Cheese"]

    if "”" in page_text[0] and "“" in page_text[0]:
        question_key = page_text[0][page_text[0].index("“") + 1:page_text[0].index("”")]
        
    if question_key == "":
        page_text = page_text[1:]
        question_key = page_text[0]


    options = page_text[1:]
    print(question_key)
    print(options)
    if " " in question_key:
        question_key_list = question_key.split(" ")
        for j in range(0 , len(question_key_list)):
            for i in range(j, min(len(question_key_list), 5 + j)):
                if lookup_word(" ".join(question_key_list[0:i + 1])) != " ".join(question_key_list[0:i + 1]):
                    question_key_list[0:i + 1] = " ".join(question_key_list[0:i + 1])
    else:
        question_key_list = [question_key]
    for i in range(0, len(question_key_list)):
        search = question_key_list[i]
        search_list.append(search)
        possibility = wort_erkennen(options, search)
        for option in options:
            if possibility.lower() == option.lower():
                answers.append(option)
                break
        if answers == []:
            possibility = possibility.split(" ")
            for word in possibility:
                for option in options:
                    if word.lower() == option.lower():
                        answers.append(option) 

    if answers != []:
        for answer in answers:
            print(answer)
        
    else:
        print("No answer")
    check_answer(search_list, answers)


    input()
        