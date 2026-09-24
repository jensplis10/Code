def pri(out):
    print(out)


def error():
    print("ERROR")


promt = input("")
i = 0
for letters in promt:
    if promt[i] == "pri("[i] and promt[len(promt) - 1] == ")":
        i += 1
    if i == 3:
        out = promt[4 : len(promt) - 1]
        pri(out)
        exit()
