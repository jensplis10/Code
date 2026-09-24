import re
import os
import sys
import random
import time
import operator

# -----------------------------------------------------------------------------------------

opers = {
    "=": operator.eq,
    "<": operator.lt,
    ">": operator.gt,
    "<=": operator.le,
    ">=": operator.ge,
}
commands = {}
variables = {}
colors = {
    "BLACK": "\033[30m",
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "NEON_GREEN": "\033[38;2;57;255;20m",
    "YELLOW": "\033[33m",
    "BLUE": "\033[34m",
    "MAGENTA": "\033[35m",
    "CYAN": "\033[36m",
    "WHITE": "\033[37m",
    "GRAY": "\033[90m",
    "LIGHT BLUE": "\033[94m",
    "ORANGE": "\033[91m",
    "PURPLE": "\033[95m",
    "RESET": "\033[0m",
}
prin = False
color = colors["RESET"]
last_input = ""
last_line = ""
line = -1
line_index = line
start_index = -1
end_index = -1
start_loop = -1
end_loop = -1
alt_start_loop = -1
code = []
code_backup = []
deleted_lines = 0

# -----------------------------------------------------------------------------------------


def reg(name):
    def wra(func):
        commands[name.upper()] = func
        return func

    return wra


def finPar(rec):
    parts = re.findall(r"\d+|[+*/:()-]|[a-zA-Z_]+", rec)
    return parts


def sort(parts):
    priority = {"+": 1, "-": 1, "*": 2, "/": 2, ":": 2}
    out = []
    zwS = []

    for part in parts:
        if part.isalpha():
            if part in variables:
                out.append(get_var(part))
                if out[-1].isalpha():
                    print(f"\033[38;2;255;0;0m VAR '{part}' NOT INT \033[0m")
                    print(f"\033[38;2;255;0;0m SET VAR '{part}' TO 0 \033[0m")
                    out[-1] = 0
                else:
                    out[-1] = int(get_var(part))

            else:
                out.append(0)
                print(f"\033[38;2;255;0;0m VAR '{part}' NOT IN VARIABLES \033[0m")
                print(f"\033[38;2;255;0;0m SET VAR '{part}' TO 0 \033[0m")
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
    return out


def solve(rRF):
    zwS = []

    for part in rRF:
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


def def_var(name, val):
    if re.findall(r"[*/:+-]", str(val)):
        val = calc(val)
    elif str(val).isalpha():
        val = det_var(val)
    variables[name] = val


def get_var(name):
    return variables[name]


def get_pat(filename):
    for dirpath, dirname, name in os.walk("."):
        for file in name:
            if file == (filename):
                filepath = os.path.join(dirpath, file)
                path = filepath
                return path


def save_input(input):
    global last_input
    last_input = input
    return last_input


def step(val, direction):
    if direction == 1:
        if val >= 255:
            direction = -1
        val += 1
    else:
        if val <= 128:
            direction = 1
        val -= 1
    return val, direction


def det_var(inh):
    while "{" in inh:
        start = inh.find("{")
        count = 1
        i = start + 1
        while count != 0:
            if inh[i] == "}":
                count -= 1
            i += 1
        var = inh[start + 1 : i - 1]
        inh = inh[:start] + str(get_var(str(var))) + inh[i:]
    return inh


def order(inp):
    global line
    global code
    exclams = []
    alt_len_inp = 0

    if "(" in inp and ")" in inp:
        exclams = [""]

    while exclams != []:
        if alt_len_inp != len(inp):
            exclams = []
            i = 0
            while i < len(inp):
                if inp[i] == "(" or inp[i] == ")":
                    exclams.append(i)
                i += 1
            alt_len_inp = len(inp)
        last = len(exclams) - 1
        start = -1
        while start == -1 and last != -1:
            if inp[exclams[last]] == "(":
                start = exclams[last]
            else:
                last -= 1

        while start != 0 and inp[start - 1].isalpha():
            start -= 1
        name = inp[start : exclams[last]].upper()

        pos_exclam = last + 1

        inh = inp[exclams[last] + 1 : exclams[pos_exclam]]
        if name in commands:
            com = commands[name](inh)
            inp = inp[:start] + str(com) + inp[exclams[pos_exclam] + 1 :]
        exclams.pop(pos_exclam)
        exclams.pop(last)

    if not line == -1:
        code.pop(line)

    return ""


