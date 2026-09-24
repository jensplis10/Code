from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException,ElementNotInteractableException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import random

from itertools import permutations

def safe_click(element):
    for _ in range(3):
        try:
            element.click()
            return
        except StaleElementReferenceException:
            continue
        except ElementNotInteractableException:
            continue
        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)
            time.sleep(0.5)
            try:
                element.click()
                return
            except Exception:
                driver.execute_script("arguments[0].click();", element)
                return
    

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

def get_page_text():
    page_text = driver.find_element(By.TAG_NAME, "body").text
    page_text = page_text.splitlines()
    page_text = [line for line in page_text if not line.isdigit() and line.upper() != line]
    try:
        page_text = page_text[0:page_text.index("verified_user")] + page_text[page_text.index("close") + 1:]
    except:
        pass
    return page_text

def skip_answer():
    try:
        driver.find_element(By.XPATH, f"//span[text()='Skip']").click()
        with open("DuolingoBot/words.json","r") as words:
            vocab = json.load(words)
            vocab.update({search.lower().strip(): page_text[page_text.index("Correct solution:") + 1].lower().strip()})

        with open("DuolingoBot/words.json","w") as words:
            json.dump(vocab, words)
    except:
        print("Skip button not found.")

def check_answer(search_list, answers):
    try:
        driver.find_element(By.XPATH, f"//span[text()='Check']").click()
    except:
        print("Check button not found.")
        return
    
    page_text = get_page_text()
    while answers != [] or search_list != []:
        if "Correct solution:" in page_text:
            print("Wrong answer.")
            print("Correct answer was: " + page_text[page_text.index("Correct solution:") + 1])
            with open("DuolingoBot/words.json","r") as words:
                vocab = json.load(words)
                vocab.update({search_list[0].lower().strip(): page_text[page_text.index("Correct solution:") + 1].lower().split(" ").strip()})

            with open("DuolingoBot/words.json","w") as words:
                json.dump(vocab, words)
        else:
            print("Correct answer!")
            with open("DuolingoBot/words.json","r") as words:
                vocab = json.load(words)
                vocab.update({search_list[0].lower().strip(): answers[0].lower().strip()})

            with open("DuolingoBot/words.json","w") as words:
                json.dump(vocab, words)
        search_list.pop(0)
        answers.pop(0)


def next_question():
    try:
        driver.find_element(By.XPATH, f"//span[text()='Continue']").click()
    except:
        print("Continue button not found.")
        



driver = webdriver.Firefox(options=Options())

driver.get("https://www.duolingo.com")

try:
    driver.find_element(By.XPATH, "//span[text()='I ALREADY HAVE AN ACCOUNT']").click()

    driver.find_element(By.ID, "web-ui1").send_keys("mrfox125twitch@gmail.com")

    driver.find_element(By.ID, "web-ui2").send_keys("Ih0mMdtwitch.")

    time.sleep(random.randint(1,3))

    driver.find_element(By.XPATH, "//span[text()='LOG IN']").click()

#    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//p[text()='Manage options']"))).click()

#    driver.find_element(By.XPATH, "//p[text()='Confirm choices']").click()

except:
    print("Login elements not found.")



start = input("Press Enter to start the bot.")
while True:
    global search
    global options
    question_key_list = []
    question_key = ""
    search_list = []
    answers = []
    search = ""
    print("-----------------------------------------------------------------")
    
    page_text = get_page_text()

    if page_text == []:
        next_question()
        continue    

    if "”" in page_text[0] and "“" in page_text[0]:
        question_key = page_text[0][page_text[0].index("“") + 1:page_text[0].index("”")]
    elif page_text[0].startswith("Fill in"):
        skip_answer()
        next_question()
        continue
        
    if question_key == "":
        page_text = page_text[1:]
        if page_text == []:
            next_question()
            continue 
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
            try:
                element = driver.find_element(By.XPATH, f"//span[text()='{answer}']")
                safe_click(element)
            except:
                raise Exception(f"Option '{answer}' not found.")
    else:
        skip_answer()
        break

    check_answer(search_list, answers)
    next_question()

    time.sleep(1)
        