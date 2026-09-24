import re
import os
import sys
import random
import time
import operator
from tkinter import *


window = Tk()
window.geometry("600x350")
window.title("Texpy")
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
special_caracters = []
prin = False
color = colors["RESET"]
last_input = ""
last_line = ""
line = 0
code = []
code_backup = []
block = []

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

    while exclams != [] and not inp.startswith("#"):
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

    line += 1

    return ""


def get_block():
    global line
    global code
    global block
    global special_caracters
    block = []
    start_index = 0
    last_index = -1
    count = 0

    start_index = line + 1

    i = line
    while i < len(code):
        if code[i].strip("\t\n").endswith(":") or code[i].strip("\t\n").endswith(","):
            special_caracters.append(i)
        i += 1

    count = 0
    count_line = line
    while last_index == -1:
        if code[count_line].strip("\t\n").endswith(","):
            if count == 0:
                last_index = count_line
                break
            elif count == 1:
                last_index = count_line
            count -= 1
        elif code[count_line].strip("\t\n").endswith(":"):
            count += 1
        count_line += 1

    pos_comma = last_index

    block = code[start_index : pos_comma + 1].copy()

    return ""


def main():
    global line
    global code

    for i, _ in enumerate(code):
        code[i] = code[i].rstrip("\n\t")
        order(code[i])


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
    return save_input(gui_input(inh))


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
    global special_caracters
    global line
    global code

    inh = det_var(inh)
    bed, oper, val = re.findall(r"\d+|[<>=]+|[a-zA-Z_]+", inh)

    get_block()

    block_index = len(block) + 1

    if opers[oper](bed, val):
        if line + block_index < len(code) and code[
            line + block_index
        ].upper().startswith("ELSE"):
            code[line + block_index] = "#" + code[line + block_index]
            count = 1
            while count > 0:
                block_index += 1
                if code[line + block_index].strip("\t\n").endswith(","):
                    count -= 1
                elif code[line + block_index].strip("\t\n").endswith(":"):
                    count += 1
                code[line + block_index] = "#" + code[line + block_index]

    else:
        for i in range(0, len(block) + 1):
            code[line + i] = "#" + code[line + i]

    return ""


@reg("FOR")
def for_loop(inh):
    global line
    global code
    global code_backup
    var_i, _, start_val, end_val = re.split(r"[ ,]", inh)
    start_val = int(start_val)
    end_val = int(end_val)

    get_block()
    line += 1
    code_backup = code.copy()
    line_backup = line
    block_len = len(block)

    code_backup = code.copy()
    for i in range(start_val, end_val):
        def_var(var_i, i)
        code = code_backup.copy()
        line = line_backup
        for _ in range(0, block_len):
            order(code[line])

    code = code_backup.copy()
    line = line_backup

    get_block()

    for i in range(0, len(block) + 1):
        code[line + i] = "#" + code[line + i]

    return ""


@reg("WHILE")
def while_loop(inh):
    global line
    global block
    global code
    global code_backup

    inh_backup = inh
    inh = det_var(inh)
    bed, oper, val = re.findall(r"\d+|[<>=]+|[a-zA-Z_]+", inh)

    get_block()
    line += 1
    code_backup = code.copy()
    line_backup = line
    block_len = len(block)
    if oper == "<" or oper == ">" or oper == ">=" or oper == "<=":
        bed = int(bed)
        val = int(val)
    while opers[oper](bed, val):
        code = code_backup.copy()
        line = line_backup
        for _ in range(0, block_len):
            order(code[line])
        inh = inh_backup
        inh = det_var(inh)
        bed, oper, val = re.findall(r"\d+|[<>=]+|[a-zA-Z_]+", inh)
        if oper == "<" or oper == ">" or oper == ">=" or oper == "<=":
            bed = int(bed)
            val = int(val)

    code = code_backup.copy()
    line = line_backup

    line -= 1
    get_block()

    for i in range(0, len(block) + 1):
        code[line + i] = "#" + code[line + i]

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

# with open(get_pat("TruefalseNEW.txt")) as data:
# with open(get_pat("AlterNEW.txt")) as data:

# with open(get_pat("JahrMonat.txt")) as data:
#    code = data.readlines()

# code = [line for line in code if line.strip() != ""]
# for i in range(0, len(code)):
#    code[i] = code[i].strip("\t")


class TextRedirector:
    def __init__(self, widget):
        self.widget = widget

    def write(self, text):
        self.widget.insert(END, text)
        self.widget.see(END)

    def flush(self):
        pass


def block_edit(event):
    if output.compare("insert", "<", input_start):
        return "break"


def gui_input(prompt=""):
    global input_start

    write_output(prompt)

    input_ready = BooleanVar()
    value = {"text": ""}

    input_start = output.index("end-1c")

    def enter(event=None):
        value["text"] = output.get(input_start, "end-1c")
        output.insert(END, "\n")
        input_ready.set(True)

    output.bind("<Return>", enter)

    window.wait_variable(input_ready)

    return value["text"]


def write_output(text):
    global input_start
    output.insert(END, text)
    output.see(END)
    input_start = output.index(END)


def run_code():
    global code
    output.delete("1.0", END)
    code = code_input.get("1.0", END).split("\n")
    code = [line for line in code if line.strip() != ""]
    for i in range(0, len(code)):
        code[i] = code[i].strip("\t")
    main()


l_input = Label(text="Code")
code_input = Text(window, height=10, width=50)
run_button = Button(text="RUN", height=1, width=10, command=lambda: run_code())
l_output = Label(text="Output")
output = Text(window, height=5, width=50)
sys.stdout = TextRedirector(output)

output.bind("<Key>", block_edit)


l_input.pack()
code_input.pack()
run_button.pack()
l_output.pack()
output.pack()
mainloop()


print("------------")
print("  Code End  ")
print("------------")
