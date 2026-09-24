from collections import defaultdict
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def wort_erkennen(words,ges_word):
    possibilities = {}

    ges_word = ges_word.lower()

    for i in range(0,3):
        matches = 0

        for number, char in enumerate(ges_word.lower()):
            if char in words[i][number - 2 if number - 2 >= 0 else number - 1 if number - 1 >= 0 else number:number + 2 if number + 2 < len(words[i]) else number + 1 if number + 1 < len(words[i]) else number if number < len(words[i]) else len(words[i]) - 1]:
                matches += 1


        possibilities.setdefault(words[i], matches / max(len(words[i]), len(ges_word)))

    highest_poss = max(possibilities,key=possibilities.get)
    return highest_poss

def next_question():
    check = driver.find_element(By.CSS_SELECTOR, "._1rcV8 > span:nth-child(1)")
    check.click()

    next = driver.find_element(By.CSS_SELECTOR, "span._9lHjd")
    next.click()
        


options = Options()

driver = webdriver.Firefox(options=options)

driver.get("https://www.duolingo.com")

check_input = driver.find_element(By.CSS_SELECTOR, "button._2V6ug > span:nth-child(1)")
check_input.click()

email = driver.find_element(By.ID, "web-ui1")
email.send_keys("mrfox125twitch@gmail.com")

password = driver.find_element(By.ID, "web-ui2")
password.send_keys("Ih0mMdtwitch.")

login_button = driver.find_element(By.CSS_SELECTOR, "button._1rcV8:nth-child(3)")
login_button.click()

WebDriverWait(driver, 30).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".fc-cta-manage-options > p:nth-child(2)")
    )
)

cookies_options = driver.find_element(By.CSS_SELECTOR, ".fc-cta-manage-options > p:nth-child(2)")
cookies_options.click()

accept_cookies = driver.find_element(By.CSS_SELECTOR,
"div.fc-dialog:nth-child(3) > div:nth-child(3) > div:nth-child(2) > button:nth-child(2) > p:nth-child(2)")
accept_cookies.click()

while True:
    page_text = driver.find_element(By.TAG_NAME, "body").text
    print(page_text)
    start = False
    question_key = ""
    while True:
        try:
            question = driver.find_element(By.CSS_SELECTOR, "._3EOK0 > span:nth-child(1)")
            question_text = question.text
            break
        except:
            print("Question not found")
            time.sleep(1)

        
    

    print(question_text)

    if "”" in question_text and "“" in question_text:
        for i in range(0,len(question_text)):
            if question_text[i] == '”':
                start = False
                break
            if start == True:
                question_key += question_text[i] 
            if question_text[i] == '“':
                start = True
    else:
        question_key = question_text

    try:
        option1,option2,option3 = driver.find_element(By.CSS_SELECTOR, pictures[0]), driver.find_element(By.CSS_SELECTOR, pictures[1]), driver.find_element(By.CSS_SELECTOR, pictures[2])
        option1_text, option2_text, option3_text = option1.text, option2.text, option3.text

        print(option1_text, option2_text, option3_text)
    except:
        option1_text, option2_text, option3_text = "Option 1 not found", "Option 2 not found", "Option 3 not found"
        option1, option2, option3 = None, None, None

    

    answer = wort_erkennen([option1_text, option2_text, option3_text], question_key)

    if answer == option1_text and option1:
        option1.click()
        next_question()
    elif answer == option2_text and option2:
        option2.click()
        next_question()
    elif answer == option3_text and option3:
        option3.click()
        next_question()
    else:
        print("No valid answer found, skipping...")

    time.sleep(3)