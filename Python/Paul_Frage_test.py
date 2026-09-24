a = True
b = True
c = True

variables = {"a": a, "b": b, "c": c}

priority_lamp = {"a": 2, "b": 1, "c": 0}

priority_to_name = {v: k for k, v in priority_lamp.items()}

x = input("Enter variable name (a, b, c): ")

prior = priority_lamp[x]

while prior > 0:
    prior -= 1
    var_name = priority_to_name[prior]