def main():
    global line
    global code
    global deleted_lines
    global start_index
    global end_index
    global start_loop
    global end_loop
    global alt_start_loop

    for line_code, inp in enumerate(code):
        line = line_code

        if start_index != -1 and end_index != -1:
            line = start_index
            while start_index <= end_index:
                order(code[start_index])
                if start_index == -1 and end_index == -1:
                    break
                end_index -= 1

            if line == -1:
                break

            if start_index != -1 and end_index != -1:
                code.pop(start_index - 1)

                end_index = -1
                break

        if start_loop != -1 and end_loop != -1:
            line = start_loop
            deleted_lines = 0
            while start_loop <= end_loop:
                line = alt_start_loop
                order(code[start_loop])
                if start_loop == -1 and end_loop == -1:
                    break
                end_loop = end_loop - 1 - deleted_lines
                deleted_lines = 0

            if line == -1:
                break

            if start_loop != -1 and end_loop != -1:
                code.pop(start_loop - 1)

                start_loop = -1
                end_loop = -1
                break

        elif inp not in code:
            break

        else:
            inp = inp.rstrip("\n\t")
            order(inp)
            break


def get_start_end_condition():
    global code
    global start_index
    global end_index
    global line_index

    start_index = line_index + 1
    stop = 1
    while stop != 0 and line_index + 1 != len(code):
        if code[line_index + 1].rstrip("\n\t").endswith(","):
            if stop == 1:
                end_index = line_index + 1
            stop -= 1
        elif (
            code[line_index + 1].rstrip("\n\t").upper().startswith("IF")
            or code[line_index + 1].rstrip("\n\t").upper().startswith("ELSE")
            or code[line_index + 1].rstrip("\n\t").upper().startswith("FOR")
        ):
            stop += 1
        line_index += 1
    return ""


def get_start_end_loop():
    global code
    global start_loop
    global end_loop
    global line_index

    start_loop = line_index + 1
    stop = 1
    while stop != 0 and line_index + 1 != len(code):
        if code[line_index + 1].rstrip("\n\t").endswith(","):
            if stop == 1:
                end_loop = line_index + 1
            stop -= 1
        elif (
            code[line_index + 1].rstrip("\n\t").upper().startswith("IF")
            or code[line_index + 1].rstrip("\n\t").upper().startswith("ELSE")
            or code[line_index + 1].rstrip("\n\t").upper().startswith("FOR")
        ):
            stop += 1
        line_index += 1
    return ""


# -----------------------------------------------------------------------------------------


@reg("COLORCICLE")
def colcic(inh):
    global last_line
    rdirect = 1
    gdirect = 1
    bdirect = 1
    r = int(256 / 3 * 1)
    g = int(256 / 3 * 2)
    b = int(256 / 3 * 3)
    i = 0

    while i <= int(inh):
        time.sleep(0.05)
        sys.stdout.write("\033[1A")
        sys.stdout.write("\033[2K")

        r, rdirect = step(r, rdirect)
        g, gdirect = step(g, gdirect)
        b, bdirect = step(b, bdirect)

        print(f"\033[38;2;{r};{g};{b}m {last_line} \033[0m")
        i += 1


@reg("COL")
def col(inh):
    global color
    color = colors[inh.upper()]
    return color


@reg("COLEND")
def colend(inh):
    global color
    color = colors["RESET"]
    check = code[line].strip("\n\t").rstrip(",")[0:-1]
    if check == f"colend({inh}":
        sys.stdout.write("\033[1A")
        sys.stdout.write(f"\033[{code[line].strip("\n\t,")[-1]}C")
        sys.stdout.write(f"{color}\n")
        sys.stdout.flush()
        return ""
    else:
        return color


@reg("INPUT")
def input_user(inh):
    inh = det_var(inh)
    return save_input(input(f"{inh}\n"))


