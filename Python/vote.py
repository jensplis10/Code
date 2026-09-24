from selenium import webdriver
from selenium.webdriver.common.by import By
import time

mcname = "Jensiboy125"
driver = webdriver.Firefox()
voteseiten = [
    #    {
    #        "url": "https://topminecraftservers.org/server/21765",
    #        "consent": "/html/body/div[7]/div[2]/div[2]/div[2]/div[2]/button[1]",
    #        "weiterleitung": "/html/body/div[3]/div/div/div/div[2]/a",
    #        "chapta": "",
    #        "name": '//*[@id="username"]',
    #        "vote": '//*[@id="voteButton"]',
    #    },
    {
        "url": "https://best-minecraft-servers.co/server-pikanetwork.4401/vote",
        "name": "/html/body/div[4]/section/div[9]/div[2]/div[3]/form/div[1]/input[3]",
        "vote": "/html/body/div[3]/section/div[8]/div[2]/div[2]/form/button",
    },
    {
        "url": "https://servers-minecraft.net/server-pikanetwork.956/vote",
        "name": '//*[@id="username"]',
        "vote": '//*[@id="voteSubmitBtn"]',
    },
    {
        "url": "https://minecraft.buzz/server/3387&tab=vote",
        "weiterleitung": "/html/body/div/div/section[1]/div[1]/a[1]",
        "name": '//*[@id="username-input"]',
        "vote": '//*[@id="submitter"]',
    },
    {
        "url": "https://minecraftservers.page/servers/pikanetwork",
        "weiterleitung": "/html/body/section/div/div/div[3]/div/div[1]/a",
        "name": "/html/body/section/div/div/div[3]/div/form/input[2]",
        "vote": "/html/body/section/div/div/div[3]/div/form/input[2]",
    },
    {
        "url": "https://minecraft-mp.com/server/41366/vote/",
        "name": '//*[@id="nickname"]',
        "vote": "/html/body/div[3]/div/div[4]/div[1]/form/div[5]/div/button",
    },
    {
        "url": "https://minecraft-server-list.com/server/424827/vote/",
        "name": '//*[@id="ignn"]',
        "vote": '//*[@id="voteButton"]',
    },
]

for site in voteseiten:
    driver.get(site["url"])
    time.sleep(5)
    if "consent" in site:
        consent_button = driver.find_element(By.XPATH, site["consent"])
        consent_button.click()
    time.sleep(1)
    if "weiterleitung" in site:
        weiterleiten_button = driver.find_element(By.XPATH, site["weiterleitung"])
        weiterleiten_button.click()

    time.sleep(1)
    if "chapta" in site:
        input(".")
    time.sleep(1)

    name_input = driver.find_element(By.XPATH, site["name"])
    name_input.clear()
    name_input.send_keys(mcname)

    vote_button = driver.find_element(By.XPATH, site["vote"])
    vote_button.click()

    time.sleep(11)

driver.close()
