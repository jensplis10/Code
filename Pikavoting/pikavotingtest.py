from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


driver = webdriver.Firefox(options=Options())
#1
driver.get("https://topminecraftservers.org/vote/21765")
input()
try:
    driver.find_element(By.ID, "username").send_keys("Jensiboy125")
    sleep(1)
    driver.find_element(By.ID, "voteButton").click()
except:
    print("not found")
#2
driver.get("https://best-minecraft-servers.co/server-pikanetwork-bestq-pika-host.4401/vote")
input()
try:
    driver.find_element(By.NAME, "username").send_keys("Jensiboy125")
    sleep(1)
    driver.find_element(By.NAME, "voteSubmit").click()
except:
    print("not found")
sleep(11)
#3
driver.get("https://www.minerank.com/pikanetwork/vote")
input()
try:
    driver.find_element(By.ID, "mc_username").send_keys("Jensiboy125")
    sleep(1)
    driver.find_element(By.XPATH, "//div[text()='Send Vote']").click()
except:
    print("not found")
#4
driver.get("https://minecraft.buzz/vote/3387")
input()
try:
    driver.find_element(By.ID, "username-input").send_keys("Jensiboy125")
    sleep(1)
    driver.find_element(By.ID, "submitter").click()
except:
    print("not found")
#5
driver.get("https://minecraftkrant.nl/server/pikanetwork/vote")
input()
try:
    driver.find_element(By.ID, "minecraft_name").send_keys("Jensiboy125")
    sleep(1)
    driver.find_element(By.XPATH, "//button[text()='Stem op deze server']").click()
except:
    print("not found")
#6
driver.get("https://minecraft-mp.com/server/41366/vote/")
input()
try:
    driver.find_element(By.ID, "nickname").send_keys("Jensiboy125")
    sleep(1)
    driver.find_element(By.XPATH, "//button[text()='Vote']").click()
except:
    print("not found")
#7
driver.get("https://minecraft-server-list.com/server/424827/vote/")
input()
try:
    driver.find_element(By.ID, "ignnn").send_keys("Jensiboy125")
    sleep(1)
    driver.find_element(By.ID, "voteButton").click()
except:
    print("not found")


