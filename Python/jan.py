
BASES={"hex": 16, "dez": 10, "bin": 2}

inp = input("Enter a number: ")
base = input("Enter base [hex,dez,bin]: ")

if base.lower() not in ["hex", "dez", "bin"]:
    exit()

if base.lower() != "bin":
    print("BINÄR", str(bin(int(inp,BASES[base.lower()]))).replace("0b","").upper())
if base.lower() != "hex":
    print("HEXADEZIMAL", str(hex(int(inp,BASES[base.lower()]))).replace("0x","").upper())
if base.lower() != "dez":
    print("DEZIMAL", int(inp, BASES[base.lower()]))