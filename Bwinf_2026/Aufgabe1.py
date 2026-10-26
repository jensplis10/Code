
wort1 = ["","","",""]
wort2 = ["","","",""]
wort3 = ["","","",""]
wort4 = ["","","",""]
print(*wort1)




for i in range(len(wort1)):
    print("")

with open("Bwinf_2026/451/A1_Kreuzwortkreuze/kreuz0a.txt","r") as data:
    test = data.readlines()
test = [line.strip() for line in test]
word1 = [test[0][1],test[1][1],test[2][1],test[3][1]]
print(*word1)

