
wort1 = ["","","",""]
wort2 = ["","","",""]
wort3 = ["","","",""]
wort4 = ["","","",""]
print(*wort1)




for i in range(len(wort1)):
    print("")

with open("Bwinf_2026/451/A1_Kreuzwortkreuze/kreuz0a.txt","r",encoding="utf-8") as data:
    test = data.readlines()
test = [line.strip() for line in test]
word1 = [test[0][1],test[1][1],test[2][1],test[3][1]]
word2 = [test[0][2],test[1][2],test[2][2],test[3][2]]
word3 = [test[1][0],test[1][1],test[1][2],test[1][3]]
word4 = [test[2][0],test[2][1],test[2][2],test[2][3]]
print(*word1)
print(*word2)
print(*word3)
print(*word4)
