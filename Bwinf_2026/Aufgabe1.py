
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
print(*test)






















word1ver = [test[0][1],test[1][1],test[2][1],test[3][1]]
word2ver = [test[0][2],test[1][2],test[2][2],test[3][2]]
word3hor = [test[1][0],test[1][1],test[1][2],test[1][3]]
word4hor = [test[2][0],test[2][1],test[2][2],test[2][3]]
print(*word2ver)
print(*word1ver,"\n")
print(*word3hor)
print(*word4hor)
