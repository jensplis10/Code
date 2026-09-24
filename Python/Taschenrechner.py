import re
def solve(rec):
    parts = re.findall(r"\d+|[+*/:()-]|[a-zA-Z_]+", rec)

    priority = {"+": 1, "-": 1, "*": 2, "/": 2, ":": 2}
    out = []
    zwS = []

    for part in parts:
        if part.isalpha():
            print("No letters.")
            exit()
        elif part.isdigit():
            out.append(int(part))
        elif part in priority:
            while zwS and zwS[-1] in priority and priority[zwS[-1]] >= priority[part]:
                out.append(zwS.pop())
            zwS.append(part)
        elif part == "(":
            zwS.append(part)
        elif part == ")":
            while zwS and zwS[-1] != "(":
                out.append(zwS.pop())
            zwS.pop()
    while zwS:
        out.append(zwS.pop())

    zwS = []

    for part in out:
        if isinstance(part, int):
            zwS.append(part)
        else:
            y = zwS.pop()
            x = zwS.pop()

            if part == "+":
                zwS.append(x + y)
            elif part == "-":
                zwS.append(x - y)
            elif part == "*":
                zwS.append(x * y)
            elif part == "/" or part == ":":
                zwS.append(x / y)
    return zwS[0]



rec = input()
erg = solve(rec)
print(erg)