@reg("VAR")
def var(inh):
    name, val = inh.split("=")
    def_var(name, val)
    return ""


@reg("PRINT")
def pri(inh):
    global last_line
    inh = det_var(inh)

    last_line = f"{inh}"
    print(f"{inh}")
    return ""


@reg("CALC")
def calc(inh):
    rec = inh
    parts = finPar(rec)
    rRF = sort(parts)
    erg = solve(rRF)
    return erg


@reg("COUNT")
def count(inh):
    reihe = ""
    von, bis = inh.split("-")
    for i in range(int(von), int(bis) + 1):
        reihe += f"{i} "
    pri(reihe)
    return ""


@reg("IF")
def when(inh):
    global line
    global code
    global deleted_lines
    global start_index
    global end_index
    global line_index

    line_index = line
    inh = det_var(inh)
    bed, oper, val = re.findall(r"\d+|[<>=]+|[a-zA-Z_]+", inh)

    get_start_end_condition()
    deleted_lines += end_index - start_index + 1

    if opers[oper](bed, val):
        main()
        if code[start_index - 1].strip("\n\t").upper().startswith("ELSE"):
            line_index = start_index - 1
            get_start_end_condition()
            for _ in range(start_index, end_index + 1):
                code.pop(start_index)

            code.pop(start_index - 1)
            deleted_lines += end_index - start_index + 2

    else:
        for _ in range(start_index, end_index + 1):
            code.pop(start_index)

        code.pop(start_index - 1)

        if start_index - 1 != len(code) and code[start_index - 1].strip(
            "\n\t"
        ).upper().startswith("ELSE"):
            line_index = line
            get_start_end_condition()

            deleted_lines += end_index - start_index + 2
            main()

    line = -1
    start_index = -1
    end_index = -1
    return ""


@reg("FOR")
def for_loop(inh):
    global line
    global code
    global start_loop
    global end_loop
    global code_backup
    global line_index
    global alt_start_loop
    var_i, _, start_val, end_val = re.split(r"[ ,]", inh)
    start_val = int(start_val)
    end_val = int(end_val)
    line_index = line

    get_start_end_loop()

    alt_start_loop = start_loop
    alt_end_loop = end_loop
    code_backup = code.copy()
    for i in range(start_val, end_val):
        start_loop = alt_start_loop
        end_loop = alt_end_loop
        code = code_backup.copy()
        def_var(var_i, i)
        main()

    line = -1
    start_loop = -1
    end_loop = -1
    return ""


@reg("WHILE")
def while_loop(inh):
    global line
    global code
    global start_loop
    global end_loop
    global code_backup
    global line_index
    global alt_start_loop

    inh_backup = inh
    inh = det_var(inh)
    bed, oper, val = re.findall(r"\d+|[<>=]+|[a-zA-Z_]+", inh)
    line_index = line

    get_start_end_loop()

    alt_start_loop = start_loop
    alt_end_loop = end_loop
    code_backup = code.copy()
    while opers[oper](bed, val):
        code = code_backup.copy()
        start_loop = alt_start_loop
        end_loop = alt_end_loop
        main()
        inh = inh_backup
        inh = det_var(inh)
        bed, oper, val = re.findall(r"\d+|[<>=]+|[a-zA-Z_]+", inh)

    line = -1
    start_loop = -1
    end_loop = -1
    return ""


@reg("ENTER")
def enter(line):
    line = int(line)
    while line != 0:
        pri("")
        line -= 1
    return ""


@reg("RANDOM")
def random_int(inh):

    inh = det_var(inh)
    inh = re.split(r"[ ,]", inh)
    start_val, end_val = inh
    x = random.randint(int(start_val), int(end_val))
    return x


# -----------------------------------------------------------------------------------------

# txtname = input("Wie heißt die Datei (mit Dateiendung)?\n")
# with open(get_pat(txtname)) as data:

with open(get_pat("Ratespiel.txt")) as data:
    code = data.readlines()

code = [line for line in code if line.strip() != ""]
while code != []:
    main()
print("------------")
print("  Code End  ")
print("------------")
